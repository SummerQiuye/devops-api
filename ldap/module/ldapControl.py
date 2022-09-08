import random
import re
import socket

import redis

from alert.module.sendMailModule import sendMail
from flask import jsonify

from ldap.module.ldapManager import LdapOp
from config import ldap, token, redisHost, redisPort

connLdap = LdapOp(ldap["server"], 389, ldap["dc"], ldap["passwd"])
forgotPassConfirmList = {}
redisConn = redis.StrictRedis(host=redisHost, port=redisPort, db=1)


class ldapControl(object):

    def __init__(self, **kwargs):
        self.user = kwargs.get("user")
        self.passwd = kwargs.get("passwd")

    # 定义管理员操作LDAP身份验证
    def authAdminTest(self):
        if self.user == "ye.qiu" or self.user == "wenxuan.zhang":
            authResult = self.login()
            print("管理员权限验证：", authResult)
            if authResult["rv"] == "ok":
                return "success"
        raise Exception("admin auth failed")

    # 修改用户密码
    def changePasswd(self, newpasswd):
        # 验证密码强度
        if len(newpasswd) < 8:
            return "密码不能小于8位数"
        elif newpasswd == self.passwd:
            return "新密码不能和旧密码相同"
        try:
            assert re.search("^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*$", newpasswd), '密码中需包含大小写字母'
        except Exception as e:
            print(e)
            return '密码中需包含特殊字符或数字及大写字母'

        # 验证旧密码
        oldPassAuth = self.login()
        if oldPassAuth["rv"] == "ok":
            setUser = connLdap.setPasswd(user=self.user, passwd=newpasswd)
            print("修改用户密码,用户：", self.user, ", result:", setUser)
            return jsonify(setUser)
        return jsonify({"status": "旧密码匹配失败，修改密码失败。"})

    def login(self):
        return connLdap.authUser(self.user, self.passwd)

    def authToken(self, user, token):
        try:
            cacheToken = redisConn.get(user).decode("utf-8")
            if cacheToken and cacheToken == token:
                rv = 'ok'
                data = '认证成功'
                return {'rv': rv, 'data': data, 'token': cacheToken}
            else:
                rv = 'err'
                data = 'token不匹配'
                return {'rv': rv, 'data': data, 'token': token}
        except Exception as e:
            print("认证失败", e)
            return {'rv': 'err', 'data': '认证失败'}

    def getAlertToken(self):
        authResult = self.login()
        print(authResult)
        if authResult["rv"] == "ok":
            return jsonify(token)
        return "failed auth"

    # 添加用户
    def addUserToLdap(self, **kwargs):
        self.authAdminTest()
        user = kwargs.get('user')
        givenName = kwargs.get('givenName')
        mail = kwargs.get("mail")
        title = kwargs.get("title")
        addUserRe = connLdap.addUser(user=user,
                                     mail=mail,
                                     title=title,
                                     givenName=givenName)
        print(addUserRe)
        if addUserRe['data'] == "用户已存在":
            return addUserRe
        randomPass = ''.join(random.sample('zyxwvutsrqponmlkji%$#^&*(~!@,;.hgfedcba', 10))
        setUserPass = connLdap.setPasswd(user=user, passwd=randomPass)
        print(setUserPass, randomPass)
        addUserRe["userpass"] = randomPass
        return addUserRe

    # 删除用户
    def delUserFromLdap(self, user):
        self.authAdminTest()
        delUserRe = connLdap.deleteUser(user)
        print(delUserRe)
        return delUserRe

    # 忘记密码身份验证+邮件确认
    def forgotPasswd(self, mail):
        try:
            assert self.user
            assert self.user == str(mail).split("@")[0]
        except Exception:
            print("请输入正确的用户名或邮箱")
            return "用户名不存在或邮箱不匹配"

        apiUrl = "http://api.devops.com/html/forgotPasswdConfirm?user_id="
        for user_mail in forgotPassConfirmList:
            if mail == user_mail:
                mailContent = f'''
                            <p>你好，后台接收到忘记密码请求，点击下方生成新的随机密码：</p>
                            <a href="{apiUrl}{forgotPassConfirmList[user_mail]}&user={self.user}">点击修改密码</a>
                        '''
                return sendMail(mail=mail, mailHeader="忘记密码找回", mailData=mailContent)

        randomPass = ''.join(random.sample('AbcaubB12KL3JNbu7wqeCXAS45D343csdcdwpik2jNKVTUVcwe467cq', 10))
        forgotPassConfirmList[mail] = randomPass
        print(forgotPassConfirmList)
        mailContent = f'''
                        <p>你好，后台接收到忘记密码请求，点击下方生成新的随机密码：</p>
                        <a href="{apiUrl}{randomPass}&user={self.user}">点击修改密码</a>
                    '''
        return sendMail(mail=mail, mailHeader="忘记密码找回", mailData=mailContent)

    @staticmethod
    def forgotPasswdConfirm(userNewPass, user):
        for mail in forgotPassConfirmList:
            if str(userNewPass).replace(" ", "") == forgotPassConfirmList[mail]:
                print(user + "随机新密码为:", userNewPass)
                setUserPass = connLdap.setPasswd(user=user, passwd=userNewPass)
                print(setUserPass)
                return "checked"
        return "unchecked"

# re = ldapControl(user="qiuye", passwd="denghou12.").login()
# print(re)
# addre = ldapControl().addUserToLdap()
# delre = ldapControl(user="lisi", passwd="denghou12.").delUserFromLdap('wangwu')
# ldapControl(user="zhangsan").forgotPasswd('qiuye@novelpro.cn')


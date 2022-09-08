import socket

from __init__ import app
from flask import request, render_template
from flasgger import swag_from
from ldap.module.ldapControl import ldapControl


@app.route("/changePasswd/<string:user>/<string:passwd>", methods=["POST"])
@swag_from('/ldap/document/changePasswd.yml')
def changePasswdApi(user, passwd):
    newpasswd = request.args.get('newpasswd')
    return ldapControl(user=user, passwd=passwd).changePasswd(newpasswd)


@app.route("/login/<string:user>/<string:passwd>", methods=["POST"])
@swag_from('/ldap/document/login.yml')
def loginApi(user, passwd):
    return ldapControl(user=user, passwd=passwd).login()


@app.route("/authToken/<string:user>/<string:token>", methods=["POST"])
@swag_from('/ldap/document/authToken.yml')
def authTokenApi(user, token):
    # print(user, token)
    if user == 'undefined' or token == 'undefined':
        return {'rv': 'err', 'data': '参数错误'}
    return ldapControl().authToken(user, token)


@app.route("/getAlertToken/<string:user>/<string:passwd>", methods=["POST"])
@swag_from('/ldap/document/getAlertToken.yml')
def getAlertTokenApi(user, passwd):
    return ldapControl(user=user, passwd=passwd).getAlertToken()


@app.route("/addUser/<string:user>/<string:passwd>", methods=["POST"])
@swag_from('/ldap/document/addUser.yml')
def addUserApi(user, passwd):
    userData = request.json
    print(userData)
    return ldapControl(user=user, passwd=passwd).addUserToLdap(user=userData['user'],
                                                               userPassword=userData['passwd'],
                                                               mail=userData['mail'],
                                                               title=userData['title'],
                                                               givenName=userData['givenName'])


@app.route("/delUser/<string:user>/<string:passwd>", methods=["POST"])
@swag_from('/ldap/document/delUser.yml')
def delUserApi(user, passwd):
    delusername = request.args.get("delusername")
    return ldapControl(user=user, passwd=passwd).delUserFromLdap(delusername)


@app.route("/forgotPasswd/<string:user>/<string:mail>", methods=["POST"])
@swag_from('/ldap/document/forgotPasswd.yml')
def forgotPasswdApi(user, mail):
    return ldapControl(user=user).forgotPasswd(mail=mail)


@app.route("/html/forgotPasswdConfirm")
def forgotPasswdConfirmApi():
    userNewPass = request.args.get("user_id")
    user = request.args.get("user")
    assert userNewPass
    assert user
    confirm = ldapControl().forgotPasswdConfirm(userNewPass, user)
    print(confirm)
    if confirm == "unchecked":
        return render_template("forgot.html", newpasswd="preAuthFailed")
    return render_template("forgot.html", newpasswd=userNewPass)

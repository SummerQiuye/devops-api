# -*- coding: utf-8 -*-
# author : s

import random, string
import redis
from config import *
from ldap3 import Server, Connection, ALL, SUBTREE, ALL_ATTRIBUTES, MODIFY_REPLACE, MODIFY_ADD, MODIFY_DELETE
from passlib.hash import ldap_salted_sha1 as ssha

redisConn = redis.StrictRedis(host=redisHost, port=redisPort, db=1)


class LdapOp(object):
    """
    Operation Dcouments: http://ldap3.readthedocs.io/
    """

    def __init__(self, ip, port, user, passwd):
        self._ip = ip
        self._port = port
        self._user = user
        self._passwd = passwd
        self.dn = self._user.split(',', 1)[1]
        self.s = Server(self._ip, self._port, get_info=ALL)
        self._conn = Connection(self.s, self._user, self._passwd, auto_bind=True)

    @property
    def conn(self):

        if not self._conn:
            print('ldap conn init ')
            self._conn = Connection(self.s, self._user, self._passwd, auto_bind=True)

        return self._conn

    def searchAll(self, name='top'):
        entries = self.conn.extend.standard.paged_search(self.dn, '(objectClass=%s)' % name,
                                                         attributes=['cn', 'mail'])
        en = list(entries)
        # print(en)

        ulist = [v["raw_attributes"] for v in en if 'hunteron-tech' in v.get('dn', '')]
        # print(ulist)
        l = []
        for v in ulist:
            udict = {}
            udict['mail'] = v['mail']
            udict['cn'] = v['cn']
            # print(v['mail'], v['cn'])
            l.append(udict)
        # print(l)
        return l

    def addUser(self, **kwargs):

        cndn = 'cn=%s,cn=hunteron-tech,dc=ldap,dc=com' % (kwargs.get('user'))

        attr = {
            'userPassword': 'HunterOn263',
            'cn': kwargs.get('user'),
            'mail': kwargs.get('mail'),
            'title': kwargs.get('title'),
            'sn': 'hunteron-tech',
            'givenName': kwargs.get('givenName'),
            'o': 'hunteron-tech',
            'objectClass': ['inetOrgPerson', 'posixAccount', 'top'],
            'uid': kwargs.get('user'),
            'uidNumber': '1000',
            'gidNumber': '500',
            'homeDirectory': '/home/' + kwargs.get('user')
        }
        try:
            data = self.conn.add(cndn, attributes=attr)
            msg = self.conn.result['message']
            if not data:
                data = "用户已存在"
        except Exception as e:
            data = e
            msg = 'err'
        return {'msg': msg, 'data': data}

    def deleteUser(self, user=''):
        dn = 'cn=%s,cn=hunteron-tech,dc=ldap,dc=com' % user
        try:
            self.conn.delete(dn)
            rv = {'msg': 'ok', 'data': ''}
        except Exception as e:
            rv = {'msg': 'err', 'data': e}
        return rv

    def searchUser(self, name):
        try:
            users = self.searchAll()
            print(users)
            if name:
                data = [user for user in users if name in user['cn']]
            else:
                data = users
            rv = 'ok'
        except Exception as e:
            data = e
            rv = 'err'
        finally:
            return {'msg': rv, 'data': data}

    def searchSinUser(self, name):
        try:
            ga = self.conn.extend.standard.paged_search(search_base=self.dn,
                                                        search_filter='(uid=%s)' % name,
                                                        search_scope=SUBTREE,
                                                        attributes=ALL_ATTRIBUTES)
            user = list(ga)
            if user:
                data = user[0].get('attributes')

                d = {
                    'user': str(data.get('cn')[0]),
                    'passwd': data.get('userPassword')[0].decode('utf-8'),
                    'gid': data.get('gidNumber'),
                    'mail': data.get('mail')[0],
                    'phonenumber': data.get('uidNumber')

                }

            else:
                d = {}
            users = self.searchAll()
            usingle = [d for d in users if d.get('cn') == name]
            u = {}
            if usingle:
                u = usingle[0]
        except Exception as e:
            print(e)
            u = {'msg': "error"}

        finally:
            # print('user=',u)
            x = u.update(d)
            print('u=', u)
            return u

    def editUser(self, args):
        data = ""
        try:
            cn = 'uid=%s,ou=People,%s' % (args.get('user'), self.dn)
            print(cn)
            passwd = args.get('passwd', '')

            user = self.searchSinUser(args.get('user'))
            data = ''
            if user.get('passwd') != passwd:
                if 'SSHA' not in passwd:
                    passwd = self.encodePasswd(passwd)

                    data = self.conn.modify(cn, {'userPassword': (MODIFY_REPLACE, passwd)})
            if user.get('gid') != args.get('gid') and args.get('gid') != 'default':
                data = self.conn.modify(cn, {'gidNumber': (MODIFY_REPLACE, args.get('gid'))})

        except Exception as e:

            data = e
        finally:
            print('data', data)
            return data

    def setPasswd(self, **kwargs):
        data = ""
        try:
            cn = 'cn=%s,cn=hunteron-tech,dc=ldap,dc=com' % (kwargs.get('user', ''))
            # print(cn)
            data = self.conn.modify(cn, {'userPassword': (MODIFY_REPLACE, kwargs.get('passwd', ''))})
            # print(data)
        except Exception as e:
            data = "error"
        finally:
            return data

    @staticmethod
    def GenPasswd():
        return ''.join(random.sample(string.ascii_letters + string.digits, 8))

    def _searchUser_org(self, username):
        print('in-search-org')
        ga = self.conn.extend.standard.paged_search(search_base=self.dn,
                                                    search_filter='(uid=%s)' % username,
                                                    search_scope=SUBTREE,
                                                    attributes=ALL_ATTRIBUTES)
        user = list(ga)
        print(user)
        entry = self.conn.response[0]
        dn = entry['dn']
        attr_dict = entry['attributes']

        return (dn, attr_dict)

    def authUser(self, username, password):
        rv = ""
        data = ""
        jstoken = ""
        role = ""
        try:

            cn = 'cn=%s,cn=hunteron-tech,dc=ldap,dc=com' % username
            conn2 = Connection(self._ip, user=cn, password=password,
                               check_names=True, lazy=False, raise_exceptions=False)
            conn2.bind()
            # print(conn2.result)
            if conn2.result["description"] == "success":
                rv = 'ok'
                data = '认证成功'
                jstoken = ''.join(random.sample('AbcaubB12KL3JNbu7wqeCXAS45D343csdcdwpik2jNKVTUVcwe467cq', 50))
                redisConn.set(username, jstoken)
                redisConn.expire(username, 28800)
                if username in adminRole:
                    role = "admin"
                else:
                    role = "user"
            else:
                rv = 'err'
                data = '认证失败,用户名或密码错误！'
        except Exception as e:
            print(e)
            rv = 'err'
            data = "error"
        finally:
            return {'rv': rv, 'data': data, 'token': jstoken, 'role': role}

    @staticmethod
    def encodePasswd(password=''):
        """
        :param password:
        :return:
        """
        if password:
            return ssha.encrypt(password, salt_size=12)
        return ''

    def get_ouname(self, ouname):
        """
         ouname = '(|(ou=Groups)(ou=Group))'
        :param ouname:
        :return:
        """
        print(self.dn, ouname)
        ou = self.conn.search('%s' % self.dn, '%s' % ouname)
        print(ou)
        retry = self.conn.entries
        num = len(retry)
        if num == 0:
            return []

        else:
            return retry[0].entry_get_dn()

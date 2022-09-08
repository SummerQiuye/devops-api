from functools import wraps
from ldap.module.ldapControl import ldapControl
from flask import request
from config import adminRole


# 管理员权限验证装饰器
def authwapper(func):
    @wraps(func)
    def authtest(**kwargs):
        try:
            print("开始判断")
            token = request.headers["Authentication"].split(';')[0].split('=')[1]
            user = request.headers["Authentication"].split(';')[1].split('=')[1]
            print(user, adminRole.index(user))
            assert adminRole.index(user) >= 0
            result = ldapControl().authToken(user=user, token=token)
            print(result)
            if result["rv"] == "ok":
                print("auth success")
                return func(**kwargs)
            else:
                print("auth failed")
                return "auth failed"
        except Exception as e:
            print("error:", e)
            return "auth failed"
    return authtest


# 配置文件权限验证装饰器
def authConfigRoleWapper(func):
    @wraps(func)
    def authtest(**kwargs):
        try:
            print("开始判断")
            token = request.headers["Authentication"].split(';')[0].split('=')[1]
            user = request.headers["Authentication"].split(';')[1].split('=')[1]
            print(user, adminRole.index(user))
            assert adminRole.index(user) >= 0
            result = ldapControl().authToken(user=user, token=token)
            print(result)
            if result["rv"] == "ok":
                print("auth success")
                return func(**kwargs)
            else:
                print("auth failed")
                return "auth failed"
        except Exception as e:
            print("error:", e)
            return "auth failed"
    return authtest

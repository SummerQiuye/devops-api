import os


def Proxy_on():
    os.system('networksetup -setautoproxyurl Wi-Fi http://47.103.223.252:8200/proxy.pac')
    os.system('networksetup -setautoproxystate "WI-FI" off')


Proxy_on()


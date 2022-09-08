## 运维接口工程

> 安装工程依赖包：pip3 install -r requirements.txt
> 
> 启动程序：uwsgi --ini devops-api-uwsgi.ini
>
> 重启程序：uwsgi --reload logs/app.pid
> 
> 停止程序：uwsgi --stop logs/app.pid


### 工程目录说明：
``` 
directory detail:
    cicd:
        for jenkins support api, such as create tag、get branch list by project id.
    public:
        some outside or inside feature support, such as:
            1.send message to wechat or mail.
            2.scheduler task run in daemon.
        # remark: weixin api doc : https://work.weixin.qq.com/api/doc/90000/90135/90664
    ldap:
        user account manager module, such as:
            1.user login
            2.change passwd
            3.forgot passwd
            4.token verify
controller.py:
    modules api view manager.
```
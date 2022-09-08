FROM nexus-tech.shruisong.cn/ops/centos:7

WORKDIR /app

RUN pwd
RUN pip3 install -r requirements.txt && mkdir -p logs

CMD ["uwsgi --ini devops-api-uwsgi.ini"]


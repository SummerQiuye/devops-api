# coding: utf-8
from __init__ import app
from flask_sqlalchemy import SQLAlchemy

app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@:3306/devops?charset=utf8&autocommit=true'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_POOL_SIZE'] = 100
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 10
app.config['SQLALCHEMY_POOL_RECYCLE'] = True
app_context = app.app_context()
app_context.push()
# db = SQLAlchemy(session_options={'autocommit': True})
db = SQLAlchemy()
db.init_app(app)


class CloudDatabase(db.Model):
    __tablename__ = 'cloud_database'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='资产id')
    internal_ip = db.Column(db.String(50, 'utf8_bin'), comment='内部ip')
    internal_port = db.Column(db.String(30, 'utf8_bin'), comment='内部端口')
    VPC = db.Column(db.String(100, 'utf8_bin'), comment='vpc网络')
    role = db.Column(db.String(50, 'utf8_bin'), comment='数据库角色')
    region = db.Column(db.String(50, 'utf8_bin'), comment='区域')
    node = db.Column(db.String(50, 'utf8_bin'), comment='数据库节点数')
    system = db.Column(db.String(50, 'utf8_bin'), comment='数据库版本')
    ro_instance_id = db.Column(db.String(100, 'utf8_bin'), comment='数据库只读实例id')
    user = db.Column(db.String(50, 'utf8_bin'), comment='数据库管理账户')
    password = db.Column(db.String(50, 'utf8_bin'), comment='数据库管理密码')
    monitor = db.Column(db.String(100, 'utf8_bin'), comment='数据库监控')


class CloudHost(db.Model):
    __tablename__ = 'cloud_host'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, comment='资产id')
    internal_ip = db.Column(db.String(20, 'utf8_bin'), primary_key=True, nullable=False, comment='资产内部IP')
    external_ip = db.Column(db.String(255, 'utf8_bin'), comment='资产外部IP')
    monitor = db.Column(db.String(100, 'utf8_bin'), comment='主机监控')
    region = db.Column(db.String(30, 'utf8_bin'), comment='主机所属区域')
    vpc = db.Column(db.String(100, 'utf8_bin'), comment='主机所属网络')
    image = db.Column(db.String(255, 'utf8_bin'), comment='主机镜像/使用镜像')
    system = db.Column(db.String(255, 'utf8_bin'), comment='主机系统版本')
    # user = db.Column(db.String(50, 'utf8_bin'), comment='主机管理账户')
    # password = db.Column(db.String(50, 'utf8_bin'), comment='主机管理密码')


class CloudOthers(db.Model):
    __tablename__ = 'cloud_others'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, comment='资产id')
    internal_ip = db.Column(db.String(20, 'utf8_bin'), primary_key=True, nullable=False, comment='资产内部IP')
    region = db.Column(db.String(30, 'utf8_bin'), comment='资产区域')
    detail = db.Column(db.String(256, 'utf8_bin'), comment='资产详情')


class CloudPropertyPublic(db.Model):
    __tablename__ = 'cloud_property_public'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, comment='资产id')
    external_ip = db.Column(db.String(100, 'utf8_bin'), comment='资产外部IP')
    internal_ip = db.Column(db.String(100, 'utf8_bin'), primary_key=True, nullable=False, comment='资产内部IP')
    name = db.Column(db.String(100, 'utf8_bin'), nullable=False, comment='资产名')
    line = db.Column(db.String(50, 'utf8_bin'), comment='资产所属业务线')
    owner = db.Column(db.String(20, 'utf8_bin'), comment='资产归属人')
    config = db.Column(db.String(150, 'utf8_bin'), comment='资产配置')
    env = db.Column(db.String(20, 'utf8_bin'), comment='资产所属环境')
    status = db.Column(db.String(50, 'utf8_bin'), comment='资产当前状态')
    usage = db.Column(db.String(255, 'utf8_bin'), comment='资产用途')
    createDate = db.Column(db.DateTime, server_default=db.FetchedValue(), comment='资产创建时间')
    type = db.Column(db.String(100, 'utf8_bin'), comment='资产类型')
    updateDate = db.Column(db.DateTime, server_default=db.FetchedValue(), comment='资产更新时间')


class ConfigDev(db.Model):
    __tablename__ = 'config_dev'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, comment='配置id')
    name = db.Column(db.String(60, 'utf8_bin'), primary_key=True, comment='应用名称')
    usage = db.Column(db.String(60, 'utf8_bin'), comment='应用说明')
    owner = db.Column(db.String(50, 'utf8_bin'), comment='应用负责人')
    version = db.Column(db.String(20, 'utf8_bin'), comment='当前应用版本')
    lastUpdateRemark = db.Column(db.String(255, 'utf8_bin'), comment='最后更新内容')
    lastUpdateDate = db.Column(db.DateTime, server_default=db.FetchedValue(), comment='最后更新时间')
    lastUpdateUser = db.Column(db.String(30, 'utf8_bin'), comment='最后更新用户')
    createDate = db.Column(db.DateTime, server_default=db.FetchedValue(), comment='创建时间')
    config = db.Column(db.BLOB(21845), comment='配置内容')
    updateCount = db.Column(db.Integer, comment='配置更新次数')
    useCount = db.Column(db.Integer, comment='配置调用次数')


class ConfigProd(db.Model):
    __tablename__ = 'config_prod'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, comment='配置id')
    name = db.Column(db.String(60, 'utf8_bin'), primary_key=True, comment='应用名称')
    usage = db.Column(db.String(60, 'utf8_bin'), comment='应用说明')
    owner = db.Column(db.String(50, 'utf8_bin'), comment='应用负责人')
    version = db.Column(db.String(20, 'utf8_bin'), comment='当前应用版本')
    lastUpdateRemark = db.Column(db.String(255, 'utf8_bin'), comment='最后更新内容')
    lastUpdateDate = db.Column(db.DateTime, server_default=db.FetchedValue(), comment='最后更新时间')
    lastUpdateUser = db.Column(db.String(30, 'utf8_bin'), comment='最后更新用户')
    createDate = db.Column(db.DateTime, server_default=db.FetchedValue(), comment='创建时间')
    config = db.Column(db.BLOB(21845), comment='配置内容')
    updateCount = db.Column(db.Integer, comment='配置更新次数')
    useCount = db.Column(db.Integer, comment='配置调用次数')


class ConfigHistory(db.Model):
    __tablename__ = 'config_history'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, comment='配置id')
    name = db.Column(db.String(60, 'utf8_bin'), nullable=False, comment='应用名称')
    version = db.Column(db.String(20, 'utf8_bin'), nullable=False, comment='当前应用版本')
    lastUpdateRemark = db.Column(db.String(255, 'utf8_bin'), comment='最后更新内容')
    lastUpdateDate = db.Column(db.DateTime, server_default=db.FetchedValue(), comment='最后更新时间')
    config = db.Column(db.BLOB(21845), comment='配置内容')
    configEnv = db.Column(db.String(60, 'utf8_bin'), nullable=False, comment='配置环境')


class NavigationDatum(db.Model):
    __tablename__ = 'navigation_data'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255, 'utf8mb4_unicode_ci'), info='导航名称')
    tag = db.Column(db.String(255, 'utf8mb4_unicode_ci'), info='导航类型')
    urldata = db.Column(db.JSON, info='导航数据')


class ProxyGateway(db.Model):
    __tablename__ = 'proxy_gateway'

    id = db.Column(db.Integer, primary_key=True)
    proxyMac = db.Column(db.String(255, 'utf8mb4_unicode_ci'), info='用户mac地址')
    proxyUserName = db.Column(db.String(255, 'utf8mb4_unicode_ci'), info='账户名称')
    proxyRealName = db.Column(db.String(255, 'utf8mb4_unicode_ci'), info='用户名称')
    createDate = db.Column(db.DateTime, server_default=db.FetchedValue(), comment='创建时间')
    updateDate = db.Column(db.DateTime, server_default=db.FetchedValue(), comment='更新时间')


db.create_all()

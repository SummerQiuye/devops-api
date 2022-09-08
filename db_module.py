# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class ConfigDev(db.Model):
    __tablename__ = 'config_dev'

    id = db.Column(db.Integer, primary_key=True, nullable=False, info='配置id')
    name = db.Column(db.String(60, 'utf8_bin'), primary_key=True, nullable=False, info='应用名称')
    usage = db.Column(db.String(60, 'utf8_bin'), info='应用说明')
    owner = db.Column(db.String(50, 'utf8_bin'), info='应用负责人')
    version = db.Column(db.String(20, 'utf8_bin'), info='当前应用版本')
    lastUpdateRemark = db.Column(db.String(255, 'utf8_bin'), info='最后更新内容')
    lastUpdateDate = db.Column(db.DateTime, server_default=db.FetchedValue(), info='最后更新时间')
    lastUpdateUser = db.Column(db.String(30, 'utf8_bin'), info='最后更新用户')
    createDate = db.Column(db.DateTime, server_default=db.FetchedValue(), info='创建时间')
    config = db.Column(db.LargeBinary, info='配置内容')
    updateCount = db.Column(db.Integer, info='配置更新次数')
    useCount = db.Column(db.Integer, info='配置调用次数')



class ConfigHistory(db.Model):
    __tablename__ = 'config_history'

    id = db.Column(db.Integer, primary_key=True, info='配置id')
    name = db.Column(db.String(60, 'utf8_bin'), nullable=False, info='应用名称')
    version = db.Column(db.String(20, 'utf8_bin'), nullable=False, info='当前应用版本')
    lastUpdateRemark = db.Column(db.String(255, 'utf8_bin'), info='最后更新内容')
    lastUpdateDate = db.Column(db.DateTime, server_default=db.FetchedValue(), info='最后更新时间')
    config = db.Column(db.LargeBinary, info='配置内容')
    configEnv = db.Column(db.String(60, 'utf8_bin'), nullable=False, info='配置环境')



class ConfigProd(db.Model):
    __tablename__ = 'config_prod'

    id = db.Column(db.Integer, primary_key=True, nullable=False, info='配置id')
    name = db.Column(db.String(60, 'utf8_bin'), primary_key=True, nullable=False, info='应用名称')
    usage = db.Column(db.String(60, 'utf8_bin'), info='应用说明')
    owner = db.Column(db.String(50, 'utf8_bin'), info='应用负责人')
    version = db.Column(db.String(20, 'utf8_bin'), info='当前应用版本')
    lastUpdateRemark = db.Column(db.String(255, 'utf8_bin'), info='最后更新内容')
    lastUpdateDate = db.Column(db.DateTime, server_default=db.FetchedValue(), info='最后更新时间')
    lastUpdateUser = db.Column(db.String(30, 'utf8_bin'), info='最后更新用户')
    createDate = db.Column(db.DateTime, server_default=db.FetchedValue(), info='创建时间')
    config = db.Column(db.LargeBinary, info='配置内容')
    updateCount = db.Column(db.Integer, info='配置更新次数')
    useCount = db.Column(db.Integer, info='配置调用次数')



class NavigationDatum(db.Model):
    __tablename__ = 'navigation_data'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255, 'utf8mb4_unicode_ci'), info='导航名称')
    urldata = db.Column(db.JSON, info='导航数据')
    tag = db.Column(db.String(255, 'utf8mb4_unicode_ci'), info='导航类型')



class TxcloudDatabase(db.Model):
    __tablename__ = 'txcloud_database'

    id = db.Column(db.Integer, primary_key=True, info='资产id')
    internal_ip = db.Column(db.String(50, 'utf8_bin'), info='内部ip')
    internal_port = db.Column(db.String(30, 'utf8_bin'), info='内部端口')
    VPC = db.Column(db.String(100, 'utf8_bin'), info='vpc网络')
    role = db.Column(db.String(50, 'utf8_bin'), info='数据库角色')
    region = db.Column(db.String(50, 'utf8_bin'), info='区域')
    node = db.Column(db.String(50, 'utf8_bin'), info='数据库节点数')
    system = db.Column(db.String(50, 'utf8_bin'), info='数据库版本')
    ro_instance_id = db.Column(db.String(100, 'utf8_bin'), info='数据库只读实例id')
    user = db.Column(db.String(50, 'utf8_bin'), info='数据库管理账户')
    password = db.Column(db.String(50, 'utf8_bin'), info='数据库管理密码')
    monitor = db.Column(db.String(100, 'utf8_bin'), info='数据库监控')



class TxcloudHost(db.Model):
    __tablename__ = 'txcloud_host'

    id = db.Column(db.Integer, primary_key=True, nullable=False, info='资产id')
    internal_ip = db.Column(db.String(20, 'utf8_bin'), primary_key=True, nullable=False, info='资产内部IP')
    external_ip = db.Column(db.String(255, 'utf8_bin'), info='资产外部IP')
    monitor = db.Column(db.String(100, 'utf8_bin'), info='主机监控')
    region = db.Column(db.String(30, 'utf8_bin'), info='主机所属区域')
    vpc = db.Column(db.String(100, 'utf8_bin'), info='主机所属网络')
    image = db.Column(db.String(255, 'utf8_bin'), info='主机镜像/使用镜像')
    system = db.Column(db.String(255, 'utf8_bin'), info='主机系统版本')



class TxcloudOther(db.Model):
    __tablename__ = 'txcloud_others'

    id = db.Column(db.Integer, primary_key=True, nullable=False, info='资产id')
    internal_ip = db.Column(db.String(20, 'utf8_bin'), primary_key=True, nullable=False, info='资产内部IP')
    region = db.Column(db.String(30, 'utf8_bin'), info='资产区域')
    detail = db.Column(db.String(256, 'utf8_bin'), info='资产详情')



class TxcloudPropertyPublic(db.Model):
    __tablename__ = 'txcloud_property_public'

    id = db.Column(db.Integer, primary_key=True, nullable=False, info='资产id')
    external_ip = db.Column(db.String(100, 'utf8_bin'), info='资产外部IP')
    internal_ip = db.Column(db.String(100, 'utf8_bin'), primary_key=True, nullable=False, info='资产内部IP')
    name = db.Column(db.String(100, 'utf8_bin'), nullable=False, info='资产名')
    line = db.Column(db.String(50, 'utf8_bin'), info='资产所属业务线')
    owner = db.Column(db.String(20, 'utf8_bin'), info='资产归属人')
    config = db.Column(db.String(150, 'utf8_bin'), info='资产配置')
    env = db.Column(db.String(20, 'utf8_bin'), info='资产所属环境')
    status = db.Column(db.String(50, 'utf8_bin'), info='资产当前状态')
    usage = db.Column(db.String(255, 'utf8_bin'), info='资产用途')
    createDate = db.Column(db.DateTime, server_default=db.FetchedValue(), info='资产创建时间')
    type = db.Column(db.String(100, 'utf8_bin'), info='资产类型')
    updateDate = db.Column(db.DateTime, server_default=db.FetchedValue(), info='资产更新时间')



class UrlList(db.Model):
    __tablename__ = 'url_list'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255, 'utf8mb4_unicode_ci'))
    url = db.Column(db.String(255, 'utf8mb4_unicode_ci'))
    img = db.Column(db.String(255, 'utf8mb4_unicode_ci'))
    detail = db.Column(db.String(255, 'utf8mb4_unicode_ci'))
    tag = db.Column(db.String(255, 'utf8mb4_unicode_ci'))

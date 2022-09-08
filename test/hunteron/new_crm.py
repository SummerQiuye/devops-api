# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Checksum(db.Model):
    __tablename__ = 'checksums'
    __table_args__ = (
        db.Index('ts_db_tbl', 'ts', 'db', 'tbl'),
    )

    db = db.Column(db.String(64), primary_key=True, nullable=False)
    tbl = db.Column(db.String(64), primary_key=True, nullable=False)
    chunk = db.Column(db.Integer, primary_key=True, nullable=False)
    chunk_time = db.Column(db.Float)
    chunk_index = db.Column(db.String(200))
    lower_boundary = db.Column(db.Text)
    upper_boundary = db.Column(db.Text)
    this_crc = db.Column(db.String(40), nullable=False)
    this_cnt = db.Column(db.Integer, nullable=False)
    master_crc = db.Column(db.String(40))
    master_cnt = db.Column(db.Integer)
    ts = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())



class CrmPaGroupUser(db.Model):
    __tablename__ = 'crm_pa_group_user'

    id = db.Column(db.BigInteger, primary_key=True, info='主键Id，组ID')
    group_id = db.Column(db.BigInteger, nullable=False, index=True, info='组ID')
    pm_group_user_id = db.Column(db.BigInteger, nullable=False, index=True, info='PM组用户关系ID')
    pm_id = db.Column(db.BigInteger, nullable=False, index=True, info='PM ID')
    user_id = db.Column(db.BigInteger, nullable=False, index=True, info='用户ID(PAID)')
    whether_leader = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否是leader')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    defunct = db.Column(db.Integer, nullable=False, index=True, info='是否删除 0 否 1是')



class CrmPasGroupUser(db.Model):
    __tablename__ = 'crm_pas_group_user'

    id = db.Column(db.BigInteger, primary_key=True, info='主键Id，组ID')
    group_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='组ID')
    pm_group_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='PM组用户关系ID')
    pa_group_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='PA_PM关系ID')
    pm_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='PM ID')
    pa_id = db.Column(db.BigInteger, nullable=False, info='PA ID')
    user_id = db.Column(db.BigInteger, nullable=False, info='用户ID(PASID)')
    whether_leader = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否是leader')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    defunct = db.Column(db.Integer, nullable=False, info='是否删除 0 否 1是')



class CrmPmGroup(db.Model):
    __tablename__ = 'crm_pm_group'

    id = db.Column(db.BigInteger, primary_key=True, info='主键Id，组ID')
    group_name = db.Column(db.String(256), nullable=False, info='组名称')
    parent_group_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='父组ID')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    defunct = db.Column(db.Integer, nullable=False, index=True, info='是否删除 0 否 1是')



class CrmPmGroupUser(db.Model):
    __tablename__ = 'crm_pm_group_user'

    id = db.Column(db.BigInteger, primary_key=True, info='主键Id，组ID')
    group_id = db.Column(db.BigInteger, nullable=False, info='组ID')
    user_id = db.Column(db.BigInteger, nullable=False, info='用户ID')
    whether_leader = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否是leader')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    defunct = db.Column(db.Integer, nullable=False, info='是否删除 0 否 1是')



class CrmServiceBusinessCard(db.Model):
    __tablename__ = 'crm_service_business_card'

    id = db.Column(db.BigInteger, primary_key=True, info='主键Id')
    user_id = db.Column(db.BigInteger, nullable=False, index=True, info='用户ID tb_user 表 user_info_id')
    self_introduction = db.Column(db.String(2000), info='个人介绍')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    defunct = db.Column(db.Integer, nullable=False, index=True, info='是否删除 0 否 1是')
    respondeat_superior = db.Column(db.String(2000), nullable=False, info='主要负责雇主')



class TbAdvertisementChannel(db.Model):
    __tablename__ = 'tb_advertisement_channel'
    __table_args__ = (
        db.Index('menu_key', 'menu_key', 'defunct'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    menu_key = db.Column(db.String(31), nullable=False, info='广告系统菜单表menu_key字段')
    channel_key = db.Column(db.String(63), nullable=False, info='频道key')
    channel_name = db.Column(db.String(63), nullable=False, info='频道名称')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='逻辑删除')
    create_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.Integer)



class TbAdvertisementConfRelation(db.Model):
    __tablename__ = 'tb_advertisement_conf_relation'

    id = db.Column(db.BigInteger, primary_key=True)
    pc_conf_id = db.Column(db.BigInteger, index=True)
    h5_conf_id = db.Column(db.BigInteger)
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='逻辑删除')
    create_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.Integer)



class TbAdvertisementLocation(db.Model):
    __tablename__ = 'tb_advertisement_location'
    __table_args__ = (
        db.Index('channel_key', 'channel_key', 'defunct'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    channel_key = db.Column(db.String(63), nullable=False, info='tb_advertisement_channel表的channel_key')
    location_key = db.Column(db.String(63), nullable=False, info='广告位定位key')
    location_title = db.Column(db.String(63), info='广告位标题')
    location_info = db.Column(db.String(255), info='广告位描述信息')
    display_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='广告位展示方式；1：固定，2：流式')
    display_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='广告位展示数量上限；对于固定位置和数量的广告位，比如4；则最多展示最早创建且有效的广告位配置；对于流式广告配置，则展示有效期内的配置数量')
    example_img_url = db.Column(db.String(255), info='示例图片路径；绝对路径直接展示；相对路径会经过转换')
    example_img_width = db.Column(db.Integer, server_default=db.FetchedValue(), info='示例图片宽度')
    example_img_height = db.Column(db.Integer, server_default=db.FetchedValue(), info='示例图片高度')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='逻辑删除')
    create_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)



class TbAdvertisementLocationConf(db.Model):
    __tablename__ = 'tb_advertisement_location_conf'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    location_id = db.Column(db.BigInteger, nullable=False, index=True, info='广告位基本信息表主键')
    location_key = db.Column(db.String(63), nullable=False, index=True, info='广告位基本信息表key')
    conf_title = db.Column(db.String(63), info='广告配置的标题')
    conf_info = db.Column(db.String(255), info='描述')
    conf_status = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='广告上线下线状态；1：上线；0：下线')
    img_url = db.Column(db.String(512), nullable=False, info='广告图地址')
    link_url = db.Column(db.String(255), nullable=False, info='连接地址')
    start_time = db.Column(db.DateTime, info='有效期开始，可以为空，表示立即生效')
    end_time = db.Column(db.DateTime, info='有效期结束，可以为空，表示不限')
    sort_value = db.Column(db.Integer, server_default=db.FetchedValue(), info='排序值；越大，越靠前')
    defunct = db.Column(db.Integer, index=True, info='逻辑删除')
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)



class TbAdvertisementLocationConfMessage(db.Model):
    __tablename__ = 'tb_advertisement_location_conf_message'

    id = db.Column(db.BigInteger, primary_key=True)
    conf_id = db.Column(db.BigInteger, index=True, info='tb_advertisement_location_conf表主键')
    message_title = db.Column(db.String(255), info='广告对应消息的内容')
    send_status = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='消息是否发出去；0：未发，1：已发')
    send_time = db.Column(db.DateTime, info='消息发送时间')
    defunct = db.Column(db.Integer, index=True, info='逻辑删除')
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)



class TbAdvertisementMenu(db.Model):
    __tablename__ = 'tb_advertisement_menu'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    pid = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='上级菜单主键')
    menu_key = db.Column(db.String(31), nullable=False, info='菜单key')
    menu_name = db.Column(db.String(31), nullable=False, info='菜单名字')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='逻辑删除')
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)



class TbAuthMenu(db.Model):
    __tablename__ = 'tb_auth_menu'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    name = db.Column(db.String(60), nullable=False, server_default=db.FetchedValue(), info='菜单名称')
    key_name = db.Column(db.String(60), nullable=False)
    url = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='菜单url')
    parent = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='父菜单ID')
    sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序位置')
    remark = db.Column(db.String(60), nullable=False, server_default=db.FetchedValue(), info='备注')
    valid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否有效， 0 无效， 1有效')
    version = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='版本号 0 旧版 1 TDCV4')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新人')



class TbAuthOperation(db.Model):
    __tablename__ = 'tb_auth_operation'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    name = db.Column(db.String(180), info='操作名称')
    menu_id = db.Column(db.BigInteger, info='菜单ID')
    type = db.Column(db.Integer, info='1 查询类型 ， 2 更新类型')
    columns = db.Column(db.String(3000), info='查询中字段的控制: 格式为json字符串{"字段名":"中文解释"}')
    valid = db.Column(db.Integer, info='是否有效， 0 无效， 1有效')
    version = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='版本号 0 旧版 1 TDCV4')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='更新时间')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    update_user_id = db.Column(db.BigInteger, info='更新人')



class TbAuthOperationBak20150918(db.Model):
    __tablename__ = 'tb_auth_operation_bak20150918'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    name = db.Column(db.String(60), nullable=False, info='操作名称')
    menu_id = db.Column(db.BigInteger, nullable=False, info='菜单ID')
    type = db.Column(db.Integer, nullable=False, info='1 查询类型 ， 2 更新类型')
    columns = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='查询中字段的控制: 格式为json字符串{"字段名":"中文解释"}')
    valid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否有效， 0 无效， 1有效')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新人')



class TbAuthOperationUrl(db.Model):
    __tablename__ = 'tb_auth_operation_url'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    operation_id = db.Column(db.BigInteger, info='操作id')
    url = db.Column(db.String(135), info='操作url')
    version = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='版本号 0 旧版 1 TDCV4')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='更新时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新人')



class TbAuthOperationUrlBak20150918(db.Model):
    __tablename__ = 'tb_auth_operation_url_bak20150918'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    operation_id = db.Column(db.BigInteger, nullable=False, info='操作id')
    url = db.Column(db.String(45), nullable=False, server_default=db.FetchedValue(), info='操作url')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新人')



t_tb_auth_operation_url_bak20160111 = db.Table(
    'tb_auth_operation_url_bak20160111',
    db.Column('id', db.BigInteger),
    db.Column('operation_id', db.BigInteger),
    db.Column('url', db.String(135)),
    db.Column('create_time', db.DateTime),
    db.Column('update_time', db.DateTime),
    db.Column('create_user_id', db.BigInteger),
    db.Column('update_user_id', db.BigInteger)
)



class TbAuthOrganization(db.Model):
    __tablename__ = 'tb_auth_organization'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    name = db.Column(db.String(60), nullable=False, info='组织名称')
    parent = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='父组id')
    remark = db.Column(db.String(60), nullable=False, server_default=db.FetchedValue(), info='备注')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0:未删除,1:已删除')



class TbAuthPoPam(db.Model):
    __tablename__ = 'tb_auth_po_pam'

    id = db.Column(db.Integer, primary_key=True, info='主键ID')
    po_id = db.Column(db.BigInteger, info='po')
    auth_type = db.Column(db.Integer, info='权限类型')
    pam_ids = db.Column(db.String(255), info='被授权的PAM')
    create_time = db.Column(db.DateTime, info='创建时间')
    updae_time = db.Column(db.DateTime, info='更新时间')



class TbAuthRole(db.Model):
    __tablename__ = 'tb_auth_role'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    name = db.Column(db.String(60), nullable=False, info='角色名称')
    remark = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='备注')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新人')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0:未删除,1:已删除')



class TbAuthRoleMenuoperation(db.Model):
    __tablename__ = 'tb_auth_role_menuoperation'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    role_id = db.Column(db.BigInteger, nullable=False, info='角色Id')
    menuoperation_id = db.Column(db.BigInteger, nullable=False, info='菜单id或操作id或组id')
    columns = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='赋予角色查询，对应的字段过滤')
    type = db.Column(db.Integer, nullable=False, info='1：菜单 , 2：操作, 3：组')
    version = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='版本号 0 旧版 1 TDCV4')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新人')



class TbAuthUserGroup(db.Model):
    __tablename__ = 'tb_auth_user_group'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    group_name = db.Column(db.String(60), nullable=False, info='组名')
    user_ids = db.Column(db.String(5000), nullable=False, info='用户id，逗号隔开')
    type = db.Column(db.Integer, nullable=False, info='1:基础组, 2:其它')
    remark = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='备注')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新人')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0:未删除,1:已删除')



class TbAuthUserMenuoperation(db.Model):
    __tablename__ = 'tb_auth_user_menuoperation'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    user_id = db.Column(db.BigInteger, nullable=False, info='用户ID')
    menuoperation_id = db.Column(db.BigInteger, nullable=False, info='菜单id或操作id或组id')
    columns = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='赋予用户查询，对应的字段过滤')
    type = db.Column(db.Integer, nullable=False, info='1：菜单 , 2：操作, 3：组')
    version = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='版本号 0 旧版 1 TDCV4')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新人')



class TbAuthUserOrganization(db.Model):
    __tablename__ = 'tb_auth_user_organization'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    orga_id = db.Column(db.BigInteger, nullable=False, index=True, info='组织结构ID')
    user_id = db.Column(db.BigInteger, nullable=False, index=True, info='用户ID')
    leader = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否是leader  0 不是 ，  1是')
    is_main_org = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='该组是否是用户的主要组织')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新人')
    user_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='crm用户状态:1:正在,2:离职,3:删除')
    is_in_org = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='该用户是否在当前组织')



class TbAuthUserRole(db.Model):
    __tablename__ = 'tb_auth_user_role'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_id = db.Column(db.BigInteger, nullable=False, index=True, info='用户ID')
    role_id = db.Column(db.BigInteger, nullable=False, info='角色ID')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新人')
    user_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='crm用户状态:1:正在,2:离职,3:删除')



class TbAuthUserValidate(db.Model):
    __tablename__ = 'tb_auth_user_validate'

    user_id = db.Column(db.BigInteger, nullable=False)
    UUID = db.Column(db.String(40), nullable=False)
    valid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否有效， 0 无效， 1有效')
    expiry_date = db.Column(db.DateTime, nullable=False, info='有效期')
    type = db.Column(db.Integer, nullable=False, info='类型：1，找回密码')
    id = db.Column(db.BigInteger, primary_key=True)



class TbCallCtsHd(db.Model):
    __tablename__ = 'tb_call_cts_hd'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201507(db.Model):
    __tablename__ = 'tb_call_cts_hd201507'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201508(db.Model):
    __tablename__ = 'tb_call_cts_hd201508'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201509(db.Model):
    __tablename__ = 'tb_call_cts_hd201509'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201510(db.Model):
    __tablename__ = 'tb_call_cts_hd201510'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201511(db.Model):
    __tablename__ = 'tb_call_cts_hd201511'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201512(db.Model):
    __tablename__ = 'tb_call_cts_hd201512'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201601(db.Model):
    __tablename__ = 'tb_call_cts_hd201601'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201602(db.Model):
    __tablename__ = 'tb_call_cts_hd201602'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201603(db.Model):
    __tablename__ = 'tb_call_cts_hd201603'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201604(db.Model):
    __tablename__ = 'tb_call_cts_hd201604'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201605(db.Model):
    __tablename__ = 'tb_call_cts_hd201605'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201606(db.Model):
    __tablename__ = 'tb_call_cts_hd201606'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201607(db.Model):
    __tablename__ = 'tb_call_cts_hd201607'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201608(db.Model):
    __tablename__ = 'tb_call_cts_hd201608'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201609(db.Model):
    __tablename__ = 'tb_call_cts_hd201609'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201610(db.Model):
    __tablename__ = 'tb_call_cts_hd201610'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201611(db.Model):
    __tablename__ = 'tb_call_cts_hd201611'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201612(db.Model):
    __tablename__ = 'tb_call_cts_hd201612'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201701(db.Model):
    __tablename__ = 'tb_call_cts_hd201701'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201702(db.Model):
    __tablename__ = 'tb_call_cts_hd201702'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201703(db.Model):
    __tablename__ = 'tb_call_cts_hd201703'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201704(db.Model):
    __tablename__ = 'tb_call_cts_hd201704'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201705(db.Model):
    __tablename__ = 'tb_call_cts_hd201705'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201706(db.Model):
    __tablename__ = 'tb_call_cts_hd201706'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201707(db.Model):
    __tablename__ = 'tb_call_cts_hd201707'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201708(db.Model):
    __tablename__ = 'tb_call_cts_hd201708'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201709(db.Model):
    __tablename__ = 'tb_call_cts_hd201709'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201710(db.Model):
    __tablename__ = 'tb_call_cts_hd201710'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201711(db.Model):
    __tablename__ = 'tb_call_cts_hd201711'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201712(db.Model):
    __tablename__ = 'tb_call_cts_hd201712'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201801(db.Model):
    __tablename__ = 'tb_call_cts_hd201801'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201802(db.Model):
    __tablename__ = 'tb_call_cts_hd201802'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201803(db.Model):
    __tablename__ = 'tb_call_cts_hd201803'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201804(db.Model):
    __tablename__ = 'tb_call_cts_hd201804'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201805(db.Model):
    __tablename__ = 'tb_call_cts_hd201805'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201806(db.Model):
    __tablename__ = 'tb_call_cts_hd201806'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201807(db.Model):
    __tablename__ = 'tb_call_cts_hd201807'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201808(db.Model):
    __tablename__ = 'tb_call_cts_hd201808'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201809(db.Model):
    __tablename__ = 'tb_call_cts_hd201809'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201810(db.Model):
    __tablename__ = 'tb_call_cts_hd201810'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201811(db.Model):
    __tablename__ = 'tb_call_cts_hd201811'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201812(db.Model):
    __tablename__ = 'tb_call_cts_hd201812'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201901(db.Model):
    __tablename__ = 'tb_call_cts_hd201901'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201902(db.Model):
    __tablename__ = 'tb_call_cts_hd201902'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201903(db.Model):
    __tablename__ = 'tb_call_cts_hd201903'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201904(db.Model):
    __tablename__ = 'tb_call_cts_hd201904'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201905(db.Model):
    __tablename__ = 'tb_call_cts_hd201905'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201906(db.Model):
    __tablename__ = 'tb_call_cts_hd201906'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201907(db.Model):
    __tablename__ = 'tb_call_cts_hd201907'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201908(db.Model):
    __tablename__ = 'tb_call_cts_hd201908'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201909(db.Model):
    __tablename__ = 'tb_call_cts_hd201909'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201910(db.Model):
    __tablename__ = 'tb_call_cts_hd201910'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd201911(db.Model):
    __tablename__ = 'tb_call_cts_hd201911'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallCtsHd202104(db.Model):
    __tablename__ = 'tb_call_cts_hd202104'

    id = db.Column(db.BigInteger, primary_key=True)
    callid = db.Column(db.String(18), info='呼叫编号（每次用户打入产生一个）')
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    username = db.Column(db.String(30), info='用户名称')
    trunk = db.Column(db.String(10), info='中继号码')
    trunkcalled = db.Column(db.String(20), info='呼入到中继线时的被叫号码')
    direction = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫方向 0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    dest_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫入时，目标类型 0：未知  1：路由点  2：IVR  3：座席分机 4：其它分机  5：外线号码')
    ext = db.Column(db.String(15), info='分机号码，根据 dest_type 决定 DEST_TYPE =1：路由点号  2：IVR分机号  3：坐席分机号')
    ghid = db.Column(db.String(20), info='座席人员工号-接答 ')
    op_name = db.Column(db.String(20), info='座席员姓名')
    groups = db.Column(db.String(20), info='ACD组号')
    sdate = db.Column(db.String(8), info='通话日期（20020704）')
    edate = db.Column(db.String(8), info='结束日期（20020704）')
    stime = db.Column(db.String(6), info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len_ring = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='振铃时长（秒）')
    len_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通话时长（秒）')
    trans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='呼叫转接标志，0：一次呼叫  1：转入，2：转出  3：转入+转出  4：代接 5：代接+转出  6：被代接')
    ext_in = db.Column(db.String(15), info='分机号码  转入')
    ext_out = db.Column(db.String(15), info='分机号码  转出')
    calltype = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='呼叫话单类型：0：正常通话话单   10：表示外线排队等待的话单')
    qn_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队的类型  1：表示在分组上排队  2：表示在坐席上排队 3：表示在分机上排队')
    qn_dest = db.Column(db.String(20), info='表示排队的目标，根据 QN_TYPE 决定  qn_type=1，表示组号  2：工号  3：分机号  4：IVR端口号')
    qn_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='表示排队开始原因   1：表示全忙进入排队  2：表示无人接听进入排队 3：表示其它原因进入排队')
    qn_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排队结束原因  1：表示成功转入  2：表示挂断，排队失败  3：表示其它原因 21：超时')
    disc_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='挂机标志  0：未知  1：主叫先挂  2：坐席先挂')
    callid_1 = db.Column(db.String(18), info='呼叫编号1（交换机原始ID,如:avaya)')



class TbCallLogTelhd(db.Model):
    __tablename__ = 'tb_call_log_telhd'

    id = db.Column(db.BigInteger, primary_key=True)
    serverid = db.Column(db.SmallInteger, nullable=False)
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    op_flag = db.Column(db.SmallInteger)
    msg_type = db.Column(db.SmallInteger, info='呼叫方向   0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    sdate = db.Column(db.String(8), nullable=False, info='通话日期（20020704）')
    stime = db.Column(db.String(6), nullable=False, info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len = db.Column(db.Integer, nullable=False, info='通话时长（秒）')
    lenm = db.Column(db.Integer, nullable=False, info='通话时长（分）')
    chnum = db.Column(db.SmallInteger, nullable=False, info='录音通道号')
    file_path = db.Column(db.String(250), info='录音存放物理路径 如：d:\\recwav20141008ch005c091822.wav')
    file_label = db.Column(db.String(10))
    opid = db.Column(db.String(12), info='座席人员工号')
    ucid = db.Column(db.String(21), nullable=False, info='呼叫标识（唯一编号）')
    info1 = db.Column(db.String(100))
    info2 = db.Column(db.String(100))
    info3 = db.Column(db.String(100))
    info4 = db.Column(db.String(100))
    status = db.Column(db.SmallInteger, nullable=False)
    screencopy = db.Column(db.String(256))
    event_code = db.Column(db.String(20))
    iscode = db.Column(db.SmallInteger, nullable=False)
    score = db.Column(db.Numeric(18, 0))
    state = db.Column(db.SmallInteger, nullable=False)
    temp_id = db.Column(db.SmallInteger)
    upload_file = db.Column(db.String(250))
    backup_flag = db.Column(db.SmallInteger)



class TbCallLogTelhd201507(db.Model):
    __tablename__ = 'tb_call_log_telhd201507'

    id = db.Column(db.BigInteger, primary_key=True)
    serverid = db.Column(db.SmallInteger, nullable=False)
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    op_flag = db.Column(db.SmallInteger)
    msg_type = db.Column(db.SmallInteger, info='呼叫方向   0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    sdate = db.Column(db.String(8), nullable=False, info='通话日期（20020704）')
    stime = db.Column(db.String(6), nullable=False, info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len = db.Column(db.Integer, nullable=False, info='通话时长（秒）')
    lenm = db.Column(db.Integer, nullable=False, info='通话时长（分）')
    chnum = db.Column(db.SmallInteger, nullable=False, info='录音通道号')
    file_path = db.Column(db.String(250), info='录音存放物理路径 如：d:\\recwav20141008ch005c091822.wav')
    file_label = db.Column(db.String(10))
    opid = db.Column(db.String(12), info='座席人员工号')
    ucid = db.Column(db.String(21), nullable=False, info='呼叫标识（唯一编号）')
    info1 = db.Column(db.String(100))
    info2 = db.Column(db.String(100))
    info3 = db.Column(db.String(100))
    info4 = db.Column(db.String(100))
    status = db.Column(db.SmallInteger, nullable=False)
    screencopy = db.Column(db.String(256))
    event_code = db.Column(db.String(20))
    iscode = db.Column(db.SmallInteger, nullable=False)
    score = db.Column(db.Numeric(18, 0))
    state = db.Column(db.SmallInteger, nullable=False)
    temp_id = db.Column(db.SmallInteger)
    upload_file = db.Column(db.String(250))
    backup_flag = db.Column(db.SmallInteger)



class TbCallLogTelhd201508(db.Model):
    __tablename__ = 'tb_call_log_telhd201508'

    id = db.Column(db.BigInteger, primary_key=True)
    serverid = db.Column(db.SmallInteger, nullable=False)
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    op_flag = db.Column(db.SmallInteger)
    msg_type = db.Column(db.SmallInteger, info='呼叫方向   0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    sdate = db.Column(db.String(8), nullable=False, info='通话日期（20020704）')
    stime = db.Column(db.String(6), nullable=False, info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len = db.Column(db.Integer, nullable=False, info='通话时长（秒）')
    lenm = db.Column(db.Integer, nullable=False, info='通话时长（分）')
    chnum = db.Column(db.SmallInteger, nullable=False, info='录音通道号')
    file_path = db.Column(db.String(250), info='录音存放物理路径 如：d:\\recwav20141008ch005c091822.wav')
    file_label = db.Column(db.String(10))
    opid = db.Column(db.String(12), info='座席人员工号')
    ucid = db.Column(db.String(21), nullable=False, info='呼叫标识（唯一编号）')
    info1 = db.Column(db.String(100))
    info2 = db.Column(db.String(100))
    info3 = db.Column(db.String(100))
    info4 = db.Column(db.String(100))
    status = db.Column(db.SmallInteger, nullable=False)
    screencopy = db.Column(db.String(256))
    event_code = db.Column(db.String(20))
    iscode = db.Column(db.SmallInteger, nullable=False)
    score = db.Column(db.Numeric(18, 0))
    state = db.Column(db.SmallInteger, nullable=False)
    temp_id = db.Column(db.SmallInteger)
    upload_file = db.Column(db.String(250))
    backup_flag = db.Column(db.SmallInteger)



class TbCallLogTelhd201509(db.Model):
    __tablename__ = 'tb_call_log_telhd201509'

    id = db.Column(db.BigInteger, primary_key=True)
    serverid = db.Column(db.SmallInteger, nullable=False)
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    op_flag = db.Column(db.SmallInteger)
    msg_type = db.Column(db.SmallInteger, info='呼叫方向   0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    sdate = db.Column(db.String(8), nullable=False, info='通话日期（20020704）')
    stime = db.Column(db.String(6), nullable=False, info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len = db.Column(db.Integer, nullable=False, info='通话时长（秒）')
    lenm = db.Column(db.Integer, nullable=False, info='通话时长（分）')
    chnum = db.Column(db.SmallInteger, nullable=False, info='录音通道号')
    file_path = db.Column(db.String(250), info='录音存放物理路径 如：d:\\recwav20141008ch005c091822.wav')
    file_label = db.Column(db.String(10))
    opid = db.Column(db.String(12), info='座席人员工号')
    ucid = db.Column(db.String(21), nullable=False, info='呼叫标识（唯一编号）')
    info1 = db.Column(db.String(100))
    info2 = db.Column(db.String(100))
    info3 = db.Column(db.String(100))
    info4 = db.Column(db.String(100))
    status = db.Column(db.SmallInteger, nullable=False)
    screencopy = db.Column(db.String(256))
    event_code = db.Column(db.String(20))
    iscode = db.Column(db.SmallInteger, nullable=False)
    score = db.Column(db.Numeric(18, 0))
    state = db.Column(db.SmallInteger, nullable=False)
    temp_id = db.Column(db.SmallInteger)
    upload_file = db.Column(db.String(250))
    backup_flag = db.Column(db.SmallInteger)



class TbCallLogTelhd201510(db.Model):
    __tablename__ = 'tb_call_log_telhd201510'

    id = db.Column(db.BigInteger, primary_key=True)
    serverid = db.Column(db.SmallInteger, nullable=False)
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    op_flag = db.Column(db.SmallInteger)
    msg_type = db.Column(db.SmallInteger, info='呼叫方向   0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    sdate = db.Column(db.String(8), nullable=False, info='通话日期（20020704）')
    stime = db.Column(db.String(6), nullable=False, info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len = db.Column(db.Integer, nullable=False, info='通话时长（秒）')
    lenm = db.Column(db.Integer, nullable=False, info='通话时长（分）')
    chnum = db.Column(db.SmallInteger, nullable=False, info='录音通道号')
    file_path = db.Column(db.String(250), info='录音存放物理路径 如：d:\\recwav20141008ch005c091822.wav')
    file_label = db.Column(db.String(10))
    opid = db.Column(db.String(12), info='座席人员工号')
    ucid = db.Column(db.String(21), nullable=False, info='呼叫标识（唯一编号）')
    info1 = db.Column(db.String(100))
    info2 = db.Column(db.String(100))
    info3 = db.Column(db.String(100))
    info4 = db.Column(db.String(100))
    status = db.Column(db.SmallInteger, nullable=False)
    screencopy = db.Column(db.String(256))
    event_code = db.Column(db.String(20))
    iscode = db.Column(db.SmallInteger, nullable=False)
    score = db.Column(db.Numeric(18, 0))
    state = db.Column(db.SmallInteger, nullable=False)
    temp_id = db.Column(db.SmallInteger)
    upload_file = db.Column(db.String(250))
    backup_flag = db.Column(db.SmallInteger)



class TbCallLogTelhd201511(db.Model):
    __tablename__ = 'tb_call_log_telhd201511'

    id = db.Column(db.BigInteger, primary_key=True)
    serverid = db.Column(db.SmallInteger, nullable=False)
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    op_flag = db.Column(db.SmallInteger)
    msg_type = db.Column(db.SmallInteger, info='呼叫方向   0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    sdate = db.Column(db.String(8), nullable=False, info='通话日期（20020704）')
    stime = db.Column(db.String(6), nullable=False, info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len = db.Column(db.Integer, nullable=False, info='通话时长（秒）')
    lenm = db.Column(db.Integer, nullable=False, info='通话时长（分）')
    chnum = db.Column(db.SmallInteger, nullable=False, info='录音通道号')
    file_path = db.Column(db.String(250), info='录音存放物理路径 如：d:\\recwav20141008ch005c091822.wav')
    file_label = db.Column(db.String(10))
    opid = db.Column(db.String(12), info='座席人员工号')
    ucid = db.Column(db.String(21), nullable=False, info='呼叫标识（唯一编号）')
    info1 = db.Column(db.String(100))
    info2 = db.Column(db.String(100))
    info3 = db.Column(db.String(100))
    info4 = db.Column(db.String(100))
    status = db.Column(db.SmallInteger, nullable=False)
    screencopy = db.Column(db.String(256))
    event_code = db.Column(db.String(20))
    iscode = db.Column(db.SmallInteger, nullable=False)
    score = db.Column(db.Numeric(18, 0))
    state = db.Column(db.SmallInteger, nullable=False)
    temp_id = db.Column(db.SmallInteger)
    upload_file = db.Column(db.String(250))
    backup_flag = db.Column(db.SmallInteger)



class TbCallLogTelhd201512(db.Model):
    __tablename__ = 'tb_call_log_telhd201512'

    id = db.Column(db.BigInteger, primary_key=True)
    serverid = db.Column(db.SmallInteger, nullable=False)
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    op_flag = db.Column(db.SmallInteger)
    msg_type = db.Column(db.SmallInteger, info='呼叫方向   0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    sdate = db.Column(db.String(8), nullable=False, info='通话日期（20020704）')
    stime = db.Column(db.String(6), nullable=False, info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len = db.Column(db.Integer, nullable=False, info='通话时长（秒）')
    lenm = db.Column(db.Integer, nullable=False, info='通话时长（分）')
    chnum = db.Column(db.SmallInteger, nullable=False, info='录音通道号')
    file_path = db.Column(db.String(250), info='录音存放物理路径 如：d:\\recwav20141008ch005c091822.wav')
    file_label = db.Column(db.String(10))
    opid = db.Column(db.String(12), info='座席人员工号')
    ucid = db.Column(db.String(21), nullable=False, info='呼叫标识（唯一编号）')
    info1 = db.Column(db.String(100))
    info2 = db.Column(db.String(100))
    info3 = db.Column(db.String(100))
    info4 = db.Column(db.String(100))
    status = db.Column(db.SmallInteger, nullable=False)
    screencopy = db.Column(db.String(256))
    event_code = db.Column(db.String(20))
    iscode = db.Column(db.SmallInteger, nullable=False)
    score = db.Column(db.Numeric(18, 0))
    state = db.Column(db.SmallInteger, nullable=False)
    temp_id = db.Column(db.SmallInteger)
    upload_file = db.Column(db.String(250))
    backup_flag = db.Column(db.SmallInteger)



class TbCallLogTelhd201601(db.Model):
    __tablename__ = 'tb_call_log_telhd201601'

    id = db.Column(db.BigInteger, primary_key=True)
    serverid = db.Column(db.SmallInteger, nullable=False)
    caller = db.Column(db.String(30), info='主叫号码')
    called = db.Column(db.String(30), info='被叫号码')
    op_flag = db.Column(db.SmallInteger)
    msg_type = db.Column(db.SmallInteger, info='呼叫方向   0：未知  1：外线呼入  2：外线呼出  3：内线呼入 4：内线呼出')
    sdate = db.Column(db.String(8), nullable=False, info='通话日期（20020704）')
    stime = db.Column(db.String(6), nullable=False, info='起始时间（083000）')
    etime = db.Column(db.String(6), info='结束时间（083507）')
    len = db.Column(db.Integer, nullable=False, info='通话时长（秒）')
    lenm = db.Column(db.Integer, nullable=False, info='通话时长（分）')
    chnum = db.Column(db.SmallInteger, nullable=False, info='录音通道号')
    file_path = db.Column(db.String(250), info='录音存放物理路径 如：d:\\recwav20141008ch005c091822.wav')
    file_label = db.Column(db.String(10))
    opid = db.Column(db.String(12), info='座席人员工号')
    ucid = db.Column(db.String(21), nullable=False, info='呼叫标识（唯一编号）')
    info1 = db.Column(db.String(100))
    info2 = db.Column(db.String(100))
    info3 = db.Column(db.String(100))
    info4 = db.Column(db.String(100))
    status = db.Column(db.SmallInteger, nullable=False)
    screencopy = db.Column(db.String(256))
    event_code = db.Column(db.String(20))
    iscode = db.Column(db.SmallInteger, nullable=False)
    score = db.Column(db.Numeric(18, 0))
    state = db.Column(db.SmallInteger, nullable=False)
    temp_id = db.Column(db.SmallInteger)
    upload_file = db.Column(db.String(250))
    backup_flag = db.Column(db.SmallInteger)



class TbCallVipTel(db.Model):
    __tablename__ = 'tb_call_vip_tel'

    id = db.Column(db.BigInteger, primary_key=True)
    ghid = db.Column(db.String(40), info='转接的工号')
    tel = db.Column(db.String(20), info='电话号码')



class TbClue(db.Model):
    __tablename__ = 'tb_clue'

    id = db.Column(db.BigInteger, primary_key=True, info='主键id')
    name = db.Column(db.String(256), nullable=False, info='公司名称')
    display_name = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue(), info='显示名称')
    short_name = db.Column(db.String(256), info='简称')
    investigate_id = db.Column(db.BigInteger, info='企调id')
    province_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='省id')
    city_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='城市id')
    address = db.Column(db.String(256), info='地址')
    introduce = db.Column(db.Text, info='公司简介')
    industry_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='行业id')
    other_industry_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='行业id')
    industry_ids = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue())
    establish_year = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='成立年份')
    logo = db.Column(db.String(256), info='logo')
    scale = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='规模')
    style = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='性质')
    channel = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='录入方式：0 hr注册；1 系统录入；2 注册匹配')
    web_site = db.Column(db.String(256), info='网址')
    bdo_id = db.Column(db.BigInteger, info='销售负责人BDO')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='修改时间')
    approve_time = db.Column(db.DateTime, info='线索转客户时间')
    enterprise_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='客户id')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='（0 黄页，1 公海，2 线索，3 客户，4垃圾库）')
    defunt = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除')



class TbClueBak20151030(db.Model):
    __tablename__ = 'tb_clue_bak20151030'

    id = db.Column(db.BigInteger, primary_key=True, info='主键id')
    name = db.Column(db.String(256), nullable=False, info='公司名称')
    short_name = db.Column(db.String(256), info='简称')
    investigate_id = db.Column(db.BigInteger, info='企调id')
    province_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='省id')
    city_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='城市id')
    address = db.Column(db.String(256), info='地址')
    introduce = db.Column(db.Text, info='公司简介')
    industry_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='行业id')
    other_industry_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='行业id')
    logo = db.Column(db.String(256), info='logo')
    scale = db.Column(db.BigInteger, info='规模')
    style = db.Column(db.BigInteger, info='性质')
    channel = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='录入方式：0 hr注册；1 系统录入；2 注册匹配')
    web_site = db.Column(db.String(256), info='网址')
    bdo_id = db.Column(db.BigInteger, info='销售负责人BDO')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='修改时间')
    approve_time = db.Column(db.DateTime, info='线索转客户时间')
    enterprise_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='客户id')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='（0 黄页，1 公海，2 线索，3 客户，4垃圾库）')
    defunt = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除')



class TbClueBak20151102(db.Model):
    __tablename__ = 'tb_clue_bak20151102'

    id = db.Column(db.BigInteger, primary_key=True, info='主键id')
    name = db.Column(db.String(256), nullable=False, info='公司名称')
    short_name = db.Column(db.String(256), info='简称')
    investigate_id = db.Column(db.BigInteger, info='企调id')
    province_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='省id')
    city_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='城市id')
    address = db.Column(db.String(256), info='地址')
    introduce = db.Column(db.Text, info='公司简介')
    industry_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='行业id')
    other_industry_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='行业id')
    logo = db.Column(db.String(256), info='logo')
    scale = db.Column(db.BigInteger, info='规模')
    style = db.Column(db.BigInteger, info='性质')
    channel = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='录入方式：0 hr注册；1 系统录入；2 注册匹配')
    web_site = db.Column(db.String(256), info='网址')
    bdo_id = db.Column(db.BigInteger, info='销售负责人BDO')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='修改时间')
    approve_time = db.Column(db.DateTime, info='线索转客户时间')
    enterprise_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='客户id')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='（0 黄页，1 公海，2 线索，3 客户，4垃圾库）')
    defunt = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除')



class TbCollectHeadhunter(db.Model):
    __tablename__ = 'tb_collect_headhunter'

    id = db.Column(db.BigInteger, primary_key=True)
    headhunter_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎头id')
    position_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职位编号')
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否收藏:0:取消收藏, 1:收藏')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人ID')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新人ID')



class TbContact(db.Model):
    __tablename__ = 'tb_contact'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    name = db.Column(db.String(256), nullable=False, info='名字')
    email = db.Column(db.String(128), info='email')
    mobile = db.Column(db.String(128), info='手机')
    gender = db.Column(db.Integer, info='性别: 0 女 1 男 ')
    phone = db.Column(db.String(128), info='手机')
    qq = db.Column(db.String(128), info='qq')



class TbCrmBdoChangeLog(db.Model):
    __tablename__ = 'tb_crm_bdo_change_log'

    id = db.Column(db.BigInteger, primary_key=True)
    obj_id = db.Column(db.BigInteger, nullable=False, info='对象id')
    obj_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='对象类型, 1:企业, 2:手动录入的企业')
    before_bdo_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改前的bdo id')
    after_bdo_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改后的bdo id')
    comment = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='修改bdo的备注')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbCrmCollect(db.Model):
    __tablename__ = 'tb_crm_collect'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    obj_id = db.Column(db.BigInteger, nullable=False, info='对象id')
    obj_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='对象类型')
    content = db.Column(db.Text, nullable=False, info='内容')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')



class TbCrmComment(db.Model):
    __tablename__ = 'tb_crm_comment'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    obj_id = db.Column(db.BigInteger, nullable=False, index=True, info='对象id')
    obj_type = db.Column(db.Integer, nullable=False, info='1:企业, 2:线索, 3:成单, 4:HR, 5:职位, 6:猎头, 7:猎头公司, 8:订单 ')
    contact_start_time = db.Column(db.DateTime, info='沟通的开始时间')
    contact_end_time = db.Column(db.DateTime, info='沟通的结束时间')
    contacter = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='联系人')
    phone = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='联系方式')
    comment = db.Column(db.Text, nullable=False, info='备注内容')
    contact_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='沟通类型: 1:上门拜访,2.电话联系,3.客户来访')
    attach_name = db.Column(db.String(1024), nullable=False, server_default=db.FetchedValue(), info='附件名称')
    attach_url = db.Column(db.String(1024), nullable=False, server_default=db.FetchedValue(), info='url')
    attach_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='附件类型:1:沟通记录附件, 2:一般附件')
    function_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='功能类型:1:添加沟通记录,2:添加附件')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否删除 0 否 1是')
    tag_ids = db.Column(db.String(100), info='标签ID列表')



class TbCrmCommentTag(db.Model):
    __tablename__ = 'tb_crm_comment_tag'

    id = db.Column(db.BigInteger, primary_key=True)
    tag_name = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='标签名称')
    enterprise_id = db.Column(db.BigInteger, index=True, info='企业ID')
    statistics_count = db.Column(db.Integer, server_default=db.FetchedValue(), info='统计数')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否删除 0 否 1是')



class TbCrmLogSnapshot(db.Model):
    __tablename__ = 'tb_crm_log_snapshot'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    log_id = db.Column(db.BigInteger, nullable=False, info='来自表tb_crm_sale_log的外键')
    class_name = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='快照对象类名')
    snapshot = db.Column(db.String, nullable=False, info='变更对象的快照内容')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbCrmOperateCandidateRecord(db.Model):
    __tablename__ = 'tb_crm_operate_candidate_record'

    id = db.Column(db.BigInteger, primary_key=True)
    candidate_id = db.Column(db.BigInteger, nullable=False, index=True, info='候选人id')
    user_id = db.Column(db.BigInteger, nullable=False, info='操作人id')
    operate_type = db.Column(db.Integer, nullable=False, info='操作类型，1：提前到岗确认，2：提前过保确认，3：内部备注')
    operate_value = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='操作结果，1：true，0：false')
    operate_desc = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='操作描述')
    confirm_time = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='预计时间')
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否操作，1：true，0：false')
    create_time = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='创建时间')
    invisible = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='不可见性，-1：不做隐藏，所有人可见，1：猎头不可见，2：hr不可见')



class TbCrmPositionEditLog(db.Model):
    __tablename__ = 'tb_crm_position_edit_log'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    position_id = db.Column(db.BigInteger, nullable=False, info='职位id')
    status_edit_before = db.Column(db.Integer, info='状态修改前')
    status_edit_after = db.Column(db.Integer, info='状态修改后')
    snapshot_edit_before = db.Column(db.String, info='快照前')
    snapshot_edit_after = db.Column(db.String, info='快照后')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbCrmPositionVarReport(db.Model):
    __tablename__ = 'tb_crm_position_var_report'

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, nullable=False, info='crm用户id')
    new_add_position_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='今日新增职位数')
    new_add_position_value = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='新增职位价值')
    count_date = db.Column(db.Date, nullable=False, info='统计日期')
    create_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())



class TbCrmSaleLog(db.Model):
    __tablename__ = 'tb_crm_sale_log'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    obj_id = db.Column(db.BigInteger, nullable=False, index=True, info='对象id')
    obj_type = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='对象类型, 1:企业, 2:猎头公司, 3:黄页, 4:待跟进')
    history = db.Column(db.String(500), nullable=False, index=True, server_default=db.FetchedValue(), info='修改对象绑定的销售历史记录')
    create_user_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbCrmSchedule(db.Model):
    __tablename__ = 'tb_crm_schedule'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    enterprise_id = db.Column(db.BigInteger, nullable=False, info='企业id')
    start_time = db.Column(db.DateTime, nullable=False, info='计划开始时间')
    content = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='计划内容描述')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新时间')



class TbCrmSignCompanyDayLog(db.Model):
    __tablename__ = 'tb_crm_sign_company_day_log'

    id = db.Column(db.BigInteger, primary_key=True)
    company_id = db.Column(db.BigInteger, nullable=False, info='猎企id')
    sign_date = db.Column(db.DateTime, nullable=False, info='签约日期')
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())



class TbCrmUserOperation(db.Model):
    __tablename__ = 'tb_crm_user_operation'

    id = db.Column(db.BigInteger, primary_key=True, info='自增主键')
    obj_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='操作数据编号')
    obj_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='操作数据类型 1 九宫格数据')
    operation_id = db.Column(db.BigInteger, nullable=False, info='操作编号')
    user_id = db.Column(db.BigInteger, nullable=False, index=True, info='用户编号')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, info='修改人')



class TbCrmUserPortrait(db.Model):
    __tablename__ = 'tb_crm_user_portrait'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    user_id = db.Column(db.BigInteger, nullable=False, info='用户id')
    sign_enterprise_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='签约企业数')
    sign_company_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='签约猎企数')
    count_date = db.Column(db.Date, nullable=False, info='统计时间')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')



class TbCrmUserPosition(db.Model):
    __tablename__ = 'tb_crm_user_position'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    position_title = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue(), info='用户职位')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')



class TbCrmUserSelfSet(db.Model):
    __tablename__ = 'tb_crm_user_self_set'

    user_id = db.Column(db.BigInteger, primary_key=True, info='crm用户id')
    recommend_feedback = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='查看新推反馈多少天以前的数据')
    interview_feedback = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='查看面试反馈多少天以前的数据')
    is_first_login = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否首次登陆,0:不是, 1:是')
    history_password = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='历史密码,多个以逗号分隔')
    white_ip_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='白名单表的id')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    last_change_pwd_time = db.Column(db.DateTime, info='最后一次改密时间')
    change_pwd_interval_month = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='每隔多少个月就需要改密')



class TbCrmWhiteIp(db.Model):
    __tablename__ = 'tb_crm_white_ip'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    ip_segment_start = db.Column(db.String(30), nullable=False, server_default=db.FetchedValue(), info='白名单IP段的开始范围,如果ip段的结束范围为空，此字段代表具体的ip地址')
    ip_segment_end = db.Column(db.String(30), nullable=False, server_default=db.FetchedValue(), info='白名单IP段的结束范围范围')
    start_time = db.Column(db.DateTime, info='白名单有效的开始时间,非空则不做限制')
    end_time = db.Column(db.DateTime, info='白名单有效的结束时间,非空则不做限制')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='白名单使用类型:1:上海猎上外网IP,2,深圳猎上外网IP,3:北京猎上外网IP, 4:crm用户的IP白名单,')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbCrmWorkOrder(db.Model):
    __tablename__ = 'tb_crm_work_order'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    handle_obj_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='处理对象类型:1:客户公司, 2:HR,3:职位,4:猎企, 5:猎头, 6:订单, 7:其他')
    obj_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='对象id')
    obj_name = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='处理对象名')
    handle_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='处理人id')
    handle_start_time = db.Column(db.DateTime, info='处理开始时间')
    handle_end_time = db.Column(db.DateTime, info='处理结束时间')
    handle_method_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='回复要求: 1:电话回复,2:IM回复,3:邮件回复,4:其他')
    contacter_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='联系人id')
    contacter = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='联系人姓名')
    contacter_method = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue(), info='联系人方式')
    contacter_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='联系人类型:1:猎头,2:HR,3:候选人')
    work_order_type_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='工单类型表id')
    work_order_handle_type_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='工单处理类型表id')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='工单状态:1:未处理,2:已处理')
    latest_content_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='work_order_content表中最新的工单内容')
    menu_data_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='主要为了区分处理对象为客户时，是线索客户还是企业客户')
    handle_finished_time = db.Column(db.DateTime, info='处理完成时间')
    assigner_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='分配人id')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')



class TbCrmWorkOrderContent(db.Model):
    __tablename__ = 'tb_crm_work_order_content'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    work_order_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='工单表id')
    content = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='工单对应的内容')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')



class TbCrmWorkOrderHandleType(db.Model):
    __tablename__ = 'tb_crm_work_order_handle_type'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    work_order_type_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='工单类型表的主键id')
    name = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='处理类型名')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')



class TbCrmWorkOrderType(db.Model):
    __tablename__ = 'tb_crm_work_order_type'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    work_order_handle_obj_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='对应工单表的处理对象类型')
    name = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='工单类型名')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')



class TbCustomerContact(db.Model):
    __tablename__ = 'tb_customer_contact'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    object_id = db.Column(db.BigInteger, nullable=False, index=True, info='对象id（包括客户线索和黄页）')
    type = db.Column(db.Integer, server_default=db.FetchedValue(), info='（0 黄页，1 公海，2 线索，3 客户，4垃圾库）')
    contact_id = db.Column(db.BigInteger, nullable=False, info='联系人id')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人id')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人id')
    create_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='修改时间')
    channel = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='录入方式：0 hr注册；1 系统录入；2 注册匹配')



class TbCustomerContactBak20151030(db.Model):
    __tablename__ = 'tb_customer_contact_bak20151030'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    object_id = db.Column(db.BigInteger, nullable=False, info='对象id（包括客户线索和黄页）')
    type = db.Column(db.Integer, server_default=db.FetchedValue(), info='（0 黄页，1 公海，2 线索，3 客户，4垃圾库）')
    contact_id = db.Column(db.BigInteger, nullable=False, info='联系人id')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人id')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人id')
    create_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='修改时间')
    channel = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='录入方式：0 hr注册；1 系统录入；2 注册匹配')



class TbCustomerContactBak20151102(db.Model):
    __tablename__ = 'tb_customer_contact_bak20151102'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    object_id = db.Column(db.BigInteger, nullable=False, info='对象id（包括客户线索和黄页）')
    type = db.Column(db.Integer, server_default=db.FetchedValue(), info='（0 黄页，1 公海，2 线索，3 客户，4垃圾库）')
    contact_id = db.Column(db.BigInteger, nullable=False, info='联系人id')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人id')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人id')
    create_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='修改时间')
    channel = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='录入方式：0 hr注册；1 系统录入；2 注册匹配')



class TbEnterprisePositionReport(db.Model):
    __tablename__ = 'tb_enterprise_position_report'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    user_id = db.Column(db.BigInteger, nullable=False, info='用户')
    answered_today_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='今日回答')
    not_answer_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='未回答')
    surveyed_today_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='今日职调')
    not_survey_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='未职调')
    audited_today_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='今日审核')
    not_audit_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='未审核')
    feedback_today_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='今日反馈')
    not_feedback_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='未反馈')
    need_confirm_interview_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='需确认面试')
    newpush_feedback_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='新推反馈')
    apply_position_cooperation_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='申请合作数')
    dealed_position_cooperation_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='已处理合作数')
    no_position_enterprise_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='无职位客户')
    new_position_new_enterprise_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='首发职位客户')
    publish_position_enterprise_today_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='今日新增职位客户')
    remind_invoice_enterprise_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='待开票客户')
    need_remind_pay_enterprise_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='需催款客户')
    need_return_invoice_enterprise_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='需退票客户')
    need_renewal_enterprise_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='待续约客户')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbExtensionNumLog(db.Model):
    __tablename__ = 'tb_extension_num_log'

    id = db.Column(db.BigInteger, primary_key=True)
    talent_id = db.Column(db.BigInteger, info='简历ID')
    extension_num = db.Column(db.Integer, nullable=False, info='分机号')
    phone = db.Column(db.String(50), nullable=False, info='实际电话号码')
    expire_time = db.Column(db.DateTime, nullable=False, info='过期时间')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')



class TbGrabDispatchReport(db.Model):
    __tablename__ = 'tb_grab_dispatch_report'

    id = db.Column(db.BigInteger, primary_key=True, info='自增编号')
    count_date = db.Column(db.Date, nullable=False, unique=True, info='统计日期')
    sys_match_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='系统匹配数')
    deal_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='pa处理数')
    pass_rate = db.Column(db.Float(10, True), nullable=False, server_default=db.FetchedValue(), info='pa通过数')
    expire_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='失效订单数')
    dispatch_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='派单数')
    dispatch_received_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='派单接单数')
    dispatch_reject_count = db.Column(db.Integer, server_default=db.FetchedValue(), info='派单拒绝接单数')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbGrabDispatchReportAuth(db.Model):
    __tablename__ = 'tb_grab_dispatch_report_auth'

    user_id = db.Column(db.BigInteger, primary_key=True)
    sub_user_id = db.Column(db.String(255), nullable=False)
    is_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class TbGrabDispatchUserReport(db.Model):
    __tablename__ = 'tb_grab_dispatch_user_report'
    __table_args__ = (
        db.Index('uni_user_count_date', 'user_id', 'count_date'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='自增编号')
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='PA')
    count_date = db.Column(db.Date, nullable=False, info='统计日期')
    sys_match_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='系统匹配数')
    deal_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='pa处理数')
    pass_rate = db.Column(db.Float(10, True), nullable=False, server_default=db.FetchedValue(), info='pa通过数')
    expire_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='失效订单数')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbGroup(db.Model):
    __tablename__ = 'tb_group'

    id = db.Column(db.Integer, primary_key=True, info='id')
    group_name = db.Column(db.String(255), info='组名称')
    isShow = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否前端显示')
    parent_id = db.Column(db.Integer, server_default=db.FetchedValue(), info='父组ID')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='更新时间')
    remark = db.Column(db.String(255), info='备注')



t_tb_group_menu = db.Table(
    'tb_group_menu',
    db.Column('group_id', db.Integer, nullable=False, server_default=db.FetchedValue(), info='组id'),
    db.Column('menu_id', db.Integer, nullable=False, server_default=db.FetchedValue(), info='导航id')
)



t_tb_group_oper = db.Table(
    'tb_group_oper',
    db.Column('group_id', db.Integer, info='组id'),
    db.Column('oper_id', db.Integer, info='菜单子操作id')
)



t_tb_group_user = db.Table(
    'tb_group_user',
    db.Column('group_id', db.Integer, server_default=db.FetchedValue(), info='组id'),
    db.Column('user_id', db.Integer, server_default=db.FetchedValue(), info='用户id'),
    db.Column('create_time', db.DateTime, info='创建时间'),
    db.Column('update_time', db.DateTime, info='更新时间'),
    db.Column('isLeader', db.Integer, server_default=db.FetchedValue(), info='是否是leader')
)



class TbHhGroup(db.Model):
    __tablename__ = 'tb_hh_group'

    id = db.Column(db.BigInteger, primary_key=True, info='主键Id，组ID')
    group_name = db.Column(db.String(256), nullable=False, info='组名称')
    status = db.Column(db.Integer, nullable=False, info='1:有效,2:删除')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建人也是所属人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, info='修改用户Id')



class TbHhGroupUser(db.Model):
    __tablename__ = 'tb_hh_group_user'

    id = db.Column(db.BigInteger, primary_key=True, info='主键Id')
    group_id = db.Column(db.BigInteger, nullable=False, info='组Id')
    hh_id = db.Column(db.BigInteger, nullable=False, info='猎头Id')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, info='最后修改的用户Id')



class TbHrAdscription(db.Model):
    __tablename__ = 'tb_hr_adscription'

    id = db.Column(db.BigInteger, primary_key=True)
    po_id = db.Column(db.BigInteger)
    po_name = db.Column(db.String(255))
    start_time = db.Column(db.Date)
    end_time = db.Column(db.Date)
    enterprise_id = db.Column(db.BigInteger)
    hr_name = db.Column(db.String(255))
    position_title = db.Column(db.String(255))
    decision_date = db.Column(db.Date)



class TbHrLevel(db.Model):
    __tablename__ = 'tb_hr_level'
    __table_args__ = (
        db.Index('hr_id', 'hr_id', 'level'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    hr_id = db.Column(db.BigInteger, nullable=False, info='HR编号')
    level = db.Column(db.Integer, nullable=False, info='评级')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建人编号')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, info='更新人编号')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='删除标识 0 否 1是')



class TbImRemindRule(db.Model):
    __tablename__ = 'tb_im_remind_rule'

    id = db.Column(db.BigInteger, primary_key=True)
    remind_item = db.Column(db.String(300), info='提醒项')
    remind_type = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='提醒类型 0:固定 1:实时')
    rule = db.Column(db.String(512), info='规则')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='0未删除，1 删除')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue(), info='更新时间')



class TbLoginLog(db.Model):
    __tablename__ = 'tb_login_log'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    user_id = db.Column(db.BigInteger, nullable=False, info='crm用户id')
    last_login_time = db.Column(db.DateTime, nullable=False, info='crm用户最后登录时间')
    ip = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='用户登录id地址')
    inner_ip = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='公司内网IP')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbMailLog(db.Model):
    __tablename__ = 'tb_mail_log'

    id = db.Column(db.BigInteger, primary_key=True)
    paction_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='合同id')
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否发送成功:0:发送成功, 1:发送失败')
    send_time = db.Column(db.DateTime, nullable=False, info='发送时间')



class TbMenu(db.Model):
    __tablename__ = 'tb_menu'

    id = db.Column(db.Integer, primary_key=True, info='主键id')
    menu_name = db.Column(db.String(255), info='名称')
    menu_url = db.Column(db.String(255), info='地址')
    parent_id = db.Column(db.Integer, server_default=db.FetchedValue(), info='父菜单id')
    weight = db.Column(db.Integer, server_default=db.FetchedValue(), info='优先级')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='更新时间')
    remark = db.Column(db.String(255), info='备注')
    is_navigation = db.Column(db.Integer, server_default=db.FetchedValue())



t_tb_menu_role = db.Table(
    'tb_menu_role',
    db.Column('menu_id', db.Integer, server_default=db.FetchedValue(), info='导航id'),
    db.Column('role_id', db.Integer, server_default=db.FetchedValue(), info='角色id')
)



class TbMessageRead(db.Model):
    __tablename__ = 'tb_message_read'

    id = db.Column(db.BigInteger, primary_key=True, info='自增编号')
    user_id = db.Column(db.BigInteger, nullable=False, info='读取用户编号')
    msg_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='读取消息类型')
    read_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='读取次数')
    read_date = db.Column(db.Date, nullable=False, info='读取日期')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除 0 否 1是')



class TbOperation(db.Model):
    __tablename__ = 'tb_operation'

    id = db.Column(db.Integer, primary_key=True, info='主键id')
    menu_code = db.Column(db.String(100), info='操作代码，属于那个菜单的子操作')
    oper_url = db.Column(db.String(200), info='操作链接')
    menu_id = db.Column(db.Integer, info='菜单ID')
    type = db.Column(db.Integer, info='链接类型， 1 查询类型 ， 2 更新类型')
    valid = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否有效， 0 无效， 1有效')
    remark = db.Column(db.String(200), info='备注')



class TbOrderBook(db.Model):
    __tablename__ = 'tb_order_book'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    title = db.Column(db.String(50), info='标题')
    content = db.Column(db.Text, info='富文本')
    group = db.Column(db.String(50), server_default=db.FetchedValue(), info='所属组')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, info='更新人')
    create_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除')



class TbPaMessage(db.Model):
    __tablename__ = 'tb_pa_message'
    __table_args__ = (
        db.Index('idx_pa_massge_pa_id_time', 'pa_id', 'create_time'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键自增')
    msg_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='消息类型:1:我的关注/2:分配给我/3:共享给我')
    pa_id = db.Column(db.BigInteger, nullable=False, info='pa的id')
    pa_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='pa类型:1运营/2服务')
    hh_id = db.Column(db.BigInteger, info='猎头Id')
    hh_name = db.Column(db.String(127), server_default=db.FetchedValue(), info='猎头名字')
    hh_grade = db.Column(db.Integer, info='猎头等级')
    hh_reg_time = db.Column(db.DateTime, info='猎头注册时间')
    hh_company_id = db.Column(db.BigInteger, info='猎企id')
    hh_company_name = db.Column(db.String(255), server_default=db.FetchedValue(), info='猎企名称')
    hh_company_grade = db.Column(db.Integer, info='猎企等级')
    hh_company_reg_time = db.Column(db.DateTime, info='猎企注册时间')
    focus_label_name = db.Column(db.String(1000), info='关注标签名')
    focus_label_time = db.Column(db.DateTime, info='关注标签时间')
    liveness = db.Column(db.Integer, info='活跃度')
    last_recommend_time = db.Column(db.DateTime, info='最近推荐时间')
    last_communication_time = db.Column(db.DateTime, info='最近沟通时间')
    remark = db.Column(db.String(500), info='备注信息')
    extra_data = db.Column(db.String(1000), info='拓展数据JSON')
    recommend_count = db.Column(db.Integer, info='推荐量')
    first_interview_count = db.Column(db.Integer, info='一面数量')
    interview_rate = db.Column(db.Float(20, True), info='面试数量')
    finish_order_count = db.Column(db.Float(20, True), info='成单数量')
    on_board_count = db.Column(db.Float(20, True), info='到岗数量')
    over_warranty_count = db.Column(db.Integer, info='过保数量')
    source_id = db.Column(db.BigInteger, info='来源id')
    source_desc = db.Column(db.String(255), server_default=db.FetchedValue(), info='来源描述')
    msg_status = db.Column(db.Integer, server_default=db.FetchedValue(), info='消息状态:0:删除/1:未读/2已读')
    msg_status_desc = db.Column(db.String(255), info='消息状态描述')
    create_user_id = db.Column(db.BigInteger, info='创建人id')
    create_user_name = db.Column(db.String(255), info='创建人名字')
    create_time = db.Column(db.DateTime, info='创建时间(接收时间)')
    update_user_id = db.Column(db.BigInteger, info='更新人id')
    update_user_name = db.Column(db.String(255), info='更新人名字')
    update_time = db.Column(db.DateTime)



class TbPaMessageFocu(db.Model):
    __tablename__ = 'tb_pa_message_focus'

    id = db.Column(db.BigInteger, primary_key=True, info='主键自增')
    pa_id = db.Column(db.BigInteger, nullable=False, index=True, info='paId')
    last_function_nodes = db.Column(db.Text, info='最后一级职能编号')
    last_industry_nodes = db.Column(db.Text, info='最后以及行业编号')
    salary_range = db.Column(db.Text, info='薪资范围')
    city_range = db.Column(db.Text, info='地区范围')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_user_id = db.Column(db.BigInteger, info='更新人')
    update_time = db.Column(db.DateTime)



class TbPaOsUser(db.Model):
    __tablename__ = 'tb_pa_os_user'
    __table_args__ = (
        db.Index('idx_pa_os_user_id_defunct', 'pa_user_id', 'os_user_id', 'defunct'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    pa_user_id = db.Column(db.BigInteger, nullable=False, info='pa用户ID')
    os_user_id = db.Column(db.BigInteger, nullable=False, info='os用户ID')
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否删除 0 否 1是')



class TbPaction(db.Model):
    __tablename__ = 'tb_paction'
    __table_args__ = (
        db.Index('effect_operate_time', 'effect_operate_time', 'contract_type'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键id')
    contract_no = db.Column(db.String(50), index=True, info='合同编码(按格式)')
    status = db.Column(db.Integer, info='合同状态  0 新建  1 已寄出  2 已签订 3 已过期')
    contract_type = db.Column(db.Integer, info='合同类型  1 企业  2 猎头公司 3 管理(无效与company type 一致) 4 渠道')
    reward_type = db.Column(db.Integer, info='佣金类型 0 自定义 1 固定比例 2 固定佣金')
    reward_val = db.Column(db.Float, info='佣金类型 为 1，2 时，填写的固定值')
    refund_rate = db.Column(db.Float, info='退款比例')
    pay_time = db.Column(db.Integer, info='付款次数')
    pay_rate_setting = db.Column(db.Integer, server_default=db.FetchedValue(), info='分成比例类型：1平台标准；2：自定义；对应不是本表的pay_rate，而是company表的payRate；')
    pay_rate = db.Column(db.Float, info='付款比例，若多次 则为首次付款比例')
    pay_days = db.Column(db.Integer, info='付款天数')
    start_time = db.Column(db.DateTime, info='合同起始日期')
    end_time = db.Column(db.DateTime, info='合同结束日期')
    temp_start_time = db.Column(db.DateTime, info='临时生效开始日期')
    temp_end_time = db.Column(db.DateTime, info='临时生效截止日期')
    active = db.Column(db.Integer, info='-2：新增, -1：待确定, 0：合同确定, 1：合同生效, 2：合同失效, 3：猎头同意协议, 4：合同临时生效')
    is_temp_active = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否临时生效，0否，1是')
    company_id = db.Column(db.BigInteger, index=True, info='关联公司ID')
    bank = db.Column(db.String(100), info='开户行')
    account = db.Column(db.String(100), info='帐号名称')
    account_no = db.Column(db.String(100), info='帐号')
    company_full_name = db.Column(db.String(100), info='合同显示公司名称')
    contacter = db.Column(db.String(50), info='联系人')
    contract_style = db.Column(db.Integer, info='合同种类  0 甲方 1 乙方')
    guarantee_days = db.Column(db.Integer, info='保证期 （天）')
    contract_text = db.Column(db.String, info='合同文本')
    contract_date = db.Column(db.DateTime, info='合同签订日期')
    fax = db.Column(db.String(30), info='传真')
    phone = db.Column(db.String(30), info='电话')
    contract_address = db.Column(db.String(100), info='合同邮寄地址')
    special_term = db.Column(db.Text, info='特殊条款')
    different_contract = db.Column(db.Text, info='不同点描述')
    express = db.Column(db.String(100), info='快递信息')
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_user_id = db.Column(db.BigInteger)
    invoice_date = db.Column(db.Integer, server_default=db.FetchedValue(), info='开票期限')
    sign_department = db.Column(db.String(256), info='签约部门')
    sign_user_id = db.Column(db.Integer, server_default=db.FetchedValue(), info='签约经办人')
    send_time = db.Column(db.DateTime, info='合同寄出时间')
    receive_time = db.Column(db.DateTime, info='合同接收时间')
    remark = db.Column(db.String(5000), info='备注')
    registration_number = db.Column(db.String(128), info='税务登记证号')
    candidate_feedback_time = db.Column(db.String(1024), server_default=db.FetchedValue())
    resume_validity = db.Column(db.String(1024), server_default=db.FetchedValue())
    recommend_validity = db.Column(db.String(1024), server_default=db.FetchedValue())
    referral_calculation = db.Column(db.String(1024), server_default=db.FetchedValue())
    file_path = db.Column(db.String(1024), server_default=db.FetchedValue())
    guarantee_months = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mode = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0录入合同 1保障性邮件合同')
    storage_place = db.Column(db.String(200), info='合同存放地方')
    expense_policy = db.Column(db.Text, info='猎头费用政策')
    bdo_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    bdh_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    validate_look_time = db.Column(db.DateTime, info='合同创建的时间或从失效重置生效的时间')
    confirm_operate_time = db.Column(db.DateTime, info='确认操作时间')
    effect_operate_time = db.Column(db.DateTime, info='生效操作时间')
    proposer = db.Column(db.BigInteger, info='申请人')
    apply_time = db.Column(db.DateTime, info='申请时间')
    apply_status = db.Column(db.Integer, info='申请状态： 1 待审批 合同生效, 2 待审批 合同失效,3 待审批 合同临时生效')
    apply_reason = db.Column(db.String(200), info='申请理由')
    reject_reason = db.Column(db.String(200), info='拒绝申请理由')
    email = db.Column(db.String(100), server_default=db.FetchedValue(), info='邮箱')
    id_card = db.Column(db.String(32), info='身份证号')



class TbPactionAttach(db.Model):
    __tablename__ = 'tb_paction_attach'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    paction_id = db.Column(db.BigInteger, nullable=False, info='合同表主键')
    file_path = db.Column(db.String(100), server_default=db.FetchedValue(), info='合同附件路径')
    html_content = db.Column(db.String, info='若是传的合同类型是word,就是word文档解析的带html标签的内容')
    file_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='合同文档类型，1:word, 2:pdf, 3:image')
    temp_file_path = db.Column(db.String(1024), nullable=False, server_default=db.FetchedValue(), info='临时存储，当上传附件是存储这里，当创建或保存的时候判断前端传的附件路径是否与这个相同，若是相同代表修改附件')
    temp_html_content = db.Column(db.String, info='上传附件有就临时存储，没有就置为空，配合temp_file_path使用')
    temp_file_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='临时性的file_type,正式存储时，cope到file_type')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    STATUS = db.Column(db.Integer, server_default=db.FetchedValue(), info='附件是否生效，0：无效 1：生效')
    upload_user_name = db.Column(db.String(20), server_default=db.FetchedValue(), info='附件上传人姓名')
    attach_name = db.Column(db.String(100), server_default=db.FetchedValue(), info='附件名称')



class TbPactionBak20160127(db.Model):
    __tablename__ = 'tb_paction_bak20160127'

    id = db.Column(db.BigInteger, primary_key=True)
    contractNo = db.Column(db.String(50), info='合同编码(按格式)')
    status = db.Column(db.Integer, info='合同状态  0 新建  1 已寄出  2 已签订 3 已过期')
    contractType = db.Column(db.Integer, info='合同类型  1 企业  2 猎头公司 3 管理(无效,与company type 一致) 4 渠道')
    rewardType = db.Column(db.Integer, info='佣金类型 0 自定义 1 固定比例 2 固定佣金')
    rewardVal = db.Column(db.Float, info='佣金类型 为 1，2 时，填写的固定值')
    refundRate = db.Column(db.Float, info='退款比例')
    payTime = db.Column(db.Integer, info='付款次数')
    payRate = db.Column(db.Float, info='付款比例，若多次 则为首次付款比例')
    payDays = db.Column(db.Integer, info='付款天数')
    startTime = db.Column(db.DateTime, info='合同起始日期')
    endTime = db.Column(db.DateTime, info='合同结束日期')
    active = db.Column(db.Integer, info='-2 新增, -1 待确定 , 0 合同确定但生效, 1 合同生效, 2 合同失效, 3 猎头同意协议')
    companyId = db.Column(db.BigInteger, index=True, info='关联公司ID')
    bank = db.Column(db.String(100), info='开户行')
    account = db.Column(db.String(100), info='帐号名称')
    accountNo = db.Column(db.String(100), info='帐号')
    companyFullName = db.Column(db.String(100), info='合同显示公司名称')
    contacter = db.Column(db.String(50), info='联系人')
    contractStyle = db.Column(db.Integer, info='合同种类  0 甲方 1 乙方')
    guaranteeDays = db.Column(db.Integer, info='保证期 （天）')
    contractText = db.Column(db.String, info='合同文本')
    contractDate = db.Column(db.DateTime, info='合同签订日期')
    fax = db.Column(db.String(30), info='传真')
    phone = db.Column(db.String(30), info='电话')
    contractAddress = db.Column(db.String(100), info='合同邮寄地址')
    specialTerm = db.Column(db.Text, info='特殊条款')
    differentContract = db.Column(db.Text, info='不同点描述')
    express = db.Column(db.String(100), info='快递信息')
    createTime = db.Column(db.DateTime)
    updateTime = db.Column(db.DateTime)
    createUserId = db.Column(db.BigInteger)
    updateUserId = db.Column(db.BigInteger)
    invoice_date = db.Column(db.Integer, server_default=db.FetchedValue(), info='开票期限')
    sign_department = db.Column(db.String(256), info='签约部门')
    sign_user_id = db.Column(db.Integer, server_default=db.FetchedValue(), info='签约经办人')
    send_time = db.Column(db.DateTime, info='合同寄出时间')
    receive_time = db.Column(db.DateTime, info='合同接收时间')
    remark = db.Column(db.String(5000))
    registration_number = db.Column(db.String(128), info='税务登记证号')
    candidate_feedback_time = db.Column(db.String(1024), server_default=db.FetchedValue())
    resume_validity = db.Column(db.String(1024), server_default=db.FetchedValue())
    recommend_validity = db.Column(db.String(1024), server_default=db.FetchedValue())
    referral_calculation = db.Column(db.String(1024), server_default=db.FetchedValue())
    file_path = db.Column(db.String(1024), server_default=db.FetchedValue())
    guarantee_months = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mode = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0录入合同 1保障性邮件合同')
    storage_place = db.Column(db.String(200), info='合同存放地方')
    expense_policy = db.Column(db.String(256), info='猎头费用政策')



class TbPactionSelfSet(db.Model):
    __tablename__ = 'tb_paction_self_set'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    paction_id = db.Column(db.BigInteger, nullable=False, index=True, info='合同id')
    color = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='颜色标记:1 红色, 2 黄色, 3 绿色')
    operator_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='查看该标记记录的操作人id')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0:未删除,1:已删除')



class TbPactionSnapshot(db.Model):
    __tablename__ = 'tb_paction_snapshot'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    relation_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='关联record id')
    paction_id = db.Column(db.BigInteger, nullable=False, info='合同表主键')
    operate_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='操作类型：1：申请生效，2：同意生效，3：拒绝生效，4：申请临时生效，5：同意临时生效，6：拒绝临时生效，7：申请失效，8：同意失效，9：拒绝失效')
    snapshot = db.Column(db.String, nullable=False, info='合同表的快照内容')
    modify_reason = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='合同修改原因')
    attach_path = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='修改申请附件路径')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0:未删除,1:已删除')



class TbPermission(db.Model):
    __tablename__ = 'tb_permission'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue(), info='权限id')
    permission_name = db.Column(db.String(255), nullable=False, info='权限名称')
    remark = db.Column(db.String(255), info='备注')



class TbPermissionRole(db.Model):
    __tablename__ = 'tb_permission_role'

    id = db.Column(db.Integer, primary_key=True)
    permission_id = db.Column(db.Integer, nullable=False, info='权限id')
    role_id = db.Column(db.Integer, nullable=False, info='角色id')



class TbPersonDispatchTag(db.Model):
    __tablename__ = 'tb_person_dispatch_tag'

    id = db.Column(db.BigInteger, primary_key=True, info='自增ID')
    user_id = db.Column(db.BigInteger, info='操作人')
    industry_id1 = db.Column(db.BigInteger, info='行业一级')
    industry_id2 = db.Column(db.BigInteger, info='行业二级')
    position_title1 = db.Column(db.BigInteger, info='职能一级')
    position_title2 = db.Column(db.BigInteger, info='职能二级')
    position_title3 = db.Column(db.BigInteger, info='职能三级')
    annual_salary_level = db.Column(db.Integer, info='年薪职级 1: 30万以下, 2: 30-50万, 3: 50-100万, 4: 100-200万, 5: 200万以上')
    reward_amount = db.Column(db.Float(asdecimal=True), info='固定佣金的 金额')
    city_id = db.Column(db.BigInteger, info='城市ID')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='更新时间')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否删除 0 否 1 是')
    custom_id = db.Column(db.BigInteger, info='自定义')



class TbPositionEvaluateLog(db.Model):
    __tablename__ = 'tb_position_evaluate_log'

    position_id = db.Column(db.BigInteger, primary_key=True, info='职位id')
    position_title = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='职位名称')
    hr_id = db.Column(db.BigInteger, nullable=False, info='职位负责人id')
    hr_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='职位负责人姓名')
    enterprise_id = db.Column(db.BigInteger, nullable=False, info='职位所在企业id')
    enterprise_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='职位所在企业名')
    publist_time = db.Column(db.DateTime, nullable=False, info='职位发布时间')
    evaluate = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位估计，单位元')
    position_status = db.Column(db.Integer, nullable=False, info='职位状态')
    evaluate_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='估计是否固定，1:固定,2:不稳定')
    pa_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='pa id')
    pa_name = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue(), info='pa 名')
    bdo_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='bdo id')
    bdo_name = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue(), info='bdo 名字')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())



t_tb_position_evaluate_log_bak_20160530 = db.Table(
    'tb_position_evaluate_log_bak_20160530',
    db.Column('position_id', db.BigInteger, nullable=False, info='职位id'),
    db.Column('position_title', db.String(1000), nullable=False, server_default=db.FetchedValue()),
    db.Column('hr_id', db.BigInteger, nullable=False, info='职位负责人id'),
    db.Column('hr_name', db.String(200), nullable=False, server_default=db.FetchedValue(), info='职位负责人姓名'),
    db.Column('enterprise_id', db.BigInteger, nullable=False, info='职位所在企业id'),
    db.Column('enterprise_name', db.String(200), nullable=False, server_default=db.FetchedValue(), info='职位所在企业名'),
    db.Column('publist_time', db.DateTime, nullable=False, info='职位发布时间'),
    db.Column('evaluate', db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位估计，单位元'),
    db.Column('position_status', db.Integer, nullable=False, info='职位状态'),
    db.Column('evaluate_status', db.Integer, nullable=False, server_default=db.FetchedValue(), info='估计是否固定，1:固定,2:不稳定'),
    db.Column('pa_id', db.BigInteger, nullable=False, server_default=db.FetchedValue()),
    db.Column('pa_name', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('bdo_id', db.BigInteger, nullable=False, server_default=db.FetchedValue()),
    db.Column('bdo_name', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('create_time', db.DateTime, nullable=False),
    db.Column('update_time', db.DateTime, nullable=False),
    db.Column('create_user_id', db.BigInteger, nullable=False, server_default=db.FetchedValue()),
    db.Column('update_user_id', db.BigInteger, nullable=False, server_default=db.FetchedValue())
)



class TbPositionOverTime(db.Model):
    __tablename__ = 'tb_position_over_time'

    id = db.Column(db.BigInteger, primary_key=True)
    position_id = db.Column(db.BigInteger, nullable=False, info='职位id')
    recommend_over_time = db.Column(db.Integer, info='新推荐逾期天数')
    evaluate_over_time = db.Column(db.Integer, info='评估通过逾期天数')
    interview_to_confirm_over_time = db.Column(db.Integer, info='面试待确认逾期天数')
    interview_confirm_over_time = db.Column(db.Integer, info='面试已确认逾期天数')
    interview_pass_over_time = db.Column(db.Integer, info='面试通过逾期天数')
    offer_over_time = db.Column(db.Integer, info='OFFER逾期天数')
    on_board_over_time = db.Column(db.Integer, info='到岗逾期天数')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否删除 0 否 1 是')



class TbProjectRecording(db.Model):
    __tablename__ = 'tb_project_recording'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    project_name = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='项目名称')
    file = db.Column(db.String(150), nullable=False, server_default=db.FetchedValue(), info='附件')
    remark = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='说明')
    group = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='所属组')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, info='更新人')
    create_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除')



class TbRemind(db.Model):
    __tablename__ = 'tb_remind'
    __table_args__ = (
        db.Index('id_user_id_remind_time', 'user_id', 'remind_time'),
    )

    id = db.Column(db.Integer, primary_key=True, info='id')
    obj_id = db.Column(db.Integer, nullable=False, info='需要提醒的id')
    title = db.Column(db.String(1000), nullable=False, info='title(职位或者候选人)')
    name = db.Column(db.String(1000), nullable=False, info='公司名称or 职位')
    user_id = db.Column(db.Integer, nullable=False, info='用户id')
    type = db.Column(db.Integer, nullable=False, info='1:职位 2:候选人')
    remind_time = db.Column(db.DateTime, info='提醒时间')
    remind_content = db.Column(db.String(512), info='提醒内容')
    is_finished = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否已完成:0:待处理，1:已完成')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除,0:未删除，1：已删除')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='更新时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    ahead_time = db.Column(db.Integer, server_default=db.FetchedValue(), info='提前时间')



class TbScale(db.Model):
    __tablename__ = 'tb_scale'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    name = db.Column(db.String(256), nullable=False, info='名称')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='更新者')
    create_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='修改时间')
    defunt = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除')



class TbSign(db.Model):
    __tablename__ = 'tb_sign'
    __table_args__ = (
        db.Index('idx_userid_shouldsigndate', 'user_id', 'should_sign_date'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    user_id = db.Column(db.BigInteger, nullable=False, info='用户ID')
    user_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='用户姓名')
    customer_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='客户ID')
    customer_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='客户名称')
    customer_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='客户类型，1：HR，7：HD')
    address = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='地址')
    sign_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='签到类型，0：外勤签到，1，内勤签到,2:缺勤,3:请假')
    sign_time = db.Column(db.DateTime, info='签到时间')
    sign_out_time = db.Column(db.DateTime, info='签退时间')
    mobile_model = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='设备型号')
    vacation_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='对应请假记录的id,如果是正常考勤,该id为0')
    sign_access = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='打卡入口,1:本人打卡,2:hr代补充打卡')
    hr_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='补打卡的的hr id')
    hr_sign_time = db.Column(db.DateTime, info='hr补签到的时间')
    hr_sign_out_time = db.Column(db.DateTime, info='hr补签退的时间')
    should_sign_date = db.Column(db.Date, nullable=False, info='应该签到的日期')
    overtime_minutes = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='加班分钟数')
    sign_log_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='签到对应的tb_sign_log流水表id')
    sign_out_log_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='签退对应的tb_sign_log流水表id')
    before_vacation_sign_time = db.Column(db.DateTime, info='请假前的签到时间')
    before_vacation_sign_out_time = db.Column(db.DateTime, info='请假前的签退时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbSignLog(db.Model):
    __tablename__ = 'tb_sign_log'

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, nullable=False, info='用户ID')
    customer_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='客户ID')
    customer_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='客户名称')
    customer_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='客户类型，1：HR，7：HD')
    address = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='地址')
    sign_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='签到类型，0：外勤签到，1，内勤签到,对于流水记录只有内勤与外勤')
    sign_time = db.Column(db.DateTime, nullable=False, info='签到时间')
    mobile_model = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='设备型号')
    sign_access = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='打卡入口,1:本人打卡,2:hr代补充打卡')
    hr_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='补打开的hr id')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)



class TbSignMaterial(db.Model):
    __tablename__ = 'tb_sign_material'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    sign_log_id = db.Column(db.BigInteger, nullable=False, info='sign_log表id')
    material_url = db.Column(db.String(200), nullable=False, info='图片url')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除 0:false 1:true')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')



class TbSignVacation(db.Model):
    __tablename__ = 'tb_sign_vacation'

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, nullable=False)
    start_time = db.Column(db.DateTime, nullable=False, info='请假的开始时间')
    end_time = db.Column(db.DateTime, nullable=False, info='请假的结束时间')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='请假类型,1:事假,2:病假,3:丧假,4:产假,5:年假,6:婚假,7:调休,8:其他')
    times = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='请假总时长')
    times_unit = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='时长单位:1:分,2:时,3:天')
    reason = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='请假理由')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbStyle(db.Model):
    __tablename__ = 'tb_style'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    name = db.Column(db.String(256), nullable=False, info='名称')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='更新者')
    create_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='修改时间')
    defunt = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除')



class TbSystemLog(db.Model):
    __tablename__ = 'tb_system_log'

    id = db.Column(db.BigInteger, primary_key=True, info='主键id')
    operator_user_id = db.Column(db.BigInteger, nullable=False, info='操作用户id')
    operator_user_name = db.Column(db.String(128), info='操作用户名字')
    company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='公司')
    company_name = db.Column(db.String(128), info='公司名字')
    position_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职位')
    position_title = db.Column(db.String(128), info='职位名字')
    candidate_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='候选人')
    candidate_name = db.Column(db.String(128), info='候选人名字')
    operator_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='操作id')
    creat_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='修改时间')



class TbTdcGroup(db.Model):
    __tablename__ = 'tb_tdc_group'

    id = db.Column(db.BigInteger, primary_key=True, info='主键Id，组ID')
    user_id = db.Column(db.BigInteger, nullable=False, info='所属用户')
    group_name = db.Column(db.String(256), nullable=False, info='组名称')
    group_type = db.Column(db.Integer, nullable=False, info='组类型 1 猎企')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    defunct = db.Column(db.Integer, nullable=False, info='是否删除 0 否 1是')



class TbTdcGroupRelation(db.Model):
    __tablename__ = 'tb_tdc_group_relation'

    id = db.Column(db.BigInteger, primary_key=True, info='主键Id')
    group_id = db.Column(db.BigInteger, nullable=False, info='组Id')
    member_id = db.Column(db.BigInteger, nullable=False, info='组成员ID')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, info='最后修改的用户Id')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除 0 否 1是')



class TbTdcRole(db.Model):
    __tablename__ = 'tb_tdc_role'

    id = db.Column(db.Integer, primary_key=True, info='自增编号')
    role_code = db.Column(db.Integer, nullable=False, unique=True, info='角色编号')
    role_name = db.Column(db.String(255), nullable=False, info='角色名称')
    header_memu_ids = db.Column(db.String(255), info='默认展示菜单')
    all_menu_ids = db.Column(db.String(255), info='所有可见菜单')



class TbTdcVersion(db.Model):
    __tablename__ = 'tb_tdc_version'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    title = db.Column(db.String(500), nullable=False, info='标题')
    version_time = db.Column(db.Date, nullable=False, info='版本更新时间')
    content = db.Column(db.Text, nullable=False, info='内容')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class TbTdcVersionContent(db.Model):
    __tablename__ = 'tb_tdc_version_content'

    id = db.Column(db.BigInteger, primary_key=True, info='主键id')
    version_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='版本id')
    content = db.Column(db.Text, nullable=False, info='版本内容')
    url = db.Column(db.String(500), nullable=False, info='版本更新引导图片url')
    web_url = db.Column(db.String(500), nullable=False, info='版本更新引导图片url')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人id')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人id')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='逻辑删除')



class TbUser(db.Model):
    __tablename__ = 'tb_user'

    id = db.Column(db.Integer, primary_key=True, info='用户id')
    user_info_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='员工工号（TDC新版）')
    user_code = db.Column(db.String(64), info='用户代码')
    role_code = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='用户登录角色编号')
    role_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='角色类型(1:总部、2:合伙人)')
    user_name = db.Column(db.String(255), info='名字')
    english_name = db.Column(db.String(255), info='英文名字')
    gender = db.Column(db.Integer, info='性别')
    position_title = db.Column(db.String(255), info='职位')
    position_title_2 = db.Column(db.String(255), info='职位2')
    position_level_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='职级')
    position_level_id_2 = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='职级2')
    mobile_phone = db.Column(db.String(255), info='手机')
    mobile_bind_status = db.Column(db.Integer, server_default=db.FetchedValue(), info='手机号绑定状态')
    mobile_bind_time = db.Column(db.DateTime, info='手机号绑定时间')
    tele_phone = db.Column(db.String(255), info='座机')
    direct_no = db.Column(db.String(50), info='直线号')
    email = db.Column(db.String(255), info='邮箱')
    password = db.Column(db.String(255), info='密码')
    qq = db.Column(db.String(255), info='QQ')
    weixin = db.Column(db.String(255), info='微信')
    weixin_qr_code = db.Column(db.String(255), info='微信二维码')
    avatar = db.Column(db.String(255), info='头像')
    status = db.Column(db.Integer, server_default=db.FetchedValue(), info='状态:1.正常,2离职')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='更新时间')
    derma = db.Column(db.Integer, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    dimission_operator = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='离职用户操作人id')
    dimission_operate_time = db.Column(db.DateTime, info='离职用户操作时间')
    delete_operator = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='删除用户操作人id')
    delete_operate_time = db.Column(db.DateTime, info='删除用户操作时间')
    tele_phone2 = db.Column(db.String(255))
    dimission_time = db.Column(db.DateTime, info='离职时间')
    entry_time = db.Column(db.DateTime, info='入职时间')
    formal_time = db.Column(db.DateTime, info='转正时间')
    last_login_ip = db.Column(db.String(255), info='最后登录IP')
    last_login_time = db.Column(db.DateTime, info='最后登录时间')



class TbUserCompanyCount(db.Model):
    __tablename__ = 'tb_user_company_count'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    user_id = db.Column(db.BigInteger, nullable=False, info='用户id')
    has_recommend_company_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='有推荐的猎企数')
    has_recommend_user_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='有推荐的猎头数')
    has_placement_company_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='有成单的猎企数')
    has_placement_user_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='有成单的猎头数')
    placement_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='成单数')
    sign_company_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='签约猎企数')
    candidate_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='推荐数')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    count_date = db.Column(db.Date, nullable=False, index=True, info='统计时时间')



class TbUserEnterpriseCount(db.Model):
    __tablename__ = 'tb_user_enterprise_count'

    id = db.Column(db.BigInteger, primary_key=True, info='主键id')
    user_id = db.Column(db.BigInteger, nullable=False, info='用户id')
    sign_enterprise_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='签约雇主数')
    has_position_enterprise_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='有职位的雇主数')
    placement_enterprise_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='成单雇主数')
    position_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位数')
    placement_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='成单数')
    candidate_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='推荐数')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    count_date = db.Column(db.Date, nullable=False, index=True, info='统计时时间')



class TbUserInfo(db.Model):
    __tablename__ = 'tb_user_info'

    id = db.Column(db.BigInteger, primary_key=True, info='自增主键')
    email = db.Column(db.String(255), nullable=False, info='邮箱（账号）')
    password = db.Column(db.String(255), nullable=False, info='密码')
    login_role_code = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='当前登录的角色')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='用户状态: 1 正常 2 离职')
    dimission_operate_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='离职操作人ID')
    dimission_operate_time = db.Column(db.DateTime, info='离职操作人时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, info='更新人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    login_app_flag = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否登录过APP')
    not_remind_app_flag_time = db.Column(db.DateTime, info='点击当日不提醒时间')
    not_remind_data_perfection_time = db.Column(db.DateTime, info='点击 资料完善提醒 当日不提醒时间')



class TbUserMenu(db.Model):
    __tablename__ = 'tb_user_menu'

    user_id = db.Column(db.BigInteger, primary_key=True, info='用户编号')
    header_memu_ids = db.Column(db.String(255), nullable=False, info='用户自定义菜单')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbUserRole(db.Model):
    __tablename__ = 'tb_user_role'

    id = db.Column(db.Integer, primary_key=True, info='用户和角色id')
    user_id = db.Column(db.Integer, nullable=False, info='用户id')
    role_id = db.Column(db.Integer, nullable=False, info='角色id')



class TbUserTaskNorm(db.Model):
    __tablename__ = 'tb_user_task_norm'
    __table_args__ = (
        db.Index('org_norm_user', 'norm_id', 'norm_date', 'norm_type'),
    )

    id = db.Column(db.Integer, primary_key=True)
    norm_id = db.Column(db.BigInteger, nullable=False, info='业绩填写ID')
    norm_date = db.Column(db.Integer, nullable=False, info='创建年月')
    norm_type = db.Column(db.Integer, nullable=False, info='填报类型，0 普通用户 1 组')
    lastmon_offer_num = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='上月OFFER数')
    thismon_offer_rate = db.Column(db.Float(16, True), server_default=db.FetchedValue(), info='当月offer增长率指标')
    hc_position = db.Column(db.Float(16, True), server_default=db.FetchedValue(), info='本月职位交付转化率标准')
    lastmon_offer_amt = db.Column(db.Float(16, True), server_default=db.FetchedValue(), info='上月到岗GMV金额')
    gmv_norm_val = db.Column(db.Float(16, True), server_default=db.FetchedValue(), info='GMV当月增长率指标')
    thismon_offer_amt_rate = db.Column(db.Float(16, True), server_default=db.FetchedValue(), info='当月增长指标')
    cur_online_position_num = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='上月在线职位数')
    month_position_rate = db.Column(db.Float(16, True), server_default=db.FetchedValue(), info='有效职位留存率')
    cur_position_add_num = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='当月新增职位任务数')
    cust = db.Column(db.Float(16, True), server_default=db.FetchedValue(), info='客单价')
    pos_hr_num = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='上年度一二级客户发布职位Hr数')
    month_hr_rate = db.Column(db.Float(16, True), server_default=db.FetchedValue(), info='HR留存率')
    pos_hr = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='HR人均职位数')
    is_submit = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否提交')
    update_user_id = db.Column(db.BigInteger, info='更新人')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='更新时间')



class TbVisit(db.Model):
    __tablename__ = 'tb_visit'
    __table_args__ = (
        db.Index('idx_visitorid_enterpriseid_visittime', 'visitor_id', 'enterprise_id', 'visit_time'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键id')
    visitor_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='拜访者')
    co_visitor_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='协访者')
    reason = db.Column(db.String(200, 'utf8_bin'), info='拜访原因')
    visit_time = db.Column(db.DateTime, nullable=False, info='拜访时间')
    enterprise_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='受访客户id')
    enterprise_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='受访客户名称')
    address = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='地址')
    visited_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='受访人')
    visited_title = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='受访人职位')
    report = db.Column(db.String(2000), info='拜访报告')
    cancel_reason = db.Column(db.String(200), info='取消拜访原因')
    reject_reason = db.Column(db.String(200), info='驳回原因')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0:申请中 1:待拜访 2:已取消 3:已拜访 4:已驳回')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    type = db.Column(db.Integer, nullable=False, info='类型：0线索黄页，1企业')

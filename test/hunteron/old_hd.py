# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class HdCity(db.Model):
    __tablename__ = 'hd_city'

    id = db.Column(db.Integer, primary_key=True, info='主键ID')
    name = db.Column(db.String(100), nullable=False, info='名称')



class HdCompany(db.Model):
    __tablename__ = 'hd_company'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    name = db.Column(db.String(200), info='名称')
    addUserId = db.Column(db.BigInteger, info='创建人')
    addTime = db.Column(db.DateTime, info='创建时间')
    talentid = db.Column(db.BigInteger, index=True)



class HdCv(db.Model):
    __tablename__ = 'hd_cv'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(200))
    display_name = db.Column(db.String(200), info='显示名称')
    fileLink = db.Column(db.String(1000))
    htmlLink = db.Column(db.String(1000))
    talentId = db.Column(db.BigInteger, index=True)
    type = db.Column(db.SmallInteger, info='cv类型：0：上传；1：手动创建；2：插件保存')
    sourcewebname = db.Column(db.String(50), info='简历来源网站名称（插件保存时）')
    sourceurl = db.Column(db.String(2000), info='简历来源网站地址（插件保存时）')
    addUserId = db.Column(db.BigInteger, index=True)
    web_owner_id = db.Column(db.String(100))
    headin_old_email = db.Column(db.String(300))
    checked = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='cv是否被查看过标识')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除0否1是')
    number = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='第几个简历')
    create_time = db.Column(db.DateTime, index=True, server_default=db.FetchedValue(), info='创建时间')
    delete_time = db.Column(db.DateTime, info='删除时间')



class HdDegree(db.Model):
    __tablename__ = 'hd_degree'

    id = db.Column(db.SmallInteger, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    order_by = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序字段')



class HdHeadhunterCustomerHonor(db.Model):
    __tablename__ = 'hd_headhunter_customer_honor'
    __table_args__ = (
        db.Index('idx_customer_honor_headhunter_company_id_defunct', 'headhunter_company_id', 'headhunter_id', 'defunct'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    headhunter_id = db.Column(db.BigInteger, nullable=False, info='猎头ID')
    headhunter_company_id = db.Column(db.BigInteger, nullable=False, info='猎企ID')
    customer_honor = db.Column(db.String(600), info='客户荣誉')
    description = db.Column(db.String(600), info='描述')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否删除0:false 1:true')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='修改时间')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    update_user_id = db.Column(db.BigInteger, info='修改人')



class HdHeadhunterSuccessfulCase(db.Model):
    __tablename__ = 'hd_headhunter_successful_case'
    __table_args__ = (
        db.Index('idx_headhunter_company_id_defunct', 'headhunter_company_id', 'headhunter_id', 'defunct'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    headhunter_id = db.Column(db.BigInteger, nullable=False, info='猎头ID')
    headhunter_company_id = db.Column(db.BigInteger, nullable=False, info='猎企ID')
    company_name = db.Column(db.String(200), info='公司名称')
    company_province_id = db.Column(db.String(64), info='公司省')
    company_city_id = db.Column(db.String(64), info='公司市')
    company_position_title = db.Column(db.String(600), info='职位名称')
    company_position_annual_salary = db.Column(db.Float(asdecimal=True), info='年薪')
    company_position_degree_id = db.Column(db.Integer, info='学历')
    company_industry_id = db.Column(db.BigInteger, info='行业')
    candidate_name = db.Column(db.String(100), info='候选人姓名')
    candidate_start_work_year = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='候选人开始工作年份')
    candidate_degree_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='候选人学历')
    candidate_city_id = db.Column(db.String(64), info='候选人所在城市')
    candidate_annual_salary = db.Column(db.Float(asdecimal=True), info='候选人获得年薪')
    candidate_club_position_title = db.Column(db.String(128), info='候选人上家职位')
    customer_honor = db.Column(db.String(600), info='客户荣誉')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否删除0:false 1:true')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='修改时间')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    update_user_id = db.Column(db.BigInteger, info='修改人')



class HdProvince(db.Model):
    __tablename__ = 'hd_province'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)



class HdSendCompanyRecord(db.Model):
    __tablename__ = 'hd_send_company_record'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    company_id = db.Column(db.BigInteger, nullable=False, info='公司id')
    create_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')



class HdSendCount(db.Model):
    __tablename__ = 'hd_send_count'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    user_id = db.Column(db.BigInteger, info='用户id')
    open_id = db.Column(db.String(100), nullable=False, info='openID')
    type = db.Column(db.Integer, nullable=False, info='发送类型1.关注 2.绑定')
    create_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')



class HdTag(db.Model):
    __tablename__ = 'hd_tag'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    name = db.Column(db.String(200), info='名称')
    addUserId = db.Column(db.BigInteger, index=True, info='创建人')
    addTime = db.Column(db.DateTime, info='创建时间')
    talentid = db.Column(db.BigInteger, index=True, info='人才id')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否逻辑删除 1已删除 0未删除')
    update_time = db.Column(db.DateTime, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')



class HdTalent(db.Model):
    __tablename__ = 'hd_talent'

    id = db.Column(db.BigInteger, primary_key=True)
    gender = db.Column(db.Integer)
    anualSalary = db.Column(db.Integer, info='年薪')
    updateTime = db.Column(db.DateTime, index=True, server_default=db.FetchedValue(), info='更新时间')
    addUserId = db.Column(db.BigInteger, index=True, info='创建人')
    rank = db.Column(db.String(100), info='候选人职级')
    addTime = db.Column(db.DateTime, index=True, info='创建时间')
    comment = db.Column(db.String(5000), info='候选人备注信息')
    email = db.Column(db.String(200), index=True, info='邮箱')
    phone = db.Column(db.String(50), index=True, info='手机号')
    name = db.Column(db.String(100), info='名称')
    jobTitle = db.Column(db.String(400), info='岗位名称')
    birthYear = db.Column(db.Integer, info='出生日期（年）')
    graduateYear = db.Column(db.Integer, info='毕业时间')
    degreeId = db.Column(db.SmallInteger)
    cityId = db.Column(db.BigInteger, info='城市ID')
    deleted = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='是否删除: 0=否,1=是')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    level = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='人才等级1：顶2：优3：一般：4差')
    birthday = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='出生日期')
    marital_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='婚姻状况：0未知1已婚2未婚')
    id_card = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='身份证号码')
    address = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='地址')
    expect_annual_salary = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='期望年薪')
    avatar = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='头像')
    english_name = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='英文名')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人id')
    expect_city = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='期望城市')
    city = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='城市名')
    standardized = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否已标准化。0：未标准化，1：标准化中，2：已标准化')
    resume_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='简历id')
    default_recommand_report_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='默认推荐报告id')
    post_recommand_report_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='挂牌推荐报告id')
    self_evaluation = db.Column(db.String(5000), nullable=False, server_default=db.FetchedValue(), info='自我评价')
    salary_desc = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='薪资描述')
    current_salary = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='当前薪资')
    current_salary_months = db.Column(db.Float, nullable=False, server_default=db.FetchedValue(), info='当前月薪月数')
    expect_salary = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='期望月薪')
    expect_salary_months = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='期望月薪月数')
    other_welfare = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='其他福利')
    extra_msg = db.Column(db.Text, info='附加信息')
    apply_job_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='求职状态,1:在职,看看新机会 2:在职,急寻新工作 3:在职,暂无跳槽打算 4:离职,正在找工作')
    expect_industry = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='期望行业id')
    expect_function = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='期望职能id')
    open_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='公开状态,1:公开,2:私密,3:私密公开')
    company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='公司id')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    old_open_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    start_work_year = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开始工作年份')
    start_work_month = db.Column(db.Integer, server_default=db.FetchedValue(), info='开始工作月份')
    integrity = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='简历完整度')
    hh_category_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎头对人才的分类 对应表 tb_hh_talent_category')
    expect_annual_salary_desc = db.Column(db.String(600), nullable=False, server_default=db.FetchedValue(), info='期望年薪描述')
    expect_position_titles = db.Column(db.String(511), nullable=False, server_default=db.FetchedValue(), info='期望职位')
    expect_extra_position_titles = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='自定义期望职能')
    default_resume_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='默认简历, 0：没有  1：非标 2：标准')
    company_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='公司名')
    school = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='学校')
    cv_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue())
    jobhunter_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='C端用户id')
    other_require = db.Column(db.String(550), nullable=False, server_default=db.FetchedValue(), info='其他要求')
    salary_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='年薪类型：0税前，1税后')
    cover_by_jobhunter = db.Column(db.Integer, server_default=db.FetchedValue(), info='显示提示将C端简历导入并覆盖该数据，0：不显示，1：显示')
    jobhunter_update_time = db.Column(db.DateTime, info='C端简历最后更新时间')
    expert_tagContent = db.Column(db.String(200), info='精通技能')
    competent_tagContent = db.Column(db.String(200), info='熟悉技能')
    contact_period = db.Column(db.Integer, server_default=db.FetchedValue(), info='0.不限 1.工作日(10:00-18:00) 2.工作日(18:00-21:00) 3.节假日')
    outside_talent_id = db.Column(db.String(50), nullable=False, index=True, server_default=db.FetchedValue(), info='外部人才id')
    source = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='来源，0：猎头上传，1：抢人才抢到的，2：孵化器关注到的人才，3：人才市场关注到的人才')
    delete_time = db.Column(db.DateTime, info='删除时间')
    expect_salary_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='期望薪资税收类型,0:税前,1:税后')
    last_recommend_time = db.Column(db.DateTime, info='最后推荐时间')
    active_user_time = db.Column(db.DateTime, info='积极用户更新时间')
    special_work_year = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职能经验(特殊工作年限)')
    special_work_exp = db.Column(db.String(1000), info='细分职能(内容类型)')
    degree_entrance_examination = db.Column(db.Integer, info='null:未填;0:非统招;1:统招')
    selling_price = db.Column(db.Numeric(11, 4), server_default=db.FetchedValue(), info='简历售价')
    selling_state = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='在售状态 0 下架 1 上架')
    graduate_time = db.Column(db.String(100), info='解析-毕业时间')
    lesson = db.Column(db.String(100), info='所学课程')
    computer = db.Column(db.String(100), info='解析-计算机水平')
    english = db.Column(db.String(100), info='解析-外语水平')
    school_type = db.Column(db.Integer, info='解析-院校类别:// 0:普通，1:211 院校，2:985 院校，3:既是 211 又是 985 院校')
    speciality = db.Column(db.String(100), info='解析-专业')
    jiguan = db.Column(db.String(100), info='解析- 籍贯')
    national = db.Column(db.String(100), info='解析-民族')
    nationality = db.Column(db.String(100), info='解析-国籍')
    family_name = db.Column(db.String(100), info='解析-姓氏(例如:李)')
    now_location = db.Column(db.String(100), info='解析-现工作地址')
    forward_location = db.Column(db.String(100), info='解析-期望工作地址')
    advanced_degree = db.Column(db.String(100), info='解析-最高学位')
    vocation = db.Column(db.String(100), info='解析-现从事行业')
    political = db.Column(db.String(100), info='解析-政治面貌')
    start_from = db.Column(db.String(100), info='解析-到岗时间')
    qq = db.Column(db.String(100), info='解析-QQ号')
    last_title = db.Column(db.String(100), info='解析-最近职位')
    overseas_work = db.Column(db.String(100), info='解析-海外工作经验(是/否)')
    job_hopping_frequency = db.Column(db.String(100), info='解析-跳槽频率(1-10级逐步递增，默认为100) ')
    work_type = db.Column(db.String(100), info='解析-工作类型(全职、兼职、实习)')
    web_chat = db.Column(db.String(100), info='解析-微信号')
    do_not_recommend = db.Column(db.String(100), info='解析-勿投企业 ')
    personal_interests = db.Column(db.String(100), info='解析-兴趣爱好')
    exclusive_hh_id = db.Column(db.String(255))
    exclusive_operator_id = db.Column(db.BigInteger)
    domicile_place = db.Column(db.String(200), info='户籍')
    fertility_status = db.Column(db.Integer, info='生育状况 1已育，2未育')
    domicile_place_id = db.Column(db.BigInteger, info='户籍ID')
    jiguan_id = db.Column(db.BigInteger, info='籍贯ID')
    current_total_revenue = db.Column(db.Float(11, True), nullable=False, server_default=db.FetchedValue(), info='目前总收入')
    current_total_revenue_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='目前总收入: 0税前，1税后')



class HdTalentDestination(db.Model):
    __tablename__ = 'hd_talent_destination'
    __table_args__ = (
        db.Index('index_talent_destination_phone_talentid', 'phone', 'talent_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    talent_id = db.Column(db.BigInteger, nullable=False, info='候选人Id')
    phone = db.Column(db.String(50), info='手机号')
    destination = db.Column(db.String(50), info='转接号')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False)
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class HdTalentIndustry(db.Model):
    __tablename__ = 'hd_talent_industry'

    id = db.Column(db.BigInteger, primary_key=True)
    talentId = db.Column(db.BigInteger, nullable=False, index=True, info='候选人Id')
    industryId = db.Column(db.BigInteger)
    functionId = db.Column(db.BigInteger)
    addUserId = db.Column(db.BigInteger)
    industry_name = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='行业名称')
    function_name = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='职能名称')



class HdTalentMergeLog(db.Model):
    __tablename__ = 'hd_talent_merge_logs'

    id = db.Column(db.BigInteger, primary_key=True)
    talent_id = db.Column(db.BigInteger, nullable=False, index=True, info='简历ID')
    merge_talent_id = db.Column(db.String(250), index=True, info='合并的简历ID')
    create_time = db.Column(db.DateTime, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建用户')
    update_time = db.Column(db.DateTime, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改用户')
    defunct = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='是否无效 -> 1 : true 已删除；0 : false 有效')



class HdTalentPloy(db.Model):
    __tablename__ = 'hd_talent_ploy'

    talent_id = db.Column(db.BigInteger, primary_key=True, server_default=db.FetchedValue(), info='简历ID')
    onwork_selling_state = db.Column(db.Integer, index=True, info='简历上架状态 0：待上架 1：上架  2：下架 ')
    onwork_selling_type = db.Column(db.Integer, info='简历上架类型 0：On人脉 1：On到岗 2：On过保 ')
    onwork_selling_price = db.Column(db.Numeric(11, 4), nullable=False, server_default=db.FetchedValue(), info='简历上架价格')
    put_sale_time = db.Column(db.DateTime, index=True, info='上架时间')
    pull_sale_time = db.Column(db.DateTime, info='下架时间')
    put_json = db.Column(db.Text, info='上架简历信息')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建者')
    update_time = db.Column(db.DateTime, info='更新时间')
    update_user_id = db.Column(db.BigInteger, info='更新者')
    refresh_time = db.Column(db.DateTime, info='刷新时间')
    portrait_authorization_qr = db.Column(db.String(256), info='画像授权二维码')
    price_time = db.Column(db.DateTime, info='定价时间')
    pull_sale_reason = db.Column(db.Text, info='下架原因')
    portrait_id = db.Column(db.BigInteger, index=True, info='画像ID')
    headhunter_id = db.Column(db.BigInteger, info='猎头ID')
    product_channel = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='产品渠道 0：hh ；1：猎小智')
    has_on_contacts = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否为 on人脉  1:是 0:否')
    auth_status = db.Column(db.Integer, info='授权状态：-1 分享未操作 0未处理,1已授权，2已拒绝')
    service_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1.简历服务；2：猎头服务')
    has_active = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否面向激活简历')
    has_intent = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否面向意向简历')
    has_interview = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否面向到面简历')
    has_read = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否已读  0:未读 1:已读')
    has_cancel_auth_head_show = db.Column(db.Integer, server_default=db.FetchedValue(), info='取消授权头部显示 0:不显示 1:显示')



class HdTalentPloyCopy20201015(db.Model):
    __tablename__ = 'hd_talent_ploy_copy20201015'

    talent_id = db.Column(db.BigInteger, primary_key=True, server_default=db.FetchedValue(), info='简历ID')
    onwork_selling_state = db.Column(db.Integer, info='简历上架状态 0：待上架 1：上架  2：下架 ')
    onwork_selling_type = db.Column(db.Integer, info='简历上架类型 0：On人脉 1：On到岗 2：On过保 ')
    onwork_selling_price = db.Column(db.Numeric(11, 4), nullable=False, server_default=db.FetchedValue(), info='简历上架价格')
    put_sale_time = db.Column(db.DateTime, info='上架时间')
    pull_sale_time = db.Column(db.DateTime, info='下架时间')
    put_json = db.Column(db.Text, info='上架简历信息')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建者')
    update_time = db.Column(db.DateTime, info='更新时间')
    update_user_id = db.Column(db.BigInteger, info='更新者')
    refresh_time = db.Column(db.DateTime, info='刷新时间')
    portrait_authorization_qr = db.Column(db.String(256), info='画像授权二维码')
    price_time = db.Column(db.DateTime, info='定价时间')
    pull_sale_reason = db.Column(db.Text, info='下架原因')
    portrait_id = db.Column(db.BigInteger, info='画像ID')
    headhunter_id = db.Column(db.BigInteger, info='猎头ID')
    product_channel = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='产品渠道 0：hh ；1：猎小智')
    has_on_contacts = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否为 on人脉  1:是 0:否')
    auth_status = db.Column(db.Integer, info='授权状态：-1 分享未操作 0未处理,1已授权，2已拒绝')



class HdTalentPutaway(db.Model):
    __tablename__ = 'hd_talent_putaway'
    __table_args__ = (
        db.Index('idx_talent_putaway_talent_id_defunct_talent_model_id', 'talent_id', 'defunct', 'talent_model_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    talent_id = db.Column(db.BigInteger, info='简历id')
    talent_model_id = db.Column(db.String(64), info='人才库ID')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False)
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    company_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='简历上架企业')



class HdTalentSaleInfo(db.Model):
    __tablename__ = 'hd_talent_sale_info'
    __table_args__ = (
        db.Index('idx_talent_sale_talent_id_defunct', 'talent_id', 'defunct'),
        db.Index('idx_talent_sale_buyer_headhunter_company_id_talent_id_defunct', 'talent_id', 'defunct', 'buyer_headhunter_id', 'buyer_company_id'),
        db.Index('idx_talent_sale_seller_headhunter_company_id_talent_id_defunct', 'talent_id', 'defunct', 'seller_headhunter_id', 'seller_company_id')
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    buyer_company_id = db.Column(db.BigInteger, info='买家猎企ID')
    buyer_headhunter_id = db.Column(db.BigInteger, info='买家猎头ID')
    seller_company_id = db.Column(db.BigInteger, info='卖家猎企ID')
    seller_headhunter_id = db.Column(db.BigInteger, info='卖家猎头ID')
    talent_id = db.Column(db.BigInteger, info='简历id')
    talent_model_id = db.Column(db.String(64), info='人才库ID')
    selling_price = db.Column(db.Numeric(11, 4), server_default=db.FetchedValue(), info='简历金额')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False)
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class HdTalentUpdated(db.Model):
    __tablename__ = 'hd_talent_updated'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    talentId = db.Column(db.BigInteger, info='人才ID')
    addTime = db.Column(db.DateTime, info='创建时间')



class RdCompanyAccount(db.Model):
    __tablename__ = 'rd_company_account'

    company_id = db.Column(db.BigInteger, primary_key=True, info='猎企ID')
    hd_balance = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='余额')
    freeze_balance = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='冻结余额')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否删除0:false 1:true')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='修改时间')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    update_user_id = db.Column(db.BigInteger, info='修改人')



class RdCompanyAccountLog(db.Model):
    __tablename__ = 'rd_company_account_log'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    company_id = db.Column(db.BigInteger, info='猎企ID')
    operate_user_id = db.Column(db.BigInteger, info='操作人')
    talent_model_id = db.Column(db.String(64), info='人才库ID')
    operate_type = db.Column(db.Integer, info='操作类型')
    operate_amount = db.Column(db.BigInteger, info='操作金额')
    before_balance = db.Column(db.BigInteger, info='操作前余额')
    after_balance = db.Column(db.BigInteger, info='操作后余额')
    before_freeze_balance = db.Column(db.BigInteger, info='操作前冻结余额')
    after_freeze_balance = db.Column(db.BigInteger, info='操作后冻结余额')
    description = db.Column(db.Text, info='操作描述')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='修改时间')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    update_user_id = db.Column(db.BigInteger, info='修改人')



class RdTalentCollect(db.Model):
    __tablename__ = 'rd_talent_collect'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    company_id = db.Column(db.BigInteger, info='猎企ID')
    talent_model_id = db.Column(db.String(64), info='人才库ID')
    headhunter_id = db.Column(db.BigInteger, info='收藏猎头ID')
    position_id = db.Column(db.BigInteger, info='收藏职位ID')
    status_no = db.Column(db.Integer, info='收藏状态')
    collect_time = db.Column(db.DateTime, info='收藏时间')
    cancel_collect_time = db.Column(db.DateTime, info='取消收藏时间')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='修改时间')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    update_user_id = db.Column(db.BigInteger, info='修改人')



class RdTalentInvite(db.Model):
    __tablename__ = 'rd_talent_invite'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    company_id = db.Column(db.BigInteger, index=True, info='猎企ID')
    talent_model_id = db.Column(db.String(64), index=True, info='人才库ID')
    hd_talent_id = db.Column(db.BigInteger, info='HD人才ID')
    headhunter_id = db.Column(db.BigInteger, info='邀约猎头ID')
    invite_position_id = db.Column(db.BigInteger, info='邀约职位ID')
    invite_status = db.Column(db.Integer, info='邀约状态')
    invite_time = db.Column(db.DateTime, info='邀约时间')
    invite_complete_time = db.Column(db.DateTime, info='邀约完成时间')
    invite_complete_user_id = db.Column(db.BigInteger, info='邀约完成用户')
    invite_package_type = db.Column(db.Integer, info='邀约套餐类型')
    invite_price = db.Column(db.BigInteger, info='邀约单价')
    defunct = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='是否删除0:false 1:true')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='修改时间')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    update_user_id = db.Column(db.BigInteger, info='修改人')



class RdTalentInviteLog(db.Model):
    __tablename__ = 'rd_talent_invite_log'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    invite_id = db.Column(db.BigInteger, info='邀约ID')
    operate_user_id = db.Column(db.BigInteger, info='操作人')
    operate_type = db.Column(db.Integer, info='操作类型')
    before_status = db.Column(db.Integer, info='操作前状态')
    after_status = db.Column(db.Integer, info='操作后状态')
    operate_time = db.Column(db.DateTime, info='操作时间')
    remark = db.Column(db.String(2000), info='备注')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='修改时间')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    update_user_id = db.Column(db.BigInteger, info='修改人')



class RdTalentInviteReport(db.Model):
    __tablename__ = 'rd_talent_invite_report'

    invite_id = db.Column(db.BigInteger, primary_key=True, info='邀约ID')
    company_id = db.Column(db.BigInteger, info='猎企ID')
    talent_model_id = db.Column(db.String(64), info='人才库ID')
    hd_talent_id = db.Column(db.BigInteger, info='HD人才ID')
    invite_position_id = db.Column(db.BigInteger, info='邀约职位ID')
    call_result = db.Column(db.Integer, info='呼叫结果')
    invite_result = db.Column(db.Integer, info='邀约结果')
    not_answer_reason = db.Column(db.Integer, info='未接通原因')
    oneself = db.Column(db.Integer, info='是否本人')
    job_status = db.Column(db.Integer, info='求职状态')
    work_status = db.Column(db.Integer, info='在职状态')
    accept_work_place = db.Column(db.Integer, info='是否接受工作地点')
    voice_url = db.Column(db.String(255), info='电话录音URL')
    current_company = db.Column(db.String(256), info='当前公司')
    current_position = db.Column(db.String(256), info='当前职位')
    intention_company = db.Column(db.String(256), info='期望公司')
    intention_position = db.Column(db.String(256), info='期望职位')
    best_contact_time = db.Column(db.String(500), info='最佳联系时间')
    remark = db.Column(db.Text, info='备注')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='修改时间')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    update_user_id = db.Column(db.BigInteger, info='修改人')



class TbCvContent(db.Model):
    __tablename__ = 'tb_cv_content'

    cv_id = db.Column(db.BigInteger, primary_key=True, server_default=db.FetchedValue(), info='cv id')
    txt_content = db.Column(db.String, info='txt内容')
    htm_content = db.Column(db.String, info='htm内容')



class TbCvJsonContent(db.Model):
    __tablename__ = 'tb_cv_json_content'

    cv_id = db.Column(db.BigInteger, primary_key=True, server_default=db.FetchedValue(), info='cv id')
    json_content = db.Column(db.String, info='简历解析结果')
    create_time = db.Column(db.DateTime, info='创建时间')



class TbCvUpdated(db.Model):
    __tablename__ = 'tb_cv_updated'

    cv_id = db.Column(db.BigInteger, primary_key=True)
    file_link = db.Column(db.String(1000))



class TbHdMatchSearchCondition(db.Model):
    __tablename__ = 'tb_hd_match_search_condition'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_id = db.Column(db.BigInteger, info='所属用户')
    source_type = db.Column(db.Integer, info='来源类型(1:正常添加;2:搜索;3:擅长方向)')
    show_str = db.Column(db.String(1000), info='条件显示字符')
    keyword = db.Column(db.String(255), info='关键字')
    area_ids = db.Column(db.String(255), info='工作地点')
    industry_ids = db.Column(db.String(255), info='行业')
    profession_ids = db.Column(db.String(255), info='职能IDS')
    status_no = db.Column(db.Integer, info='状态(0:未启用;1:启用;)')
    defunct = db.Column(db.Integer, info='是否删除0:false 1:true')
    update_user_id = db.Column(db.BigInteger, info='修改人')
    update_time = db.Column(db.DateTime, info='修改时间')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    create_time = db.Column(db.DateTime, info='创建时间')
    min_show_annual_salary = db.Column(db.Float(10, True), info='最小年薪')
    max_show_annual_salary = db.Column(db.Float(10, True), info='最大年薪')
    spa_user_id = db.Column(db.BigInteger, info='spa用户ID')
    position_tag_id = db.Column(db.String(200), info='职位标签')
    enterprise_id = db.Column(db.BigInteger, info='雇主ID ')



class TbHeadhunterCacheTalent(db.Model):
    __tablename__ = 'tb_headhunter_cache_talent'

    id = db.Column(db.BigInteger, primary_key=True)
    headhunter_id = db.Column(db.BigInteger, nullable=False, info='猎头id')
    company_id = db.Column(db.BigInteger, nullable=False, info='猎企id')
    talent_md5_id = db.Column(db.String(50), nullable=False, info='外部人才id')
    create_user_id = db.Column(db.BigInteger, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False)
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除')
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)



class TbHhTalentCategory(db.Model):
    __tablename__ = 'tb_hh_talent_category'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    parent_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='父分类id')
    title = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='分类名称')
    headhunter_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='猎头ID')
    headhunter_company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎头公司ID')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除0未删除 1已删除')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='修改时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')



class TbHhTalentCategoryDefunct(db.Model):
    __tablename__ = 'tb_hh_talent_category_defunct'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    headhunter_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='猎头ID')
    category_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎头修改过的默认分类id')
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())



class TbLanguageLevel(db.Model):
    __tablename__ = 'tb_language_level'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    language_type_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='语言种类id')
    level_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='语言等级名称')



class TbLanguageType(db.Model):
    __tablename__ = 'tb_language_type'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    language_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='语言名称')



class TbPluginResume(db.Model):
    __tablename__ = 'tb_plugin_resume'

    id = db.Column(db.BigInteger, primary_key=True)
    uuid = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='uuid')
    source_web_link = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='简历内容来源网址')
    source_web_name = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='简历内容来源网址名称')
    html_content = db.Column(db.String, info='简历内容')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    cookie_content = db.Column(db.String(4000), nullable=False, server_default=db.FetchedValue(), info='网站cookie')



class TbPluginResumeRegular(db.Model):
    __tablename__ = 'tb_plugin_resume_regular'

    id = db.Column(db.BigInteger, primary_key=True)
    title = db.Column(db.String(255), info='字段描述')
    reg_key = db.Column(db.String(255), info='字段')
    reg_value = db.Column(db.String(255), info='正则')
    website = db.Column(db.Integer)



class TbTalentBatchRecord(db.Model):
    __tablename__ = 'tb_talent_batch_records'

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, nullable=False, info='用户编号')
    import_number = db.Column(db.String(200), unique=True, info='批次编号')
    import_time = db.Column(db.DateTime, info='导入时间')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='状态；0：正在导入；1:导入完成')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)



class TbTalentCollect(db.Model):
    __tablename__ = 'tb_talent_collect'

    id = db.Column(db.BigInteger, primary_key=True)
    talent_id = db.Column(db.BigInteger, nullable=False, info='人才Id')
    create_user_id = db.Column(db.BigInteger, info='增加用户id')
    create_time = db.Column(db.DateTime, info='增加时间')
    update_user_id = db.Column(db.BigInteger, info='更新用户id')
    update_time = db.Column(db.DateTime, info='更新时间')



class TbTalentContact(db.Model):
    __tablename__ = 'tb_talent_contact'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    talent_id = db.Column(db.BigInteger, nullable=False, index=True, info='人才ID')
    contact_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='联系类型：1手机2邮箱')
    contact = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='联系方式')
    create_time = db.Column(db.DateTime, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否无效 -> 1 : true 已删除；0 : false 有效')



class TbTalentDraft(db.Model):
    __tablename__ = 'tb_talent_draft'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    talent_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='人才id')
    phone = db.Column(db.String(100), info='电话')
    email = db.Column(db.String(200), info='邮箱')
    gender = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0女1男2未知')
    reason = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='推荐理由')
    motivation = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='求职动机')
    dimission_time = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='离职时间')
    current_annualsalary = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='当前年薪')
    expect_annualsalary = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='期望年薪')
    expect_interview_time = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='期望面试时间')
    create_time = db.Column(db.DateTime, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    avatar = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='头像url地址')
    talent_report_id = db.Column(db.BigInteger)
    position_name = db.Column(db.String(100), nullable=False, info='职位名称')
    position_id = db.Column(db.BigInteger, nullable=False, info='职位ID')
    name = db.Column(db.String(2000))
    is_edit = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否编辑过')
    current_salary = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='当前月薪')
    current_salary_months = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='当前月薪月数')
    expect_salary = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='期望月薪')
    expect_salary_months = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='期望月薪月数')
    other_welfare = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='其他福利')
    position_company_name = db.Column(db.String(2000), info='职位所属公司名称')



class TbTalentFollow(db.Model):
    __tablename__ = 'tb_talent_follow'

    id = db.Column(db.BigInteger, primary_key=True)
    talent_id = db.Column(db.BigInteger, nullable=False, info='人才id')
    hh_id = db.Column(db.BigInteger, nullable=False, info='猎头id')
    end_time = db.Column(db.DateTime, info='人才被跟进的结束时间')
    is_following_candidate = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否有流程中的订单')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())



class TbTalentFollowLog(db.Model):
    __tablename__ = 'tb_talent_follow_log'

    id = db.Column(db.BigInteger, primary_key=True)
    talent_id = db.Column(db.BigInteger, nullable=False, info='人才')
    hunter_id = db.Column(db.BigInteger, nullable=False, info='猎头')
    follow_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='更新日志的类型：1：跟进；2：放弃跟进')
    create_time = db.Column(db.DateTime, info='记录创建时间')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    update_time = db.Column(db.DateTime, info='更新时间')
    update_user_id = db.Column(db.BigInteger, info='更新人ID')
    company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())



class TbTalentImportRecord(db.Model):
    __tablename__ = 'tb_talent_import_record'

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, nullable=False, info='用户编号')
    cv_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='cv id')
    import_number = db.Column(db.String(200), index=True, info='批次编号')
    resume_name = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='简历名字')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='状态；-1:待上传; 0：全部；1:上传成功；2:正在解析；3:导入成功；4:导入失败；5:解析失败；6:上传失败；')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    fail_reason = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='失败原因')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    txt_content = db.Column(db.String, info='txt内容')
    talentId = db.Column(db.BigInteger, info='人才id')
    is_reanalysis = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否要重新解析；0:false;1:true')



class TbTalentIntentReport(db.Model):
    __tablename__ = 'tb_talent_intent_report'
    __table_args__ = (
        db.Index('talent_hunter', 'talent_id', 'hunter_id', 'company_id', 'defunct'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    talent_id = db.Column(db.BigInteger, info='意向报告对应的简历')
    hunter_id = db.Column(db.BigInteger, info='猎头')
    company_id = db.Column(db.BigInteger, info='猎企')
    report_title = db.Column(db.String(127), info='意向报告的名称')
    defunct = db.Column(db.Integer)
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)



class TbTalentIntentReportDetail(db.Model):
    __tablename__ = 'tb_talent_intent_report_detail'
    __table_args__ = (
        db.Index('reportIdDe', 'report_id', 'defunct'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    report_id = db.Column(db.BigInteger)
    intent_explan_id = db.Column(db.BigInteger, info='意向字典扩展表主键；如果是0，表示是自定义意向问题')
    intent_explan_title = db.Column(db.String(255), info='意向问题，也可能是自定义的问题')
    intent_explan_type = db.Column(db.Integer)
    intent_explan_value = db.Column(db.String(255), info='意向问题转换为的字符串')
    intent_explan_value_json = db.Column(db.String(2047), info='意向问题实际结果json')
    defunct = db.Column(db.Integer)
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)



class TbTalentLanguage(db.Model):
    __tablename__ = 'tb_talent_language'

    id = db.Column(db.BigInteger, primary_key=True)
    talent_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='人才id')
    language_type_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='语言种类id')
    language_level_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='语言等级id')
    other_language = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='其他语言名称')



class TbTalentMatchPosition(db.Model):
    __tablename__ = 'tb_talent_match_position'

    id = db.Column(db.BigInteger, primary_key=True, info='唯一编号')
    user_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='猎头编号')
    talent_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='人才编号')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='职位编号')
    match_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='匹配状态；0：默认；1：匹配；2：不匹配')
    is_read = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否已读')
    is_ignore = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否忽略:0未忽略；1忽略')
    ignore_reason_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='忽略原因状态字段')
    ignore_reason_desc = db.Column(db.String(255), info='忽略原因描述字段')
    source_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='记录产生来源:1、走九宫格匹配产生的;2、忽略备选简历产生的')
    match_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='匹配度')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    sort_type = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='排序序号')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, index=True)
    update_time = db.Column(db.DateTime, nullable=False)



class TbTalentModel(db.Model):
    __tablename__ = 'tb_talent_model'

    id = db.Column(db.BigInteger, primary_key=True)
    hunter_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='猎头id')
    model_condition = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='条件')
    model_description = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='描述')
    create_time = db.Column(db.DateTime, info='创建时间')



class TbTalentRecommandReport(db.Model):
    __tablename__ = 'tb_talent_recommand_report'

    id = db.Column(db.BigInteger, primary_key=True)
    talent_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='人才id')
    title = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='推荐报告名称')
    reason = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='推荐理由')
    motivation = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='求职动机')
    dimission_time = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='离职时间')
    current_annual_salary_desc = db.Column(db.String(600), nullable=False, server_default=db.FetchedValue(), info='当前年薪描述')
    expect_annual_salary_desc = db.Column(db.String(600), nullable=False, server_default=db.FetchedValue(), info='期望年薪描述')
    expect_annual_salary_new = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='期望年薪新字段:-1：面议')
    expect_interview_time = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='期望面试时间')
    create_time = db.Column(db.DateTime, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否无效 -> 1 : true 已删除；0 : false 有效')
    expect_salary = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='期望月薪')
    expect_salary_months = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='期望月薪月数')
    expect_annual_salary = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='期望年薪薪')
    communication_time = db.Column(db.DateTime, info='人才沟通时间')
    expect_salary_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='期望薪资税收类型,0:税前,1:税后')



class TbTalentResume(db.Model):
    __tablename__ = 'tb_talent_resume'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    talent_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='人才ID')
    title = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='简历名称')
    display_name = db.Column(db.String(200), info='显示名称')
    has_work_exp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否有工作经验 -> 1 : true 有；0 : false 无')
    has_project_exp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否有项目经验 -> 1 : true 有；0 : false 无')
    has_edu_exp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否有教育经历 -> 1 : true 有；0 : false 无')
    create_time = db.Column(db.DateTime, index=True, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    defunct = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='是否无效 -> 1 : true 已删除；0 : false 有效')
    integrity = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='简历完整度')
    source_url = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info=' 简历来源网站地址')



class TbTalentResumeCertification(db.Model):
    __tablename__ = 'tb_talent_resume_certification'

    id = db.Column(db.BigInteger, primary_key=True)
    resume_id = db.Column(db.BigInteger, nullable=False, index=True, info='求职者id')
    cer_name = db.Column(db.String(1023), nullable=False, server_default=db.FetchedValue(), info='证书名称')
    issued_year = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='证书获得年份')
    issued_month = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='证书获得月')
    description = db.Column(db.String(3000), nullable=False, server_default=db.FetchedValue(), info='描述')
    create_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())



class TbTalentResumeCompanyExp(db.Model):
    __tablename__ = 'tb_talent_resume_company_exp'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    resume_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='简历id')
    start_year = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开始年')
    start_month = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开始月')
    end_year = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='结束年')
    end_month = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='结束月')
    company_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='公司名称')
    industry_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='行业')
    company_kind = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='性质')
    company_scale = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='规模')
    description = db.Column(db.String(3000), nullable=False, server_default=db.FetchedValue(), info='公司描述')
    create_time = db.Column(db.DateTime, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    defunct = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='是否无效 -> 1 : true 已删除；0 : false 有效')



class TbTalentResumeCompanyWorkExp(db.Model):
    __tablename__ = 'tb_talent_resume_company_work_exp'

    id = db.Column(db.BigInteger, primary_key=True)
    resume_company_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='公司经历id')
    start_year = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开始年')
    start_month = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开始月')
    end_year = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='结束年')
    end_month = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='结束月')
    job_title = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='职位名称')
    work_address = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='工作地点')
    subordinate = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='下属人数')
    work_duty = db.Column(db.String(3000), nullable=False, server_default=db.FetchedValue(), info='工作职责')
    depart = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='所在部门')
    report = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='汇报对象')
    salary = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='月薪')
    salary_months = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='月薪月数')
    achievement = db.Column(db.String(3000), nullable=False, server_default=db.FetchedValue(), info='工作业绩')
    create_time = db.Column(db.DateTime, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    defunct = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='是否无效 -> 1 : true 已删除；0 : false 有效')



class TbTalentResumeEduExp(db.Model):
    __tablename__ = 'tb_talent_resume_edu_exp'

    id = db.Column(db.BigInteger, primary_key=True)
    resume_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='简历id')
    start_time = db.Column(db.String(200))
    end_time = db.Column(db.String(200))
    school = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='学校')
    school_logo = db.Column(db.String(500), server_default=db.FetchedValue(), info='学校logo')
    profession = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='专业')
    degree_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='学历id')
    degree = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='学历名称')
    create_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    defunct = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='是否无效 -> 1 : true 已删除；0 : false 有效')
    start_year = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开始年')
    start_month = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开始月')
    end_year = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='结束年')
    end_month = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='结束月')
    advanced_degree = db.Column(db.String(100), info='学位')
    department = db.Column(db.String(100), info='院系')
    summary = db.Column(db.String(6000), info='详细介绍 ')
    studii = db.Column(db.String(100), info='留学经历 ')
    overseas_work = db.Column(db.Integer, info='是否海外经验-1是；0否')
    recruitment_status = db.Column(db.Integer, info='是否统招 1是, 2否')
    remark = db.Column(db.Text, info='备注')



class TbTalentResumeLanguageAbility(db.Model):
    __tablename__ = 'tb_talent_resume_language_ability'

    id = db.Column(db.BigInteger, primary_key=True)
    resume_id = db.Column(db.BigInteger, nullable=False, index=True, info='求职者id')
    language_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='语种')
    verbal = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='口语能力  一般:1 \t良好:2  \t熟练:3 \t精通:4')
    literacy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='读写能力  一般:1 \t良好:2  \t熟练:3 \t精通:4')
    language_level = db.Column(db.String(30), nullable=False, server_default=db.FetchedValue(), info='语言等级')
    score = db.Column(db.String(100), info='分数')
    create_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())



class TbTalentResumeProjectExp(db.Model):
    __tablename__ = 'tb_talent_resume_project_exp'

    id = db.Column(db.BigInteger, primary_key=True)
    resume_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='简历id')
    start_time = db.Column(db.String(200))
    end_time = db.Column(db.String(200))
    company_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='公司名称')
    project_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='项目名称')
    description = db.Column(db.String(6000), nullable=False, server_default=db.FetchedValue(), info='项目描述')
    create_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    defunct = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='是否无效 -> 1 : true 已删除；0 : false 有效')
    start_year = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开始年')
    start_month = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开始月')
    end_year = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='结束年')
    end_month = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='结束月')
    project_job_title = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='项目职务')
    project_duty = db.Column(db.String(5000))
    time_desc = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='项目时间描述')
    achievement = db.Column(db.String(5000), info='项目业绩')



class TbTalentResumeSkillAbility(db.Model):
    __tablename__ = 'tb_talent_resume_skill_ability'

    id = db.Column(db.BigInteger, primary_key=True)
    resume_id = db.Column(db.BigInteger, nullable=False, index=True)
    skill_name = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='技能名称')
    level = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='熟练程度')
    how_long = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='使用时间')
    create_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())



class TbTalentResumeTrainExp(db.Model):
    __tablename__ = 'tb_talent_resume_train_exp'

    id = db.Column(db.BigInteger, primary_key=True)
    resume_id = db.Column(db.BigInteger, nullable=False, index=True, info='求职者id')
    cer_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='证书名称')
    agency_name = db.Column(db.String(200), server_default=db.FetchedValue(), info='培训机构名称')
    description = db.Column(db.String(3000), nullable=False, server_default=db.FetchedValue(), info='描述')
    start_year = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开始年份')
    end_year = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='结束年份')
    start_month = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开始月')
    end_month = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='结束月')
    create_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    course = db.Column(db.String(200), info='课程')
    address = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='地点')
    title = db.Column(db.String(500), info='培训名称 ')



class TbTalentResumeWorkExp(db.Model):
    __tablename__ = 'tb_talent_resume_work_exp'

    id = db.Column(db.BigInteger, primary_key=True)
    resume_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='简历id')
    start_time = db.Column(db.String(200))
    end_time = db.Column(db.String(200))
    company_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='公司名称')
    company_logo = db.Column(db.String(500), server_default=db.FetchedValue(), info='公司logo')
    profession = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='职能')
    position = db.Column(db.String(400), nullable=False, server_default=db.FetchedValue(), info='职位')
    description = db.Column(db.String(6000), nullable=False, server_default=db.FetchedValue(), info='工作描述')
    create_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue(), info='更新时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    defunct = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='是否无效 -> 1 : true 已删除；0 : false 有效')
    start_year = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开始年')
    start_month = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开始月')
    end_year = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='结束年')
    end_month = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='结束月')
    function_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职能id')
    industry_ids = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='公司行业编号：多个以逗号隔开')
    department = db.Column(db.String(500), info='所属部门')
    periods_of_time = db.Column(db.String(100), info='工作时间段 ')
    work_location = db.Column(db.String(500), info='工作地点 ')
    company_size = db.Column(db.String(100), info='公司规模 ')
    company_type = db.Column(db.String(100), info='公司性质')
    title = db.Column(db.String(100), info='职务')
    salary = db.Column(db.String(100), info='薪水 ')
    leader = db.Column(db.String(100), info='领导/汇报对象')
    underling_number = db.Column(db.String(100), info='下属人数')
    reason_of_leaving = db.Column(db.String(500))
    achievement = db.Column(db.String(5000))
    work_type = db.Column(db.String(100), info='工作类型(实习经历、工作经历) ')
    overseas_work = db.Column(db.Integer, info='是否海外经验-1是；0否')
    company_description = db.Column(db.Text, info='公司介绍')
    responsible_area = db.Column(db.String(100), info='负责区域')
    work_location_ids = db.Column(db.String(100), server_default=db.FetchedValue(), info='工作地点 ids 用英文 , 隔开')



class TbTalentSearchCondition(db.Model):
    __tablename__ = 'tb_talent_search_condition'

    id = db.Column(db.BigInteger, primary_key=True)
    source = db.Column(db.Integer)
    condition_json = db.Column(db.String(1500))
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)



class TbTalentTimingAlert(db.Model):
    __tablename__ = 'tb_talent_timing_alert'

    id = db.Column(db.BigInteger, primary_key=True)
    talent_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    user_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue())
    content = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue())
    alert_time = db.Column(db.DateTime, nullable=False)
    advance_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime)



class TbUserCompanyApplication(db.Model):
    __tablename__ = 'tb_user_company_application'
    __table_args__ = (
        db.Index('company_id', 'company_id', 'job_number'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_id = db.Column(db.BigInteger, nullable=False)
    company_id = db.Column(db.BigInteger, nullable=False, info='公司ID')
    status = db.Column(db.SmallInteger, server_default=db.FetchedValue(), info='1=申请中、2=已拒绝、3=已撤销、4=已通过、5=已取消关联')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建人')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, info='修改人')
    update_time = db.Column(db.DateTime, info='修改时间')
    comment = db.Column(db.String(100), nullable=False)
    job_number = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='猎头工号')
    handover_job_number = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='交接猎头工号')



t_test = db.Table(
    'test',
    db.Column('id', db.Integer)
)

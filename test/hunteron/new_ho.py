# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Candidate(db.Model):
    __tablename__ = 'candidate'
    __table_args__ = (
        db.Index('idx_candidate_updatetime_headComId', 'updateTime', 'headhunterCompanyId'),
        db.Index('positionAssignId', 'positionAssignId', 'headhunterId', 'createTime'),
        db.Index('idx_positionCompanyId_allstatus', 'positionCompanyId', 'all_status'),
        db.Index('idx_talentId_positionCompanyId', 'talentId', 'positionCompanyId'),
        db.Index('idx_email_positionCompanyId', 'email', 'positionCompanyId'),
        db.Index('createTime', 'createTime', 'updateTime'),
        db.Index('idx_candidate_positionAssignId', 'positionAssignId', 'all_status'),
        db.Index('idx_positionCompanyId_recommendtime', 'positionCompanyId', 'recommend_time'),
        db.Index('idx_headhunterCompanyId_recommendtime', 'headhunterCompanyId', 'recommend_time'),
        db.Index('idx_userid_status', 'createUserId', 'all_status'),
        db.Index('idx_cellPhone_positionCompanyId', 'cellPhone', 'positionCompanyId')
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    talentId = db.Column(db.BigInteger, index=True)
    positionId = db.Column(db.BigInteger, index=True, info='职位ID')
    positionCompanyId = db.Column(db.BigInteger, index=True, info='职位的公司id')
    headhunterCompanyId = db.Column(db.BigInteger, index=True, info='猎头的公司id')
    headhunterId = db.Column(db.BigInteger, index=True, info='猎头id')
    name = db.Column(db.String(100), info='从talent copy，可以修改')
    cellPhone = db.Column(db.String(100), index=True, info='手机号')
    email = db.Column(db.String(200), index=True, info='邮箱')
    rewardType = db.Column(db.Integer, info='0：固定佣金  1：年薪百分比')
    fixedRewardAmount = db.Column(db.Float(asdecimal=True), info='固定佣金的 金额   ')
    percentageNumbric = db.Column(db.Float(asdecimal=True), info='百分比 数字 20 表示 年薪* 20%')
    resumeId = db.Column(db.BigInteger, index=True)
    description = db.Column(db.String(2000), info='描述')
    terminatedReason = db.Column(db.String(1000))
    status = db.Column(db.Integer, index=True, info='-4：待猎上审核，-3：猎上拒绝，-2：打回待审核的候选人，-1：新创建待审核的候选人，0：新创建的候选人 ，1：已下载简历的候选人 ，2：被拒绝的候选人 ，3：面试中的候选人 ，4:已雇佣的候选人(有了placement) ，5：被撤消的候选人（hh取消了），7：待定')
    createUserId = db.Column(db.BigInteger, info='创建者')
    updateUserId = db.Column(db.BigInteger, info='更新者')
    createTime = db.Column(db.DateTime, info='创建时间')
    updateTime = db.Column(db.DateTime, server_default=db.FetchedValue(), info='更新时间')
    interviewed = db.Column(db.Integer, info='点击过Interview的candidate，更新这个状态 0 =没interview过 1= interview过')
    positionCreateId = db.Column(db.BigInteger)
    resumeName = db.Column(db.String(800))
    resumeUrl = db.Column(db.String(800))
    hastenCandidateTime = db.Column(db.Integer, server_default=db.FetchedValue(), info='系统通知HR催促处理候选人次数')
    positionAssignId = db.Column(db.BigInteger, info='职位负责人')
    engageType = db.Column(db.Integer, info='候选人身份识别 0签约，1合作')
    otherReward = db.Column(db.String(500), info='其他佣金形式')
    holderId = db.Column(db.BigInteger, info='候选人持有者')
    currentAnnual = db.Column(db.String(800), info='当前年薪')
    expectAnnual = db.Column(db.String(200), info='期望年薪')
    interviewId = db.Column(db.BigInteger, info='当前面试ID')
    priority = db.Column(db.Integer, server_default=db.FetchedValue())
    hr_priority = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    last_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    undetermined_reason = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue())
    undetermined_time = db.Column(db.DateTime)
    gender = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0女1男2未知')
    birthday = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='出生日期')
    marital_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='婚姻状况：0未知1已婚2未婚')
    id_card = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='身份证号码')
    city_id = db.Column(db.BigInteger, info='城市id')
    city = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='城市名称')
    address = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='地址')
    expect_city = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='期望城市')
    avatar = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='头像')
    recommand_report_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='推荐报告')
    standardized = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否标准化过0未标准化1标准化中2已标准化')
    degree_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='学历id')
    self_evaluation = db.Column(db.String(5000), nullable=False, server_default=db.FetchedValue(), info='自我评价')
    salary_desc = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='薪资描述')
    extra_msg = db.Column(db.Text, info='附加信息')
    apply_job_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='求职状态,1:在职,看看新机会 2:在职,急寻新工作 3:在职,暂无跳槽打算 4:离职,正在找工作')
    expect_industry = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='期望行业id')
    expect_function = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='期望职能id')
    primal_referee_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='原本的推荐猎头ID')
    old_head_hunter_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='原猎头ID')
    english_name = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='英文名')
    guarantee_time = db.Column(db.Integer, info='保证期')
    integrity = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='简历完整度')
    status_time = db.Column(db.DateTime, index=True, info='状态最后更新时间')
    report_standardized = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='推荐报告是否标准化;0:未标准化;1:标准化')
    hr_read_time = db.Column(db.DateTime, info='hr第一次阅读候选人时间')
    hr_feedback_time = db.Column(db.DateTime, info='hr反馈时间')
    last_hr_feedback_time = db.Column(db.DateTime, info='在新推已阅状态下，最后一次反馈时间')
    recommend_time = db.Column(db.DateTime, index=True, info='推荐时间')
    cv_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='使用的cv')
    hide_hr = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info=' 是否隐藏')
    revoke_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info=' 撤销类型;0:非撤销;1:自动撤销;2:猎头撤销;3:crm撤销')
    school = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='学校')
    start_work_year = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开始工作年份')
    start_work_month = db.Column(db.Integer, server_default=db.FetchedValue(), info='开始工作月份')
    company_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='公司')
    job_title = db.Column(db.String(400), nullable=False, server_default=db.FetchedValue(), info='职位')
    original_reward = db.Column(db.Float(asdecimal=True), info='原始佣金')
    original_guarantee_time = db.Column(db.Integer, info='原始保证期')
    arrived = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info=' 是否到达：0未到达1到达')
    contacted = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否联系过候选人,0:未联系过，1：联系过')
    jobhunter_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='C端用户id')
    position_activity_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职位活动id')
    all_status = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='候选人整个流程中的状态')
    resume_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='对候选人简历的标记：1 简历通过，2 简历未通过，3 简历已处理，4 重复')
    overdue_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否逾期， 0未逾期  1 逾期')
    hr_feedback_hours = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='hr约定反馈时长（小时数）')
    current_overdue_status = db.Column(db.Integer, server_default=db.FetchedValue(), info='订单的当前逾期状态；0：未逾期；1：当前逾期')
    last_overdue_time = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='最后一次反馈逾期的，逾期时间，（工作日9小时）分钟数；没有逾期过，则是0')
    position_annual_salary = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='职位基本年薪(计算佣金)')
    position_max_annual_salary = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='职位最大基本年薪(计算佣金)')
    pre_rate = db.Column(db.Float(asdecimal=True), server_default=db.FetchedValue(), info='到岗预付比率')
    is_noticed = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否已经通知')
    product_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='职位产品类型:1:标准版,2：佣金宝，3：到岗快')
    product_pay_rate = db.Column(db.Integer, info='产品到岗时付的佣金比例')
    expert_tagContent = db.Column(db.String(200), info='精通技能')
    competent_tagContent = db.Column(db.String(200), info='熟悉技能')
    other_require = db.Column(db.String(550), server_default=db.FetchedValue(), info='其它要求')
    expect_position_titles = db.Column(db.String(200), server_default=db.FetchedValue(), info='期望职位')
    contact_period = db.Column(db.Integer, server_default=db.FetchedValue(), info='0.不限 1.工作日(10:00-18:00) 2.工作日(18:00-21:00) 3.节假日')
    pay_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='猎头分成比例')
    specific_pay_rate = db.Column(db.Integer, info='特殊分成比例')
    has_new_feedback = db.Column(db.Integer, server_default=db.FetchedValue())
    pa_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='成单的时候，pa_id')
    order_source = db.Column(db.Integer, server_default=db.FetchedValue())
    special_work_year = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职能经验(特殊工作年限)')
    special_work_exp = db.Column(db.String(1000), info='细分职能(内容类型)')
    degree_entrance_examination = db.Column(db.Integer, info='null:未填;0:非统招;1:统招')
    operation_pa_id = db.Column(db.String(1000), server_default=db.FetchedValue(), info='成单时职位的运营pa id')
    inner_level_code = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='内部级别')



class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.BigInteger, primary_key=True, server_default=db.FetchedValue(), info='主键')
    name = db.Column(db.String(255), info='名称')
    order = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序')
    display_name = db.Column(db.String(30), server_default=db.FetchedValue(), info='显示名')



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



class City(db.Model):
    __tablename__ = 'city'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    name = db.Column(db.String(100), info='名称')
    provinceId = db.Column(db.BigInteger, info='省市ID')
    districtcode = db.Column(db.String(10), info='行政区号')
    postcode = db.Column(db.String(10), info='邮编')
    order = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序')



class CityBak20160219(db.Model):
    __tablename__ = 'city_bak20160219'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(100))
    provinceId = db.Column(db.BigInteger)
    postcode = db.Column(db.String(10))
    order = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序')



class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    objId = db.Column(db.BigInteger, index=True, info='对象ID')
    objType = db.Column(db.String(15), info='对象类型')
    createUserId = db.Column(db.BigInteger, info='创建者')
    createCompanyId = db.Column(db.BigInteger, info='公司ID')
    createUserType = db.Column(db.Integer, info='1：企业，2：猎头，3：管理员，4：渠道用户')
    createTime = db.Column(db.DateTime, info='创建时间')
    comment = db.Column(db.Text, info='备注')
    module = db.Column(db.String(15), info='对象模型')
    title = db.Column(db.String(150), info='备注标题')
    candidate_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='候选人ID')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除')
    candidate_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='候选人状态')
    position_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='候选人沟通记录职位id')



class Company(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    companyName = db.Column(db.String(200), info='公司名')
    displayName = db.Column(db.String(200), info='保密时候显示')
    country = db.Column(db.String(200), info='国家')
    province = db.Column(db.String(200), info='省')
    city = db.Column(db.String(200), info='市')
    address = db.Column(db.String(300), info='地址')
    zipCode = db.Column(db.String(100))
    recommendBy = db.Column(db.BigInteger, info='公司加入时使用的推荐号')
    webSite = db.Column(db.String(200))
    introduction = db.Column(db.Text, info='限制在1000字内')
    enterpriseCode = db.Column(db.String(200))
    enterpriseCodeVerification = db.Column(db.Integer, info='证书验证 0：未验证；1：以验证')
    mainContact = db.Column(db.String(200), info='猎企负责人')
    status = db.Column(db.Integer, info='-2 审核未通过 ，0 待审核，1 正常，2 已注销，3 已删除，4 系统录入，5 未提交审核，6 升级中')
    createUserId = db.Column(db.BigInteger, info='创建者')
    createTime = db.Column(db.DateTime, info='创建时间')
    updateUserId = db.Column(db.BigInteger, info='更新者')
    updateTime = db.Column(db.DateTime, server_default=db.FetchedValue(), info='更新时间')
    companyType = db.Column(db.Integer, info='1：企业公司；2：猎头公司；3.管理员用户；4.渠道用户')
    companyScale = db.Column(db.Integer, info='1-10\\r\\n            10-50\\r\\n            50-100\\r\\n            100-500\\r\\n            500以上')
    industry1 = db.Column(db.Integer)
    industry2 = db.Column(db.Integer)
    totalInterview = db.Column(db.Integer, server_default=db.FetchedValue(), info='面试数')
    totalCandidate = db.Column(db.Integer, server_default=db.FetchedValue(), info='收到候选人数')
    totalPlacement = db.Column(db.Integer, server_default=db.FetchedValue(), info='录用数')
    contractStatus = db.Column(db.Integer, server_default=db.FetchedValue(), info='合同状态（0 未寄出合同，1 已寄出合同，2 签约）')
    marketId = db.Column(db.BigInteger, info='销售负责人（admin user id）公司销售')
    afterId = db.Column(db.BigInteger, info='售后负责人（admin user id）客服')
    logoUrl = db.Column(db.String(100), info='logo（可以存路径）')
    hastenCandidateTime = db.Column(db.Integer, server_default=db.FetchedValue(), info='系统通知HR催促处理候选人次数')
    companyStyle = db.Column(db.Integer, info='企业性质,形式 0,外资（欧美)1,外资（非欧美)2,合资（欧美）  3,合资（非欧美） 4,国企/上市公司  5,民营/私营公司 6,外企代表处 7,其它性质')
    approveTime = db.Column(db.DateTime, info='通过审核时间')
    phone = db.Column(db.String(50), info='电话号码')
    fax = db.Column(db.String(50), info='公司传真')
    rootId = db.Column(db.BigInteger, index=True, info='公司负责人ID')
    pact = db.Column(db.Integer, info='是否同意系统协议')
    pactTime = db.Column(db.DateTime, info='同意协议时间')
    contractNo = db.Column(db.String(25), info='合同编号')
    guaranteeMonth = db.Column(db.Integer, info='保证期（单位：月）')
    officialName = db.Column(db.String(50), info='企业合同名称')
    specialTerm = db.Column(db.String(1000), info='特殊条款')
    allowance = db.Column(db.String(1000), info='企业福利')
    agreeContractDate = db.Column(db.Date, info='合同签订日期')
    differentContract = db.Column(db.String(1000), info='合同包括与平台协议不同点的描述内容')
    serviceAdmin = db.Column(db.BigInteger)
    salseAdmin = db.Column(db.BigInteger, info='销售负责人')
    establish_year = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='成立年份')
    registration_number = db.Column(db.String(128), nullable=False, server_default=db.FetchedValue(), info='税务登记证号')
    bank = db.Column(db.String(50), info='开户行')
    account = db.Column(db.String(50), info='银行账户名')
    accountNumber = db.Column(db.String(50), info='银行账号')
    contractattachment = db.Column(db.String(100), info='法人代表')
    payDays = db.Column(db.Integer, info='付款日期')
    payRate = db.Column(db.Float(asdecimal=True), info='付款比例')
    shortName = db.Column(db.String(100), info='后台显示公司名简称')
    source = db.Column(db.Integer, info='客户来源')
    sourceMark = db.Column(db.String(30), info='客户来源备注')
    firstContactTime = db.Column(db.String(30), info='第一次联系时间')
    express = db.Column(db.String(50), info='快递信息')
    contractAddress = db.Column(db.String(50), info='合同寄出地址')
    contractRecipients = db.Column(db.String(50), info='合同接收人')
    activeContract = db.Column(db.Integer, info='合同的有效性')
    referredBy = db.Column(db.BigInteger, info='推荐人ID')
    taskAdmin = db.Column(db.BigInteger, info='任务负责人')
    activeReferred = db.Column(db.Integer, info='是否已过推荐期')
    totalPosition = db.Column(db.Integer, info='企业：发布的总职位数；猎头：推荐过的总职位数')
    totalOpenPosition = db.Column(db.Integer, info='企业 : 开放中职位总数；猎头：正在做的开放中的职位')
    totalUser = db.Column(db.Integer, info='用户数')
    totalVisit = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否拜访过客户')
    totalFollow = db.Column(db.Integer, info='跟进次数')
    totalSecondInterview = db.Column(db.Integer, server_default=db.FetchedValue(), info='二面')
    totalContract = db.Column(db.Integer, info='企业：合作猎头数；猎头：合作企业数')
    totalRequest = db.Column(db.Integer, info='企业 : 当前申请数；猎头：当前申请数')
    independent = db.Column(db.SmallInteger, server_default=db.FetchedValue(), info='猎头公司注册类型 0 猎头公司 1 全职SOHO猎头 2 兼职SOHO猎头')
    bdhAdmin = db.Column(db.BigInteger, info='BDH')
    parentId = db.Column(db.BigInteger)
    enterpriseCodeAttachment = db.Column(db.String(100))
    registerIP = db.Column(db.String(100))
    rejectReason = db.Column(db.String(200))
    provinceId = db.Column(db.Integer)
    cityId = db.Column(db.Integer)
    organizationCodeCertificateAttachment = db.Column(db.String(100))
    permissionStatus = db.Column(db.String(10))
    reject_content = db.Column(db.String(150), nullable=False, server_default=db.FetchedValue(), info='拒绝原因')
    reject_time = db.Column(db.DateTime, info='拒绝时间')
    experienced_areas = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='公司擅长地区')
    experienced_industrys = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='公司擅长行业')
    submit_verify_time = db.Column(db.DateTime, info='提交公司认证时间')
    rejected_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0：正常；打回类型 1：审核通过前打回；2：审核通过后打回')
    paction_start_time = db.Column(db.DateTime, info='合同的开始时间')
    paction_end_time = db.Column(db.DateTime, info='合同的结束时间')
    old_pay_rate = db.Column(db.Float(asdecimal=True))
    bdh_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='BDH')
    em_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='EM')
    single_verify_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='做单认证状态；0:审核中;1:审核通过;2:审核拒绝')
    credit_code = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='信用等级code,默认0为未评级')
    business_volume = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='年营业额')
    contacts_cellphone = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue(), info='联系人手机号')
    area_code = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue(), info='联系人手机号区号')
    contacts_identity = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='联系人身份：1：职员；2：合伙人；3：创始人')
    contacts_email = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='联系邮箱')
    legal_person_name = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='法人代表姓名')
    paction_active = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='合同状态:-2 新增, -1 待确定 , 0 合同确定, 1 合同生效, 2 合同失效')
    identification_code = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='唯一标识码')
    am_id = db.Column(db.BigInteger, info='am_id')
    pay_rate_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='分成类型 1 19分成 2 28分成 3 37分成 4 28&37')
    collateral = db.Column(db.Numeric(20, 4), server_default=db.FetchedValue(), info='保证金')
    resume_balance = db.Column(db.Numeric(20, 4), server_default=db.FetchedValue(), info='简历宝余额')
    is_lieying = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否为猎英,0:非猎英,1:猎英')
    collateral_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='保证金状态 1：已缴纳；2：未缴纳')
    cooperation_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='合作类型;1:DEMO团队;2:合资;3:加盟;4:平台')
    customer_id = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='FDD 客户ID')
    fdd_email_account = db.Column(db.String(50), server_default=db.FetchedValue(), info='FDD 邮箱账号')
    source_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='来源类型（1：正常；2：线下供应商）')



class CompanyBak2016(db.Model):
    __tablename__ = 'company_bak2016'

    id = db.Column(db.BigInteger, primary_key=True)
    companyName = db.Column(db.String(200))
    displayName = db.Column(db.String(200), info='保密时候显示')
    country = db.Column(db.String(200))
    province = db.Column(db.String(200))
    city = db.Column(db.String(200))
    address = db.Column(db.String(300))
    zipCode = db.Column(db.String(100))
    recommendBy = db.Column(db.BigInteger, info='公司加入时使用的推荐号')
    webSite = db.Column(db.String(200))
    introduction = db.Column(db.Text, info='限制在1000字内')
    enterpriseCode = db.Column(db.String(200))
    enterpriseCodeVerification = db.Column(db.Integer, info='证书验证 0：未验证；1：以验证')
    mainContact = db.Column(db.String(200))
    status = db.Column(db.Integer, info='-2 审核未通过 ，0 待审核，1 正常，2 已注销，3 已删除，4 系统录入，5 未提交审核，6 升级中')
    createUserId = db.Column(db.BigInteger)
    createTime = db.Column(db.DateTime)
    updateUserId = db.Column(db.BigInteger)
    updateTime = db.Column(db.DateTime)
    companyType = db.Column(db.Integer, info='1：企业公司；2：猎头公司；3.管理员用户；4.渠道用户')
    companyScale = db.Column(db.Integer, info='1-10\\r\\n            10-50\\r\\n            50-100\\r\\n            100-500\\r\\n            500以上')
    industry1 = db.Column(db.Integer)
    industry2 = db.Column(db.Integer)
    totalInterview = db.Column(db.Integer, server_default=db.FetchedValue(), info='面试数')
    totalCandidate = db.Column(db.Integer, server_default=db.FetchedValue(), info='收到候选人数')
    totalPlacement = db.Column(db.Integer, server_default=db.FetchedValue(), info='录用数')
    contractStatus = db.Column(db.Integer, server_default=db.FetchedValue(), info='合同状态（0 未寄出合同，1 已寄出合同，2 签约）')
    marketId = db.Column(db.BigInteger, info='销售负责人（admin user id）公司销售')
    afterId = db.Column(db.BigInteger, info='售后负责人（admin user id）客服')
    logoUrl = db.Column(db.String(100), info='logo（可以存路径）')
    hastenCandidateTime = db.Column(db.Integer, server_default=db.FetchedValue(), info='系统通知HR催促处理候选人次数')
    companyStyle = db.Column(db.Integer, info='企业性质,形式 0,外资（欧美)1,外资（非欧美)2,合资（欧美）  3,合资（非欧美） 4,国企/上市公司  5,民营/私营公司 6,外企代表处 7,其它性质')
    approveTime = db.Column(db.DateTime, info='通过审核时间')
    phone = db.Column(db.String(50), info='电话号码')
    fax = db.Column(db.String(50), info='公司传真')
    rootId = db.Column(db.BigInteger, info='公司负责人ID')
    pact = db.Column(db.Integer, info='是否同意系统协议')
    pactTime = db.Column(db.DateTime, info='同意协议时间')
    contractNo = db.Column(db.String(25), info='合同编号')
    guaranteeMonth = db.Column(db.Integer, info='保证期（单位：月）')
    officialName = db.Column(db.String(50), info='企业合同名称')
    specialTerm = db.Column(db.String(1000), info='特殊条款')
    allowance = db.Column(db.String(1000), info='企业福利')
    agreeContractDate = db.Column(db.Date, info='合同签订日期')
    differentContract = db.Column(db.String(1000), info='合同包括与平台协议不同点的描述内容')
    serviceAdmin = db.Column(db.BigInteger)
    salseAdmin = db.Column(db.BigInteger, info='销售负责人（BDH）')
    bank = db.Column(db.String(50), info='开户行')
    account = db.Column(db.String(50), info='银行账户名')
    accountNumber = db.Column(db.String(50), info='银行账号')
    contractattachment = db.Column(db.String(100), info='法人代表')
    payDays = db.Column(db.Integer, info='付款日期')
    payRate = db.Column(db.Float(asdecimal=True), info='付款比例')
    shortName = db.Column(db.String(100), info='后台显示公司名简称')
    source = db.Column(db.Integer, info='客户来源')
    sourceMark = db.Column(db.String(30), info='客户来源备注')
    firstContactTime = db.Column(db.String(30), info='第一次联系时间')
    express = db.Column(db.String(50), info='快递信息')
    contractAddress = db.Column(db.String(50), info='合同寄出地址')
    contractRecipients = db.Column(db.String(50), info='合同接收人')
    activeContract = db.Column(db.Integer, info='合同的有效性')
    referredBy = db.Column(db.BigInteger, info='推荐人ID')
    taskAdmin = db.Column(db.BigInteger, info='任务负责人')
    activeReferred = db.Column(db.Integer, info='是否已过推荐期')
    totalPosition = db.Column(db.Integer, info='企业：发布的总职位数；猎头：推荐过的总职位数')
    totalOpenPosition = db.Column(db.Integer, info='企业 : 开放中职位总数；猎头：正在做的开放中的职位')
    totalUser = db.Column(db.Integer, info='用户数')
    totalVisit = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否拜访过客户')
    totalFollow = db.Column(db.Integer, info='跟进次数')
    totalSecondInterview = db.Column(db.Integer, server_default=db.FetchedValue(), info='二面')
    totalContract = db.Column(db.Integer, info='企业：合作猎头数；猎头：合作企业数')
    totalRequest = db.Column(db.Integer, info='企业 : 当前申请数；猎头：当前申请数')
    independent = db.Column(db.SmallInteger, server_default=db.FetchedValue(), info='猎头公司注册类型 0 猎头公司 1 全职SOHO猎头 2 兼职SOHO猎头')
    bdhAdmin = db.Column(db.BigInteger, info='BDH')
    parentId = db.Column(db.BigInteger)
    enterpriseCodeAttachment = db.Column(db.String(100))
    registerIP = db.Column(db.String(100))
    rejectReason = db.Column(db.String(200))
    provinceId = db.Column(db.Integer)
    cityId = db.Column(db.Integer)
    organizationCodeCertificateAttachment = db.Column(db.String(100))
    permissionStatus = db.Column(db.String(10))
    reject_content = db.Column(db.String(150), nullable=False, server_default=db.FetchedValue(), info='拒绝原因')
    reject_time = db.Column(db.DateTime, info='拒绝时间')
    experienced_areas = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='公司擅长地区')
    experienced_industrys = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='公司擅长行业')
    submit_verify_time = db.Column(db.DateTime, info='提交公司认证时间')
    rejected_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0：正常；打回类型 1：审核通过前打回；2：审核通过后打回')



class CompanyBak20160216(db.Model):
    __tablename__ = 'company_bak20160216'

    id = db.Column(db.BigInteger, primary_key=True)
    companyName = db.Column(db.String(200))
    displayName = db.Column(db.String(200), info='保密时候显示')
    country = db.Column(db.String(200))
    province = db.Column(db.String(200))
    city = db.Column(db.String(200))
    address = db.Column(db.String(300))
    zipCode = db.Column(db.String(100))
    recommendBy = db.Column(db.BigInteger, info='公司加入时使用的推荐号')
    webSite = db.Column(db.String(200))
    introduction = db.Column(db.Text, info='限制在1000字内')
    enterpriseCode = db.Column(db.String(200))
    enterpriseCodeVerification = db.Column(db.Integer, info='证书验证 0：未验证；1：以验证')
    mainContact = db.Column(db.String(200))
    status = db.Column(db.Integer, info='-2 审核未通过 ，0 待审核，1 正常，2 已注销，3 已删除，4 系统录入，5 未提交审核，6 升级中')
    createUserId = db.Column(db.BigInteger)
    createTime = db.Column(db.DateTime)
    updateUserId = db.Column(db.BigInteger)
    updateTime = db.Column(db.DateTime)
    companyType = db.Column(db.Integer, info='1：企业公司；2：猎头公司；3.管理员用户；4.渠道用户')
    companyScale = db.Column(db.Integer, info='1-10\\r\\n            10-50\\r\\n            50-100\\r\\n            100-500\\r\\n            500以上')
    industry1 = db.Column(db.Integer)
    industry2 = db.Column(db.Integer)
    totalInterview = db.Column(db.Integer, server_default=db.FetchedValue(), info='面试数')
    totalCandidate = db.Column(db.Integer, server_default=db.FetchedValue(), info='收到候选人数')
    totalPlacement = db.Column(db.Integer, server_default=db.FetchedValue(), info='录用数')
    contractStatus = db.Column(db.Integer, server_default=db.FetchedValue(), info='合同状态（0 未寄出合同，1 已寄出合同，2 签约）')
    marketId = db.Column(db.BigInteger, info='销售负责人（admin user id）公司销售')
    afterId = db.Column(db.BigInteger, info='售后负责人（admin user id）客服')
    logoUrl = db.Column(db.String(100), info='logo（可以存路径）')
    hastenCandidateTime = db.Column(db.Integer, server_default=db.FetchedValue(), info='系统通知HR催促处理候选人次数')
    companyStyle = db.Column(db.Integer, info='企业性质,形式 0,外资（欧美)1,外资（非欧美)2,合资（欧美）  3,合资（非欧美） 4,国企/上市公司  5,民营/私营公司 6,外企代表处 7,其它性质')
    approveTime = db.Column(db.DateTime, info='通过审核时间')
    phone = db.Column(db.String(50), info='电话号码')
    fax = db.Column(db.String(50), info='公司传真')
    rootId = db.Column(db.BigInteger, info='公司负责人ID')
    pact = db.Column(db.Integer, info='是否同意系统协议')
    pactTime = db.Column(db.DateTime, info='同意协议时间')
    contractNo = db.Column(db.String(25), info='合同编号')
    guaranteeMonth = db.Column(db.Integer, info='保证期（单位：月）')
    officialName = db.Column(db.String(50), info='企业合同名称')
    specialTerm = db.Column(db.String(1000), info='特殊条款')
    allowance = db.Column(db.String(1000), info='企业福利')
    agreeContractDate = db.Column(db.Date, info='合同签订日期')
    differentContract = db.Column(db.String(1000), info='合同包括与平台协议不同点的描述内容')
    serviceAdmin = db.Column(db.BigInteger)
    salseAdmin = db.Column(db.BigInteger, info='销售负责人（BDH）')
    bank = db.Column(db.String(50), info='开户行')
    account = db.Column(db.String(50), info='银行账户名')
    accountNumber = db.Column(db.String(50), info='银行账号')
    contractattachment = db.Column(db.String(100), info='法人代表')
    payDays = db.Column(db.Integer, info='付款日期')
    payRate = db.Column(db.Float(asdecimal=True), info='付款比例')
    shortName = db.Column(db.String(100), info='后台显示公司名简称')
    source = db.Column(db.Integer, info='客户来源')
    sourceMark = db.Column(db.String(30), info='客户来源备注')
    firstContactTime = db.Column(db.String(30), info='第一次联系时间')
    express = db.Column(db.String(50), info='快递信息')
    contractAddress = db.Column(db.String(50), info='合同寄出地址')
    contractRecipients = db.Column(db.String(50), info='合同接收人')
    activeContract = db.Column(db.Integer, info='合同的有效性')
    referredBy = db.Column(db.BigInteger, info='推荐人ID')
    taskAdmin = db.Column(db.BigInteger, info='任务负责人')
    activeReferred = db.Column(db.Integer, info='是否已过推荐期')
    totalPosition = db.Column(db.Integer, info='企业：发布的总职位数；猎头：推荐过的总职位数')
    totalOpenPosition = db.Column(db.Integer, info='企业 : 开放中职位总数；猎头：正在做的开放中的职位')
    totalUser = db.Column(db.Integer, info='用户数')
    totalVisit = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否拜访过客户')
    totalFollow = db.Column(db.Integer, info='跟进次数')
    totalSecondInterview = db.Column(db.Integer, server_default=db.FetchedValue(), info='二面')
    totalContract = db.Column(db.Integer, info='企业：合作猎头数；猎头：合作企业数')
    totalRequest = db.Column(db.Integer, info='企业 : 当前申请数；猎头：当前申请数')
    independent = db.Column(db.SmallInteger, server_default=db.FetchedValue(), info='猎头公司注册类型 0 猎头公司 1 全职SOHO猎头 2 兼职SOHO猎头')
    bdhAdmin = db.Column(db.BigInteger, info='BDH')
    parentId = db.Column(db.BigInteger)
    enterpriseCodeAttachment = db.Column(db.String(100))
    registerIP = db.Column(db.String(100))
    rejectReason = db.Column(db.String(200))
    provinceId = db.Column(db.Integer)
    cityId = db.Column(db.Integer)
    organizationCodeCertificateAttachment = db.Column(db.String(100))
    permissionStatus = db.Column(db.String(10))
    reject_content = db.Column(db.String(150), nullable=False, server_default=db.FetchedValue(), info='拒绝原因')
    reject_time = db.Column(db.DateTime, info='拒绝时间')
    experienced_areas = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='公司擅长地区')
    experienced_industrys = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='公司擅长行业')
    submit_verify_time = db.Column(db.DateTime, info='提交公司认证时间')
    rejected_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0：正常；打回类型 1：审核通过前打回；2：审核通过后打回')



t_connection = db.Table(
    'connection',
    db.Column('id1', db.BigInteger, nullable=False, index=True, info='HR id'),
    db.Column('id2', db.BigInteger, nullable=False, index=True, info='猎头id'),
    db.Column('type', db.String(10), nullable=False, info='类型'),
    db.Column('status', db.Integer, info='状态'),
    db.Column('createtime', db.DateTime, info='创建时间')
)



class Contract(db.Model):
    __tablename__ = 'contract'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    employerCompanyId = db.Column(db.BigInteger, index=True, info='雇主公司ID')
    headhunterCompanyId = db.Column(db.BigInteger, index=True, info='猎头公司ID')
    expireTime = db.Column(db.DateTime, info='合同过期时间')
    createTime = db.Column(db.DateTime, info='创建时间')
    updateTime = db.Column(db.DateTime, info='更新时间')
    createUser = db.Column(db.BigInteger, info='添加人')
    rewardType = db.Column(db.Integer, info='佣金类型( 可以和职位上不一样 )0按年薪 1按固定薪水 ')
    fixedRewardAmount = db.Column(db.Float(asdecimal=True), info='固定佣金金额 ( 可以和职位上不一样 )')
    percentageNumbric = db.Column(db.Float(asdecimal=True), info='佣金比例 ( 可以和职位上不一样 )')
    type = db.Column(db.Integer, info='合作类型 0签约 1私密')
    otherReward = db.Column(db.String(100), info='其他佣金类型 文字说明')



class Country(db.Model):
    __tablename__ = 'country'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    name = db.Column(db.String(100), info='名称')



class County(db.Model):
    __tablename__ = 'county'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    name = db.Column(db.String(100), info='名称')
    postcode = db.Column(db.String(10), info='邮编')
    cityId = db.Column(db.BigInteger, info='城市ID')
    districtcode = db.Column(db.String(10), info='行政区号')



class CrmCandidateGroup(db.Model):
    __tablename__ = 'crm_candidate_group'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='组名')
    candidate_all_status = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='支持加入的订单状态,多个以逗号分隔')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class CrmCandidateGroupRelation(db.Model):
    __tablename__ = 'crm_candidate_group_relation'

    id = db.Column(db.BigInteger, primary_key=True)
    candidate_group_id = db.Column(db.BigInteger, nullable=False, index=True)
    candidate_id = db.Column(db.BigInteger, nullable=False, index=True)
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False, index=True)



class CrmRoleDeleteTransferLog(db.Model):
    __tablename__ = 'crm_role_delete_transfer_log'

    id = db.Column(db.BigInteger, primary_key=True, info='主键Id，组ID')
    create_time = db.Column(db.DateTime, info='创建时间')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人')
    defunct = db.Column(db.Integer, info='是否删除 0 否 1是')
    transfer_table_name = db.Column(db.String(64), info='移交相关表名称')
    from_user_id = db.Column(db.BigInteger, index=True, info='交接人用户ID')
    to_user_id = db.Column(db.BigInteger, info='被交接人用户ID')
    class_name = db.Column(db.String(64), info='快照对象类名')
    snapshot = db.Column(db.String, info='原变更对象的快照内容')



class Date(db.Model):
    __tablename__ = 'date'

    date_value = db.Column(db.Date, primary_key=True)
    yearid = db.Column(db.Integer, nullable=False, index=True)
    monthid = db.Column(db.Integer, nullable=False, index=True)
    weekid = db.Column(db.Integer, nullable=False, index=True)
    workday = db.Column(db.String(10), index=True)
    rownum = db.Column(db.Integer, index=True, info='工作日序列号')



t_dispatch1 = db.Table(
    'dispatch1',
    db.Column('id', db.BigInteger),
    db.Column('position_id', db.BigInteger, server_default=db.FetchedValue()),
    db.Column('candidate_id', db.BigInteger, server_default=db.FetchedValue()),
    db.Column('hunter_id', db.BigInteger, server_default=db.FetchedValue()),
    db.Column('talent_id', db.BigInteger, server_default=db.FetchedValue()),
    db.Column('status', db.Integer, server_default=db.FetchedValue()),
    db.Column('fail_status', db.Integer, server_default=db.FetchedValue()),
    db.Column('fail_time', db.DateTime),
    db.Column('expire_time', db.DateTime),
    db.Column('undetermined_time', db.DateTime),
    db.Column('dispatch_time', db.DateTime),
    db.Column('reject_type', db.Integer),
    db.Column('reject_user_id', db.BigInteger, server_default=db.FetchedValue()),
    db.Column('reject_reason', db.String(200)),
    db.Column('reject_reason_expend', db.String(200)),
    db.Column('defunct', db.Integer, server_default=db.FetchedValue()),
    db.Column('create_user_id', db.BigInteger, server_default=db.FetchedValue()),
    db.Column('update_user_id', db.BigInteger, server_default=db.FetchedValue()),
    db.Column('create_time', db.DateTime),
    db.Column('update_time', db.DateTime)
)



class DwConfAntRpoHhMailList(db.Model):
    __tablename__ = 'dw_conf_ant_rpo_hh_mail_list'

    hh_id = db.Column(db.BigInteger, primary_key=True)
    send_date = db.Column(db.Date)



class HdDegree(db.Model):
    __tablename__ = 'hd_degree'

    id = db.Column(db.SmallInteger, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    order_by = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序字段')



class HhInnerLevelCfg(db.Model):
    __tablename__ = 'hh_inner_level_cfg'

    id = db.Column(db.BigInteger, primary_key=True)
    cfg_name = db.Column(db.String(200), info='配置名称')
    cfg_desc = db.Column(db.String(200), info='配置描述')
    create_ime = db.Column(db.DateTime, info='配置创建时间')



class HoAttachment(db.Model):
    __tablename__ = 'ho_attachment'
    __table_args__ = (
        db.Index('idx_sourceid_sourcetype', 'source_id', 'source_type'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    source_id = db.Column(db.BigInteger, info='附件来源表的主键ID,例如:talent.id or candidate.id')
    source_type = db.Column(db.Integer, info='附件来源:1=Talent;2=Candidate;')
    attachment_name = db.Column(db.String(800), info='附件名称')
    attachment_path = db.Column(db.String(2000), info='附件路径')
    create_user_id = db.Column(db.BigInteger, info='创建用户')
    create_time = db.Column(db.DateTime, info='创建时间')



t_ho_candidate_lock = db.Table(
    'ho_candidate_lock',
    db.Column('company_id', db.BigInteger, index=True, info='公司ID'),
    db.Column('headhunter_id', db.BigInteger, info='猎头ID'),
    db.Column('email', db.String(100), info='邮箱'),
    db.Column('cellphone', db.String(100), info='手机号'),
    db.Column('expire_time', db.DateTime, info='过期时间')
)



class HrHdConnection(db.Model):
    __tablename__ = 'hr_hd_connection'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    id1 = db.Column(db.BigInteger, nullable=False, index=True, info='猎头id')
    id2 = db.Column(db.BigInteger, nullable=False, index=True, info='hrId')
    type = db.Column(db.String(10), info='WL:白名单')
    status = db.Column(db.Integer, info='0:收藏,1:合作')
    enterpriseId = db.Column(db.BigInteger, nullable=False, info='HR企业Id')
    companyId = db.Column(db.BigInteger, nullable=False, info='猎头企业Id')
    createUserId = db.Column(db.BigInteger, nullable=False, info='创建者id')
    createType = db.Column(db.Integer, nullable=False, info='创建者类型')
    createtime = db.Column(db.DateTime, info='创建时间')
    updatetime = db.Column(db.DateTime, info='更新时间')



t_identitybinding = db.Table(
    'identitybinding',
    db.Column('identity', db.String(50), index=True, info='第三方id'),
    db.Column('type', db.String(4), info='类型 见IdentityBindingType'),
    db.Column('userid', db.BigInteger, index=True, info='用户id')
)



class Industry(db.Model):
    __tablename__ = 'industry'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    name = db.Column(db.String(100), info='名称')
    code = db.Column(db.String(100), info='编码')
    clsId = db.Column(db.Integer, info='大类')
    order = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序')



class Interview(db.Model):
    __tablename__ = 'interview'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    candidateId = db.Column(db.BigInteger, index=True, info='候选人ID')
    headhunterId = db.Column(db.BigInteger, index=True, info='猎头ID')
    employerId = db.Column(db.BigInteger, info='雇主ID')
    headhunterCompanyId = db.Column(db.BigInteger, index=True, info='猎头公司ID')
    employerCompanyId = db.Column(db.BigInteger, info='雇主公司ID')
    interviewType = db.Column(db.Integer, info='1: 电话2: 面谈3: 笔试4: 视频')
    contact = db.Column(db.String(200), info='联系人')
    contactPhone = db.Column(db.String(200), info='联系电话')
    ps = db.Column(db.String(1000), info='附言')
    proposeAddress = db.Column(db.String(1000), info='建议地点')
    proposeDateTime = db.Column(db.String(1000), info='建议时间')
    status = db.Column(db.Integer, info='0: 新创建 1: 面试通过 2: 面试失败')
    feedback = db.Column(db.String(1000))
    createTime = db.Column(db.DateTime, index=True, info='创建时间')
    updateTime = db.Column(db.DateTime, server_default=db.FetchedValue(), info='更新时间')
    createUser = db.Column(db.BigInteger, info='创建者')
    updateUser = db.Column(db.BigInteger, info='更新者')
    positionId = db.Column(db.BigInteger, index=True, info='职位ID')
    terminatedReason = db.Column(db.String(1000))
    confirmTime = db.Column(db.DateTime)
    remark = db.Column(db.String(1000))
    editTime = db.Column(db.DateTime)
    editInterviewType = db.Column(db.Integer)
    adminRemark = db.Column(db.Text)
    positionAssignId = db.Column(db.BigInteger, info='职位负责人')
    interviewTimes = db.Column(db.Integer, info='0一次，1多次')
    interviewed = db.Column(db.Integer, info='第几次面试')
    confirm_interview_time = db.Column(db.DateTime)
    request_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0表示不需要走特殊面试流程-1猎头约面试-2HR自己约')
    extra_interview_type = db.Column(db.String(10), nullable=False, server_default=db.FetchedValue(), info='额外的面试方式')
    extra_confirm_time = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='确认面试时间')
    candidate_interview_invite_confirm = db.Column(db.Integer, info='候选人是否确认面试邀请')



class Messagemap(db.Model):
    __tablename__ = 'messagemap'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    messageId = db.Column(db.BigInteger)
    recipientId = db.Column(db.BigInteger, index=True)
    senderId = db.Column(db.BigInteger)
    status = db.Column(db.Integer)
    readStatus = db.Column(db.Integer, info='0：未读 1：已读')
    mailStatus = db.Column(db.Integer, info='不需要:-1；初始化状态:0；Push到队列失败:1；Push到队列成功:2；发送email失败: 3；发送email成功: 4；')
    failReason = db.Column(db.String(1000), info='邮件发送失败原因')
    createUserId = db.Column(db.BigInteger, info='创建者')
    updateUserId = db.Column(db.BigInteger, info='更新者')
    createTime = db.Column(db.DateTime, info='创建时间')
    updateTime = db.Column(db.DateTime, info='更新时间')
    replyId = db.Column(db.BigInteger, info='回复邮件ID')



class Online(db.Model):
    __tablename__ = 'online'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    userId = db.Column(db.BigInteger, index=True, info='用户ID')
    loginLocation = db.Column(db.String(30), info='登陆地点')
    trueName = db.Column(db.String(30), info='真实姓名')
    userType = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1 : hr; 2 : hh;')
    userName = db.Column(db.String(30), info='登陆用户名')
    source = db.Column(db.Integer, info='来源： 1 网页端登录， 2 Andorid 3 IOS')
    ip = db.Column(db.String(20), info='登录地址')
    loginTime = db.Column(db.DateTime, index=True, info='登录时间')
    logoutTime = db.Column(db.DateTime, info='登出时间')
    status = db.Column(db.Integer, info='0 离线，1在线')



class Paction(db.Model):
    __tablename__ = 'paction'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
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
    active = db.Column(db.Integer, info='合同是否活动 0 合同未生效, 1 合同生效, 2 合同失效, 3 猎头同意协议')
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
    createTime = db.Column(db.DateTime, info='创建时间')
    updateTime = db.Column(db.DateTime, info='更新时间')
    createUserId = db.Column(db.BigInteger, info='创建者')
    updateUserId = db.Column(db.BigInteger, info='更新者')
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



class Payment(db.Model):
    __tablename__ = 'payment'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    serialNumber = db.Column(db.String(20), index=True)
    placementId = db.Column(db.BigInteger, nullable=False, index=True)
    userId = db.Column(db.BigInteger, info='相关user')
    cost = db.Column(db.Float, info='金额')
    rate = db.Column(db.Float, info='与成单金额的比例')
    financial = db.Column(db.Integer, info='财务任务： 0 无需 1 未收款 2 已收款 3 未支出 4 已支出')
    status = db.Column(db.Integer, info='0 失效 1 生效')
    type = db.Column(db.Integer, info='1 向客户收款 2 支付猎头 3 支付企业渠道 4 支付猎头渠道 5 向客户退款(支付)')
    invoice = db.Column(db.Integer, info='0 未开票 1 已开票 2 需退票 3 已退票')
    payNum = db.Column(db.Integer, info='次数')
    invoiceTime = db.Column(db.DateTime, info='开票日期 / 收到退票日期')
    payTime = db.Column(db.DateTime, info='支付时间')
    startTime = db.Column(db.DateTime, info='起始时间')
    endTime = db.Column(db.DateTime, info='结束时间')
    contacter = db.Column(db.String(200))
    contactInfo = db.Column(db.String(200))
    createTime = db.Column(db.DateTime, info='创建时间')
    createUserId = db.Column(db.BigInteger, info='创建者')
    updateTime = db.Column(db.DateTime, server_default=db.FetchedValue(), info='更新时间')
    updateUserId = db.Column(db.BigInteger, info='更新者')
    prepay_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='预付状态：0：不能预付，1：未预付，2：已预付，3：须回收，4：已回收')
    prepay_cost = db.Column(db.Float, nullable=False, server_default=db.FetchedValue(), info='预付金额')
    prepay_time = db.Column(db.DateTime, info='预付时间')
    recover_cost = db.Column(db.Float, nullable=False, server_default=db.FetchedValue(), info='回收金额（多次回收金额累加）')
    recover_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='回收次数')
    recover_time = db.Column(db.DateTime, info='回收时间')
    invoice_sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='猎头发票类型：1：普票，2：6%增值税，3：3%增值税，4：不提供发票')
    should_pay_cost = db.Column(db.Float, nullable=False, server_default=db.FetchedValue(), info='应付金额')



class PaymentBak20160418(db.Model):
    __tablename__ = 'payment_bak20160418'

    id = db.Column(db.BigInteger, primary_key=True)
    serialNumber = db.Column(db.String(20))
    placementId = db.Column(db.BigInteger, nullable=False, index=True)
    userId = db.Column(db.BigInteger, info='相关user')
    cost = db.Column(db.Float, info='金额')
    rate = db.Column(db.Float, info='与成单金额的比例')
    financial = db.Column(db.Integer, info='财务任务： 0 无需 1 未收款 2 已收款 3 未支出 4 已支出')
    status = db.Column(db.Integer, info='0 失效 1 生效')
    type = db.Column(db.Integer, info='1 向客户收款 2 支付猎头 3 支付企业渠道 4 支付猎头渠道 5 向客户退款(支付)')
    invoice = db.Column(db.Integer, info='0 未开票 1 已开票 2 需退票 3 已退票')
    payNum = db.Column(db.Integer, info='次数')
    invoiceTime = db.Column(db.DateTime, info='开票日期 / 收到退票日期')
    payTime = db.Column(db.DateTime, info='支付时间')
    startTime = db.Column(db.DateTime, info='起始时间')
    endTime = db.Column(db.DateTime, info='结束时间')
    contacter = db.Column(db.String(200))
    contactInfo = db.Column(db.String(200))
    createTime = db.Column(db.DateTime)
    createUserId = db.Column(db.BigInteger)
    updateTime = db.Column(db.DateTime)
    updateUserId = db.Column(db.BigInteger)
    prepay_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='预付状态：0：不能预付，1：未预付，2：已预付，3：须回收，4：已回收')
    prepay_cost = db.Column(db.Float, nullable=False, server_default=db.FetchedValue(), info='预付金额')
    prepay_time = db.Column(db.DateTime, info='预付时间')
    recover_cost = db.Column(db.Float, nullable=False, server_default=db.FetchedValue(), info='回收金额（多次回收金额累加）')
    recover_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='回收次数')
    recover_time = db.Column(db.DateTime, info='回收时间')
    invoice_sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='猎头发票类型：1：普票，2：6%增值税，3：3%增值税，4：不提供发票')
    should_pay_cost = db.Column(db.Float, nullable=False, server_default=db.FetchedValue(), info='应付金额')



t_paymentstatus = db.Table(
    'paymentstatus',
    db.Column('id', db.Integer, info='ID'),
    db.Column('name', db.String(255), info='名称'),
    db.Column('type', db.String(255), info='类型')
)



class Placement(db.Model):
    __tablename__ = 'placement'
    __table_args__ = (
        db.Index('idx_candidateId_delStatus', 'candidateId', 'delStatus'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    serialNumber = db.Column(db.String(20), index=True, info='成单编号')
    employerId = db.Column(db.BigInteger, info='职位负责人')
    employerCompanyId = db.Column(db.BigInteger, index=True, info='客户公司')
    headhunterId = db.Column(db.BigInteger, index=True, info='成单猎头')
    headhunterCompanyId = db.Column(db.BigInteger, index=True, info='成单猎头公司')
    candidateId = db.Column(db.BigInteger, index=True, info='相关候选人')
    positionId = db.Column(db.BigInteger, index=True, info='相关职位')
    employerPactionId = db.Column(db.BigInteger, info='企业合同')
    headhunterPactionId = db.Column(db.BigInteger, info='猎头合同')
    onboard = db.Column(db.Integer, info='到岗状态，0 新成单，未到岗  1 已到岗  2 放弃到岗  3 已过保证期  4 已离岗')
    expectOnboardDate = db.Column(db.DateTime, info='期望到岗时间')
    status = db.Column(db.Integer, info='成单状态，0 签约成单, 1 新成单，2 成单成功，3 成单失败')
    reward = db.Column(db.Float(15), info='实际成单佣金')
    annualSalary = db.Column(db.Integer, info='实际年薪')
    onboardDate = db.Column(db.DateTime, info='到岗时间')
    guaranteeTime = db.Column(db.DateTime, info='保证期')
    createUserId = db.Column(db.BigInteger, info='创建人')
    updateUserId = db.Column(db.BigInteger, info='最后更新')
    postscript = db.Column(db.String(1000), info='成单附言，企业填写，非备注')
    createTime = db.Column(db.DateTime, index=True, info='创建时间')
    updateTime = db.Column(db.DateTime, server_default=db.FetchedValue(), info='更新时间')
    taxRate = db.Column(db.Float, info='税率')
    tax = db.Column(db.Float, info='税')
    delStatus = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='删除状态：\\r\\n0,HR HH正常\\r\\n1,HR正常\u3000HH删除\\r\\n2,HR删除\u3000HH正常\\r\\n3,HR删除\u3000HH删除\\r\\n0正1删除 ')
    attachment = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='附件（可以用来做不过保证明）')
    termination_reason = db.Column(db.String(800), nullable=False, server_default=db.FetchedValue(), info='理由')
    termination_time = db.Column(db.DateTime, info='终止时间（离岗时间）')
    enterprise_name = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue(), info='企业公司名称')
    company_name = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue(), info='猎企公司名称')
    employer_name = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue(), info='企业人姓名')
    hunter_name = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue(), info='猎头姓名')
    candidate_name = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue(), info='候选人姓名')
    position_title = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue(), info='职位名称')
    offer_progress = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='offer进度0：完成1：待确认')
    over_guarantee_operate_time = db.Column(db.DateTime, index=True, info='过保操作时间')
    placement_record_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='未过保申请流水记录id')
    is_hide = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否隐藏')
    onboard_pay = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否到岗付')
    onboard_on_operate_time = db.Column(db.DateTime, index=True, info='放弃到岗,到岗操作时间')
    confirm_guarantee_time = db.Column(db.DateTime, info='确认过保时间')
    reward_type = db.Column(db.Integer, info='佣金类型 position copy')
    percentage_numbric = db.Column(db.Float(asdecimal=True), info='百分比 数字 20 表示 年薪* 20%')
    guarantee_month = db.Column(db.Integer, info='保证期存、月数')
    pre_rate = db.Column(db.Float(asdecimal=True), server_default=db.FetchedValue(), info='预付比例')
    pre_cost = db.Column(db.Float(asdecimal=True), server_default=db.FetchedValue(), info='预付金额')
    pre_channel = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='产生预付通道,1:猎得快，2:手动设置')
    over_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='成单销账:1:手动销账')
    over_time = db.Column(db.DateTime, info='销账时间')
    over_operator_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='销账人id')
    confirme_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0:普通需确认，1：信息变更需确认，2：已确认')
    confirmed = db.Column(db.Integer, server_default=db.FetchedValue())
    pay_rate = db.Column(db.Float(asdecimal=True), server_default=db.FetchedValue(), info='猎企佣金比例')
    contact = db.Column(db.String(50), info='联系人')
    contact_phone = db.Column(db.String(50), info='联系人电话')
    onboard_address = db.Column(db.String(300), info='入职地址')



t_placement_back_delete = db.Table(
    'placement_back_delete',
    db.Column('id', db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='主键ID'),
    db.Column('serialNumber', db.String(20), info='成单编号'),
    db.Column('employerId', db.BigInteger, info='职位负责人'),
    db.Column('employerCompanyId', db.BigInteger, info='客户公司'),
    db.Column('headhunterId', db.BigInteger, info='成单猎头'),
    db.Column('headhunterCompanyId', db.BigInteger, info='成单猎头公司'),
    db.Column('candidateId', db.BigInteger, info='相关候选人'),
    db.Column('positionId', db.BigInteger, info='相关职位'),
    db.Column('employerPactionId', db.BigInteger, info='企业合同'),
    db.Column('headhunterPactionId', db.BigInteger, info='猎头合同'),
    db.Column('onboard', db.Integer, info='到岗状态，0 新成单，未到岗  1 已到岗  2 放弃到岗  3 已过保证期  4 已离岗'),
    db.Column('expectOnboardDate', db.DateTime, info='期望到岗时间'),
    db.Column('status', db.Integer, info='成单状态，0 签约成单, 1 新成单，2 成单成功，3 成单失败'),
    db.Column('reward', db.Float, info='实际成单佣金'),
    db.Column('annualSalary', db.Integer, info='实际年薪'),
    db.Column('onboardDate', db.DateTime, info='到岗时间'),
    db.Column('guaranteeTime', db.DateTime, info='保证期'),
    db.Column('createUserId', db.BigInteger, info='创建人'),
    db.Column('updateUserId', db.BigInteger, info='最后更新'),
    db.Column('postscript', db.String(1000), info='成单附言，企业填写，非备注'),
    db.Column('createTime', db.DateTime, info='创建时间'),
    db.Column('updateTime', db.DateTime, server_default=db.FetchedValue(), info='更新时间'),
    db.Column('taxRate', db.Float, info='税率'),
    db.Column('tax', db.Float, info='税'),
    db.Column('delStatus', db.Integer, server_default=db.FetchedValue(), info='删除状态：\\r\\n0,HR HH正常\\r\\n1,HR正常\u3000HH删除\\r\\n2,HR删除\u3000HH正常\\r\\n3,HR删除\u3000HH删除\\r\\n0正1删除 '),
    db.Column('attachment', db.String(200), nullable=False, server_default=db.FetchedValue(), info='附件（可以用来做不过保证明）'),
    db.Column('termination_reason', db.String(800), nullable=False, server_default=db.FetchedValue(), info='理由'),
    db.Column('termination_time', db.DateTime, info='终止时间（离岗时间）'),
    db.Column('enterprise_name', db.String(300), nullable=False, server_default=db.FetchedValue(), info='企业公司名称'),
    db.Column('company_name', db.String(300), nullable=False, server_default=db.FetchedValue(), info='猎企公司名称'),
    db.Column('employer_name', db.String(300), nullable=False, server_default=db.FetchedValue(), info='企业人姓名'),
    db.Column('hunter_name', db.String(300), nullable=False, server_default=db.FetchedValue(), info='猎头姓名'),
    db.Column('candidate_name', db.String(300), nullable=False, server_default=db.FetchedValue(), info='候选人姓名'),
    db.Column('position_title', db.String(300), nullable=False, server_default=db.FetchedValue(), info='职位名称'),
    db.Column('offer_progress', db.Integer, nullable=False, server_default=db.FetchedValue(), info='offer进度0：完成1：待确认'),
    db.Column('over_guarantee_operate_time', db.DateTime, info='过保操作时间'),
    db.Column('placement_record_id', db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='未过保申请流水记录id'),
    db.Column('is_hide', db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否隐藏'),
    db.Column('onboard_pay', db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否到岗付'),
    db.Column('onboard_on_operate_time', db.DateTime, info='放弃到岗,到岗操作时间'),
    db.Column('confirm_guarantee_time', db.DateTime, info='确认过保时间'),
    db.Column('reward_type', db.Integer, info='佣金类型 position copy'),
    db.Column('percentage_numbric', db.Float(asdecimal=True), info='百分比 数字 20 表示 年薪* 20%'),
    db.Column('guarantee_month', db.Integer, info='保证期存、月数'),
    db.Column('pre_rate', db.Float(asdecimal=True), server_default=db.FetchedValue(), info='预付比例'),
    db.Column('pre_cost', db.Float(asdecimal=True), server_default=db.FetchedValue(), info='预付金额'),
    db.Column('pre_channel', db.Integer, nullable=False, server_default=db.FetchedValue(), info='产生预付通道,1:猎得快，2:手动设置'),
    db.Column('over_type', db.Integer, nullable=False, server_default=db.FetchedValue(), info='成单销账:1:手动销账'),
    db.Column('over_time', db.DateTime, info='销账时间'),
    db.Column('over_operator_id', db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='销账人id'),
    db.Column('confirme_type', db.Integer, nullable=False, server_default=db.FetchedValue(), info='0:普通需确认，1：信息变更需确认，2：已确认'),
    db.Column('confirmed', db.Integer, server_default=db.FetchedValue()),
    db.Column('pay_rate', db.Float(asdecimal=True), server_default=db.FetchedValue(), info='猎企佣金比例'),
    db.Column('contact', db.String(50), info='联系人'),
    db.Column('contact_phone', db.String(50), info='联系人电话'),
    db.Column('onboard_address', db.String(300), info='入职地址')
)



class Position(db.Model):
    __tablename__ = 'position'
    __table_args__ = (
        db.Index('idx_positionAssignId_publishtime', 'positionAssignId', 'publish_time'),
        db.Index('idx_status_positionAssignId_companyId', 'status', 'positionAssignId', 'companyId')
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    title = db.Column(db.String(600), info='标题')
    countryId = db.Column(db.BigInteger, info='职位，所在国家')
    provinceId = db.Column(db.BigInteger, info='职位，所在省ID')
    cityId = db.Column(db.BigInteger, info='职位，所在市ID')
    countyId = db.Column(db.BigInteger, info='职位所在县id')
    location = db.Column(db.String(511), info='上班地址（详细描述）')
    professionTypeId = db.Column(db.BigInteger, info='职能类别')
    professionTypeParentId = db.Column(db.BigInteger, info='职能类别(父级）')
    industryId = db.Column(db.BigInteger, info='行业Id')
    internalCode = db.Column(db.String(300), info='内部编号（企业）')
    categoryId = db.Column(db.BigInteger, info='分类（暂时不用）')
    jobDescription = db.Column(db.Text, info='职位描述')
    jobRequirement = db.Column(db.Text, info='职位需求')
    positionType = db.Column(db.Integer, info='0：需要申请 1：不需要申请 2：不能申请（内部，暂时没有engagement概念）')
    expectFillDate = db.Column(db.DateTime, info='期望到岗时间')
    headCount = db.Column(db.Integer, info='招聘人数')
    annualSalary = db.Column(db.Float(asdecimal=True), info='年薪')
    rewardType = db.Column(db.Integer, info='佣金类型 0：固定佣金   1：年薪百分比 ')
    fixedRewardAmount = db.Column(db.Float(asdecimal=True), info='固定佣金的 金额')
    percentageNumbric = db.Column(db.Float(asdecimal=True), server_default=db.FetchedValue(), info='百分比 数字 20 表示 年薪* 20%')
    commissionSupplement = db.Column(db.String(600), info='佣金补充说明')
    totalCandidate = db.Column(db.Integer, info='当前猎头数')
    totalPlacement = db.Column(db.Integer, info='职位成单数')
    totalActiveCandidate = db.Column(db.Integer, info='活跃猎头数')
    pageViews = db.Column(db.Integer, info='点击量（总）')
    totalCollection = db.Column(db.Integer, info='关注数')
    totalEngage = db.Column(db.Integer, info='合作猎头数')
    totalRequest = db.Column(db.Integer, info='当前申请数')
    terminatedReason = db.Column(db.String(2000), info='结束原因')
    status = db.Column(db.Integer, index=True, info='0：published 发布  1：draft 草稿 2：申请关闭 3：已关闭 4：暂停')
    createTime = db.Column(db.DateTime, info='创建时间')
    createUserId = db.Column(db.BigInteger, info='创建者')
    updateTime = db.Column(db.DateTime, index=True, server_default=db.FetchedValue(), info='更新时间')
    updateUserId = db.Column(db.BigInteger, info='更新者')
    notifyHeadhunterFlag = db.Column(db.Integer, info='是否通知签约猎头')
    notifyHeadhunterNote = db.Column(db.String(1023), info='通知签约猎头的内容')
    companyId = db.Column(db.BigInteger, index=True, info='职位对应的公司id')
    comment = db.Column(db.String(500))
    commentDate = db.Column(db.DateTime)
    urgency = db.Column(db.Integer)
    prompt = db.Column(db.Text, info='系统调研职位的内容')
    salaryDescription = db.Column(db.String(1023))
    hasActive = db.Column(db.Integer)
    refreshTime = db.Column(db.Integer, server_default=db.FetchedValue(), info='职位刷新次数')
    positionAssignId = db.Column(db.BigInteger, index=True, info='职位负责人')
    positionOrder = db.Column(db.Integer, info='职位排序序号')
    isContract = db.Column(db.Integer, info='0 不是合同职位,1是合同职位')
    isPrivate = db.Column(db.Integer, info='0 不是私密职位,1是私密职位')
    isPublic = db.Column(db.Integer, info='0 不是公开职位,1是公开职位')
    address = db.Column(db.String(1000), info='职位所在地')
    department = db.Column(db.String(1000), info='所属部门')
    reportpo = db.Column(db.String(1000), info='汇报对象')
    subordinate = db.Column(db.String(200), info='下属团队')
    totalAssign = db.Column(db.Integer, info='操作猎头数')
    priority = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    hr_priority = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    service_admin = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='对应EM的id')
    investigated = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0没有调研 1已经调研')
    publish_time = db.Column(db.DateTime, index=True, info='职位发布时间')
    position_style = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位类型 0:500强 1:稳定型 2：创业型 3：合伙人')
    remark = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue())
    salary_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='薪资类型0：年薪1：月薪')
    division_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='事业部id')
    browse_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位浏览量')
    max_base_annual_salary = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='最大基本年薪')
    min_show_annual_salary = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='最小显示年薪')
    max_show_annual_salary = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='最大显示年薪')
    max_reward = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='最大佣金')
    guarantee_time = db.Column(db.Integer, info='保证期月数，-1表示无保证期')
    month_salary_rule = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='月薪制度 12：12薪  13：13薪 14：14薪   15：15薪  16：16薪  100：16薪以上')
    interview_style = db.Column(db.String(60), info='面试方式')
    interview_times = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='面试轮次 1：1轮  2：2轮 3：3轮 4：4轮 5：4轮以上')
    interview_province_id = db.Column(db.BigInteger, info='面试地点-省份')
    interview_city_id = db.Column(db.BigInteger, info='面试地点-城市')
    interview_address = db.Column(db.String(250), info='面试地点-地址')
    interviewer = db.Column(db.String(255), info='面试官')
    interviewer_order = db.Column(db.String(250), info='面试官顺序')
    phone_interview = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否可以电话面试')
    video_interview = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否可以视频面试')
    language_required = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='语言要求,存汉字[英语,日语,汉语]')
    language_string_required = db.Column(db.String(255), server_default=db.FetchedValue(), info='语言要求,存字符串[1,2,3,4]')
    college_required = db.Column(db.String(200), info='hr输入的学院证书要求')
    degree_required = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='学历要求 0:不限 1：大专及以上 2：本科及以上 3：硕士及以上 4：博士及以上')
    gender_required = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='性别要求 0：不限  1：男  2：女')
    work_exp_required = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='工作经验要求 ：0:不限 1:1年以上  2:2年以上 3:3年以上 4：4年以上 5：5年以上 6：6年以上 7：7年以上')
    work_exp_year_desc = db.Column(db.String(60), server_default=db.FetchedValue(), info='工作年限要求')
    highlights = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='职位亮点')
    temptation = db.Column(db.String(1023), nullable=False, server_default=db.FetchedValue(), info='职位诱惑')
    open_date = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开放时间  1:小于1周  2：小于两周 3：两周以上')
    approval_pass = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否审核通过')
    important_msg = db.Column(db.Text, info='职位重要信息')
    modify_time = db.Column(db.DateTime, info='最后刷新时间')
    unanswer_question = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否有未回答的问题 0:没有 1:有')
    question_update_time = db.Column(db.Date, info='问题最后更新时间')
    answer_update_time = db.Column(db.Date, info='回答最后更新时间')
    priority_feedback_hours = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info=' hr反馈小时数')
    priority_feedback_channel = db.Column(db.String(60), info='反馈渠道')
    keep_contact_time = db.Column(db.String(211), info='可联系时间段')
    position_title_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职能id')
    age_required = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='年龄要求')
    certificate = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='证书')
    open_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开放原因')
    qr_code = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='二维码图片')
    edit_time = db.Column(db.DateTime, info='职位编辑时间')
    pa_proxy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否需要pa代指定')
    status_time = db.Column(db.DateTime, info='状态变更时间(主要暂停及恢复)')
    apply_required = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='申请要求')
    pa_remark = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='pa公告')
    contact = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='职位联系方式')
    feedback_remark = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='反馈备注')
    level_code = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='级别CODE')
    remark_time = db.Column(db.DateTime, info='发布公告时间')
    other_priority_feedback_time = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='其他反馈时间')
    is_contact_headhunter = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否直接对接猎头，0:仅通过猎上平台在线沟通,1:支持猎头看到我的联系方式，可直接联系我')
    contact_headhunter = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='支持猎头看到我的联系方式(我的联系方式)')
    is_grab_order = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否抢单职位,0:false,1:true')
    grab_order_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='抢单职位数量')
    pa_remark_time = db.Column(db.DateTime, info='pa发布公告时间')
    denyreason = db.Column(db.String(1000), info='拒绝理由')
    verify_time = db.Column(db.DateTime, info='提交审核时间')
    important_degree = db.Column(db.Integer, server_default=db.FetchedValue(), info='重要程度')
    lastfresh_date = db.Column(db.DateTime, info='职位最新更新时间')
    isGrab = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否抢单职位')
    is_noticed = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否已经通知')
    investigation_time = db.Column(db.DateTime, info='职位调研时间')
    is_pa_survey = db.Column(db.Integer, server_default=db.FetchedValue(), info='PA是否调研：公开需求无需调研默认为0,私密职位需要调研设置为：1,PA调研之后修改为：2')
    team_size = db.Column(db.Integer, server_default=db.FetchedValue(), info='团队人数')
    position_survey_status = db.Column(db.Integer, server_default=db.FetchedValue(), info='待PO审核：101; 待调研：102; 待审核：103; 审核不通过：104; 审核通过待发布：105; ')
    is_lieying = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否为猎英,0:非猎英,1:猎英')



class Position1(db.Model):
    __tablename__ = 'position1'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    title = db.Column(db.String(600), info='标题')
    countryId = db.Column(db.BigInteger, info='职位，所在国家')
    provinceId = db.Column(db.BigInteger, info='职位，所在省ID')
    cityId = db.Column(db.BigInteger, info='职位，所在市ID')
    countyId = db.Column(db.BigInteger, info='职位所在县id')
    location = db.Column(db.String(511), info='上班地址（详细描述）')
    professionTypeId = db.Column(db.BigInteger, info='职能类别')
    professionTypeParentId = db.Column(db.BigInteger, info='职能类别(父级）')
    industryId = db.Column(db.BigInteger, info='行业Id')
    internalCode = db.Column(db.String(300), info='内部编号（企业）')
    categoryId = db.Column(db.BigInteger, info='分类（暂时不用）')
    jobDescription = db.Column(db.Text, info='职位描述')
    jobRequirement = db.Column(db.Text, info='职位需求')
    positionType = db.Column(db.Integer, info='0：需要申请 1：不需要申请 2：不能申请（内部，暂时没有engagement概念）')
    expectFillDate = db.Column(db.DateTime, info='期望到岗时间')
    headCount = db.Column(db.Integer, info='招聘人数')
    annualSalary = db.Column(db.Float(asdecimal=True), info='年薪')
    rewardType = db.Column(db.Integer, info='佣金类型 0：固定佣金   1：年薪百分比 ')
    fixedRewardAmount = db.Column(db.Float(asdecimal=True), info='固定佣金的 金额')
    percentageNumbric = db.Column(db.Float(asdecimal=True), info='百分比 数字 20 表示 年薪* 20%')
    commissionSupplement = db.Column(db.String(600), info='佣金补充说明')
    totalCandidate = db.Column(db.Integer, info='当前猎头数')
    totalPlacement = db.Column(db.Integer, info='职位成单数')
    totalActiveCandidate = db.Column(db.Integer, info='活跃猎头数')
    pageViews = db.Column(db.Integer, info='点击量（总）')
    totalCollection = db.Column(db.Integer, info='关注数')
    totalEngage = db.Column(db.Integer, info='合作猎头数')
    totalRequest = db.Column(db.Integer, info='当前申请数')
    terminatedReason = db.Column(db.String(2000), info='结束原因')
    status = db.Column(db.Integer, index=True, info='0：published 发布  1：draft 草稿 2：申请关闭 3：已关闭 4：暂停')
    createTime = db.Column(db.DateTime, info='创建时间')
    createUserId = db.Column(db.BigInteger, info='创建者')
    updateTime = db.Column(db.DateTime, index=True, server_default=db.FetchedValue(), info='更新时间')
    updateUserId = db.Column(db.BigInteger, info='更新者')
    notifyHeadhunterFlag = db.Column(db.Integer, info='是否通知签约猎头')
    notifyHeadhunterNote = db.Column(db.String(1023), info='通知签约猎头的内容')
    companyId = db.Column(db.BigInteger, index=True, info='职位对应的公司id')
    comment = db.Column(db.String(500))
    commentDate = db.Column(db.DateTime)
    urgency = db.Column(db.Integer)
    prompt = db.Column(db.Text, info='系统调研职位的内容')
    salaryDescription = db.Column(db.String(1023))
    hasActive = db.Column(db.Integer)
    refreshTime = db.Column(db.Integer, server_default=db.FetchedValue(), info='职位刷新次数')
    positionAssignId = db.Column(db.BigInteger, index=True, info='职位负责人')
    positionOrder = db.Column(db.Integer, info='职位排序序号')
    isContract = db.Column(db.Integer, info='0 不是合同职位,1是合同职位')
    isPrivate = db.Column(db.Integer, info='0 不是私密职位,1是私密职位')
    isPublic = db.Column(db.Integer, info='0 不是公开职位,1是公开职位')
    address = db.Column(db.String(1000), info='职位所在地')
    department = db.Column(db.String(1000), info='所属部门')
    reportpo = db.Column(db.String(1000), info='汇报对象')
    subordinate = db.Column(db.String(200), info='下属团队')
    totalAssign = db.Column(db.Integer, info='操作猎头数')
    priority = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    hr_priority = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    service_admin = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='对应EM的id')
    investigated = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0没有调研 1已经调研')
    publish_time = db.Column(db.DateTime, index=True, info='职位发布时间')
    position_style = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位类型 0:500强 1:稳定型 2：创业型 3：合伙人')
    remark = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue())
    salary_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='薪资类型0：年薪1：月薪')
    division_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='事业部id')
    browse_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位浏览量')
    max_base_annual_salary = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='最大基本年薪')
    min_show_annual_salary = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='最小显示年薪')
    max_show_annual_salary = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='最大显示年薪')
    max_reward = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='最大佣金')
    guarantee_time = db.Column(db.Integer, info='保证期月数，-1表示无保证期')
    month_salary_rule = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='月薪制度 12：12薪  13：13薪 14：14薪   15：15薪  16：16薪  100：16薪以上')
    interview_style = db.Column(db.String(60), info='面试方式')
    interview_times = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='面试轮次 1：1轮  2：2轮 3：3轮 4：4轮 5：4轮以上')
    interview_province_id = db.Column(db.BigInteger, info='面试地点-省份')
    interview_city_id = db.Column(db.BigInteger, info='面试地点-城市')
    interview_address = db.Column(db.String(250), info='面试地点-地址')
    interviewer = db.Column(db.String(255), info='面试官')
    interviewer_order = db.Column(db.String(250), info='面试官顺序')
    phone_interview = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否可以电话面试')
    video_interview = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否可以视频面试')
    language_required = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='语言要求,存汉字[英语,日语,汉语]')
    language_string_required = db.Column(db.String(255), server_default=db.FetchedValue(), info='语言要求,存字符串[1,2,3,4]')
    college_required = db.Column(db.String(200), info='hr输入的学院证书要求')
    degree_required = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='学历要求 0:不限 1：大专及以上 2：本科及以上 3：硕士及以上 4：博士及以上')
    gender_required = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='性别要求 0：不限  1：男  2：女')
    work_exp_required = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='工作经验要求 ：0:不限 1:1年以上  2:2年以上 3:3年以上 4：4年以上 5：5年以上 6：6年以上 7：7年以上')
    work_exp_year_desc = db.Column(db.String(60), server_default=db.FetchedValue(), info='工作年限要求')
    highlights = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='职位亮点')
    temptation = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='职位诱惑')
    open_date = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开放时间  1:小于1周  2：小于两周 3：两周以上')
    approval_pass = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否审核通过')
    important_msg = db.Column(db.Text, info='职位重要信息')
    modify_time = db.Column(db.DateTime, info='最后刷新时间')
    unanswer_question = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否有未回答的问题 0:没有 1:有')
    question_update_time = db.Column(db.Date, info='问题最后更新时间')
    answer_update_time = db.Column(db.Date, info='回答最后更新时间')
    priority_feedback_hours = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info=' hr反馈小时数')
    priority_feedback_channel = db.Column(db.String(60), info='反馈渠道')
    keep_contact_time = db.Column(db.String(211), info='可联系时间段')
    position_title_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职能id')
    age_required = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='年龄要求')
    certificate = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='证书')
    open_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开放原因')
    qr_code = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='二维码图片')
    edit_time = db.Column(db.DateTime, info='职位编辑时间')
    pa_proxy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否需要pa代指定')
    status_time = db.Column(db.DateTime, info='状态变更时间(主要暂停及恢复)')
    apply_required = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='申请要求')
    pa_remark = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='pa公告')
    contact = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='职位联系方式')
    feedback_remark = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='反馈备注')
    level_code = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='级别CODE')
    remark_time = db.Column(db.DateTime, info='发布公告时间')
    other_priority_feedback_time = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='其他反馈时间')
    is_contact_headhunter = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否直接对接猎头，0:仅通过猎上平台在线沟通,1:支持猎头看到我的联系方式，可直接联系我')
    contact_headhunter = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='支持猎头看到我的联系方式(我的联系方式)')
    is_grab_order = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否抢单职位,0:false,1:true')
    grab_order_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='抢单职位数量')
    pa_remark_time = db.Column(db.DateTime, info='pa发布公告时间')
    denyreason = db.Column(db.String(1000), info='拒绝理由')
    verify_time = db.Column(db.DateTime, info='提交审核时间')
    important_degree = db.Column(db.Integer, server_default=db.FetchedValue(), info='重要程度')
    lastfresh_date = db.Column(db.DateTime, info='职位最新更新时间')
    isGrab = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否抢单职位')
    is_noticed = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否已经通知')
    investigation_time = db.Column(db.DateTime, info='职位调研时间')
    is_pa_survey = db.Column(db.Integer, server_default=db.FetchedValue(), info='PA是否调研：公开需求无需调研默认为0,私密职位需要调研设置为：1,PA调研之后修改为：2')
    team_size = db.Column(db.Integer, server_default=db.FetchedValue(), info='团队人数')
    position_survey_status = db.Column(db.Integer, server_default=db.FetchedValue(), info='待PO审核：101; 待调研：102; 待审核：103; 审核不通过：104; 审核通过待发布：105; ')
    is_lieying = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否为猎英,0:非猎英,1:猎英')



t_position_20190829 = db.Table(
    'position_20190829',
    db.Column('id', db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='主键ID'),
    db.Column('title', db.String(600), info='标题'),
    db.Column('countryId', db.BigInteger, info='职位，所在国家'),
    db.Column('provinceId', db.BigInteger, info='职位，所在省ID'),
    db.Column('cityId', db.BigInteger, info='职位，所在市ID'),
    db.Column('countyId', db.BigInteger, info='职位所在县id'),
    db.Column('location', db.String(511), info='上班地址（详细描述）'),
    db.Column('professionTypeId', db.BigInteger, info='职能类别'),
    db.Column('professionTypeParentId', db.BigInteger, info='职能类别(父级）'),
    db.Column('industryId', db.BigInteger, info='行业Id'),
    db.Column('internalCode', db.String(300), info='内部编号（企业）'),
    db.Column('categoryId', db.BigInteger, info='分类（暂时不用）'),
    db.Column('jobDescription', db.Text, info='职位描述'),
    db.Column('jobRequirement', db.Text, info='职位需求'),
    db.Column('positionType', db.Integer, info='0：需要申请 1：不需要申请 2：不能申请（内部，暂时没有engagement概念）'),
    db.Column('expectFillDate', db.DateTime, info='期望到岗时间'),
    db.Column('headCount', db.Integer, info='招聘人数'),
    db.Column('annualSalary', db.Float(asdecimal=True), info='年薪'),
    db.Column('rewardType', db.Integer, info='佣金类型 0：固定佣金   1：年薪百分比 '),
    db.Column('fixedRewardAmount', db.Float(asdecimal=True), info='固定佣金的 金额'),
    db.Column('percentageNumbric', db.Float(asdecimal=True), info='百分比 数字 20 表示 年薪* 20%'),
    db.Column('commissionSupplement', db.String(600), info='佣金补充说明'),
    db.Column('totalCandidate', db.Integer, info='当前猎头数'),
    db.Column('totalPlacement', db.Integer, info='职位成单数'),
    db.Column('totalActiveCandidate', db.Integer, info='活跃猎头数'),
    db.Column('pageViews', db.Integer, info='点击量（总）'),
    db.Column('totalCollection', db.Integer, info='关注数'),
    db.Column('totalEngage', db.Integer, info='合作猎头数'),
    db.Column('totalRequest', db.Integer, info='当前申请数'),
    db.Column('terminatedReason', db.String(2000), info='结束原因'),
    db.Column('status', db.Integer, info='0：published 发布  1：draft 草稿 2：申请关闭 3：已关闭 4：暂停'),
    db.Column('createTime', db.DateTime, info='创建时间'),
    db.Column('createUserId', db.BigInteger, info='创建者'),
    db.Column('updateTime', db.DateTime, server_default=db.FetchedValue(), info='更新时间'),
    db.Column('updateUserId', db.BigInteger, info='更新者'),
    db.Column('notifyHeadhunterFlag', db.Integer, info='是否通知签约猎头'),
    db.Column('notifyHeadhunterNote', db.String(1023), info='通知签约猎头的内容'),
    db.Column('companyId', db.BigInteger, info='职位对应的公司id'),
    db.Column('comment', db.String(500)),
    db.Column('commentDate', db.DateTime),
    db.Column('urgency', db.Integer),
    db.Column('prompt', db.Text, info='系统调研职位的内容'),
    db.Column('salaryDescription', db.String(1023)),
    db.Column('hasActive', db.Integer),
    db.Column('refreshTime', db.Integer, server_default=db.FetchedValue(), info='职位刷新次数'),
    db.Column('positionAssignId', db.BigInteger, info='职位负责人'),
    db.Column('positionOrder', db.Integer, info='职位排序序号'),
    db.Column('isContract', db.Integer, info='0 不是合同职位,1是合同职位'),
    db.Column('isPrivate', db.Integer, info='0 不是私密职位,1是私密职位'),
    db.Column('isPublic', db.Integer, info='0 不是公开职位,1是公开职位'),
    db.Column('address', db.String(1000), info='职位所在地'),
    db.Column('department', db.String(1000), info='所属部门'),
    db.Column('reportpo', db.String(1000), info='汇报对象'),
    db.Column('subordinate', db.String(200), info='下属团队'),
    db.Column('totalAssign', db.Integer, info='操作猎头数'),
    db.Column('priority', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('hr_priority', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('service_admin', db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='对应EM的id'),
    db.Column('investigated', db.Integer, nullable=False, server_default=db.FetchedValue(), info='0没有调研 1已经调研'),
    db.Column('publish_time', db.DateTime, info='职位发布时间'),
    db.Column('position_style', db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位类型 0:500强 1:稳定型 2：创业型 3：合伙人'),
    db.Column('remark', db.String(2000), nullable=False, server_default=db.FetchedValue()),
    db.Column('salary_type', db.Integer, nullable=False, server_default=db.FetchedValue(), info='薪资类型0：年薪1：月薪'),
    db.Column('division_id', db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='事业部id'),
    db.Column('browse_count', db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位浏览量'),
    db.Column('max_base_annual_salary', db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='最大基本年薪'),
    db.Column('min_show_annual_salary', db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='最小显示年薪'),
    db.Column('max_show_annual_salary', db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='最大显示年薪'),
    db.Column('max_reward', db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='最大佣金'),
    db.Column('guarantee_time', db.Integer, info='保证期月数，-1表示无保证期'),
    db.Column('month_salary_rule', db.Integer, nullable=False, server_default=db.FetchedValue(), info='月薪制度 12：12薪  13：13薪 14：14薪   15：15薪  16：16薪  100：16薪以上'),
    db.Column('interview_style', db.String(60), info='面试方式'),
    db.Column('interview_times', db.Integer, nullable=False, server_default=db.FetchedValue(), info='面试轮次 1：1轮  2：2轮 3：3轮 4：4轮 5：4轮以上'),
    db.Column('interview_province_id', db.BigInteger, info='面试地点-省份'),
    db.Column('interview_city_id', db.BigInteger, info='面试地点-城市'),
    db.Column('interview_address', db.String(250), info='面试地点-地址'),
    db.Column('interviewer', db.String(255), info='面试官'),
    db.Column('interviewer_order', db.String(250), info='面试官顺序'),
    db.Column('phone_interview', db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否可以电话面试'),
    db.Column('video_interview', db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否可以视频面试'),
    db.Column('language_required', db.String(200), nullable=False, server_default=db.FetchedValue(), info='语言要求,存汉字[英语,日语,汉语]'),
    db.Column('language_string_required', db.String(255), server_default=db.FetchedValue(), info='语言要求,存字符串[1,2,3,4]'),
    db.Column('college_required', db.String(200), info='hr输入的学院证书要求'),
    db.Column('degree_required', db.Integer, nullable=False, server_default=db.FetchedValue(), info='学历要求 0:不限 1：大专及以上 2：本科及以上 3：硕士及以上 4：博士及以上'),
    db.Column('gender_required', db.Integer, nullable=False, server_default=db.FetchedValue(), info='性别要求 0：不限  1：男  2：女'),
    db.Column('work_exp_required', db.Integer, nullable=False, server_default=db.FetchedValue(), info='工作经验要求 ：0:不限 1:1年以上  2:2年以上 3:3年以上 4：4年以上 5：5年以上 6：6年以上 7：7年以上'),
    db.Column('work_exp_year_desc', db.String(60), server_default=db.FetchedValue(), info='工作年限要求'),
    db.Column('highlights', db.String(1000), nullable=False, server_default=db.FetchedValue(), info='职位亮点'),
    db.Column('temptation', db.String(500), nullable=False, server_default=db.FetchedValue(), info='职位诱惑'),
    db.Column('open_date', db.Integer, nullable=False, server_default=db.FetchedValue(), info='开放时间  1:小于1周  2：小于两周 3：两周以上'),
    db.Column('approval_pass', db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否审核通过'),
    db.Column('important_msg', db.Text, info='职位重要信息'),
    db.Column('modify_time', db.DateTime, info='最后刷新时间'),
    db.Column('unanswer_question', db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否有未回答的问题 0:没有 1:有'),
    db.Column('question_update_time', db.Date, info='问题最后更新时间'),
    db.Column('answer_update_time', db.Date, info='回答最后更新时间'),
    db.Column('priority_feedback_hours', db.Integer, nullable=False, server_default=db.FetchedValue(), info=' hr反馈小时数'),
    db.Column('priority_feedback_channel', db.String(60), info='反馈渠道'),
    db.Column('keep_contact_time', db.String(211), info='可联系时间段'),
    db.Column('position_title_id', db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职能id'),
    db.Column('age_required', db.String(200), nullable=False, server_default=db.FetchedValue(), info='年龄要求'),
    db.Column('certificate', db.String(100), nullable=False, server_default=db.FetchedValue(), info='证书'),
    db.Column('open_reason', db.Integer, nullable=False, server_default=db.FetchedValue(), info='开放原因'),
    db.Column('qr_code', db.String(200), nullable=False, server_default=db.FetchedValue(), info='二维码图片'),
    db.Column('edit_time', db.DateTime, info='职位编辑时间'),
    db.Column('pa_proxy', db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否需要pa代指定'),
    db.Column('status_time', db.DateTime, info='状态变更时间(主要暂停及恢复)'),
    db.Column('apply_required', db.String(200), nullable=False, server_default=db.FetchedValue(), info='申请要求'),
    db.Column('pa_remark', db.String(2000), nullable=False, server_default=db.FetchedValue(), info='pa公告'),
    db.Column('contact', db.String(100), nullable=False, server_default=db.FetchedValue(), info='职位联系方式'),
    db.Column('feedback_remark', db.String(100), nullable=False, server_default=db.FetchedValue(), info='反馈备注'),
    db.Column('level_code', db.Integer, nullable=False, server_default=db.FetchedValue(), info='级别CODE'),
    db.Column('remark_time', db.DateTime, info='发布公告时间'),
    db.Column('other_priority_feedback_time', db.String(500), nullable=False, server_default=db.FetchedValue(), info='其他反馈时间'),
    db.Column('is_contact_headhunter', db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否直接对接猎头，0:仅通过猎上平台在线沟通,1:支持猎头看到我的联系方式，可直接联系我'),
    db.Column('contact_headhunter', db.String(500), nullable=False, server_default=db.FetchedValue(), info='支持猎头看到我的联系方式(我的联系方式)'),
    db.Column('is_grab_order', db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否抢单职位,0:false,1:true'),
    db.Column('grab_order_count', db.Integer, nullable=False, server_default=db.FetchedValue(), info='抢单职位数量'),
    db.Column('pa_remark_time', db.DateTime, info='pa发布公告时间'),
    db.Column('denyreason', db.String(1000), info='拒绝理由'),
    db.Column('verify_time', db.DateTime, info='提交审核时间'),
    db.Column('important_degree', db.Integer, server_default=db.FetchedValue(), info='重要程度'),
    db.Column('lastfresh_date', db.DateTime, info='职位最新更新时间'),
    db.Column('isGrab', db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否抢单职位'),
    db.Column('is_noticed', db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否已经通知'),
    db.Column('investigation_time', db.DateTime, info='职位调研时间'),
    db.Column('is_pa_survey', db.Integer, server_default=db.FetchedValue(), info='PA是否调研：公开需求无需调研默认为0,私密职位需要调研设置为：1,PA调研之后修改为：2'),
    db.Column('team_size', db.Integer, server_default=db.FetchedValue(), info='团队人数'),
    db.Column('position_survey_status', db.Integer, server_default=db.FetchedValue(), info='待PO审核：101; 待调研：102; 待审核：103; 审核不通过：104; 审核通过待发布：105; '),
    db.Column('is_lieying', db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否为猎英,0:非猎英,1:猎英')
)



t_position_2019_09_03 = db.Table(
    'position_2019_09_03',
    db.Column('id', db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='主键ID'),
    db.Column('title', db.String(600), info='标题'),
    db.Column('countryId', db.BigInteger, info='职位，所在国家'),
    db.Column('provinceId', db.BigInteger, info='职位，所在省ID'),
    db.Column('cityId', db.BigInteger, info='职位，所在市ID'),
    db.Column('countyId', db.BigInteger, info='职位所在县id'),
    db.Column('location', db.String(511), info='上班地址（详细描述）'),
    db.Column('professionTypeId', db.BigInteger, info='职能类别'),
    db.Column('professionTypeParentId', db.BigInteger, info='职能类别(父级）'),
    db.Column('industryId', db.BigInteger, info='行业Id'),
    db.Column('internalCode', db.String(300), info='内部编号（企业）'),
    db.Column('categoryId', db.BigInteger, info='分类（暂时不用）'),
    db.Column('jobDescription', db.Text, info='职位描述'),
    db.Column('jobRequirement', db.Text, info='职位需求'),
    db.Column('positionType', db.Integer, info='0：需要申请 1：不需要申请 2：不能申请（内部，暂时没有engagement概念）'),
    db.Column('expectFillDate', db.DateTime, info='期望到岗时间'),
    db.Column('headCount', db.Integer, info='招聘人数'),
    db.Column('annualSalary', db.Float(asdecimal=True), info='年薪'),
    db.Column('rewardType', db.Integer, info='佣金类型 0：固定佣金   1：年薪百分比 '),
    db.Column('fixedRewardAmount', db.Float(asdecimal=True), info='固定佣金的 金额'),
    db.Column('percentageNumbric', db.Float(asdecimal=True), info='百分比 数字 20 表示 年薪* 20%'),
    db.Column('commissionSupplement', db.String(600), info='佣金补充说明'),
    db.Column('totalCandidate', db.Integer, info='当前猎头数'),
    db.Column('totalPlacement', db.Integer, info='职位成单数'),
    db.Column('totalActiveCandidate', db.Integer, info='活跃猎头数'),
    db.Column('pageViews', db.Integer, info='点击量（总）'),
    db.Column('totalCollection', db.Integer, info='关注数'),
    db.Column('totalEngage', db.Integer, info='合作猎头数'),
    db.Column('totalRequest', db.Integer, info='当前申请数'),
    db.Column('terminatedReason', db.String(2000), info='结束原因'),
    db.Column('status', db.Integer, info='0：published 发布  1：draft 草稿 2：申请关闭 3：已关闭 4：暂停'),
    db.Column('createTime', db.DateTime, info='创建时间'),
    db.Column('createUserId', db.BigInteger, info='创建者'),
    db.Column('updateTime', db.DateTime, server_default=db.FetchedValue(), info='更新时间'),
    db.Column('updateUserId', db.BigInteger, info='更新者'),
    db.Column('notifyHeadhunterFlag', db.Integer, info='是否通知签约猎头'),
    db.Column('notifyHeadhunterNote', db.String(1023), info='通知签约猎头的内容'),
    db.Column('companyId', db.BigInteger, info='职位对应的公司id'),
    db.Column('comment', db.String(500)),
    db.Column('commentDate', db.DateTime),
    db.Column('urgency', db.Integer),
    db.Column('prompt', db.Text, info='系统调研职位的内容'),
    db.Column('salaryDescription', db.String(1023)),
    db.Column('hasActive', db.Integer),
    db.Column('refreshTime', db.Integer, server_default=db.FetchedValue(), info='职位刷新次数'),
    db.Column('positionAssignId', db.BigInteger, info='职位负责人'),
    db.Column('positionOrder', db.Integer, info='职位排序序号'),
    db.Column('isContract', db.Integer, info='0 不是合同职位,1是合同职位'),
    db.Column('isPrivate', db.Integer, info='0 不是私密职位,1是私密职位'),
    db.Column('isPublic', db.Integer, info='0 不是公开职位,1是公开职位'),
    db.Column('address', db.String(1000), info='职位所在地'),
    db.Column('department', db.String(1000), info='所属部门'),
    db.Column('reportpo', db.String(1000), info='汇报对象'),
    db.Column('subordinate', db.String(200), info='下属团队'),
    db.Column('totalAssign', db.Integer, info='操作猎头数'),
    db.Column('priority', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('hr_priority', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('service_admin', db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='对应EM的id'),
    db.Column('investigated', db.Integer, nullable=False, server_default=db.FetchedValue(), info='0没有调研 1已经调研'),
    db.Column('publish_time', db.DateTime, info='职位发布时间'),
    db.Column('position_style', db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位类型 0:500强 1:稳定型 2：创业型 3：合伙人'),
    db.Column('remark', db.String(2000), nullable=False, server_default=db.FetchedValue()),
    db.Column('salary_type', db.Integer, nullable=False, server_default=db.FetchedValue(), info='薪资类型0：年薪1：月薪'),
    db.Column('division_id', db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='事业部id'),
    db.Column('browse_count', db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位浏览量'),
    db.Column('max_base_annual_salary', db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='最大基本年薪'),
    db.Column('min_show_annual_salary', db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='最小显示年薪'),
    db.Column('max_show_annual_salary', db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='最大显示年薪'),
    db.Column('max_reward', db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='最大佣金'),
    db.Column('guarantee_time', db.Integer, info='保证期月数，-1表示无保证期'),
    db.Column('month_salary_rule', db.Integer, nullable=False, server_default=db.FetchedValue(), info='月薪制度 12：12薪  13：13薪 14：14薪   15：15薪  16：16薪  100：16薪以上'),
    db.Column('interview_style', db.String(60), info='面试方式'),
    db.Column('interview_times', db.Integer, nullable=False, server_default=db.FetchedValue(), info='面试轮次 1：1轮  2：2轮 3：3轮 4：4轮 5：4轮以上'),
    db.Column('interview_province_id', db.BigInteger, info='面试地点-省份'),
    db.Column('interview_city_id', db.BigInteger, info='面试地点-城市'),
    db.Column('interview_address', db.String(250), info='面试地点-地址'),
    db.Column('interviewer', db.String(255), info='面试官'),
    db.Column('interviewer_order', db.String(250), info='面试官顺序'),
    db.Column('phone_interview', db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否可以电话面试'),
    db.Column('video_interview', db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否可以视频面试'),
    db.Column('language_required', db.String(200), nullable=False, server_default=db.FetchedValue(), info='语言要求,存汉字[英语,日语,汉语]'),
    db.Column('language_string_required', db.String(255), server_default=db.FetchedValue(), info='语言要求,存字符串[1,2,3,4]'),
    db.Column('college_required', db.String(200), info='hr输入的学院证书要求'),
    db.Column('degree_required', db.Integer, nullable=False, server_default=db.FetchedValue(), info='学历要求 0:不限 1：大专及以上 2：本科及以上 3：硕士及以上 4：博士及以上'),
    db.Column('gender_required', db.Integer, nullable=False, server_default=db.FetchedValue(), info='性别要求 0：不限  1：男  2：女'),
    db.Column('work_exp_required', db.Integer, nullable=False, server_default=db.FetchedValue(), info='工作经验要求 ：0:不限 1:1年以上  2:2年以上 3:3年以上 4：4年以上 5：5年以上 6：6年以上 7：7年以上'),
    db.Column('work_exp_year_desc', db.String(60), server_default=db.FetchedValue(), info='工作年限要求'),
    db.Column('highlights', db.String(1000), nullable=False, server_default=db.FetchedValue(), info='职位亮点'),
    db.Column('temptation', db.String(500), nullable=False, server_default=db.FetchedValue(), info='职位诱惑'),
    db.Column('open_date', db.Integer, nullable=False, server_default=db.FetchedValue(), info='开放时间  1:小于1周  2：小于两周 3：两周以上'),
    db.Column('approval_pass', db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否审核通过'),
    db.Column('important_msg', db.Text, info='职位重要信息'),
    db.Column('modify_time', db.DateTime, info='最后刷新时间'),
    db.Column('unanswer_question', db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否有未回答的问题 0:没有 1:有'),
    db.Column('question_update_time', db.Date, info='问题最后更新时间'),
    db.Column('answer_update_time', db.Date, info='回答最后更新时间'),
    db.Column('priority_feedback_hours', db.Integer, nullable=False, server_default=db.FetchedValue(), info=' hr反馈小时数'),
    db.Column('priority_feedback_channel', db.String(60), info='反馈渠道'),
    db.Column('keep_contact_time', db.String(211), info='可联系时间段'),
    db.Column('position_title_id', db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职能id'),
    db.Column('age_required', db.String(200), nullable=False, server_default=db.FetchedValue(), info='年龄要求'),
    db.Column('certificate', db.String(100), nullable=False, server_default=db.FetchedValue(), info='证书'),
    db.Column('open_reason', db.Integer, nullable=False, server_default=db.FetchedValue(), info='开放原因'),
    db.Column('qr_code', db.String(200), nullable=False, server_default=db.FetchedValue(), info='二维码图片'),
    db.Column('edit_time', db.DateTime, info='职位编辑时间'),
    db.Column('pa_proxy', db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否需要pa代指定'),
    db.Column('status_time', db.DateTime, info='状态变更时间(主要暂停及恢复)'),
    db.Column('apply_required', db.String(200), nullable=False, server_default=db.FetchedValue(), info='申请要求'),
    db.Column('pa_remark', db.String(2000), nullable=False, server_default=db.FetchedValue(), info='pa公告'),
    db.Column('contact', db.String(100), nullable=False, server_default=db.FetchedValue(), info='职位联系方式'),
    db.Column('feedback_remark', db.String(100), nullable=False, server_default=db.FetchedValue(), info='反馈备注'),
    db.Column('level_code', db.Integer, nullable=False, server_default=db.FetchedValue(), info='级别CODE'),
    db.Column('remark_time', db.DateTime, info='发布公告时间'),
    db.Column('other_priority_feedback_time', db.String(500), nullable=False, server_default=db.FetchedValue(), info='其他反馈时间'),
    db.Column('is_contact_headhunter', db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否直接对接猎头，0:仅通过猎上平台在线沟通,1:支持猎头看到我的联系方式，可直接联系我'),
    db.Column('contact_headhunter', db.String(500), nullable=False, server_default=db.FetchedValue(), info='支持猎头看到我的联系方式(我的联系方式)'),
    db.Column('is_grab_order', db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否抢单职位,0:false,1:true'),
    db.Column('grab_order_count', db.Integer, nullable=False, server_default=db.FetchedValue(), info='抢单职位数量'),
    db.Column('pa_remark_time', db.DateTime, info='pa发布公告时间'),
    db.Column('denyreason', db.String(1000), info='拒绝理由'),
    db.Column('verify_time', db.DateTime, info='提交审核时间'),
    db.Column('important_degree', db.Integer, server_default=db.FetchedValue(), info='重要程度'),
    db.Column('lastfresh_date', db.DateTime, info='职位最新更新时间'),
    db.Column('isGrab', db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否抢单职位'),
    db.Column('is_noticed', db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否已经通知'),
    db.Column('investigation_time', db.DateTime, info='职位调研时间'),
    db.Column('is_pa_survey', db.Integer, server_default=db.FetchedValue(), info='PA是否调研：公开需求无需调研默认为0,私密职位需要调研设置为：1,PA调研之后修改为：2'),
    db.Column('team_size', db.Integer, server_default=db.FetchedValue(), info='团队人数'),
    db.Column('position_survey_status', db.Integer, server_default=db.FetchedValue(), info='待PO审核：101; 待调研：102; 待审核：103; 审核不通过：104; 审核通过待发布：105; '),
    db.Column('is_lieying', db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否为猎英,0:非猎英,1:猎英')
)



t_position_2019_12_10 = db.Table(
    'position_2019_12_10',
    db.Column('id', db.BigInteger, nullable=False, info='主键，系统生成'),
    db.Column('title', db.String(500), server_default=db.FetchedValue()),
    db.Column('name', db.String(500), server_default=db.FetchedValue()),
    db.Column('user_name', db.String(128), server_default=db.FetchedValue()),
    db.Column('is_ai', db.Integer, server_default=db.FetchedValue())
)



class Position20200825(db.Model):
    __tablename__ = 'position_20200825'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    title = db.Column(db.String(600), info='标题')
    countryId = db.Column(db.BigInteger, info='职位，所在国家')
    provinceId = db.Column(db.BigInteger, info='职位，所在省ID')
    cityId = db.Column(db.BigInteger, info='职位，所在市ID')
    countyId = db.Column(db.BigInteger, info='职位所在县id')
    location = db.Column(db.String(511), info='上班地址（详细描述）')
    professionTypeId = db.Column(db.BigInteger, info='职能类别')
    professionTypeParentId = db.Column(db.BigInteger, info='职能类别(父级）')
    industryId = db.Column(db.BigInteger, info='行业Id')
    internalCode = db.Column(db.String(300), info='内部编号（企业）')
    categoryId = db.Column(db.BigInteger, info='分类（暂时不用）')
    jobDescription = db.Column(db.Text, info='职位描述')
    jobRequirement = db.Column(db.Text, info='职位需求')
    positionType = db.Column(db.Integer, info='0：需要申请 1：不需要申请 2：不能申请（内部，暂时没有engagement概念）')
    expectFillDate = db.Column(db.DateTime, info='期望到岗时间')
    headCount = db.Column(db.Integer, info='招聘人数')
    annualSalary = db.Column(db.Float(asdecimal=True), info='年薪')
    rewardType = db.Column(db.Integer, info='佣金类型 0：固定佣金   1：年薪百分比 ')
    fixedRewardAmount = db.Column(db.Float(asdecimal=True), info='固定佣金的 金额')
    percentageNumbric = db.Column(db.Float(asdecimal=True), info='百分比 数字 20 表示 年薪* 20%')
    commissionSupplement = db.Column(db.String(600), info='佣金补充说明')
    totalCandidate = db.Column(db.Integer, info='当前猎头数')
    totalPlacement = db.Column(db.Integer, info='职位成单数')
    totalActiveCandidate = db.Column(db.Integer, info='活跃猎头数')
    pageViews = db.Column(db.Integer, info='点击量（总）')
    totalCollection = db.Column(db.Integer, info='关注数')
    totalEngage = db.Column(db.Integer, info='合作猎头数')
    totalRequest = db.Column(db.Integer, info='当前申请数')
    terminatedReason = db.Column(db.String(2000), info='结束原因')
    status = db.Column(db.Integer, index=True, info='0：published 发布  1：draft 草稿 2：申请关闭 3：已关闭 4：暂停')
    createTime = db.Column(db.DateTime, info='创建时间')
    createUserId = db.Column(db.BigInteger, info='创建者')
    updateTime = db.Column(db.DateTime, index=True, server_default=db.FetchedValue(), info='更新时间')
    updateUserId = db.Column(db.BigInteger, info='更新者')
    notifyHeadhunterFlag = db.Column(db.Integer, info='是否通知签约猎头')
    notifyHeadhunterNote = db.Column(db.String(1023), info='通知签约猎头的内容')
    companyId = db.Column(db.BigInteger, index=True, info='职位对应的公司id')
    comment = db.Column(db.String(500))
    commentDate = db.Column(db.DateTime)
    urgency = db.Column(db.Integer)
    prompt = db.Column(db.Text, info='系统调研职位的内容')
    salaryDescription = db.Column(db.String(1023))
    hasActive = db.Column(db.Integer)
    refreshTime = db.Column(db.Integer, server_default=db.FetchedValue(), info='职位刷新次数')
    positionAssignId = db.Column(db.BigInteger, index=True, info='职位负责人')
    positionOrder = db.Column(db.Integer, info='职位排序序号')
    isContract = db.Column(db.Integer, info='0 不是合同职位,1是合同职位')
    isPrivate = db.Column(db.Integer, info='0 不是私密职位,1是私密职位')
    isPublic = db.Column(db.Integer, info='0 不是公开职位,1是公开职位')
    address = db.Column(db.String(1000), info='职位所在地')
    department = db.Column(db.String(1000), info='所属部门')
    reportpo = db.Column(db.String(1000), info='汇报对象')
    subordinate = db.Column(db.String(200), info='下属团队')
    totalAssign = db.Column(db.Integer, info='操作猎头数')
    priority = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    hr_priority = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    service_admin = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='对应EM的id')
    investigated = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0没有调研 1已经调研')
    publish_time = db.Column(db.DateTime, index=True, info='职位发布时间')
    position_style = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位类型 0:500强 1:稳定型 2：创业型 3：合伙人')
    remark = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue())
    salary_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='薪资类型0：年薪1：月薪')
    division_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='事业部id')
    browse_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位浏览量')
    max_base_annual_salary = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='最大基本年薪')
    min_show_annual_salary = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='最小显示年薪')
    max_show_annual_salary = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='最大显示年薪')
    max_reward = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='最大佣金')
    guarantee_time = db.Column(db.Integer, info='保证期月数，-1表示无保证期')
    month_salary_rule = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='月薪制度 12：12薪  13：13薪 14：14薪   15：15薪  16：16薪  100：16薪以上')
    interview_style = db.Column(db.String(60), info='面试方式')
    interview_times = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='面试轮次 1：1轮  2：2轮 3：3轮 4：4轮 5：4轮以上')
    interview_province_id = db.Column(db.BigInteger, info='面试地点-省份')
    interview_city_id = db.Column(db.BigInteger, info='面试地点-城市')
    interview_address = db.Column(db.String(250), info='面试地点-地址')
    interviewer = db.Column(db.String(255), info='面试官')
    interviewer_order = db.Column(db.String(250), info='面试官顺序')
    phone_interview = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否可以电话面试')
    video_interview = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否可以视频面试')
    language_required = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='语言要求,存汉字[英语,日语,汉语]')
    language_string_required = db.Column(db.String(255), server_default=db.FetchedValue(), info='语言要求,存字符串[1,2,3,4]')
    college_required = db.Column(db.String(200), info='hr输入的学院证书要求')
    degree_required = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='学历要求 0:不限 1：大专及以上 2：本科及以上 3：硕士及以上 4：博士及以上')
    gender_required = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='性别要求 0：不限  1：男  2：女')
    work_exp_required = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='工作经验要求 ：0:不限 1:1年以上  2:2年以上 3:3年以上 4：4年以上 5：5年以上 6：6年以上 7：7年以上')
    work_exp_year_desc = db.Column(db.String(60), server_default=db.FetchedValue(), info='工作年限要求')
    highlights = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='职位亮点')
    temptation = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='职位诱惑')
    open_date = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开放时间  1:小于1周  2：小于两周 3：两周以上')
    approval_pass = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否审核通过')
    important_msg = db.Column(db.Text, info='职位重要信息')
    modify_time = db.Column(db.DateTime, info='最后刷新时间')
    unanswer_question = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否有未回答的问题 0:没有 1:有')
    question_update_time = db.Column(db.Date, info='问题最后更新时间')
    answer_update_time = db.Column(db.Date, info='回答最后更新时间')
    priority_feedback_hours = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info=' hr反馈小时数')
    priority_feedback_channel = db.Column(db.String(60), info='反馈渠道')
    keep_contact_time = db.Column(db.String(211), info='可联系时间段')
    position_title_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职能id')
    age_required = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='年龄要求')
    certificate = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='证书')
    open_reason = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开放原因')
    qr_code = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='二维码图片')
    edit_time = db.Column(db.DateTime, info='职位编辑时间')
    pa_proxy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否需要pa代指定')
    status_time = db.Column(db.DateTime, info='状态变更时间(主要暂停及恢复)')
    apply_required = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='申请要求')
    pa_remark = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='pa公告')
    contact = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='职位联系方式')
    feedback_remark = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='反馈备注')
    level_code = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='级别CODE')
    remark_time = db.Column(db.DateTime, info='发布公告时间')
    other_priority_feedback_time = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='其他反馈时间')
    is_contact_headhunter = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否直接对接猎头，0:仅通过猎上平台在线沟通,1:支持猎头看到我的联系方式，可直接联系我')
    contact_headhunter = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='支持猎头看到我的联系方式(我的联系方式)')
    is_grab_order = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否抢单职位,0:false,1:true')
    grab_order_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='抢单职位数量')
    pa_remark_time = db.Column(db.DateTime, info='pa发布公告时间')
    denyreason = db.Column(db.String(1000), info='拒绝理由')
    verify_time = db.Column(db.DateTime, info='提交审核时间')
    important_degree = db.Column(db.Integer, server_default=db.FetchedValue(), info='重要程度')
    lastfresh_date = db.Column(db.DateTime, info='职位最新更新时间')
    isGrab = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否抢单职位')
    is_noticed = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否已经通知')
    investigation_time = db.Column(db.DateTime, info='职位调研时间')
    is_pa_survey = db.Column(db.Integer, server_default=db.FetchedValue(), info='PA是否调研：公开需求无需调研默认为0,私密职位需要调研设置为：1,PA调研之后修改为：2')
    team_size = db.Column(db.Integer, server_default=db.FetchedValue(), info='团队人数')
    position_survey_status = db.Column(db.Integer, server_default=db.FetchedValue(), info='待PO审核：101; 待调研：102; 待审核：103; 审核不通过：104; 审核通过待发布：105; ')
    is_lieying = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否为猎英,0:非猎英,1:猎英')



class Positioncollection(db.Model):
    __tablename__ = 'positioncollection'
    __table_args__ = (
        db.Index('uidx_ positionid_headhunterid', 'positionId', 'headhunterId'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    positionId = db.Column(db.BigInteger, info='职位ID')
    headhunterId = db.Column(db.BigInteger, index=True, info='猎头ID')
    status = db.Column(db.Integer, info='0：有效 1：删除')
    createUserId = db.Column(db.BigInteger, info='创建者')
    updateUserId = db.Column(db.BigInteger, info='更新者')
    createTime = db.Column(db.DateTime, info='创建时间')
    updateTime = db.Column(db.DateTime, info='更新者')
    headhunterCompanyId = db.Column(db.BigInteger, info='猎头公司ID')



class Professiontype(db.Model):
    __tablename__ = 'professiontype'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    name = db.Column(db.String(100))
    code = db.Column(db.String(100))
    parentId = db.Column(db.BigInteger)



class Province(db.Model):
    __tablename__ = 'province'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    name = db.Column(db.String(100), info='名称')
    countryId = db.Column(db.BigInteger, info='国家ID')
    districtcode = db.Column(db.String(10), info='行政区号')
    postcode = db.Column(db.String(10), info='编码')



t_received1 = db.Table(
    'received1',
    db.Column('position_id', db.BigInteger),
    db.Column('headhunter_id', db.BigInteger),
    db.Column('talent_id', db.BigInteger, server_default=db.FetchedValue())
)



t_recommendview1 = db.Table(
    'recommendview1',
    db.Column('candidateId', db.BigInteger, server_default=db.FetchedValue()),
    db.Column('headhunterId', db.BigInteger),
    db.Column('positionId', db.BigInteger),
    db.Column('talentId', db.BigInteger),
    db.Column('all_status', db.Integer, server_default=db.FetchedValue()),
    db.Column('interviewId', db.BigInteger)
)



class Request(db.Model):
    __tablename__ = 'request'
    __table_args__ = (
        db.Index('uidx_positionId_headhunterCompanyId', 'positionId', 'headhunterCompanyId'),
    )

    Id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    positionId = db.Column(db.BigInteger, info='职位ID')
    employerCompanyId = db.Column(db.BigInteger, info='招聘经理的公司 id')
    employerId = db.Column(db.BigInteger, info='招聘经理 id')
    headhunterId = db.Column(db.BigInteger, info='猎头id')
    headhunterCompanyId = db.Column(db.BigInteger, index=True, info='猎头公司ID')
    content = db.Column(db.Text, info='内容')
    rejectedReason = db.Column(db.String(500), info='拒绝原因')
    status = db.Column(db.Integer, info='0：等待申请  1：同意 2：rejected（拒绝）')
    createUserId = db.Column(db.BigInteger, info='创建者')
    createTime = db.Column(db.DateTime, info='创建时间')
    updateUserId = db.Column(db.BigInteger, info='更新者')
    updateTime = db.Column(db.DateTime, info='更新时间')
    positionAssignId = db.Column(db.BigInteger, info='职位负责人')
    rewardType = db.Column(db.Integer, info='佣金类型')
    fixedRewardAmount = db.Column(db.Float(asdecimal=True), info='固定佣金金额')
    percentageNumbric = db.Column(db.Float(asdecimal=True), info='佣金百分比')
    engageUserId = db.Column(db.BigInteger, info='签约猎头ID')
    engageCompanyId = db.Column(db.BigInteger, info='签约猎头ID')
    engageType = db.Column(db.Integer, info='签约类型0 平台签约, 1 企业猎头私自签约')
    statusType = db.Column(db.Integer, info=' 0直接提交候选人合作 1申请提交合作 2邀请合作')
    reject_times = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='拒绝次数')



class Requestassign(db.Model):
    __tablename__ = 'requestassign'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    requestId = db.Column(db.BigInteger, info='请求ID')
    positionId = db.Column(db.BigInteger, nullable=False, info='职位ID')
    headhunterId = db.Column(db.BigInteger, nullable=False, index=True, info='猎头ID')
    assignHunterId = db.Column(db.Integer, info='分配ID')
    headhunterCompanyId = db.Column(db.BigInteger, info='猎企ID')
    createTime = db.Column(db.DateTime, info='创建时间')
    updateTime = db.Column(db.DateTime, info='更新时间')
    employerCompanyId = db.Column(db.Integer, info='雇主公司ID')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1:主动分配  2：被动分配')



class Syndatum(db.Model):
    __tablename__ = 'syndata'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    tableName = db.Column(db.Integer, info='1,user \t2,company \t3,position \t4,candidate \t5,interview \t6,placement \t7,payment \t8,request \t9,positioncollection')
    objId = db.Column(db.BigInteger)
    changetype = db.Column(db.Integer, info='1,插入\t2,更新\t3,删除')
    createTime = db.Column(db.DateTime, info='创建时间')



class Sysconf(db.Model):
    __tablename__ = 'sysconf'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    mailSendFlag = db.Column(db.Integer, info='邮件发送标志')
    domain = db.Column(db.String(50), info='域名')
    defaultFlag = db.Column(db.Integer)
    absoluteResumeFileRootDir = db.Column(db.String(100))
    resumeExt = db.Column(db.String(300))
    urgency = db.Column(db.String(100), server_default=db.FetchedValue(), info='登录,点职位,修改职位,一天不登陆,最高,最低,警戒,新发职位')
    mailHost = db.Column(db.String(200))
    mailUsername = db.Column(db.String(200))
    mailPassword = db.Column(db.String(200))
    mailPort = db.Column(db.Integer)
    batchMailSleep = db.Column(db.Integer)
    incomingOnboardDate = db.Column(db.Integer, server_default=db.FetchedValue(), info='职位过期提前邮件通知时间（天）')
    expiredOnboardDate = db.Column(db.Integer, server_default=db.FetchedValue(), info='职位过期每隔几天邮件通知')
    msgNoticeDate = db.Column(db.Integer, server_default=db.FetchedValue(), info='新消息间隔时间（秒）')



class Syslog(db.Model):
    __tablename__ = 'syslog'

    id = db.Column(db.BigInteger, primary_key=True)
    userId = db.Column(db.BigInteger, index=True)
    createTime = db.Column(db.DateTime, index=True)
    description = db.Column(db.String(1000))
    referModule = db.Column(db.Integer)
    referModuleId = db.Column(db.BigInteger)
    ip = db.Column(db.String(15))



class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    cnName = db.Column(db.String(100), nullable=False, info='中文标签名称')
    enName = db.Column(db.String(100), nullable=False, info='英文标签名称')
    pinyin = db.Column(db.String(500), info='拼音')
    firstPinyin = db.Column(db.String(20), info='拼音首字')
    categoryId = db.Column(db.BigInteger, info='所属类别')
    positionCallTimes = db.Column(db.Integer, server_default=db.FetchedValue(), info='职位调用次数')
    candidateCallTimes = db.Column(db.Integer, server_default=db.FetchedValue(), info='候选人调用次数')
    headhunterCallTimes = db.Column(db.Integer, server_default=db.FetchedValue(), info='猎头调用次数')
    description = db.Column(db.String(1000), info='定义')
    createTime = db.Column(db.DateTime, info='创建时间')
    createUserId = db.Column(db.BigInteger, info='创建者')



t_tags2 = db.Table(
    'tags2',
    db.Column('createuserid', db.BigInteger, index=True, info='创建者'),
    db.Column('objid', db.BigInteger, index=True, info='对象ID'),
    db.Column('objtype', db.String(15), info='SysConf.MODULE_XXX'),
    db.Column('tags', db.String(1000), info='标签')
)



class Tagscategory(db.Model):
    __tablename__ = 'tagscategory'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    cnName = db.Column(db.String(20), info='中文名')
    enName = db.Column(db.String(20), info='英文名')
    pid = db.Column(db.BigInteger, info='上级类别ID')



class TbActivityConfig(db.Model):
    __tablename__ = 'tb_activity_config'
    __table_args__ = (
        db.Index('IDX_ACTIVITY_CONFIG_CONFIG_TYPE', 'activity_code', 'config_type'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    activity_code = db.Column(db.String(64), info='活动Code')
    config_type = db.Column(db.String(50), info='配置类型')
    start_time = db.Column(db.DateTime, info='开始时间')
    end_time = db.Column(db.DateTime, info='结束时间')
    config_name = db.Column(db.String(50), info='配置名称')
    config_value = db.Column(db.String(512), info='配置值')
    config_param1 = db.Column(db.String(2048), info='配置参数1')
    config_param2 = db.Column(db.String(2048), info='配置参数2')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否删除0:false 1:true')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='修改时间')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    update_user_id = db.Column(db.BigInteger, info='修改人')



class TbActivityDecRedelivery(db.Model):
    __tablename__ = 'tb_activity_dec_redelivery'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_id = db.Column(db.BigInteger, nullable=False, info='用户ID')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    candidate_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='相关候选人')
    red_packet = db.Column(db.Integer, server_default=db.FetchedValue(), info='红包')
    interview_redelivery_status = db.Column(db.Integer, info='面试跟投状态 0正常  1 复投 2 复投失败 3 提取 4 提取成功 5 提取失败')
    offer_redelivery_status = db.Column(db.Integer, info='offer跟投状态 0正常  1 复投 2 复投失败 3 提取 4 提取成功 5 提取失败')
    duty_redelivery_status = db.Column(db.Integer, info='到岗跟投状态 0正常  1 复投 2 复投失败 3 提取 4 提取成功 5 提取失败')
    guarantee_redelivery_status = db.Column(db.Integer, info='过保跟投状态 0正常  1 复投 2 复投失败 3 提取 4 提取成功 5 提取失败')
    recommend_redelivery_status = db.Column(db.Integer, server_default=db.FetchedValue(), info='推荐跟投状态 0正常  1 复投 2 复投失败 3 提取 4 提取成功 5 提取失败')



class TbActivityLottery(db.Model):
    __tablename__ = 'tb_activity_lottery'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='名称')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='是否删除0false 1true')
    start_time = db.Column(db.DateTime, nullable=False, info='开始时间')
    end_time = db.Column(db.DateTime, info='结束时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbActivityLotteryPrize(db.Model):
    __tablename__ = 'tb_activity_lottery_prize'
    __table_args__ = (
        db.Index('idx_activity_lottery_prize_defunct', 'activity_lottery_id', 'defunct'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    activity_lottery_id = db.Column(db.BigInteger, nullable=False, info='抽奖活动ID')
    name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='奖品名称')
    description = db.Column(db.String(500), server_default=db.FetchedValue(), info='奖品描述')
    probability = db.Column(db.Float(15, True), nullable=False, info='中奖概率')
    prize_out_id = db.Column(db.String(100), server_default=db.FetchedValue(), info='奖品外部ID')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除0false 1true')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    num = db.Column(db.Integer, server_default=db.FetchedValue(), info='奖品数量 -1  无限')
    prize_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='奖品类型 1:分成比例 2:红包')



class TbActivityLotteryRecord(db.Model):
    __tablename__ = 'tb_activity_lottery_record'
    __table_args__ = (
        db.Index('idx_prizeid_defunct_createtime', 'prize_id', 'defunct', 'create_time'),
        db.Index('idx_activity_lottery_record_defunct', 'activity_lottery_id', 'defunct', 'create_time', 'user_id'),
        db.Index('user_defunct_time', 'user_id', 'defunct', 'create_time'),
        db.Index('idx_activity_lottery_prize_id_defunct', 'prize_id', 'defunct', 'create_time')
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    activity_lottery_id = db.Column(db.BigInteger, nullable=False, index=True, info='抽奖活动ID')
    prize_id = db.Column(db.BigInteger, nullable=False, info='奖品ID')
    prize_out_id = db.Column(db.String(100), server_default=db.FetchedValue(), info='奖品外部ID')
    user_id = db.Column(db.BigInteger, nullable=False, info='用户ID')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='是否删除0false 1true')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    prize_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='奖品类型 1:分成比例 2:红包')
    candidate_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='相关候选人')
    status = db.Column(db.Integer, server_default=db.FetchedValue(), info='0正常  1 复投 2 复投失败 3 提取 4 提取成功 5 提取失败')



class TbActivityPrizePool(db.Model):
    __tablename__ = 'tb_activity_prize_pool'
    __table_args__ = (
        db.Index('IDX_ACTIVITY_PRIZE_DEFUNCT', 'activity_code', 'defunct'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    activity_code = db.Column(db.String(64), info='活动Code')
    prize_type = db.Column(db.String(32), info='奖品类型')
    prize_text = db.Column(db.String(2048), info='奖品文本')
    data_code1 = db.Column(db.BigInteger, info='奖品数据Code1')
    data_code2 = db.Column(db.BigInteger, index=True, info='奖品数据Code2')
    data_code3 = db.Column(db.String(128), info='奖品数据Code2')
    prize_isuse_time = db.Column(db.DateTime, info='奖品发放时间')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否删除0:false 1:true')
    status_no = db.Column(db.Integer, server_default=db.FetchedValue(), info='状态（0：默认待处理；1：可用；2：不可用）')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, info='修改时间')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    update_user_id = db.Column(db.BigInteger, info='修改人')



class TbAdminMission(db.Model):
    __tablename__ = 'tb_admin_mission'
    __table_args__ = (
        db.Index('idx_userid_status_type', 'user_id', 'status', 'type'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='用户ID')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='类型1:发布职位2:候选人到岗3:候选人过保4:职位暂停5:申请关闭职位6:修改职位')
    description = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='描述')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='状态0:新建1:待处理2:时间表3:已处理')
    process_time = db.Column(db.DateTime, info='处理时间')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')



class TbAdvert(db.Model):
    __tablename__ = 'tb_advert'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    app_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0:hr;1:hd;2:c;')
    advert_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='广告类型 0:首页下方广告；1：首页头部广告；等')
    advert_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='广告名称')
    web_logo_path = db.Column(db.String(200), info='web端Logo')
    mobile_logo_path = db.Column(db.String(200), info='手机端Logo')
    page_link = db.Column(db.String(200), server_default=db.FetchedValue(), info='链接地址')
    show_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0：web端；1：手机端；2：所有(all)')
    location = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='放置位置')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除0:false 1:true')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    share_title = db.Column(db.String(100), server_default=db.FetchedValue(), info='分享标题')
    share_content = db.Column(db.String(400), server_default=db.FetchedValue(), info='分享内容')
    share_logo = db.Column(db.String(200), server_default=db.FetchedValue(), info='分享图标')
    share_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='分享类型0:不可分享；1：可分享')



class TbAdvertisement(db.Model):
    __tablename__ = 'tb_advertisement'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='名称')
    pc_logo_path = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='PC端广告图片路径')
    mobile_logo_path = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='APP端广告图片路径')
    page_link = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='专场链接')
    description = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='广告描述，说明')
    advertisement_channel = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0：web端；1：手机端；2：所有(all)')
    platform_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='展示的平台类型，1：HR，2：HH，3：C，4：all')
    location = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='放置位置')
    share_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='分享类型0:不可分享；1：可分享')
    share_logo = db.Column(db.String(200), server_default=db.FetchedValue(), info='分享图标')
    priority = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    start_time = db.Column(db.DateTime, info='开始时间')
    end_time = db.Column(db.DateTime, info='结束时间')
    os_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='操作系统类型:1:IOS,2:安卓')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除0false 1true')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbAdvertisementLogo(db.Model):
    __tablename__ = 'tb_advertisement_logo'

    id = db.Column(db.BigInteger, primary_key=True)
    advertisement_id = db.Column(db.BigInteger, nullable=False, info='广告表主键id')
    logo_path = db.Column(db.String(200), nullable=False, info='广告图片地址')
    width = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='图片的宽,0:未知')
    high = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='图片的高,0:未知')
    sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime)



class TbAdviserPaRelation(db.Model):
    __tablename__ = 'tb_adviser_pa_relation'

    id = db.Column(db.BigInteger, primary_key=True, info='主键Id')
    hh_id = db.Column(db.BigInteger, nullable=False, index=True, info='猎头id')
    pa_id = db.Column(db.BigInteger, nullable=False, index=True, info='组成员ID')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, info='最后修改的用户Id')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除 0 否 1是')



class TbAiScreeningEnterpriseTemplate(db.Model):
    __tablename__ = 'tb_ai_screening_enterprise_template'

    id = db.Column(db.BigInteger, primary_key=True, info='主键，系统生成')
    enterprise_id = db.Column(db.BigInteger, nullable=False, info='雇主ID')
    template_name = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='模板名称')
    defunct = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='逻辑删除')
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_user_id = db.Column(db.BigInteger)



class TbAiScreeningEnterpriseTemplateCondition(db.Model):
    __tablename__ = 'tb_ai_screening_enterprise_template_condition'

    id = db.Column(db.BigInteger, primary_key=True, info='主键，系统生成')
    enterprise_id = db.Column(db.BigInteger, nullable=False, index=True, info='职位ID')
    template_id = db.Column(db.BigInteger, nullable=False, index=True, info='模板ID')
    template_group_id = db.Column(db.BigInteger, nullable=False, index=True, info='模板ID')
    group_key = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='组key')
    group_name = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='组名字')
    condition_key = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='条件key')
    condition_value = db.Column(db.String(5000), nullable=False, server_default=db.FetchedValue(), info='条件值')
    condition = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='与下一个的条件  默认 equal:等于 less:小于等于  大于等于:greater')
    sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序')
    defunct = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='逻辑删除')
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_user_id = db.Column(db.BigInteger)



class TbAiScreeningEnterpriseTemplateGroup(db.Model):
    __tablename__ = 'tb_ai_screening_enterprise_template_group'

    id = db.Column(db.BigInteger, primary_key=True, info='主键，系统生成')
    enterprise_id = db.Column(db.BigInteger, nullable=False, index=True, info='职位ID')
    template_id = db.Column(db.BigInteger, nullable=False, index=True, info='模板ID')
    has_must = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否必须 1 必须  0 不看')
    condition = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='与下一个的条件  默认 and')
    sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序')
    defunct = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='逻辑删除')
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_user_id = db.Column(db.BigInteger)



class TbAiScreeningGroup(db.Model):
    __tablename__ = 'tb_ai_screening_group'

    id = db.Column(db.BigInteger, primary_key=True, info='主键，系统生成')
    group_key = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='组key')
    group_name = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='组名字')
    defunct = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='逻辑删除')
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_user_id = db.Column(db.BigInteger)



class TbAiScreeningGroupPosition(db.Model):
    __tablename__ = 'tb_ai_screening_group_position'

    id = db.Column(db.BigInteger, primary_key=True, info='主键，系统生成')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, info='职位ID')
    group_key = db.Column(db.String(255), nullable=False, index=True, server_default=db.FetchedValue(), info='组key')
    group_name = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue(), info='组名字')
    has_must = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否必须 1 必须  0 不看')
    condition = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='与下一个的条件  默认 and')
    sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序')
    defunct = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='逻辑删除')
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_user_id = db.Column(db.BigInteger)



class TbAiScreeningGroupPositionCondition(db.Model):
    __tablename__ = 'tb_ai_screening_group_position_condition'

    id = db.Column(db.BigInteger, primary_key=True, info='主键，系统生成')
    ai_screening_group_position_id = db.Column(db.BigInteger, nullable=False, info='ID')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, info='职位ID')
    group_key = db.Column(db.String(255), nullable=False, index=True, server_default=db.FetchedValue(), info='组key')
    group_name = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue(), info='组名字')
    condition_key = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='条件key')
    condition_value = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='条件值')
    condition = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='与下一个的条件  默认 equal:等于 less:小于等于  大于等于:greater')
    sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序')
    defunct = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='逻辑删除')
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_user_id = db.Column(db.BigInteger)



class TbAiScreeningGroupPositionConditionCopy20200908(db.Model):
    __tablename__ = 'tb_ai_screening_group_position_condition_copy20200908'

    id = db.Column(db.BigInteger, primary_key=True, info='主键，系统生成')
    ai_screening_group_position_id = db.Column(db.BigInteger, nullable=False, info='ID')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, info='职位ID')
    group_key = db.Column(db.String(64), nullable=False, index=True, server_default=db.FetchedValue(), info='组key')
    group_name = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='组名字')
    condition_key = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='条件key')
    condition_value = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='条件值')
    condition = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue(), info='与下一个的条件  默认 equal:等于 less:小于等于  大于等于:greater')
    sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序')
    defunct = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='逻辑删除')
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_user_id = db.Column(db.BigInteger)



class TbAmCompany(db.Model):
    __tablename__ = 'tb_am_company'

    id = db.Column(db.BigInteger, primary_key=True)
    am_id = db.Column(db.BigInteger, nullable=False, info='PA Id')
    company_id = db.Column(db.BigInteger, nullable=False, info='companyId')
    create_time = db.Column(db.DateTime, info='创建时间')
    create_user = db.Column(db.BigInteger, info='创建用户')
    update_time = db.Column(db.DateTime, info='更新时间')
    update_user = db.Column(db.BigInteger, info='更新用户')
    status = db.Column(db.Integer, server_default=db.FetchedValue(), info='状态：0 无效；1 有效')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否删除，0 未删除 ；1已删除')



class TbAnniversarySendRecord(db.Model):
    __tablename__ = 'tb_anniversary_send_record'

    id = db.Column(db.BigInteger, primary_key=True, info='唯一编号')
    user_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='职位编号')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbAnnouncement(db.Model):
    __tablename__ = 'tb_announcement'

    id = db.Column(db.BigInteger, primary_key=True)
    title = db.Column(db.String(255), nullable=False, info='公告主题')
    content = db.Column(db.String(10240), nullable=False, info='公告内容')
    channel = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='渠道区分 1：hd端 2：c端  3：hr端')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)



class TbAnnouncementBrowseRecord(db.Model):
    __tablename__ = 'tb_announcement_browse_record'
    __table_args__ = (
        db.Index('idx_objid_announcementid', 'obj_id', 'announcement_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    announcement_id = db.Column(db.BigInteger, nullable=False, info='公告ID')
    obj_id = db.Column(db.BigInteger, nullable=False, info='ID')
    obj_type = db.Column(db.Integer, nullable=False, info='渠道区分： 1：hd端 2：c端  3：hr端')
    readed = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否阅读 1：已阅，0：未阅')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False)
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)



class TbAppkey(db.Model):
    __tablename__ = 'tb_appkey'

    id = db.Column(db.BigInteger, primary_key=True, info='主键id')
    appkey = db.Column(db.String(65), nullable=False, unique=True, info='应用Key')
    cooperate_type = db.Column(db.String(65), info='合作类型')
    company_id = db.Column(db.String(255), nullable=False, info='客户编号，此处非主键id')
    company_name = db.Column(db.String(255), info='客户名称')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_user_id = db.Column(db.BigInteger, info='更新人')
    update_time = db.Column(db.DateTime)



class TbAppkeyConf(db.Model):
    __tablename__ = 'tb_appkey_conf'

    id = db.Column(db.BigInteger, primary_key=True, info='随tb_app_key的主键')
    encryption_type = db.Column(db.String(65), server_default=db.FetchedValue(), info='加密方式:normal_md5常规md5')
    available = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否有效:1有效/0失效')
    usable_count = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='真实可用条数')
    frequency_every_day = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='每天的频率:0不限制')
    frequency_every_hour = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='每小时频率:0不限制')
    frequency_every_minute = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='每分钟频率:0不限制')
    frequency_every_second = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='每秒钟频率:0不限制')



class TbAssociate(db.Model):
    __tablename__ = 'tb_associate'

    id = db.Column(db.BigInteger, primary_key=True, info='主键id')
    headhunter_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='被关联的猎头的id')
    correlation_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='关联人bd的id')
    creat_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    creat_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人id')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人id')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='逻辑删除')



class TbAudit(db.Model):
    __tablename__ = 'tb_audit'
    __table_args__ = (
        db.Index('idx_candidateid_createtime', 'candidate_id', 'create_time'),
        db.Index('idx_company_createtime', 'company_id', 'create_time'),
        db.Index('idx_positionid_createtime', 'position_id', 'create_time'),
        db.Index('idx_createuid_createtime', 'create_uid', 'create_time')
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='公司ID')
    position_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职位ID')
    candidate_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='候选人ID')
    uid = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    serial_number = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue())
    type = db.Column(db.Integer, nullable=False)
    original_uid = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    content = db.Column(db.String)
    platform = db.Column(db.Integer, nullable=False, info='1.HD\\n2.CRM\\n3.HO\\n4.Mobile\\n5.HR')
    create_uid = db.Column(db.BigInteger, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    last_modify_time = db.Column(db.DateTime, nullable=False)



class TbAugActivityOrder(db.Model):
    __tablename__ = 'tb_aug_activity_order'

    id = db.Column(db.BigInteger, primary_key=True)
    position_id = db.Column(db.BigInteger, index=True, info='职位ID')
    candidate_id = db.Column(db.BigInteger, index=True, info='订单ID')
    headhunter_id = db.Column(db.BigInteger, index=True, info='猎头ID')
    company_id = db.Column(db.BigInteger, index=True, info='猎企ID')
    enterprise_id = db.Column(db.BigInteger, info='雇主ID')
    candidate_name = db.Column(db.String(128), info='候选人')
    position_title = db.Column(db.String(600), info='职位title')
    recommend_feedback_time = db.Column(db.Integer, server_default=db.FetchedValue(), info='推荐反馈周期 单位小时 ')
    recommend_actual_feedback_time = db.Column(db.Integer, info='推荐实际反馈周期 单位分钟')
    status = db.Column(db.Integer, server_default=db.FetchedValue(), info='提现状态  -2:新建 -1:逾期中, 0:未提现  1:提现中  2:已经提现')
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_user_id = db.Column(db.BigInteger)



class TbAugActivityOrderCerification(db.Model):
    __tablename__ = 'tb_aug_activity_order_cerification'

    headhunter_id = db.Column(db.BigInteger, primary_key=True, info='猎头ID')
    user_name = db.Column(db.String(128), info='真实姓名')
    identity_card = db.Column(db.String(128), info='身份证')
    mobile = db.Column(db.String(128), info='手机号码')
    wechat = db.Column(db.String(128), info='微信号')
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_user_id = db.Column(db.BigInteger)



class TbAuroraPushLog(db.Model):
    __tablename__ = 'tb_aurora_push_log'

    id = db.Column(db.BigInteger, primary_key=True, info='唯一编号')
    msg_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='消息id')
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎上用户id')
    user_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='猎上用户类型')
    alias = db.Column(db.String(50), info='别名')
    content = db.Column(db.String, info='推送内容')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='发送状态 1:成功；2:失败')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbAuroraPushUserBind(db.Model):
    __tablename__ = 'tb_aurora_push_user_bind'
    __table_args__ = (
        db.Index('INDEX_AURORA_PUSH_USER_ID_TYPE', 'user_id', 'user_type'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='唯一编号')
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎上用户id')
    user_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='猎上用户类型')
    registration_id = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='注册id')
    alias = db.Column(db.String(50), info='别名')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1：正常；2：禁用')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    min_forbid_push_time = db.Column(db.DateTime, info='最小禁止推送时间')
    max_forbid_push_time = db.Column(db.DateTime, info='最大禁止推送时间')



class TbAuthAccessToken(db.Model):
    __tablename__ = 'tb_auth_access_token'

    id = db.Column(db.BigInteger, primary_key=True, info='id')
    access_token = db.Column(db.String(255), nullable=False, index=True, info='Access Token')
    user_id = db.Column(db.BigInteger, nullable=False, info='关联的用户ID')
    user_name = db.Column(db.String(100), info='用户名')
    client_id = db.Column(db.BigInteger, nullable=False, index=True, info='接入的客户端ID')
    expires_in = db.Column(db.BigInteger, nullable=False, info='过期时间戳')
    grant_type = db.Column(db.String(50), info='授权类型，比如：authorization_code')
    scope = db.Column(db.String(100), info='可被访问的用户的权限范围，比如：basic、super')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='逻辑删除')
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue())



class TbAuthClientDetail(db.Model):
    __tablename__ = 'tb_auth_client_details'

    id = db.Column(db.BigInteger, primary_key=True, info='id')
    client_id = db.Column(db.String(100), nullable=False, index=True, info='接入的客户端ID')
    client_name = db.Column(db.String(100))
    client_secret = db.Column(db.String(255), nullable=False, index=True, info='接入的客户端的密钥')
    redirect_uri = db.Column(db.String(1000), nullable=False, info='回调地址')
    client_user_type = db.Column(db.String(100), info='类型')
    description = db.Column(db.String(1000), info='描述信息')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='逻辑删除')
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    status = db.Column(db.Integer, server_default=db.FetchedValue(), info='0表示未开通；1表示正常使用；2表示已被禁用')



class TbAuthRefreshToken(db.Model):
    __tablename__ = 'tb_auth_refresh_token'

    id = db.Column(db.BigInteger, primary_key=True, info='id')
    token_id = db.Column(db.BigInteger, nullable=False, index=True, info='表auth_access_token对应的Access Token记录')
    refresh_token = db.Column(db.String(255), nullable=False, index=True, info='Refresh Token')
    expires_in = db.Column(db.BigInteger, nullable=False, info='过期时间戳')
    defunct = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='是否删除0:false 1:true')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='修改时间')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    update_user_id = db.Column(db.BigInteger, info='修改人')



class TbAuthWxOpenUserBind(db.Model):
    __tablename__ = 'tb_auth_wx_open_user_bind'
    __table_args__ = (
        db.Index('open_utype_defunct', 'open_id', 'user_type', 'defunct'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    open_id = db.Column(db.String(63), info='微信在app下的openId')
    unione_id = db.Column(db.String(127))
    user_id = db.Column(db.BigInteger, info='绑定的猎上网账号用户ID')
    user_type = db.Column(db.Integer, info='猎上网账号用户类型')
    status = db.Column(db.Integer, info='绑定状态；1：未绑定；2：已绑定；3：已过期')
    expire_time = db.Column(db.DateTime, info='绑定有效期')
    defunct = db.Column(db.Integer, info='逻辑删除；解绑时会删除')
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)



class TbAuthWxSubscribeUser(db.Model):
    __tablename__ = 'tb_auth_wx_subscribe_users'
    __table_args__ = (
        db.Index('type_union', 'public_type', 'union_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    public_type = db.Column(db.Integer, info='公众号枚举')
    open_id = db.Column(db.String(63), index=True, info='微信用户对应在公众号里的openId')
    union_id = db.Column(db.String(63), info='unionid')
    create_time = db.Column(db.DateTime)
    subscribe_time = db.Column(db.DateTime)
    subscribe_scene = db.Column(db.String(63))
    subscribe = db.Column(db.Integer, server_default=db.FetchedValue(), info='当前是否关注')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class TbAuthWxUnionInfo(db.Model):
    __tablename__ = 'tb_auth_wx_union_info'

    id = db.Column(db.BigInteger, primary_key=True)
    union_id = db.Column(db.String(63), index=True)
    nick_name = db.Column(db.String(127))
    sex = db.Column(db.Integer)
    city = db.Column(db.String(63))
    province = db.Column(db.String(63))
    country = db.Column(db.String(63))
    avatar = db.Column(db.String(1023))
    subscribe_time = db.Column(db.DateTime)
    subscribe_scene = db.Column(db.String(63))
    create_time = db.Column(db.DateTime)
    defunct = db.Column(db.String(255), index=True)



class TbAuthentication(db.Model):
    __tablename__ = 'tb_authentication'

    id = db.Column(db.BigInteger, primary_key=True, info='id')
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='认证用户id')
    user_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='用户类型:1:企业用户,2:猎头用户,3:管理员用户,4:渠道用户,5:求职者用户,6:猎大用户;参考com.hunteron.api.user.bean.v2.UserType')
    authentication_mode = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='认证方式0:app刷脸认证，1微信认证')
    address = db.Column(db.String(1024), nullable=False, server_default=db.FetchedValue(), info='住址')
    birthday = db.Column(db.String(10), nullable=False, server_default=db.FetchedValue(), info='生日yyyy-MM-dd')
    gender = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='性别0:女；1:男')
    id_number = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue(), info='身份证号')
    passport_no = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='护照号')
    name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='姓名')
    race = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='民族')
    issued_by = db.Column(db.String(1024), nullable=False, server_default=db.FetchedValue(), info='签发机关')
    valid_date = db.Column(db.String(30), nullable=False, server_default=db.FetchedValue(), info='有效日期')
    id_card_front_url = db.Column(db.String(1024), nullable=False, server_default=db.FetchedValue(), info='身份证正面')
    id_card_back_url = db.Column(db.String(1024), nullable=False, server_default=db.FetchedValue(), info='身份证反面')
    certificates_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='证件类型。默认0，身份证')
    qr_code_url = db.Column(db.String(1024), nullable=False, server_default=db.FetchedValue(), info='微信认证二维码')
    authentication_time = db.Column(db.DateTime, nullable=False, info='认证时间')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建用户id')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新用户Id')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除0:false 1:true')
    work_year_status = db.Column(db.Integer, server_default=db.FetchedValue(), info='工作年限审核')
    avatar_new = db.Column(db.String(255), info='新上传待审核的头像')
    avatar_status = db.Column(db.Integer, server_default=db.FetchedValue(), info='头像审核状态')
    begin_work_year_new = db.Column(db.Integer, info='审核开始工作年限')
    full_verify = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否完整审核过')



class TbAuthorUser(db.Model):
    __tablename__ = 'tb_author_user'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    user_id = db.Column(db.BigInteger, info='用户id')
    open_id = db.Column(db.String(250), index=True, info='公众号openId')
    access_token = db.Column(db.String(1000), info='网页授权接口调用凭证')
    expires_in = db.Column(db.Integer, info='access_token接口调用凭证超时时间，单位（秒）')
    refresh_token = db.Column(db.String(1000), info='用户刷新access_token')
    scope = db.Column(db.String(50), info='用户授权的作用域，使用逗号（,）分隔')
    union_id = db.Column(db.String(100))
    type = db.Column(db.Integer, info='平台来源')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='逻辑删除')
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue())



class TbBaseIndustry(db.Model):
    __tablename__ = 'tb_base_industry'

    industry_id = db.Column(db.BigInteger, primary_key=True, info='一级行业ID')
    industry_name = db.Column(db.String(127), nullable=False, info='行业名称')
    display_name = db.Column(db.String(63), nullable=False, info='行业名称，显示用')
    display_sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='行业显示顺序，降序；0表示不显示')
    parent_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='父行业ID')



class TbBaseIndustryFunction(db.Model):
    __tablename__ = 'tb_base_industry_function'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    industry_id = db.Column(db.BigInteger, nullable=False, info='行业ID')
    position_title_id = db.Column(db.BigInteger, nullable=False, info='行业对应的一级职能ID，来源：tb_position_title表的id')



class TbBaseIndustryFunctionTag(db.Model):
    __tablename__ = 'tb_base_industry_function_tag'

    id = db.Column(db.BigInteger, primary_key=True)
    industry_id = db.Column(db.BigInteger, nullable=False, info='行业')
    function_id = db.Column(db.BigInteger, nullable=False, info='职能ID')
    create_time = db.Column(db.Date, nullable=False)
    create_user_id = db.Column(db.BigInteger, nullable=False)
    defunct = db.Column(db.Integer, nullable=False)



class TbBaseIndustryTag(db.Model):
    __tablename__ = 'tb_base_industry_tag'

    industry_id = db.Column(db.BigInteger, primary_key=True, info='一级行业ID')
    industry_name = db.Column(db.String(127), nullable=False, info='行业名称')
    display_name = db.Column(db.String(63), nullable=False, info='行业名称，显示用')
    display_sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='行业显示顺序，降序；0表示不显示')
    parent_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='父行业ID')



class TbBetaUser(db.Model):
    __tablename__ = 'tb_beta_user'

    id = db.Column(db.BigInteger, primary_key=True)
    version_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='版本类型')
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='测试用户编号')



class TbBizPackageCustRecord(db.Model):
    __tablename__ = 'tb_biz_package_cust_record'
    __table_args__ = (
        db.Index('idx_biz_package_record_enterprise', 'enterprise_id', 'biz_package_code'),
        db.Index('idx_biz_package_record_hr', 'hr_id', 'biz_package_code')
    )

    id = db.Column(db.BigInteger, primary_key=True)
    enterprise_id = db.Column(db.BigInteger, nullable=False, info='雇主企业Id')
    hr_id = db.Column(db.BigInteger, nullable=False, info='hrId')
    biz_package_code = db.Column(db.String(65), nullable=False, info='套餐包code')
    action_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='操作类型:1邀约/2激活')
    action_result = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='操作结果:1成功/0失败')
    position_apply_id = db.Column(db.BigInteger, info='订单Id')
    position_id = db.Column(db.BigInteger, info='职位Id')
    resume_feiwa_id = db.Column(db.String(65), info='飞蛙简历Id')
    resume_obj_id = db.Column(db.String(65), info='mongo自用简历Id')
    resume_level = db.Column(db.Integer, server_default=db.FetchedValue(), info='简历评定等级(目前是薪资)')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建人')



class TbBizPackageEnterprise(db.Model):
    __tablename__ = 'tb_biz_package_enterprise'
    __table_args__ = (
        db.Index('idx_biz_package_code', 'biz_package_code', 'enterprise_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    biz_package_code = db.Column(db.String(65), info='套餐包code')
    biz_package_name = db.Column(db.String(255), info='套餐包名称')
    resume_level = db.Column(db.Integer, server_default=db.FetchedValue(), info='定义简历等级')
    enterprise_id = db.Column(db.BigInteger, info='所属企业Id')
    hr_id = db.Column(db.BigInteger, info='购买套餐的hrId')
    init_voice_service_number = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='初始化语音服务数')
    init_invite_total_number = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='初始可邀约总量')
    init_level1_download_number = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='初始1等简历可下载数量')
    init_level2_download_number = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='初始2等简历可下载数量')
    init_level3_download_number = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='初始3等简历可下载数量')
    voice_service_number = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='语音服务次数')
    invite_total_number = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='现已邀约总量')
    level1_download_number = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='1等简历已下载数量')
    level2_download_number = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='2等简历已下载数量')
    level3_download_number = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='3等简历已下载数量')
    free_voice_service_number = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='空闲语音服务次数')
    free_invite_total_number = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='闲置可邀约总量')
    free_level1_download_number = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='闲置1等简历可下载数量')
    free_level2_download_number = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='闲置2等简历可下载数量')
    free_level3_download_number = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='闲置3等简历可下载数量')
    description = db.Column(db.String(255), info='套餐简介')
    begin_service_time = db.Column(db.DateTime, info='开始服务时间')
    expiry_time = db.Column(db.DateTime, info='过期时间')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_user_id = db.Column(db.BigInteger, info='更新人')
    update_time = db.Column(db.DateTime)



class TbBizPackageHr(db.Model):
    __tablename__ = 'tb_biz_package_hr'

    id = db.Column(db.BigInteger, primary_key=True)
    resume_level = db.Column(db.Integer, server_default=db.FetchedValue(), info='定义简历等级')
    enterprise_id = db.Column(db.BigInteger, nullable=False, info='雇主企业Id')
    hr_id = db.Column(db.BigInteger, nullable=False, index=True, info='hrId')
    user_id = db.Column(db.BigInteger, info='用户Id')
    is_available = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否可用:0不可用/1可用')
    init_voice_service_number = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='语音服务次数')
    init_invite_total_number = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='初始可邀约总量')
    init_voice_service_unlimited = db.Column(db.Integer, server_default=db.FetchedValue(), info='语音服务不限制:1不限制/0限制')
    init_invite_unlimited = db.Column(db.Integer, server_default=db.FetchedValue(), info='邀约服务次数不限制:1不限制/0限制')
    init_level1_download_number = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='初始1等简历可下载数量')
    init_level2_download_number = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='初始2等简历可下载数量')
    init_level3_download_number = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='初始3等简历可下载数量')
    voice_service_number = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='语音服务次数')
    invite_total_number = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='已邀约总量')
    level1_download_number = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='1等简历已下载数量')
    level2_download_number = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='2等简历已下载数量')
    level3_download_number = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='3等简历已下载数量')
    expiry_time = db.Column(db.DateTime, info='过期时间')



class TbBizPackageOperateLog(db.Model):
    __tablename__ = 'tb_biz_package_operate_log'

    id = db.Column(db.BigInteger, primary_key=True)
    enterprise_id = db.Column(db.BigInteger, index=True, info='操作对应的雇主')
    log_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='操作日志类型；1：购买套餐；2：hr管理员分配数量；3：购买套餐后台配置数量；4：直接后台配置数量')
    log_content = db.Column(db.String(4095), info='日志内容')
    operate_user_id = db.Column(db.BigInteger, info='操作人')
    operate_user_type = db.Column(db.Integer, info='操作用户的类型,对应类UserType')
    create_time = db.Column(db.DateTime)



class TbBizPackageTemplate(db.Model):
    __tablename__ = 'tb_biz_package_template'

    id = db.Column(db.BigInteger, primary_key=True)
    biz_package_code = db.Column(db.String(65), unique=True, info='套餐包code')
    biz_package_name = db.Column(db.String(255), info='套餐包名称')
    voice_server_number = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='语音服务次数')
    invite_total_number = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='可邀约总量')
    level1_download_number = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='1等简历可下载数量')
    level2_download_number = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='2等简历可下载数量')
    level3_download_number = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='3等简历可下载数量')
    description = db.Column(db.String(255), info='套餐简介')
    original_price = db.Column(db.Numeric(10, 2), info='原价')
    now_price = db.Column(db.Numeric(10, 2), info='现价')
    unit = db.Column(db.String(15), info='单位:日/月/季/年')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否删除:1已删除/0未删除')
    sorting = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='排序')



class TbCallRobotApiHistory(db.Model):
    __tablename__ = 'tb_call_robot_api_history'

    id = db.Column(db.BigInteger, primary_key=True)
    api_code = db.Column(db.String(64), info='APICode')
    call_ip = db.Column(db.String(255), info='IP')
    param = db.Column(db.String, info='参数')
    result = db.Column(db.String, info='返回参数')
    update_user_id = db.Column(db.BigInteger, info='修改用户ID')
    update_time = db.Column(db.DateTime, info='修改时间')
    create_user_id = db.Column(db.BigInteger, info='创建用户ID')
    create_time = db.Column(db.DateTime, info='创建时间')



class TbCallRobotTask(db.Model):
    __tablename__ = 'tb_call_robot_task'

    code = db.Column(db.String(64), primary_key=True, info='任务Code')
    name = db.Column(db.String(255), info='任务名称')
    supplier_code = db.Column(db.String(64), info='供应商Code')
    supplier_task_code = db.Column(db.String(255), info='供应商任务Code')
    defunct = db.Column(db.Integer, info='是否删除')
    update_user_id = db.Column(db.BigInteger, info='修改用户ID')
    update_time = db.Column(db.DateTime, info='修改时间')
    create_user_id = db.Column(db.BigInteger, info='创建用户ID')
    create_time = db.Column(db.DateTime, info='创建时间')



class TbCallRobotTaskEnterprise(db.Model):
    __tablename__ = 'tb_call_robot_task_enterprise'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    enterprise_id = db.Column(db.BigInteger, info='雇主ID')
    task_code = db.Column(db.String(64), info='任务Code')
    scene_code = db.Column(db.String(255), info='场景Code')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否有效')
    update_time = db.Column(db.DateTime, info='最后修改时间')
    update_user_id = db.Column(db.BigInteger, info='最后修改用户ID')
    create_time = db.Column(db.DateTime, info='创建时间')
    create_user_id = db.Column(db.BigInteger, info='创建用户ID')



class TbCallRobotTaskUser(db.Model):
    __tablename__ = 'tb_call_robot_task_user'

    id = db.Column(db.BigInteger, primary_key=True)
    candidate_id = db.Column(db.BigInteger, info='订单ID')
    resume_id = db.Column(db.BigInteger, info='简历ID')
    task_code = db.Column(db.String(64), info='任务Code')
    status_no = db.Column(db.Integer, info='状态（1：新加入；2：已呼叫）')
    call_result = db.Column(db.String, info='呼叫结果')
    call_result_time = db.Column(db.DateTime, info='呼叫结果同步时间')
    update_user_id = db.Column(db.BigInteger, info='修改用户')
    update_time = db.Column(db.DateTime, info='修改时间')
    create_user_id = db.Column(db.BigInteger, info='创建用户')
    create_time = db.Column(db.DateTime, info='创建时间')



class TbCandidateAtsCheckLog(db.Model):
    __tablename__ = 'tb_candidate_ats_check_log'
    __table_args__ = (
        db.Index('idx_hunter_id_create_time_enterprise_id', 'hunter_id', 'create_time', 'enterprise_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    hunter_id = db.Column(db.BigInteger)
    position_id = db.Column(db.BigInteger, index=True)
    talent_id = db.Column(db.BigInteger, index=True)
    enterprise_id = db.Column(db.BigInteger)
    result_code = db.Column(db.Integer, info='验证结果')
    candidate_id = db.Column(db.BigInteger, index=True, server_default=db.FetchedValue(), info='当前职位、简历推荐成功之后的订单')
    defunct = db.Column(db.Integer, index=True)
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_user_id = db.Column(db.BigInteger)



class TbCandidateEvaluate(db.Model):
    __tablename__ = 'tb_candidate_evaluate'

    id = db.Column(db.BigInteger, primary_key=True, info='评论表主键')
    evaluatee_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='被评人id类型')
    evaluatee_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='被评人id')
    evaluater_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='评论人id类型')
    evaluater_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='评论人id')
    candidate_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='候选人id(订单id)')
    position_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职位id')
    option_ids = db.Column(db.String(500))
    content = db.Column(db.String(512), nullable=False, server_default=db.FetchedValue(), info='评价内容')
    phase = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='阶段(1.试前拒绝2.试后拒绝3.offer)')
    display = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否显示（0:不显示，1：显示）保留字段')
    anonymous = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否匿名（0:不匿名，1：匿名）保留字段')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除 0:未删除 1:已删除')
    candidate_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='评价订单来源类型（ho订单、onwork画像）')
    position_client_type = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='发布职位的客户端类型；1：旧版本hr，包括saas版本；2：新版本OnWork')



class TbCandidateEvaluateOption(db.Model):
    __tablename__ = 'tb_candidate_evaluate_option'

    id = db.Column(db.BigInteger, primary_key=True, info='评论表主键')
    rank = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='星数')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='类型（1.候选人质量2.猎头服务）')
    phase = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='阶段(1.试前拒绝2.试后拒绝3.offer)')
    arrived = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否到达：0未到达1到达')
    content = db.Column(db.String(200), server_default=db.FetchedValue(), info='选项内容')
    sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0.未删除，1.删除')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人id')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新人id')



class TbCandidateEvaluateRank(db.Model):
    __tablename__ = 'tb_candidate_evaluate_rank'
    __table_args__ = (
        db.Index('idx_evaluateid_defunct_type', 'evaluate_id', 'defunct', 'type'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='评论表主键')
    evaluate_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='评论id')
    candidate_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='候选人id')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='类型（1.候选人质量 2.猎头服务 3.猎上服务 4.HR服务）')
    rank = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='星数')
    evaluatee_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='被评人id类型')
    evaluatee_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='被评人id')
    create_time = db.Column(db.DateTime, nullable=False, index=True, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_time = db.Column(db.DateTime, nullable=False, index=True, info='更新时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除 0:未删除 1:已删除')



class TbCandidateGrab(db.Model):
    __tablename__ = 'tb_candidate_grab'
    __table_args__ = (
        db.Index('idx_candidateid_positionid', 'candidate_id', 'position_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    hr_id = db.Column(db.BigInteger, info='hr userId')
    candidate_id = db.Column(db.BigInteger, nullable=False, info='候选人ID')
    position_id = db.Column(db.BigInteger, nullable=False, info='原职位ID')
    new_position_id = db.Column(db.BigInteger, info='新职位ID')
    is_success = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0 未抢走，1 已被抢走')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='修改时间')



class TbCandidateGrabHistory(db.Model):
    __tablename__ = 'tb_candidate_grab_history'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    hr_id = db.Column(db.BigInteger, nullable=False, info='hr userId')
    candidate_id = db.Column(db.BigInteger, nullable=False, info='候选人ID')
    position_id = db.Column(db.BigInteger, nullable=False, info='职位ID')
    create_time = db.Column(db.DateTime, info='创建时间')



class TbCandidateHspRemind(db.Model):
    __tablename__ = 'tb_candidate_hsp_remind'

    candidate_id = db.Column(db.BigInteger, primary_key=True, info='订单ID')
    company_id = db.Column(db.BigInteger, nullable=False, index=True, info='猎企id')
    headhunter_id = db.Column(db.BigInteger, nullable=False, index=True, info='猎头id')
    status = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='0：未操作 1 申请 2 通过 3 拒绝')
    remind_time = db.Column(db.DateTime, index=True, info='提醒时间')
    has_remind = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='是否提醒')
    has_root_remind = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='是否提醒')
    is_roll_back = db.Column(db.Integer, server_default=db.FetchedValue(), info='猎享付是否回退；过保之后为申请，回退为普通订单')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建者')
    update_time = db.Column(db.DateTime, info='更新时间')
    update_user_id = db.Column(db.BigInteger, info='更新者')



class TbCandidateIndustryFunction(db.Model):
    __tablename__ = 'tb_candidate_industry_function'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    candidate_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='候选人id')
    industry_id = db.Column(db.BigInteger, info='行业ID')
    industry_name = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='行业名称')
    function_id = db.Column(db.BigInteger, info='职能ID')
    function_name = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='职能名称')
    create_time = db.Column(db.DateTime, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_time = db.Column(db.DateTime, info='更新时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否无效 -> 1 : true 已删除；0 : false 有效')



class TbCandidateLabel(db.Model):
    __tablename__ = 'tb_candidate_label'

    id = db.Column(db.BigInteger, primary_key=True)
    candidate_id = db.Column(db.BigInteger, nullable=False)
    label_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class TbCandidateLanguage(db.Model):
    __tablename__ = 'tb_candidate_language'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    candidate_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='候选人id')
    language_type_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='语言种类id')
    language_level_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='语言等级id')
    other_language = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='其他语言名称')



class TbCandidateLimitRule(db.Model):
    __tablename__ = 'tb_candidate_limit_rule'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    urgent_position_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0：普通职位 1：24小时紧急职位 2：48小时紧急职位')
    limit_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='上限数')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除 0:未删除 1:已删除')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')



class TbCandidateLog(db.Model):
    __tablename__ = 'tb_candidate_log'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='用户id')
    recommend_source = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='推荐来源。0:推荐时选择候选人产生的待办事项  1:一触而就中产生的待办事项   2:适合的职位产生的待办事项   3:适合的人才产生的待办事项  4:推荐时适合的人才产生的待办事项')
    position_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职位id')
    talent_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='人才id')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    candidate_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='候选人id')
    source_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='数据来源类型')
    position_source_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位数据来源类型')



class TbCandidateMatchPa(db.Model):
    __tablename__ = 'tb_candidate_match_pa'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    user_id = db.Column(db.BigInteger, index=True, server_default=db.FetchedValue(), info='paId')
    candidate_id = db.Column(db.BigInteger, index=True, server_default=db.FetchedValue(), info='订单Id')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='逻辑删除')
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue())



class TbCandidatePloy(db.Model):
    __tablename__ = 'tb_candidate_ploy'

    candidate_id = db.Column(db.BigInteger, primary_key=True, server_default=db.FetchedValue(), info='candidateId')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建者')
    update_time = db.Column(db.DateTime, info='更新时间')
    update_user_id = db.Column(db.BigInteger, info='更新者')
    hunteron_reward_type = db.Column(db.Integer, info='佣金类型（猎上设置）0：固定佣金   1：年薪百分比')
    hunteron_fixed_reward_amount = db.Column(db.Float(asdecimal=True), info='固定佣金（猎上设置）')
    hunteron_max_reward_amount = db.Column(db.Float(asdecimal=True), info='最高佣金（猎上设置）')
    hunteron_percentage = db.Column(db.Float(asdecimal=True), info='佣金比例（猎上设置）')
    hunteron_min_reward_amount = db.Column(db.Float(asdecimal=True), info='最小佣金（猎上设置）')
    is_micro = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否微简历版本推荐')
    position_talent_match_result = db.Column(db.String, info='职位、简历匹配结果json')
    position_attribute = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位属性 1 普通职位 2 RPO职位')
    hr_last_read_tab = db.Column(db.Integer, info='HR最后阅读TabCode')
    hr_last_read_tab_time = db.Column(db.DateTime, info='HR最后阅读Tab时间')
    hr_tips_ignore_tab_code = db.Column(db.Integer, server_default=db.FetchedValue(), info='HR忽略TipsTabCode')
    complaint = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否投诉 -> 1 : true 投诉；0 : false 不投诉')
    hr_default = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='是否无效 -> 1 : true 已删除；0 : false 有效')
    interview_no_arrived = db.Column(db.Integer, info='面试是否到达 -> 1 未到达；2 到达')
    position_no_arrived = db.Column(db.Integer, info='是否入职 -> 1 未入职；2 入职')
    talent_source = db.Column(db.Integer, info='简历来源')
    recommend_is_success = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否点击推荐成功 -> 1 : true 点击成功；0 : false 未点击成功')
    pay_rate_related_data_id = db.Column(db.BigInteger, info='分成比例计算相关的数据主键，例如标签ID')
    pay_rate_related_msg = db.Column(db.String(127), info='分成比例计算相关描述文本，例如标签名')
    pay_rate_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='对应订单佣金计算的类型；0：初始化类型，未知；100：到岗预付；200：到岗快；301：活动-简历宝；302：活动-指定职位分成比例；303：活动-28/37；401：平台标准；402：猎企自定义；500：top雇主和猎企关系')
    min_pay_rate_type = db.Column(db.Integer, info='分成比例下限，对应的类型')
    min_pay_rate = db.Column(db.Float(asdecimal=True), info='分成比例下限')
    out_enterprise_source = db.Column(db.Integer, info='外部订单来源，例如平安')
    out_candidate_id = db.Column(db.String(63), info='外部订单号')
    can_ying_yan_recommand = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否能使用鹰眼重推 1:true; 0:false')
    recommend_overdue = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='推荐逾期时间')
    interview_overdue = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='面试逾期时间')
    ai_screening_serial_number = db.Column(db.BigInteger, info='AI初筛流水号')
    redelivery = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否复投 0false 1true')
    position_client_type = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='发布职位的客户端类型；1：旧版本hr，包括saas版本；2：新版本OnWork')
    candidate_client_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='产生订单的所属客户端类型；1：旧版本hr，包括saas版本；2：新版本OnWork')
    last_operation_time = db.Column(db.DateTime, index=True, info='订单最后操作时间')
    process_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='订单的处理类型；0：常规订单；1：RPO职位订单')
    position_reward_display_rate = db.Column(db.Integer, info='订单生成时')
    position_reward_display_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='从职位计算过来的，显示比例类型；1：默认；2：预扣')
    src_percent = db.Column(db.Float(6, True), info='订单生成时，职位原始佣金比例，未乘以reward_display_rate')
    src_fixed_reward = db.Column(db.Float(10, True), info='订单生成时，职位原始固定佣金金额，未乘以reward_display_rate')
    src_month_salary_multiple = db.Column(db.Float(5, True), server_default=db.FetchedValue(), info='佣金类型为月薪倍数时，记录原始的月薪倍数')
    month_salary_multiple = db.Column(db.Float(5, True), server_default=db.FetchedValue(), info='佣金类型为月薪倍数时，记录比例计算之后的月薪倍数')
    guarantee_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='职位保证期类型；1：月数；2：天数')
    ps_recommend_feed_back_days = db.Column(db.Float(11, True), server_default=db.FetchedValue(), info='订单生成时，HR在推荐阶段预计反馈周期，单位：天')
    ps_interview_confirm_feed_back_days = db.Column(db.Float(11, True), server_default=db.FetchedValue(), info='订单生成时，HR在面试确认阶段预计反馈周期，单位：天')
    ps_interview_arrive_feed_back_days = db.Column(db.Float(11, True), server_default=db.FetchedValue(), info='订单生成时，HR在面试到达阶段预计反馈周期，单位：天')
    ps_interview_remind_feed_back_days = db.Column(db.Float(11, True), server_default=db.FetchedValue(), info='订单生成时，HR在面试待定阶段预计反馈周期，单位：天')
    need_feedback = db.Column(db.Integer, server_default=db.FetchedValue(), info='面试反馈 0:无需反馈 1:需反馈')
    commision_pay_rate = db.Column(db.Float(6, True), server_default=db.FetchedValue(), info='分佣的比例')
    commision_company_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='分佣收益猎头，0表示不分佣')
    position_owner_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='职位负责人类型；1：猎上运营；2：合伙人运营')
    virtual_position_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='虚拟职位类型；1：猎头职位；2：RPO职位')
    company_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='做单猎企类型；1：普通猎企；')
    candidate_progress_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='订单搜索状态分类 1:待支付；2:流程结束')
    position_assign_company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职位负责人猎企id')
    interview_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='订单是否有下一轮面试，默认有1；1：有下一轮；2：没有下一轮（终面通过）；3：offer')
    reward_version = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='佣金计算版本号；默认1；1：当前版本；2：合伙人佣金规则版本')
    reward_snapshot_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='合伙人佣金版本对应的快照ID')
    withhold_hunteron_rate = db.Column(db.Float(6, True), nullable=False, server_default=db.FetchedValue(), info='猎上作为平台的预扣百分比')
    withhold_enterprise_rate = db.Column(db.Float(6, True), nullable=False, server_default=db.FetchedValue(), info='预扣-雇主的比例')
    withhold_pa_operate_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='预扣-PA运营类型')
    withhold_bd_operate_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='预扣-BD运营类型')
    withhold_pa_company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='预扣-PA是合伙人的情况下，对应合伙人猎企ID')
    withhold_pa_rate = db.Column(db.Float(6, True), nullable=False, server_default=db.FetchedValue(), info='预扣-PA是合伙人，对应预扣百分比')
    withhold_bd_company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='预扣-BD是合伙人的情况下，对应合伙人猎企ID')
    withhold_bd_rate = db.Column(db.Float(6, True), nullable=False, server_default=db.FetchedValue(), info='预扣-BD是合伙人，对应预扣百分比')
    commission_enterprise_rate = db.Column(db.Float(6, True), nullable=False, server_default=db.FetchedValue(), info='分佣-雇主的比例')
    commission_pa_operate_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='分佣-PA运营类型')
    commission_bd_operate_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='分佣-BD运营类型')
    commission_pa_company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='分佣-PA是合伙人的情况下，对应合伙人猎企ID；这是职位当前的PA信息')
    commission_pa_rate = db.Column(db.Float(6, True), nullable=False, server_default=db.FetchedValue(), info='分佣-PA是合伙人，对应分佣百分比')
    commission_bd_company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='分佣-BD是合伙人的情况下，对应合伙人猎企ID；这是职位当前的BD信息')
    commission_bd_rate = db.Column(db.Float(2, True), nullable=False, server_default=db.FetchedValue(), info='分佣-BD是合伙人，对应分佣百分比')
    salary_rule_month = db.Column(db.Integer, server_default=db.FetchedValue(), info='成单时职位的月薪数量')
    receipt_reward = db.Column(db.Float(12, True), server_default=db.FetchedValue(), info='收款-订单实际收款佣金')
    receipt_percent = db.Column(db.Float(6, True), server_default=db.FetchedValue(), info='收款-收款方向的实际比例')
    receipt_month_multiple = db.Column(db.Float(6, True), server_default=db.FetchedValue(), info='收款-收款方向的月薪倍数')
    receipt_pa_rate = db.Column(db.Float(6, True), server_default=db.FetchedValue(), info='先结-pa的分佣比例')
    receipt_bd_rate = db.Column(db.Float(6, True), server_default=db.FetchedValue(), info='先结-bd的分佣比例')
    settle_mode_pa = db.Column(db.Integer, server_default=db.FetchedValue(), info='合伙人pa的结算方式；1：先结；2：后结')
    settle_mode_bd = db.Column(db.Integer, server_default=db.FetchedValue(), info='合伙人bd的结算方式；1：先结；2：后结')



class TbCandidateRecommandReport(db.Model):
    __tablename__ = 'tb_candidate_recommand_report'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    candidate_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='候选人id')
    talent_recommand_report_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='人才推荐报告id')
    title = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='推荐报告名称')
    reason = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='推荐理由')
    motivation = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='求职动机')
    dimission_time = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='离职时间')
    current_annual_salary_desc = db.Column(db.String(600), nullable=False, server_default=db.FetchedValue(), info='当前年薪描述')
    expect_annual_salary_desc = db.Column(db.String(600), nullable=False, server_default=db.FetchedValue(), info='期望年薪描述')
    expect_annual_salary_new = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='期望年薪新字段:-1：面议')
    expect_interview_time = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='期望面试时间')
    create_time = db.Column(db.DateTime, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_time = db.Column(db.DateTime, info='更新时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否无效 -> 1 : true 已删除；0 : false 有效')
    other_welfare = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='其他福利')
    current_salary = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='当前月薪')
    current_salary_months = db.Column(db.Float, nullable=False, server_default=db.FetchedValue(), info='当前月薪月数')
    current_annual_salary = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='当前年薪')
    expect_salary = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='期望月薪')
    expect_salary_months = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='期望月薪月数')
    expect_annual_salary = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='期望年薪')
    salary_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='年薪类型：0税前，1税后')
    other_require = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue(), info='其他要求')
    communication_time = db.Column(db.DateTime, info='人才沟通时间')
    expect_salary_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='期望薪资税收类型,0:税前,1:税后')



class TbCandidateRemind(db.Model):
    __tablename__ = 'tb_candidate_remind'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    candidate_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='候选人ID')
    remind_from_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='候选人当前状态')
    remind_to_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='候选人目标状态')
    feedback = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否反馈;0:未反馈;1:反馈')
    feedback_time = db.Column(db.DateTime, info='反馈时间')
    hr_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    crm_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    hh_remark = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue())
    crm_remark = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbCandidateScene(db.Model):
    __tablename__ = 'tb_candidate_scene'

    candidate_id = db.Column(db.BigInteger, primary_key=True, info='candidateId')
    client_type = db.Column(db.Integer, info='客户端类型')
    scene_type = db.Column(db.Integer, info='场景类型')
    scene_code = db.Column(db.String(128), info='场景Code')
    scene_page_code = db.Column(db.String(255), info='场景页面Code')
    scene_source_code = db.Column(db.String(255), info='创建时间场景来源Code')
    first_scene_type = db.Column(db.Integer, info='首次场景类型')
    first_scene_code = db.Column(db.String(128), info='首次场景Code')
    first_scene_source_code = db.Column(db.String(255), info='首次场景来源Code')
    position_special_id = db.Column(db.BigInteger, info='职位专场ID')
    first_client_type = db.Column(db.Integer, info='首次客户端类型')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='修改时间')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    update_user_id = db.Column(db.BigInteger, info='修改人')



class TbCandidateTagDic(db.Model):
    __tablename__ = 'tb_candidate_tag_dic'

    id = db.Column(db.BigInteger, primary_key=True, info='主键，系统生成')
    tag_rule_key = db.Column(db.String(63), nullable=False, index=True, server_default=db.FetchedValue(), info='标签code，不可重复；主要用于系统预定义标签与规则代码对应；人工标签则没什么意义')
    inner_name = db.Column(db.String(31), nullable=False, info='标签的内部显示名称；可重复')
    hh_display_name = db.Column(db.String(31), info='标签的HH端显示名称，可重复，展示前去重复')
    tdc_display_name = db.Column(db.String(31), info='TDC端显示名称')
    show_message = db.Column(db.String(255), info='弹窗提示文案')
    tag_type = db.Column(db.Integer, info='标签类型；1 系统标签：预定义，不可选择；2 人工标签：人工打标签使用；3 系统定义人工打标签')
    pay_rate = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='分成比例')
    start_time = db.Column(db.DateTime, info='标签有效时间的开始时间，可以为空，表示立即生效；')
    end_time = db.Column(db.DateTime, info='标签有效时间的结束时间，可以为空，表示不限时；')
    priority = db.Column(db.Integer, server_default=db.FetchedValue(), info='标签优先级，也就是排序值，越大越靠前')
    is_mutex = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否互斥；互斥的标签，只展示优先级最高的；职位中有一个是互斥标签，则不展示其它标签')
    is_filter = db.Column(db.Integer, server_default=db.FetchedValue(), info='所有标签在职位搜索都可以搜索；这个标记为是否展示给HH用户')
    is_hh_display = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否在HH端职位上展示这个标签')
    is_tdc_dispaly = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否在TDC端职位上展示这个标签')
    tag_style = db.Column(db.String(31), info='标签样式class')
    tag_rule_json = db.Column(db.String(1023), info='标签规则json')
    mutex_calculate_tags = db.Column(db.String(255), info='互斥可计算标签，为空则互斥所有')
    calculate_type = db.Column(db.Integer, info='标签计算类型：1：按天；2：实时')
    defunct = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='逻辑删除')
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_user_id = db.Column(db.BigInteger)



class TbCandidateTagRelation(db.Model):
    __tablename__ = 'tb_candidate_tag_relation'

    id = db.Column(db.BigInteger, primary_key=True)
    company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='公司ID')
    tag_id = db.Column(db.BigInteger, nullable=False, info='标签ID')
    candidate_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='订单ID')
    talent_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='冗余人才ID')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除')
    create_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    calculate_type = db.Column(db.Integer, info='从tb_candidate_tag_dic表冗余过来')
    tag_type = db.Column(db.Integer, info='从标签表冗余过来的字段')
    start_time = db.Column(db.DateTime, info='具体在职位上的有效时间开始')
    end_time = db.Column(db.DateTime, info='标签在职位上的有效时间的结束时间')
    show_message = db.Column(db.String(255), info='标签文案，部分职位的文案跟职位信息相关')



class TbCandidateTrackRecord(db.Model):
    __tablename__ = 'tb_candidate_track_record'

    id = db.Column(db.BigInteger, primary_key=True)
    candidate_id = db.Column(db.BigInteger, nullable=False, index=True, info='订单号，candidate表主键')
    position_project_id = db.Column(db.BigInteger, nullable=False, index=True, info='职位项目表主键')
    position_id = db.Column(db.BigInteger, nullable=False, info='冗余的职位ID')
    hunter_id = db.Column(db.BigInteger, nullable=False, info='当时做单的猎头ID')
    hunter_company_id = db.Column(db.BigInteger, nullable=False, info='猎企ID')
    project_owner_id = db.Column(db.BigInteger, nullable=False, info='订单生成是职位项目的Owner')
    candidate_time = db.Column(db.DateTime, nullable=False, info='订单创建时间')
    create_time = db.Column(db.DateTime, nullable=False, info='数据创建时间')



class TbCandidateTransferLog(db.Model):
    __tablename__ = 'tb_candidate_transfer_log'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    candidate_id = db.Column(db.BigInteger, nullable=False, index=True, info='候选人订单')
    last_position_id = db.Column(db.BigInteger, info='上次推荐岗位')
    last_recomend_time = db.Column(db.DateTime)
    transfer_time = db.Column(db.DateTime)
    new_position_id = db.Column(db.BigInteger, info='本次新岗位Id')
    create_user_id = db.Column(db.BigInteger, info='操作人')



class TbCandidateUndeterminedReason(db.Model):
    __tablename__ = 'tb_candidate_undetermined_reason'

    id = db.Column(db.Integer, primary_key=True, info='主键ID')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0:简历待定，1:面试待定')
    user_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    content = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='选项内容')
    sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0未删除，1 删除')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人id')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新人id')



class TbCard(db.Model):
    __tablename__ = 'tb_card'

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='名片对应的用户id')
    user_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1:企业用户,2:猎头用户,3:管理员用户,4:渠道用户,5:求职者用户,6:猎大用户;参考com.hunteron.api.user.bean.v2.UserType')
    remote_path = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='名片对应的URL')
    card_data = db.Column(db.Text, nullable=False, info='名片内容')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    create_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())



class TbCertainly(db.Model):
    __tablename__ = 'tb_certainly'

    user_id = db.Column(db.BigInteger, primary_key=True, info='用户编号')
    is_use = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否使用 -> 1 : true 已删除；0 : false 有效')
    refresh_time = db.Column(db.DateTime, info='刷新时间')
    expire_time = db.Column(db.DateTime, info='到期时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbCollect(db.Model):
    __tablename__ = 'tb_collect'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    obj_id = db.Column(db.BigInteger, nullable=False, info='收藏的对象id')
    obj_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='对象类型')
    collect_user_id = db.Column(db.BigInteger, nullable=False, info='收藏人id')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbCollectTag(db.Model):
    __tablename__ = 'tb_collect_tags'

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, nullable=False, index=True, info='操作人id')
    obj_id = db.Column(db.BigInteger, nullable=False, index=True, info='对象id')
    obj_type = db.Column(db.Integer, nullable=False, info='对象类型')
    experienced_areas = db.Column(db.String(64), info='擅长区域')
    experienced_industries = db.Column(db.String(64), info='擅长行业')
    experienced_position_skills = db.Column(db.String(64), info='擅长职能')
    experienced_position_levels = db.Column(db.String(64), info='擅长职级')
    experienced_companies = db.Column(db.String(512), info='擅长公司')
    custom_tags = db.Column(db.String(512), info='自定义标签')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue(), info='更新时间')



class TbCompanyAccount(db.Model):
    __tablename__ = 'tb_company_account'

    company_id = db.Column(db.BigInteger, primary_key=True, info='猎企ID')
    account_balance = db.Column(db.Numeric(11, 2), server_default=db.FetchedValue(), info='账户余额')
    invoice_title = db.Column(db.String(100), info='工商名称')
    invoice_ein = db.Column(db.String(50), info='税号')
    invoice_province = db.Column(db.Integer, info='发票-省')
    invoice_city = db.Column(db.Integer, info='发票-市')
    invoice_address = db.Column(db.String(200), info='发票-详细地址')
    invoice_phone = db.Column(db.String(20), info='发票-联系电话')
    opening_bank = db.Column(db.String(50), info='开户行')
    bank_card_no = db.Column(db.String(30), info='银行账号')
    receipt_name = db.Column(db.String(50), info='收件人姓名')
    receipt_phone = db.Column(db.String(20), info='收件人电话')
    receipt_province = db.Column(db.Integer, info='收件人-省')
    receipt_city = db.Column(db.Integer, info='收件人-市')
    receipt_address = db.Column(db.String(200), info='收件人-详细地址')
    status_no = db.Column(db.Integer, info='状态')
    audit_user_id = db.Column(db.BigInteger, info='审核用户ID')
    audit_time = db.Column(db.DateTime, info='最后审核时间')
    audit_fail_reason = db.Column(db.String(500), info='审核失败原因')
    update_user_id = db.Column(db.BigInteger, info='修改人')
    update_time = db.Column(db.DateTime, info='修改时间')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    create_time = db.Column(db.DateTime, info='创建时间')



class TbCompanyAccountChange(db.Model):
    __tablename__ = 'tb_company_account_change'

    id = db.Column(db.BigInteger, primary_key=True)
    company_id = db.Column(db.BigInteger, nullable=False, info='猎企ID')
    invoice_title = db.Column(db.String(100), info='工商名称')
    invoice_ein = db.Column(db.String(50), info='税号')
    invoice_province = db.Column(db.Integer, info='发票-省')
    invoice_city = db.Column(db.Integer, info='发票-市')
    invoice_address = db.Column(db.String(200), info='发票-详细地址')
    invoice_phone = db.Column(db.String(20), info='发票-联系电话')
    opening_bank = db.Column(db.String(50), info='开户行')
    bank_card_no = db.Column(db.String(30), info='银行账号')
    receipt_name = db.Column(db.String(50), info='收件人姓名')
    receipt_phone = db.Column(db.String(20), info='收件人电话')
    receipt_province = db.Column(db.Integer, info='收件人-省')
    receipt_city = db.Column(db.Integer, info='收件人-市')
    receipt_address = db.Column(db.String(200), info='收件人-详细地址')
    status_no = db.Column(db.Integer, info='状态')
    update_user_id = db.Column(db.BigInteger, info='修改人')
    update_time = db.Column(db.DateTime, info='修改时间')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    create_time = db.Column(db.DateTime, info='创建时间')



class TbCompanyActiveApply(db.Model):
    __tablename__ = 'tb_company_active_apply'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='企业id ')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='更新者')
    update_time = db.Column(db.DateTime, info='更新时间')
    status = db.Column(db.Integer, nullable=False, info='申请状态')
    active_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='活动类型1：可用，2：不可用')
    apply_date = db.Column(db.DateTime, nullable=False, info='申请时间')



class TbCompanyCooperationApply(db.Model):
    __tablename__ = 'tb_company_cooperation_apply'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    company_name = db.Column(db.String(128), index=True, info='公司名称')
    company_corporate_name = db.Column(db.String(64), index=True, info='公司法人姓名')
    company_connection_name = db.Column(db.String(64), index=True, info='公司对接人')
    company_connection_position_title = db.Column(db.String(256), info='公司对接人职位名称')
    company_connection_mobile = db.Column(db.String(64), index=True, info='公司对接人手机号码')
    company_industry_id = db.Column(db.String(256), info='行业')
    company_function_id = db.Column(db.String(256), info='职能')
    adept_customer = db.Column(db.String(256), info='擅长客户')
    recently_oder_position_title = db.Column(db.String(256), info='最近成单职位')
    adept_city_id = db.Column(db.String(256), info='擅长城市ID')
    adept_position_commission = db.Column(db.String(256), info='擅长职位佣金')
    headhunter_city_id = db.Column(db.String(256), info='顾问所在城市ID')
    corporate_headhunter_count = db.Column(db.Integer, info='意向合作猎头数')
    expect_corporate_customer_name = db.Column(db.String(256), info='期望合作客户名称')
    defunct = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='是否删除0:false 1:true')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='修改时间')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    update_user_id = db.Column(db.BigInteger, info='修改人')



class TbCompanyGrade(db.Model):
    __tablename__ = 'tb_company_grade'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    company_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='企业编号')
    grade = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='当前等级')
    interview_rate = db.Column(db.Float(asdecimal=True), info='面试率')
    recommand_quality = db.Column(db.Float(asdecimal=True), info='推荐质量')
    service_quality = db.Column(db.Float(asdecimal=True), info='服务质量')
    hunter_total = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='猎头数')
    grade_category_value = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='等级分类值json')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbCompanyInviteCode(db.Model):
    __tablename__ = 'tb_company_invite_code'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='公司ID')
    invite_code = db.Column(db.String(63), nullable=False, server_default=db.FetchedValue(), info='邀请码')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='操作人ID')
    effective_time = db.Column(db.DateTime, nullable=False)
    expired_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())



class TbCompanyInviteUser(db.Model):
    __tablename__ = 'tb_company_invite_user'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='公司ID')
    invite_code = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue(), info='邀请码')
    invitee_email = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='被邀请人邮箱')
    invited_hh_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='被邀请猎头ID')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1未注册 3已拒绝 2已失效 4成功')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='操作人ID')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbCompanyOnboardPayWhite(db.Model):
    __tablename__ = 'tb_company_onboard_pay_white'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎企id')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除,0:false,1:true')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建者')
    update_time = db.Column(db.DateTime, nullable=False, info='更新者')



class TbCompanyPloy(db.Model):
    __tablename__ = 'tb_company_ploy'

    company_id = db.Column(db.BigInteger, primary_key=True, info='雇主/猎企id')
    type = db.Column(db.Integer, info='类型；1：雇主；2：猎企')
    first_login_time = db.Column(db.DateTime, info='从null之后，第一次登录')
    first_login_user_id = db.Column(db.BigInteger, info='从null之后，第一次登录的用户')
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    cooperation_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='合作类型 0:平台猎企 1：特殊猎企')
    offline_pay_rate_rule = db.Column(db.String(255), info='分成比例规则json')
    offline_pay_rate = db.Column(db.Float(asdecimal=True), server_default=db.FetchedValue(), info='特殊猎企分成比例')
    offline_pay_deadline = db.Column(db.Integer, info='支付期限')
    offline_pay_type = db.Column(db.Integer, info='支付类型；1:背靠背；2：过保付')
    offline_earnest_money = db.Column(db.Float(asdecimal=True), info='保证金')
    offline_kpi_content = db.Column(db.String(255), info='kpi说明')
    partner_to_self_pay_rate = db.Column(db.Float(asdecimal=True), server_default=db.FetchedValue(), info='合伙人做自己职位分成比例')
    partner_to_ho_pay_rate = db.Column(db.Float(asdecimal=True), server_default=db.FetchedValue(), info='合伙人做猎上职位分成比例')
    partner_to_general_pay_rate = db.Column(db.Float(asdecimal=True), server_default=db.FetchedValue(), info='做合伙人职位（与猎上分佣的比例）')
    pa_proportion = db.Column(db.Float(6, True), nullable=False, server_default=db.FetchedValue(), info='PA分成比例')
    bd_proportion = db.Column(db.Float(6, True), nullable=False, server_default=db.FetchedValue(), info='BD分成比例')
    partner_switch = db.Column(db.Integer, server_default=db.FetchedValue(), info='合伙人开关')
    is_acn = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否是acn')
    settle_mode = db.Column(db.Integer, server_default=db.FetchedValue(), info='结算模式；1：先结；2：后结')



class TbCompanyRegisterInfo(db.Model):
    __tablename__ = 'tb_company_register_info'

    company_id = db.Column(db.BigInteger, primary_key=True, info='公司id')
    source = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='注册来源')
    create_user_id = db.Column(db.BigInteger, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False)
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)



class TbCompanyRewardConfig(db.Model):
    __tablename__ = 'tb_company_reward_config'

    id = db.Column(db.BigInteger, primary_key=True)
    rule_json = db.Column(db.String(2047), info='规则内容json')
    company_id = db.Column(db.BigInteger, index=True, info='猎企id')
    update_user_id = db.Column(db.BigInteger, info='更新的用户')
    update_time = db.Column(db.DateTime)



class TbCompanyRewardConfigSnapshot(db.Model):
    __tablename__ = 'tb_company_reward_config_snapshot'
    __table_args__ = (
        db.Index('operate_time_companyId', 'company_id', 'operate_time'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    company_id = db.Column(db.BigInteger)
    rule_json = db.Column(db.String(2047), info='规则内容')
    rule_data_time = db.Column(db.DateTime, info='当时保存这条规则的时间')
    rule_user_id = db.Column(db.BigInteger, info='当时保存这条规则的用户')
    operate_user_id = db.Column(db.BigInteger)
    operate_time = db.Column(db.DateTime)



class TbCompanySetting(db.Model):
    __tablename__ = 'tb_company_settings'

    company_id = db.Column(db.BigInteger, primary_key=True, info='公司id')
    talent_follow_limit = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='一个人才允许跟进的猎头上限')
    talent_follow_period = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='人才跟进周期(天)')
    is_public_talent_contact = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否公开被跟进人才的联系方式')
    max_position_project_total = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='最大职位项目组数量')
    create_user_id = db.Column(db.BigInteger, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False)
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)



class TbCompanyTalentTag(db.Model):
    __tablename__ = 'tb_company_talent_tag'

    id = db.Column(db.BigInteger, primary_key=True)
    company_id = db.Column(db.BigInteger, nullable=False, info='公司ID')
    name = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='标签名字')
    first_letter = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue(), info='首字母')
    phonetic = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='拼音')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除')
    create_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())



class TbCompanyUniqueCode(db.Model):
    __tablename__ = 'tb_company_unique_code'

    id = db.Column(db.BigInteger, primary_key=True)
    unique_code = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue(), info='口令')
    company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    status = db.Column(db.Integer, server_default=db.FetchedValue(), info='0:未使用,1:使用中,2:已失效')
    effective_time = db.Column(db.DateTime, info='生效时间')
    expired_time = db.Column(db.DateTime, info='过期时间')
    operator_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='操作人ID')
    company_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='公司类型1:猎企,2:雇主')



class TbComplaint(db.Model):
    __tablename__ = 'tb_complaint'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    source = db.Column(db.Integer, server_default=db.FetchedValue(), info='投诉渠道')
    candidate_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='候选人id')
    pa_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='PAID')
    em_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='EMID')
    handle_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='处理人id')
    complainant_user_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='投诉人类型')
    complainant_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='投诉人id')
    defendant_user_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='被告人类型')
    defendant_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='被告人id')
    option_ids = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='投诉选项')
    complain = db.Column(db.String(255), server_default=db.FetchedValue(), info='投诉内容')
    handle = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否处理')
    handle_result = db.Column(db.String(255), server_default=db.FetchedValue(), info='处理结果')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0未删除，1 删除')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    attachment = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='附件')
    handle_time = db.Column(db.DateTime, nullable=False, info='处理时间')



class TbComplaintOption(db.Model):
    __tablename__ = 'tb_complaint_option'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    source = db.Column(db.Integer, server_default=db.FetchedValue(), info='投诉渠道')
    content = db.Column(db.String(255), info='投诉选项')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0未删除，1 删除')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbComplaintOptionBak20160223(db.Model):
    __tablename__ = 'tb_complaint_option_bak20160223'

    id = db.Column(db.BigInteger, primary_key=True)
    source = db.Column(db.Integer, server_default=db.FetchedValue(), info='投诉渠道')
    content = db.Column(db.String(255), info='投诉选项')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0未删除，1 删除')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)



class TbCooperationInquiry(db.Model):
    __tablename__ = 'tb_cooperation_inquiry'

    id = db.Column(db.BigInteger, primary_key=True, info='预审编号')
    cooperation_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='合作编号')
    school = db.Column(db.String(50), info='学校')
    degree_id = db.Column(db.Integer, info='学历')
    city_id = db.Column(db.BigInteger, info='所属地区')
    work_year = db.Column(db.Integer, info='工作年份')
    company_name = db.Column(db.String(200), info='所属公司')
    position_title = db.Column(db.String(200), info='当前职位')
    project_description = db.Column(db.Text, info='项目描述')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='预审状态0：新建；1：已审核；2:已删除')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='跟新人')



class TbCorrelationEnterprise(db.Model):
    __tablename__ = 'tb_correlation_enterprise'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    enterprise_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='企业编号')
    advert_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='广告名称')
    web_logo_path = db.Column(db.String(200), info='web端Logo')
    mobile_logo_path = db.Column(db.String(200), info='手机端Logo')
    page_link = db.Column(db.String(200), server_default=db.FetchedValue(), info='链接地址')
    location = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='放置位置')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除0false 1true')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')



class TbCorrelationInsideEnterprise(db.Model):
    __tablename__ = 'tb_correlation_inside_enterprise'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    enterprise_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='企业编号')
    correlation_enterprise_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='关联企业编号')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbCouponEnterprise(db.Model):
    __tablename__ = 'tb_coupon_enterprise'
    __table_args__ = (
        db.Index('idx_enterpriseid_status', 'enterprise_id', 'status'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    serial_number = db.Column(db.String(40), nullable=False, unique=True, server_default=db.FetchedValue())
    coupon_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    enterprise_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    value = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    valid_date_start = db.Column(db.DateTime, nullable=False)
    valid_date_end = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0未激活1未使用2已使用3已抵扣')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbCouponUsage(db.Model):
    __tablename__ = 'tb_coupon_usage'
    __table_args__ = (
        db.Index('idx_type_target_id', 'type', 'target_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    target_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    serial_number = db.Column(db.String(40), nullable=False, index=True, server_default=db.FetchedValue())
    coupon_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    enterprise_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    value = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0:使用中1:使用成功2:使用失败3:系统返还')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbCredit(db.Model):
    __tablename__ = 'tb_credits'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    headhunter_id = db.Column(db.BigInteger, index=True, server_default=db.FetchedValue(), info='猎头id')
    headhunter_company_id = db.Column(db.BigInteger, index=True, server_default=db.FetchedValue(), info='猎头所在的公司id')
    credit = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='积分')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='逻辑删除')
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue())



class TbCreditsBk20200731(db.Model):
    __tablename__ = 'tb_credits_bk20200731'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    headhunter_id = db.Column(db.BigInteger, index=True, server_default=db.FetchedValue(), info='猎头id')
    headhunter_company_id = db.Column(db.BigInteger, index=True, server_default=db.FetchedValue(), info='猎头所在的公司id')
    credit = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='积分')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='逻辑删除')
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue())



class TbCreditsDetail(db.Model):
    __tablename__ = 'tb_credits_detail'
    __table_args__ = (
        db.Index('conbain2', 'defunct', 'type', 'soure_type', 'obj_type', 'obj_id'),
        db.Index('conbain1', 'defunct', 'exchange_type', 'exchange_id')
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    headhunter_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='猎头id')
    headhunter_company_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='猎头所在的公司id')
    type = db.Column(db.Integer, server_default=db.FetchedValue(), info='积分增减方式;1:增加;2减少')
    soure_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='积分来源类型;1兑换; 2中奖;3登录;4上传简历;5:推荐;6面试确认;7面试通过;8:offer')
    exchange_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='1：兑换，对应tb_credits_product；2：抽奖中奖，对应tb_activity_lottery_prize')
    exchange_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='对应type的表的主键')
    exchang_number = db.Column(db.String(200), info='兑换编号')
    credit = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='积分')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='逻辑删除')
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime, index=True, server_default=db.FetchedValue(), info='兑换时间')
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    obj_type = db.Column(db.String(20), info='引用类型')
    obj_id = db.Column(db.BigInteger, info='引用ID')



class TbCreditsDetailAddres(db.Model):
    __tablename__ = 'tb_credits_detail_address'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    headhunter_id = db.Column(db.BigInteger, index=True, server_default=db.FetchedValue(), info='猎头id')
    headhunter_company_id = db.Column(db.BigInteger, index=True, server_default=db.FetchedValue(), info='猎头所在的公司id')
    credits_detail_id = db.Column(db.BigInteger, index=True, server_default=db.FetchedValue(), info='积分详情ID')
    contact = db.Column(db.String(200), info='联系人名称')
    contact_phone = db.Column(db.String(20), info='联系人电话')
    contact_email = db.Column(db.String(63), info='联系人邮箱')
    contact_wx = db.Column(db.String(63), info='联系人微信号')
    province_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='省份ID')
    city_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='城市ID')
    detail = db.Column(db.String(200), info='详细地址')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='逻辑删除')
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue())



class TbCreditsDetailAddressBk20200731(db.Model):
    __tablename__ = 'tb_credits_detail_address_bk20200731'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    headhunter_id = db.Column(db.BigInteger, index=True, server_default=db.FetchedValue(), info='猎头id')
    headhunter_company_id = db.Column(db.BigInteger, index=True, server_default=db.FetchedValue(), info='猎头所在的公司id')
    credits_detail_id = db.Column(db.BigInteger, index=True, server_default=db.FetchedValue(), info='积分详情ID')
    contact = db.Column(db.String(200), info='联系人名称')
    contact_phone = db.Column(db.String(20), info='联系人电话')
    contact_wx = db.Column(db.String(63), info='联系人微信号')
    province_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='省份ID')
    city_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='城市ID')
    detail = db.Column(db.String(200), info='详细地址')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='逻辑删除')
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue())



class TbCreditsDetailBk20200731(db.Model):
    __tablename__ = 'tb_credits_detail_bk20200731'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    headhunter_id = db.Column(db.BigInteger, index=True, server_default=db.FetchedValue(), info='猎头id')
    headhunter_company_id = db.Column(db.BigInteger, index=True, server_default=db.FetchedValue(), info='猎头所在的公司id')
    type = db.Column(db.Integer, server_default=db.FetchedValue(), info='积分增减方式;1:增加;2减少')
    soure_type = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='积分来源类型;1兑换; 2中奖;3登录;4上传简历;5:推荐;6面试确认;7面试通过;8:offer')
    exchange_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='1：兑换，对应tb_credits_product；2：抽奖中奖，对应tb_activity_lottery_prize')
    exchange_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='对应type的表的主键')
    exchang_number = db.Column(db.String(200), info='兑换编号')
    credit = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='积分')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='逻辑删除')
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue(), info='兑换时间')
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    obj_type = db.Column(db.String(20), info='引用类型')
    obj_id = db.Column(db.BigInteger, info='引用ID')



class TbCreditsProduct(db.Model):
    __tablename__ = 'tb_credits_product'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    name = db.Column(db.String(200), nullable=False, info='商品名称')
    type = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='商品类型编号')
    number = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='商品总数')
    number_on_hunter = db.Column(db.Integer, info='猎头兑换上限')
    number_type = db.Column(db.Integer, info='猎头兑换上限、商品总数对应的时间线类型；（1：天；2：自然周；3：自然月；4：自然季度；5：半年度；6：年度）')
    number_on_type_on_hunter = db.Column(db.Integer, info='猎头在类型上的兑换上限；同一个type的所有数据该数值一致；只需取一条数据的即可')
    credit = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='兑换商品需要的积分')
    start_time = db.Column(db.DateTime, info='商品有效期开始')
    end_time = db.Column(db.DateTime, info='商品有效期结束')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='逻辑删除')
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue())



class TbCreditsProductBk20200731(db.Model):
    __tablename__ = 'tb_credits_product_bk20200731'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    name = db.Column(db.String(200), nullable=False, info='商品名称')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='商品类型编号')
    number = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='商品总数')
    number_type = db.Column(db.Integer, info='猎头兑换上限、商品总数对应的时间线类型；（1：天；2：自然周；3：自然月；4：自然季度；5：半年度；6：年度）')
    number_on_hunter = db.Column(db.Integer, info='猎头兑换上限')
    credit = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='兑换商品需要的积分')
    start_time = db.Column(db.DateTime, info='商品有效期开始')
    end_time = db.Column(db.DateTime, info='商品有效期结束')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='逻辑删除')
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue())



class TbCustomPositionReward(db.Model):
    __tablename__ = 'tb_custom_position_reward'

    id = db.Column(db.BigInteger, primary_key=True)
    enterprise_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    title = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    expression = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue())
    description = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue())



class TbCustomerRelationship(db.Model):
    __tablename__ = 'tb_customer_relationship'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    enterprise_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='企业id')
    company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='公司id')
    top = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否top')
    ka = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否ka猎头')
    create_time = db.Column(db.DateTime, info='创建时间')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建者')
    update_time = db.Column(db.DateTime, info='更新时间')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='更新者')



class TbDefaultSearch(db.Model):
    __tablename__ = 'tb_default_search'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='类型')
    appType = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='App类型')
    word = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='搜索词')
    description = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='描述')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否无效 -> 1 : true 已删除；0 : false 有效')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbDfwUser(db.Model):
    __tablename__ = 'tb_dfw_user'

    id = db.Column(db.BigInteger, primary_key=True, info='主键，系统生成')
    activity_lottery_id = db.Column(db.BigInteger, nullable=False, index=True, info='抽奖活动ID')
    user_id = db.Column(db.BigInteger, nullable=False, index=True, info='用户ID')
    location = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='位置 默认 0 即开始位置')
    lottery_ticket = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='奖券数量')
    round_number = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='轮数 默认1')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='是否删除0false 1true')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbDfwUserLog(db.Model):
    __tablename__ = 'tb_dfw_user_log'

    id = db.Column(db.BigInteger, primary_key=True, info='主键，系统生成')
    activity_lottery_id = db.Column(db.BigInteger, nullable=False, index=True, info='抽奖活动ID')
    user_id = db.Column(db.BigInteger, nullable=False, index=True, info='用户ID')
    dice = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='骰子 默认1 ')
    location_content = db.Column(db.String(256), info='位置内容')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='是否删除0false 1true')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbDictionary(db.Model):
    __tablename__ = 'tb_dictionary'

    id = db.Column(db.BigInteger, primary_key=True)
    dic_no = db.Column(db.BigInteger, nullable=False, info='字典编号')
    dic_name = db.Column(db.String(200), nullable=False, info='字典名称')
    dic_remark = db.Column(db.String(200), info='字典备注')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除 0:false 1:true')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)



class TbDictionaryItem(db.Model):
    __tablename__ = 'tb_dictionary_item'

    id = db.Column(db.BigInteger, primary_key=True)
    dic_id = db.Column(db.BigInteger, nullable=False, info='字典主键')
    dic_key = db.Column(db.Integer, nullable=False, info='字典项键')
    dic_value = db.Column(db.String(200), nullable=False, info='字典项值')
    dic_remark = db.Column(db.String(200), info='字典项说明')
    dic_sort_no = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='字典项顺序')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除 0:false 1:true')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)



class TbElcCompanyAccount(db.Model):
    __tablename__ = 'tb_elc_company_account'
    __table_args__ = (
        db.Index('company_id_type', 'company_id', 'type'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    open_id = db.Column(db.String(63), nullable=False)
    company_id = db.Column(db.BigInteger, nullable=False, info='企业ID')
    type = db.Column(db.Integer, nullable=False, info='企业类型；1：雇主；2：猎企')
    customer_id = db.Column(db.String(63), info='法大大未企业账户提供的标识')
    signature_id = db.Column(db.String(63))
    contract_source = db.Column(db.Integer, info='企业选择合同类型；1：猎上合同模板；2：雇主自己的合同')
    evidence_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='存证方案；1：法大大实名存证；2：猎上存证后将文件hash256编码传给法大大')
    ca_flag = db.Column(db.Integer, info='是否已完成实名证书申请；1：已申请，0：未申请')
    contract_status = db.Column(db.Integer, server_default=db.FetchedValue(), info='合同状态；0：未签署；1：签署中；2：已签署、有效；3：已过期')
    defunct = db.Column(db.Integer)
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)



class TbElcCompanyContract(db.Model):
    __tablename__ = 'tb_elc_company_contracts'

    id = db.Column(db.BigInteger, primary_key=True)
    account_id = db.Column(db.BigInteger, index=True, info='tb_elc_company_account表主键')
    file_name = db.Column(db.String(255))
    contract_title = db.Column(db.String(255))
    contract_key = db.Column(db.String(127), info='企业自己合同上传到阿里云的key')
    defunct = db.Column(db.Integer)
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)



class TbElcCompanyVerifyInfo(db.Model):
    __tablename__ = 'tb_elc_company_verify_info'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    elc_account_id = db.Column(db.BigInteger, nullable=False, index=True, info='tb_elc_company_account表主键')
    company_name = db.Column(db.String(127), info='企业名称')
    company_credit_no = db.Column(db.String(63), info='企业统一社会信用代码')
    company_credit_img_url = db.Column(db.String(1023), info='企业统一社会信用代码招聘路径，阿里云key')
    company_email = db.Column(db.String(63), info='企业邮箱')
    company_legal_name = db.Column(db.String(31), info='企业法人姓名')
    company_legal_card_no = db.Column(db.String(63), info='企业法人身份证号')
    company_reg_form_path = db.Column(db.String(255), info='企业信息登记表图片')
    related_transaction_no = db.Column(db.String(63), info='关联法人/代理人的交易号')
    bank_name = db.Column(db.String(63), info='银行名称')
    bank_card_no = db.Column(db.String(63), info='银行账户/卡号')
    bank_branch_no = db.Column(db.String(63), info='银联号')
    bank_sub_name = db.Column(db.String(63), info='开户支行名称')
    manager_agent_flag = db.Column(db.Integer, info='管理和是否是代理人；1：代理；0：法人')
    manager_name = db.Column(db.String(31), info='法人姓名')
    manager_type = db.Column(db.Integer, info='操作人类型；1：法人；2：代理人')
    manager_cert_type = db.Column(db.String(15), info='操作人证件类型；0：身份证，1：护照，B：香港居民往来内地通行证，C：台湾居民往来大陆通行证')
    manager_auditor_time = db.Column(db.DateTime, info='操作人资料审核时间')
    manager_id = db.Column(db.String(63), info='法人证件号')
    manager_mobile = db.Column(db.String(15), info='法人手机号，仅支持国内运营商')
    manager_status = db.Column(db.Integer, info='操作人资料状态；0：未激活；1：未认证；2：审核通过；3：已提交审核；4：审核不通过')
    manager_verify_type = db.Column(db.Integer, info='操作人认证方式，0：腾讯云认证；1：三要素认证；2：手势照认证')
    manager_card_no = db.Column(db.String(63), info='法人银行卡号')
    manager_audit_fail_reason = db.Column(db.String(255), info='操作人实名认证失败的原因')
    manager_back_photo_url = db.Column(db.String(127), info='操作人证件反面照，阿里云key')
    manager_head_photo_url = db.Column(db.String(127), info='操作人证件正面照，阿里云key')
    manager_photo_url = db.Column(db.String(127), info='操作人微众照片')
    manager_gestures_photo_url = db.Column(db.String(127), info='操作人手势照')
    manager_fork = db.Column(db.String(31), info='操作人民族')
    manager_birthday = db.Column(db.String(15), info='操作人出生日期，yyyy-MM-dd')
    manager_sex = db.Column(db.Integer, info='操作人性别；1：男，2：女')
    manager_start_date = db.Column(db.String(15), info='证件生效时间开始')
    manager_end_date = db.Column(db.String(15), info='证件生效时间结束')
    manager_issue_authority = db.Column(db.String(127), info='操作人证书颁发机构')
    manager_address = db.Column(db.String(255), info='操作人地址')
    verified_serial_no = db.Column(db.String(63), info='实名认证信息提交时，法大大返回的交易号，可以据此获取实名信息')
    verify_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='认证方式；1：银行卡认证；2：纸质审核认证，默认1')
    verify_url = db.Column(db.String, info='实名认证操作地址')
    verify_status = db.Column(db.Integer, info='实名认证状态；\\n0：未认证；\\n1：管理员资料已提交；\\n2：企业基本资料(没有申请表)已提交；\\n3：已提交待审核；\\n4：审核通过；\\n5：审核不通过；\\n6 人工初审通过，')
    audit_submit_time = db.Column(db.DateTime, info='实名资料提交时间')
    audit_time = db.Column(db.DateTime, info='审核时间')
    audit_fail_reason = db.Column(db.String(255), info='审核不通过的原因')
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)
    defunct = db.Column(db.Integer, server_default=db.FetchedValue())



class TbElcContractExtsign(db.Model):
    __tablename__ = 'tb_elc_contract_extsign'

    id = db.Column(db.BigInteger, primary_key=True)
    transaction_id = db.Column(db.String(63), nullable=False, info='合同签署交易号')
    elc_account_id = db.Column(db.BigInteger, nullable=False, index=True)
    contract_id = db.Column(db.String(63), nullable=False, info='关联的合同ID')
    contract_title = db.Column(db.String(127), nullable=False, info='合同名称')
    start_time = db.Column(db.DateTime, info='合同生效开始时间')
    end_time = db.Column(db.DateTime, index=True, info='合同生效结束时间')
    partb_transaction_id = db.Column(db.String(63), info='猎上签署时的交易号，全局唯一，猎上生成')
    partb_customer_id = db.Column(db.String(63), nullable=False, info='猎上客户编号')
    partb_sign_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='猎上签署状态；0：未签署，1：待签署；2：签署成功；3：失败')
    partb_sign_time = db.Column(db.DateTime, info='猎上签署时间')
    parta_transaction_id = db.Column(db.String(63), info='雇主/猎企签署时的交易号')
    parta_customer_id = db.Column(db.String(63), nullable=False, info='雇主/猎企的客户编号')
    parta_sign_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='雇主/猎企签署状态；0：未签署，1：待签署；2：签署成功；3：失败')
    parta_sign_time = db.Column(db.DateTime, info='雇主/猎企签署时间')
    parta_sign_url = db.Column(db.String, info='雇主/猎企签署合同的地址')
    viewpdf_url = db.Column(db.String, info='合同预览地址')
    download_url = db.Column(db.String, info='合同下载地址')
    filing = db.Column(db.Integer, index=True, info='合同归档状态，0：未归档；1：已归档')
    defunct = db.Column(db.Integer)
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)



class TbElcContractTemplate(db.Model):
    __tablename__ = 'tb_elc_contract_templates'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    template_id = db.Column(db.String(63), nullable=False, info='系统生成的模板主键')
    template_title = db.Column(db.String(127), info='合同模板标题')
    template_url_key = db.Column(db.String(127), info='模板阿里云的key')
    template_url = db.Column(db.String(2047), info='模板地址，原始模板文件的阿里云地址')
    company_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='合同模板对应的公司类型；1：雇主；2：猎企')
    defucnt = db.Column(db.Integer)
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)



class TbElcContract(db.Model):
    __tablename__ = 'tb_elc_contracts'

    id = db.Column(db.BigInteger, primary_key=True)
    elc_account_id = db.Column(db.BigInteger, nullable=False, index=True, info='电子合同账户表主键')
    template_id = db.Column(db.String(63), info='如果是从模板生成合同，则记录原始模板主键')
    viewpdf_url = db.Column(db.String, info='模板生成合同的情况下，预览地址')
    download_url = db.Column(db.String, info='模板生成合同的情况下，下载地址')
    contract_id = db.Column(db.String(63), nullable=False, info='合同唯一编号')
    contract_title = db.Column(db.String(127), nullable=False, info='合同标题')
    contract_url = db.Column(db.String(2047), info='合同的阿里云地址')
    contract_key = db.Column(db.String(127))
    contract_type = db.Column(db.String(15), nullable=False, info='合同类型，默认pdf，目前只支持pdf')
    status = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='合同状态；0：未签署；1：签署中；2：已签署-已生效；3：已过期失效')
    filing = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='是否归档；0：未归档；1：已归档；已归档的合同将不能进行更新')
    defunct = db.Column(db.Integer)
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)



class TbElcHoEvidenceInfo(db.Model):
    __tablename__ = 'tb_elc_ho_evidence_info'

    id = db.Column(db.BigInteger, primary_key=True)
    elc_account_id = db.Column(db.BigInteger, nullable=False, index=True, info='tb_elc_company_account主键')
    contract_name = db.Column(db.String(63), info='联系人-姓名')
    contract_phone = db.Column(db.String(63), info='联系人-手机号')
    contract_type = db.Column(db.Integer, info='联系人-签约人身份；1：企业法人代表，2：企业授权代理人')
    contract_email = db.Column(db.String(63), info='联系人-邮箱')
    contract_province_id = db.Column(db.BigInteger, info='联系地址，省份ID')
    contract_city_id = db.Column(db.BigInteger, info='联系地址，城市ID')
    contract_address = db.Column(db.String(255), info='联系地址，明细')
    company_name = db.Column(db.String(127), info='公司信息-名称')
    company_credit_code = db.Column(db.String(63), info='公司信息-统一社会信用代码')
    company_bank_name = db.Column(db.String(63), info='公司信息-开户银行')
    company_bank_no = db.Column(db.String(63), info='公司信息-开户银行账号')
    company_bank_province_id = db.Column(db.BigInteger, info='公司信息-开户地，省份ID')
    company_bank_city_id = db.Column(db.BigInteger, info='公司信息-开户地，城市ID')
    company_bank_branch = db.Column(db.String(127), info='公司信息-开户行-支行名称')
    company_business_licene_key = db.Column(db.String(255), info='公司信息-营业执照阿里云地址key')
    info_submit_time = db.Column(db.DateTime, info='联系人以及公司信息提交时间')
    evidence_no = db.Column(db.String(63), info='法大大返回的存证序列号，申请证书时需要使用')
    transaction_no = db.Column(db.String(63), info='存在信息同步到法大大时的交易号')
    file_content_json = db.Column(db.String, info='企业实名信息的json对象，用于生成存证文件')
    file_name = db.Column(db.String(127), info='存证文件的文件名')
    file_url_key = db.Column(db.String(127), info='存证文件保存在阿里云后，返回的key')
    file_last_modify = db.Column(db.BigInteger, info='存证文件的最后修改时间')
    file_size = db.Column(db.BigInteger, info='存证文件的大小')
    file_hash_code = db.Column(db.String(255), info='存证文件的hash256值')
    evidence_time = db.Column(db.DateTime, info='存证信息同步给法大大的时间')
    defunct = db.Column(db.Integer, info='逻辑删除')
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)
    post_user_name = db.Column(db.String(31), info='邮寄信息-用户名')
    post_receiver_name = db.Column(db.String(31), info='邮寄信息-收件人')
    post_receiver_phone = db.Column(db.String(31), info='邮寄信息-手机号')
    post_receiver_email = db.Column(db.String(63), info='邮寄信息-邮箱')
    post_receiver_fax = db.Column(db.String(127), info='邮寄信息-传真')
    post_code = db.Column(db.String(15), info='邮寄信息-邮编')
    post_province_id = db.Column(db.BigInteger, info='邮寄信息-省份ID')
    post_city_id = db.Column(db.BigInteger, info='邮寄信息-城市ID')
    post_address = db.Column(db.String(255), info='邮寄信息-详细地址')



class TbElcHunteronInfo(db.Model):
    __tablename__ = 'tb_elc_hunteron_info'

    id = db.Column(db.BigInteger, primary_key=True)
    open_id = db.Column(db.String(63), info='唯一编号，这里使用猎上网主体的统一社会信用代码加上前缀')
    credit_code = db.Column(db.String(63), info='猎上网统一社会信用代码')
    customer_id = db.Column(db.String(63))
    transaction_no = db.Column(db.String(127), info='存证编号')
    evidence_file_name = db.Column(db.String(255), info='存证文件名称')
    evidence_file_key = db.Column(db.String(127), info='存证文件，oss的key')
    evidence_file_url = db.Column(db.String(2047), info='存证文件，绝对路径')
    evidence_last_modify = db.Column(db.BigInteger, info='存证文件最后修改时间')
    evidence_file_size = db.Column(db.BigInteger, info='存证文件大小')
    evidence_no = db.Column(db.String(63), info='法大大返回的存证信息编号')
    deposit_hash = db.Column(db.String(2047), info='存证文件的hash256')
    failed_message = db.Column(db.String(2047), info='失败信息')
    evidence_file_time = db.Column(db.DateTime, info='存证时间')
    defunct = db.Column(db.Integer, index=True, info='逻辑删除')



class TbEnterprise(db.Model):
    __tablename__ = 'tb_enterprise'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    member_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    name = db.Column(db.String(200), nullable=False, info='公司名')
    display_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='显示名')
    short_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='简称')
    investigate_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    logo = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='标识')
    scale = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1.1-49\\n2.50-99\\n3.100-499\\n4.500-999\\n5.1000-4999\\n6.5000-9999\\n7.10000以上')
    style = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0 —— 外商独资/外企办事处 2 —— 中外合资 4 —— 国有企业 1 —— 国内上市公司 5 —— 民企/私营企业 3 —— 政府机关 6 —— 事业单位8 —— 非赢利机构7 —— 其他')
    telephone = db.Column(db.String(64), info='固定电话')
    industry_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    other_industry_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    province_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='省ID')
    city_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='城市ID')
    area_id = db.Column(db.BigInteger, info='地区Id')
    address = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='地址')
    website = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='网址')
    introduce = db.Column(db.String(2000), info='介绍')
    license_number = db.Column(db.String(100))
    license_attachment = db.Column(db.String(200))
    legal_person_attachment = db.Column(db.String(200))
    status = db.Column(db.Integer, nullable=False, info='0.待审核（未签合同） 1.正常（已签合同） 2.合同过期  3.已删除')
    service_admin = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    pas = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='pas')
    sales_admin = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False, index=True)
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue(), info='更新时间')
    channel = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0注册 1录入')
    approve_time = db.Column(db.DateTime, info='线索转客户时间 默认NULL 老客户的转客户时间等于update时间')
    top_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='top猎头公司数量')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='企业类型0：普通1：KA')
    offer_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='offer流程类型0：标准1：非标准')
    candidate_interval_month = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='重推候选人的间隔月份')
    highlights = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='公司亮点')
    develop_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='发展状态')
    temptation = db.Column(db.String(300), server_default=db.FetchedValue(), info='企业诱惑')
    tags = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue(), info='标签')
    industry_ids = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue(), info='多个行业')
    position_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位数量')
    operated = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0:未操作过 1:操作过')
    registration_number = db.Column(db.String(128), nullable=False, server_default=db.FetchedValue(), info='税务登记证号')
    bank = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='开户银行')
    bank_account = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='银行开户名称')
    bank_account_no = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='银行账号')
    priority = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='企业优先级:3:高, 2:中, 1:低')
    paction_start_time = db.Column(db.DateTime, info='合同开始日期')
    paction_end_time = db.Column(db.DateTime, info='合同结束日期')
    register_relate_admin = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='代企业注册或为企业获取注册链接的用户id')
    bd_phase = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='BD阶段, 1:新注册, 2:待签约, 3:待跟进, 4:公海')
    service_phase = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='客服阶段, 1:新注册,2未分配,3已分配')
    remind_days = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='猎头提醒限制天数')
    show_resume_contact_way = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否显示简历联系方式')
    domain = db.Column(db.String(200), server_default=db.FetchedValue(), info='域名帐号')
    paction_active_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='合同生效类型')
    customer_type = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='客户类型：0:普通，1:KA，2:vip')
    level_code = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='级别CODE')
    is_survery = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否完成了企调')
    credit_code = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='信用等级code')
    static_over_guarantee_rate = db.Column(db.Float(asdecimal=True), server_default=db.FetchedValue(), info='静态过保率')
    account_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='账户编号')
    reward_pay_mode = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='佣金结算方式')
    pay_day = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='结算日')
    invoice_day = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开票日')
    experienced_domain = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue(), info='专业领域')
    enterprise_valuation = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='企业估值')
    pact_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='雇主分类：1. 标准雇主  2. KA雇主')
    enterprise_attribute = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='客户属性 1 普通客户 2 RPO客户')
    pay_rate_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='分成类型 1 19分成 2 28分成 3 37分成 4 28&37')



class TbEnterpriseAccount(db.Model):
    __tablename__ = 'tb_enterprise_account'

    id = db.Column(db.BigInteger, primary_key=True)
    enterprise_id = db.Column(db.BigInteger, nullable=False, info='雇主ID ')
    account_name = db.Column(db.String(100), nullable=False, info='账户信息')
    paction_account_name = db.Column(db.String(100), nullable=False, info='签约主体')
    total_amount = db.Column(db.Float, nullable=False, server_default=db.FetchedValue(), info='总金额')
    balance_amount = db.Column(db.Float, nullable=False, server_default=db.FetchedValue(), info='余额')
    tax_no = db.Column(db.String(100), nullable=False, info='税号')
    invoice_title = db.Column(db.String(100), nullable=False, info='开票名称')
    invoice_address = db.Column(db.String(100), nullable=False, info='开票地址')
    invoice_phone = db.Column(db.String(20), nullable=False, info='发票电话')
    invoice_bank_name = db.Column(db.String(100), nullable=False, info='开户行')
    invoice_bank_card = db.Column(db.String(20), nullable=False, info='银行卡号')
    express_name = db.Column(db.String(100), nullable=False, info='收件人')
    express_phone = db.Column(db.String(20), nullable=False, info='收件电话')
    express_address = db.Column(db.String(200), nullable=False, info='收件地址')
    if_audit = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否已审核')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class TbEnterpriseAccountChange(db.Model):
    __tablename__ = 'tb_enterprise_account_change'

    id = db.Column(db.BigInteger, primary_key=True)
    account_id = db.Column(db.BigInteger, nullable=False)
    enterprise_id = db.Column(db.BigInteger, nullable=False, info='雇主ID ')
    account_name = db.Column(db.String(100), nullable=False, info='账户信息')
    paction_account_name = db.Column(db.String(100), nullable=False, info='签约主体')
    total_amount = db.Column(db.Float, nullable=False, server_default=db.FetchedValue(), info='总金额')
    balance_amount = db.Column(db.Float, nullable=False, server_default=db.FetchedValue(), info='余额')
    tax_no = db.Column(db.String(100), nullable=False, info='税号')
    invoice_title = db.Column(db.String(100), nullable=False, info='开票名称')
    invoice_address = db.Column(db.String(100), nullable=False, info='开票地址')
    invoice_phone = db.Column(db.String(20), nullable=False, info='发票电话')
    invoice_bank_name = db.Column(db.String(100), nullable=False, info='开户行')
    invoice_bank_card = db.Column(db.String(20), nullable=False, info='银行卡号')
    express_name = db.Column(db.String(100), nullable=False, info='收件人')
    express_phone = db.Column(db.String(20), nullable=False, info='收件电话')
    express_address = db.Column(db.String(200), nullable=False, info='收件地址')
    account_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1 新增 2 修改')
    account_audit_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1 未审核 2 审核通过 3 审核不通过/打回')
    reject_reason = db.Column(db.String(200), info='打回原因')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class TbEnterpriseAccountLog(db.Model):
    __tablename__ = 'tb_enterprise_account_log'

    id = db.Column(db.BigInteger, primary_key=True)
    enterprise_id = db.Column(db.BigInteger, nullable=False, info='雇主ID')
    enterprise_account_id = db.Column(db.BigInteger, nullable=False, info='雇主账户ID')
    operate_type = db.Column(db.Integer, nullable=False, info='操作类型 1 回款 2 退款 3 转账入账 4 核销 5 转账出账')
    operate_amount = db.Column(db.Float, nullable=False, info='操作金额')
    remark = db.Column(db.String(200), info='备注')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')



class TbEnterpriseAddres(db.Model):
    __tablename__ = 'tb_enterprise_address'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    enterprise_id = db.Column(db.BigInteger, nullable=False)
    province_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='省')
    city_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='市')
    area_id = db.Column(db.BigInteger, info='区/县')
    address = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='详细地址')
    remark = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='备注')
    if_default = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否默认')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class TbEnterpriseBak20160425(db.Model):
    __tablename__ = 'tb_enterprise_bak20160425'

    id = db.Column(db.BigInteger, primary_key=True)
    member_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    name = db.Column(db.String(200), nullable=False)
    display_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    short_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    investigate_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    logo = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue())
    scale = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1.1-49\\n2.50-99\\n3.100-499\\n4.500-999\\n5.1000-4999\\n6.5000-9999\\n7.10000以上')
    style = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0 —— 外商独资/外企办事处 2 —— 中外合资 4 —— 国有企业 1 —— 国内上市公司 5 —— 民企/私营企业 3 —— 政府机关 6 —— 事业单位8 —— 非赢利机构7 —— 其他')
    industry_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    other_industry_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    province_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    city_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    address = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue())
    website = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue())
    introduce = db.Column(db.String(2000))
    license_number = db.Column(db.String(100))
    license_attachment = db.Column(db.String(200))
    legal_person_attachment = db.Column(db.String(200))
    status = db.Column(db.Integer, nullable=False, info='0.待审核（未签合同） 1.正常（已签合同） 2.合同过期  3.已删除')
    service_admin = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    sales_admin = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    channel = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0注册 1录入')
    approve_time = db.Column(db.DateTime, info='线索转客户时间 默认NULL 老客户的转客户时间等于update时间')
    top_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='top猎头公司数量')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='企业类型0：普通1：KA')
    offer_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='offer流程类型0：标准1：非标准')
    candidate_interval_month = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='重推候选人的间隔月份')
    highlights = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='公司亮点')
    develop_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='发展状态')
    temptation = db.Column(db.String(300), server_default=db.FetchedValue(), info='企业诱惑')
    tags = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue(), info='标签')
    industry_ids = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue(), info='多个行业')
    position_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位数量')
    operated = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0:未操作过 1:操作过')
    registration_number = db.Column(db.String(128), nullable=False, server_default=db.FetchedValue(), info='税务登记证号')
    bank = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='开户银行')
    bank_account = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='银行开户名称')
    bank_account_no = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='银行账号')
    priority = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='企业优先级:3:高, 2:中, 1:低')
    paction_start_time = db.Column(db.DateTime, info='合同开始日期')
    paction_end_time = db.Column(db.DateTime, info='合同结束日期')
    register_relate_admin = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='代企业注册或为企业获取注册链接的用户id')
    bd_phase = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='BD阶段, 1:新注册, 2:待签约, 3:待跟进, 4:公海')
    service_phase = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='客服阶段, 1:新注册,2未分配,3已分配')
    remind_days = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='猎头提醒限制天数')
    show_resume_contact_way = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否显示简历联系方式')
    domain = db.Column(db.String(100), server_default=db.FetchedValue(), info='域名帐号')
    paction_active_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='合同生效类型')
    customer_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='客户类型：0:普通，1:KA，2:vip')
    level_code = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='级别CODE')



class TbEnterpriseBlacklist(db.Model):
    __tablename__ = 'tb_enterprise_blacklist'

    id = db.Column(db.BigInteger, primary_key=True)
    enterprise_id = db.Column(db.BigInteger, nullable=False, info='企业id')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0:有效，1移除')
    remark = db.Column(db.String(512), nullable=False, server_default=db.FetchedValue(), info='备注')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)



class TbEnterpriseBudget(db.Model):
    __tablename__ = 'tb_enterprise_budget'

    id = db.Column(db.BigInteger, primary_key=True)
    enterprise_id = db.Column(db.BigInteger, nullable=False)
    budget_year = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='预算年份')
    budget_amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='预算金额')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbEnterpriseClue(db.Model):
    __tablename__ = 'tb_enterprise_clue'

    id = db.Column(db.BigInteger, primary_key=True, info='主键id')
    name = db.Column(db.String(256), nullable=False, info='公司名称')
    display_name = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue())
    short_name = db.Column(db.String(256), server_default=db.FetchedValue(), info='简称')
    province_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='省id')
    city_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='城市id')
    address = db.Column(db.String(256), info='地址')
    introduce = db.Column(db.Text, info='公司简介')
    industry_ids = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue())
    establish_year = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='成立年份')
    logo = db.Column(db.String(256), info='logo')
    scale = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='规模')
    style = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='性质')
    web_site = db.Column(db.String(256), info='网址')
    contacter = db.Column(db.String(256), nullable=False, server_default=db.FetchedValue(), info='联系人')
    email = db.Column(db.String(128), server_default=db.FetchedValue(), info='email')
    mobile = db.Column(db.String(128), nullable=False, unique=True, server_default=db.FetchedValue(), info='手机')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, index=True, server_default=db.FetchedValue(), info='更新时间')
    defunt = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除')
    source = db.Column(db.String(50), info='线索来源脉脉，领英等')
    status = db.Column(db.String(50), info='已转为客户，已失效等')
    jobtitle = db.Column(db.String(50), info='联系人岗位')
    member_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())



class TbEnterpriseClueBudget(db.Model):
    __tablename__ = 'tb_enterprise_clue_budget'

    id = db.Column(db.BigInteger, primary_key=True)
    clue_id = db.Column(db.BigInteger, nullable=False)
    budget_year = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='预算年份')
    budget_amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='预算金额')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbEnterpriseCollection(db.Model):
    __tablename__ = 'tb_enterprise_collection'

    id = db.Column(db.BigInteger, primary_key=True)
    headhunter_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='猎头id')
    company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎头公司id')
    enterprise_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='关注企业id')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    last_visit_time = db.Column(db.DateTime, info='最后一次浏览时间')



class TbEnterpriseCommissionRule(db.Model):
    __tablename__ = 'tb_enterprise_commission_rule'

    enterprise_id = db.Column(db.BigInteger, primary_key=True, info='雇主表主键')
    rule = db.Column(db.Text, info='佣金规则')
    instruction = db.Column(db.Text, info='佣金规则补充说明')
    defunct = db.Column(db.Integer, index=True)
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)
    rpo_rule = db.Column(db.Text, info='RPO佣金规则')



class TbEnterpriseDivision(db.Model):
    __tablename__ = 'tb_enterprise_division'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    name = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='事业部名称')
    enterprise_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='企业id')
    order_by = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序')
    create_time = db.Column(db.DateTime, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, info='更新时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否无效 -> 1 : true 已删除；0 : false 有效')



class TbEnterpriseGroup(db.Model):
    __tablename__ = 'tb_enterprise_group'

    id = db.Column(db.BigInteger, primary_key=True)
    group_name = db.Column(db.String(63), nullable=False, info='集团名称')
    group_info = db.Column(db.String(255), info='集团描述')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)



class TbEnterpriseGroupRecommendRule(db.Model):
    __tablename__ = 'tb_enterprise_group_recommend_rule'

    id = db.Column(db.BigInteger, primary_key=True)
    group_id = db.Column(db.BigInteger, nullable=False, index=True)
    is_top = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    level = db.Column(db.Integer, info='规则级别；0：HR；1：职位；2：雇主；3：集团')
    list_to_next = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='logical查询的数据是否可以透传到后续判定；主要针对false_recommend')
    true_next_rule_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='logical结果true的情况，对应的下一条规则')
    false_next_rule_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='logical结果false的情况，对应的下一条规则')
    defunct = db.Column(db.Integer, index=True)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)



class TbEnterpriseGroupRelation(db.Model):
    __tablename__ = 'tb_enterprise_group_relation'

    id = db.Column(db.BigInteger, primary_key=True)
    group_id = db.Column(db.BigInteger, nullable=False, index=True)
    enterprise_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='雇主ID')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)



class TbEnterpriseGroupRuleFalseRecommend(db.Model):
    __tablename__ = 'tb_enterprise_group_rule_false_recommend'

    id = db.Column(db.BigInteger, primary_key=True)
    repeat_level = db.Column(db.Integer, nullable=False, info='复推级别；1：猎头；2：猎企')
    rule_id = db.Column(db.BigInteger, nullable=False, index=True, info='所属规则')
    status_list = db.Column(db.String(255), info='可复推的状态列表，多个状态用英文逗号分隔')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbEnterpriseGroupRuleLogical(db.Model):
    __tablename__ = 'tb_enterprise_group_rule_logical'

    id = db.Column(db.BigInteger, primary_key=True)
    rule_id = db.Column(db.BigInteger, nullable=False, index=True)
    status_list = db.Column(db.String(255), info='状态列表，多个状态用英文逗号分隔')
    logical = db.Column(db.Integer, nullable=False, info='查询逻辑；1：NOT；2：IN')
    target_result = db.Column(db.Integer, nullable=False, info='目标逻辑；0：EMPTY；1：NOT_EMPTY')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbEnterpriseHhCategory(db.Model):
    __tablename__ = 'tb_enterprise_hh_category'
    __table_args__ = (
        db.Index('idx_enterpriseid_category', 'enterprise_id', 'category_name'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    enterprise_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='企业ID')
    category_name = db.Column(db.String(30), nullable=False, server_default=db.FetchedValue(), info='部门名称')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbEnterpriseHhCategoryRelationship(db.Model):
    __tablename__ = 'tb_enterprise_hh_category_relationship'
    __table_args__ = (
        db.Index('idx_headhunterid_enterpriseid', 'headhunter_id', 'enterprise_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    headhunter_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎头ID')
    enterprise_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='企业ID')
    category_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='部门ID')
    category_name = db.Column(db.String(30), nullable=False, server_default=db.FetchedValue(), info='部门名称')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')



class TbEnterpriseHighlight(db.Model):
    __tablename__ = 'tb_enterprise_highlights'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    name = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='名称')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbEnterpriseHoAccount(db.Model):
    __tablename__ = 'tb_enterprise_ho_account'

    id = db.Column(db.BigInteger, primary_key=True, info='雇主账户主键')
    enterprise_id = db.Column(db.BigInteger, nullable=False, index=True, info='关联的企业')
    enterprise_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='企业类型；1：雇主；2：猎企')
    current_amount = db.Column(db.Float(9, True), info='账户当前可用金额，单位：元')
    freeze_amount = db.Column(db.Float(9, True), server_default=db.FetchedValue(), info='账户冻结金额，单位：元')
    defunct = db.Column(db.Integer)
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)



class TbEnterpriseHoAccountFreezeLog(db.Model):
    __tablename__ = 'tb_enterprise_ho_account_freeze_log'

    tran_id = db.Column(db.BigInteger, primary_key=True, info='冻结交易号')
    ho_account_id = db.Column(db.BigInteger, info='账户')
    enterprise_id = db.Column(db.BigInteger, nullable=False, info='关联的企业')
    enterprise_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='企业类型；1：雇主；2：猎企')
    amount = db.Column(db.Float(9, True), info='金额')
    payload_id = db.Column(db.BigInteger, info='关联数据主键')
    payload = db.Column(db.String(255), info='关联数据描述')
    action_type = db.Column(db.Integer, info='操作类型；1：冻结；2：解冻（返还金额）；3：扣除（实际执行扣除金额）；4：扣除（申诉失败，也会扣除）。1会增加账户表冻结金额；2、3、4会减掉冻结金额。')
    account_changed_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='冻结金额时的账户变更类型')
    defunct = db.Column(db.Integer)
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)



class TbEnterpriseHoAccountLog(db.Model):
    __tablename__ = 'tb_enterprise_ho_account_log'

    id = db.Column(db.BigInteger, primary_key=True)
    ho_account_id = db.Column(db.BigInteger, nullable=False, index=True, info='关联雇主账号表主键')
    enterprise_id = db.Column(db.BigInteger, nullable=False, index=True, info='关联的企业')
    enterprise_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='企业类型；1：雇主；2：猎企')
    old_amount = db.Column(db.Float(9, True), info='变动前，账户余额')
    changed_amount = db.Column(db.Float(9, True), info='变动余额；负数表示消费，正数表示充值')
    changed_type = db.Column(db.Integer, info='变动类型')
    new_amount = db.Column(db.Float(9, True), info='变动后，账户余额')
    operate_user_id = db.Column(db.BigInteger, info='操作人')
    operate_user_type = db.Column(db.Integer, info='操作人类型，可以是tdc用户，可以是hr用户')
    operate_time = db.Column(db.DateTime, info='操作时间')
    defunct = db.Column(db.Integer)
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)
    comment = db.Column(db.String(255), info='备注')



class TbEnterpriseIngroup(db.Model):
    __tablename__ = 'tb_enterprise_ingroup'

    id = db.Column(db.BigInteger, primary_key=True)
    enterprise_ingroup_name = db.Column(db.String(31), nullable=False, info='雇主所属派系名')
    enterprise_ingroup_code = db.Column(db.String(31), nullable=False, info='雇主派系编码')
    enterprise_name = db.Column(db.String(127), nullable=False, info='当前雇主公司名')
    enterprise_simple_name = db.Column(db.String(127), info='当前雇主简称或者统称')
    enterprise_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='雇主公司在平台的ID，可以为空')
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    operate_user_id = db.Column(db.BigInteger)
    ingroup_type = db.Column(db.String(31), info='类型')



class TbEnterpriseInvestigate(db.Model):
    __tablename__ = 'tb_enterprise_investigate'

    id = db.Column(db.BigInteger, primary_key=True)
    enterprise_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue())
    en_short_name = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue())
    establish_year = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    industry_rank = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='行业排名')
    city_distribution = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue())
    product = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue())
    customer = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue())
    production_value = db.Column(db.Integer, info='万元')
    stock_code = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue())
    competitor = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue())
    advantage = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue())
    organization_architecture = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue())
    culture = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue())
    strategy = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue())
    attention = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)
    company_advantage = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='公司优势')



class TbEnterpriseInvestigateImage(db.Model):
    __tablename__ = 'tb_enterprise_investigate_image'

    id = db.Column(db.BigInteger, primary_key=True)
    enterprise_id = db.Column(db.BigInteger, nullable=False, info='企业id')
    image = db.Column(db.String(500), nullable=False, info='公司图片')
    cover = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否是封面（0:不是1:是），一个企业id只能有一个封面')
    sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbEnterpriseInvestigateManager(db.Model):
    __tablename__ = 'tb_enterprise_investigate_manager'

    id = db.Column(db.BigInteger, primary_key=True)
    enterprise_id = db.Column(db.BigInteger, nullable=False, info='企业id')
    name = db.Column(db.String(100), nullable=False, info='管理者姓名')
    duty = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='管理者的职务')
    weibo = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='微博')
    logo = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='头像')
    introduce = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='管理者个人信息介绍')
    sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbEnterpriseInvestigateProduct(db.Model):
    __tablename__ = 'tb_enterprise_investigate_product'

    id = db.Column(db.BigInteger, primary_key=True)
    enterprise_id = db.Column(db.BigInteger, nullable=False, info='企业id')
    name = db.Column(db.String(100), nullable=False, info='产品名')
    website = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='产品网址')
    logo = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='产品logo')
    introduce = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='产品介绍')
    sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbEnterpriseInvoiceApply(db.Model):
    __tablename__ = 'tb_enterprise_invoice_apply'

    id = db.Column(db.BigInteger, primary_key=True)
    enterprise_id = db.Column(db.BigInteger, nullable=False, info='雇主ID')
    enterprise_account_id = db.Column(db.BigInteger, nullable=False, info='雇主账户ID')
    apply_total_amount = db.Column(db.Float, nullable=False, server_default=db.FetchedValue(), info='申请总金额')
    had_apply_amount = db.Column(db.Float, nullable=False, server_default=db.FetchedValue(), info='已申请金额（相关订单总金额）')
    account_name = db.Column(db.String(100), nullable=False, info='账户信息')
    paction_account_name = db.Column(db.String(100), nullable=False, info='签约主体')
    tax_no = db.Column(db.String(100), nullable=False, info='税号')
    invoice_title = db.Column(db.String(100), nullable=False, info='开票名称')
    invoice_address = db.Column(db.String(100), nullable=False, info='开票地址')
    invoice_phone = db.Column(db.String(20), nullable=False, info='发票电话')
    invoice_bank_name = db.Column(db.String(100), nullable=False, info='开户行')
    invoice_bank_card = db.Column(db.String(20), nullable=False, info='银行卡号')
    express_name = db.Column(db.String(100), nullable=False, info='收件人')
    express_phone = db.Column(db.String(20), nullable=False, info='收件电话')
    express_address = db.Column(db.String(200), nullable=False, info='收件地址')
    invoice_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='发票种类 1  增值税普通发票 2 增值税专用发票6%')
    invoice_no = db.Column(db.String(100), info='发票编号')
    invoice_code = db.Column(db.String(100), info='发票编码')
    invoice_user_name = db.Column(db.String(100), info='开票人')
    invoice_time = db.Column(db.DateTime, info='开票时间')
    express_no = db.Column(db.String(100), info='快递单号')
    apply_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='申请状态 1 申请中 2 通过申请 3 完成开票 4 已寄件 5 已收件')
    refund_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='退票状态 0 未退票 1 部分退票 2 全部退票')
    reject_reason = db.Column(db.String(100), info='打回原因')
    express_time = db.Column(db.DateTime)
    receive_time = db.Column(db.DateTime, info='签收时间')
    shoud_pay_time = db.Column(db.DateTime, info='应回款时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class TbEnterpriseInvoiceApplyLog(db.Model):
    __tablename__ = 'tb_enterprise_invoice_apply_log'

    id = db.Column(db.BigInteger, primary_key=True)
    invoice_apply_id = db.Column(db.BigInteger, nullable=False, info='雇主开票申请ID')
    apply_status = db.Column(db.Integer, nullable=False, info='操作类型 对应相关 apply_status/refund_status')
    remark = db.Column(db.String(200), info='备注')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')



class TbEnterpriseInvoiceApplyRefundLog(db.Model):
    __tablename__ = 'tb_enterprise_invoice_apply_refund_log'

    id = db.Column(db.BigInteger, primary_key=True)
    placement_id = db.Column(db.BigInteger, nullable=False, info='成单ID')
    invoice_apply_id = db.Column(db.BigInteger, nullable=False, info='雇主开票申请ID')
    refund_status = db.Column(db.Integer, nullable=False, info='操作类型 对应相关 apply_status/refund_status')
    remark = db.Column(db.String(200), info='备注')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')



class TbEnterpriseInvoiceApplyRelation(db.Model):
    __tablename__ = 'tb_enterprise_invoice_apply_relation'

    id = db.Column(db.BigInteger, primary_key=True)
    invoice_apply_id = db.Column(db.BigInteger, nullable=False, index=True, info='开票申请ID')
    placement_id = db.Column(db.BigInteger, nullable=False, index=True, info='成单ID')
    invoice_amount = db.Column(db.Float, nullable=False, info='开票金额')
    over_amount = db.Column(db.Float, nullable=False, server_default=db.FetchedValue(), info='核销金额')
    refund_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='退款状态 1 申请中/需退票 2 确定收票 3 确定退款 4 校验通过 5 退款完成')
    refund_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='退票方式 1 退票 2 抵票')
    refund_time = db.Column(db.DateTime, info='退票款/抵票 最终时间')
    if_over = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否核销 0 否 1 是')
    over_remark = db.Column(db.String(500))
    over_user_id = db.Column(db.BigInteger, info='核销人')
    over_time = db.Column(db.DateTime, info='核销时间')
    refund_invoice_reason = db.Column(db.String(500), info='退票说明')
    refund_amount_reason = db.Column(db.String(500), info='退款说明')
    offset_audit_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1 申请中 2 审核通过 3 打回')
    offset_remark = db.Column(db.String(500), info='互抵备注')
    offset_reason = db.Column(db.String(500), info='互抵打回原因')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class TbEnterpriseInvoiceDetail(db.Model):
    __tablename__ = 'tb_enterprise_invoice_detail'

    id = db.Column(db.BigInteger, primary_key=True)
    invoice_no = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='开票编号')
    invoice_title = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='开票抬头')
    receipts_id = db.Column(db.BigInteger, nullable=False, info='对应收款单ID')
    invoice_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='发票类型')
    invoice_amount = db.Column(db.Float(12, True), nullable=False, server_default=db.FetchedValue(), info='开票金额')
    invoice_tax_amount = db.Column(db.Float(15, True), server_default=db.FetchedValue(), info='开票金额对应的税额')
    invoice_date = db.Column(db.DateTime, info='开票日期')
    retrun_invoice_date = db.Column(db.DateTime, info='退票日期')
    comment = db.Column(db.String(1000), server_default=db.FetchedValue(), info='开票备注')
    return_comment = db.Column(db.String(1000), server_default=db.FetchedValue(), info='退票备注')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='更新者')
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue(), info='更新时间')
    bounce_status = db.Column(db.Integer, server_default=db.FetchedValue(), info='1:已开票,2:需退票,3:已退票')
    attachment_path = db.Column(db.String(2000), info='附件路径')



class TbEnterpriseInvoiceDetail20190521(db.Model):
    __tablename__ = 'tb_enterprise_invoice_detail_20190521'

    id = db.Column(db.BigInteger, primary_key=True)
    invoice_no = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='开票编号')
    invoice_title = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='开票抬头')
    receipts_id = db.Column(db.BigInteger, nullable=False, info='对应收款单ID')
    invoice_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='发票类型')
    invoice_amount = db.Column(db.Float, nullable=False, server_default=db.FetchedValue(), info='开票金额')
    invoice_date = db.Column(db.DateTime, info='开票日期')
    retrun_invoice_date = db.Column(db.DateTime, info='退票日期')
    comment = db.Column(db.String(1000), server_default=db.FetchedValue(), info='开票备注')
    return_comment = db.Column(db.String(1000), server_default=db.FetchedValue(), info='退票备注')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='更新者')
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue(), info='更新时间')
    bounce_status = db.Column(db.Integer, server_default=db.FetchedValue(), info='1:已开票,2:需退票,3:已退票')



class TbEnterpriseOperation(db.Model):
    __tablename__ = 'tb_enterprise_operation'

    id = db.Column(db.BigInteger, primary_key=True, info='唯一编号')
    enterprise_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='企业编号')
    operation_enterprise_code = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='合作企业标记')
    operation_enterprise_name = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='合作企业名称')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbEnterprisePloy(db.Model):
    __tablename__ = 'tb_enterprise_ploy'

    enterprise_id = db.Column(db.BigInteger, primary_key=True, info='雇主表ID')
    rpo_switch = db.Column(db.Integer, server_default=db.FetchedValue(), info='雇主的RPO标签开关')
    create_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    recommend_notice_last_modify_time = db.Column(db.DateTime, index=True, info='雇主推荐须知最后更新时间')
    commission_rule_last_modify_time = db.Column(db.DateTime, index=True, info='雇主佣金规则')
    withhold_ratio = db.Column(db.Integer, server_default=db.FetchedValue(), info='预扣比例')
    hunt_quick_pay_tag = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否显示猎快付标签')
    operation_type = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='运营类型 0:猎上运营 1:ACN猎企运营')
    submit_time = db.Column(db.DateTime, info='提交时间')
    reject_reason = db.Column(db.String(200))
    collection_bank = db.Column(db.String(100), info='收款银行名称')
    collection_bank_account_no = db.Column(db.String(100), info='收款银行账号')
    partner_company_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='关联合伙人猎企')



class TbEnterprisePool(db.Model):
    __tablename__ = 'tb_enterprise_pool'

    id = db.Column(db.BigInteger, primary_key=True, info='主键id')
    obj_id = db.Column(db.BigInteger, index=True, server_default=db.FetchedValue(), info='客户id或clue id')
    obj_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='对象类型, 1:企业, 2:clue')
    bdo_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='销售负责人BDO')
    bd_phase = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='BD阶段, 1:新注册, 2:待签约, 3:待跟进, 4:公海, 5:垃圾库')
    bdo_assign_time = db.Column(db.DateTime, info='bdo分配时间')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    defunt = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除')
    bd_phase_time = db.Column(db.DateTime, info='bd阶段的时间')



class TbEnterpriseProContract(db.Model):
    __tablename__ = 'tb_enterprise_pro_contract'

    id = db.Column(db.BigInteger, primary_key=True)
    enterprise_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='企业id ')
    pro_id = db.Column(db.BigInteger)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)
    pro_start_time = db.Column(db.DateTime, nullable=False, info='产品订阅开始时间')
    pro_end_time = db.Column(db.DateTime, nullable=False, info='产品订阅结束时间')
    contract_id = db.Column(db.BigInteger, nullable=False, info='合同id')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='生效状态：1:新建, 2:确认,3:生效，4：失效, 5:删除')
    commission_rate = db.Column(db.Integer, info='佣金比例')
    product_type = db.Column(db.Integer, info='职位产品类型:1:标准版,2：佣金宝，3：到岗快')



class TbEnterpriseReceipt(db.Model):
    __tablename__ = 'tb_enterprise_receipts'

    id = db.Column(db.BigInteger, primary_key=True)
    placement_id = db.Column(db.BigInteger, nullable=False, index=True, info='placement成单表ID ')
    total_receipts_amount = db.Column(db.Float(12, True), server_default=db.FetchedValue(), info='总应收金额')
    had_receipts_amount = db.Column(db.Float(12, True), server_default=db.FetchedValue(), info='已收金额')
    total_receipts_tax_amount = db.Column(db.Float(15, True), server_default=db.FetchedValue(), info='总应收金额对应的税额')
    had_receipts_tax_amount = db.Column(db.Float(15, True), server_default=db.FetchedValue(), info='已收金额对应的税额')
    receipts_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='收款状态：未收款，部分收款，已收款，已完结')
    refund_receipts_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='退款状态:1 需退款,2：已退款, 3:结束')
    total_refund = db.Column(db.Float(12, True), nullable=False, server_default=db.FetchedValue(), info='总应退款金额')
    had_refund = db.Column(db.Float(12, True), nullable=False, server_default=db.FetchedValue(), info='已退款金额')
    total_invoice_amount = db.Column(db.Float(12, True), nullable=False, server_default=db.FetchedValue(), info='总开票金额')
    had_invoice_amount = db.Column(db.Float(12, True), nullable=False, server_default=db.FetchedValue(), info='已开票金额')
    total_invoice_tax_amount = db.Column(db.Float(15, True), server_default=db.FetchedValue(), info='总开票金额对应的税额')
    had_invoice_tax_amount = db.Column(db.Float(15, True), server_default=db.FetchedValue(), info='已开票金额对应的税额')
    invoice_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开票状态：未开票，部分开票，已开票')
    refund_invoice_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='退票状态: 1:需退票,2:已退票,3:结束')
    product_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='产品类型：过保付，到岗付，到岗快')
    last_receipts_time = db.Column(db.DateTime, info='最后的付款时间')
    last_invoice_time = db.Column(db.DateTime, info='最后的开票时间')
    had_apply_amount = db.Column(db.Float(12, True), nullable=False, server_default=db.FetchedValue(), info='已申请金额')
    apply_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='收款申请：0 需申请 1 部分申请 2 已申请')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue(), info='更新时间')



class TbEnterpriseRecommendNotice(db.Model):
    __tablename__ = 'tb_enterprise_recommend_notice'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    enterprise_id = db.Column(db.BigInteger, nullable=False, unique=True, info='关联公司ID')
    payment_rule = db.Column(db.String, info='付费规则')
    escheatage_rule = db.Column(db.String, info='归属权判定规则')
    order_rule = db.Column(db.String, info='做单规则')
    supplementary_information = db.Column(db.String, info='补充信息')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='逻辑删除')
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)



class TbEnterpriseReport(db.Model):
    __tablename__ = 'tb_enterprise_report'
    __table_args__ = (
        db.Index('enterprise_id', 'enterprise_id', 'count_date'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    enterprise_id = db.Column(db.BigInteger, nullable=False, info='企业id')
    bdo_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    placement_reward = db.Column(db.Float, nullable=False, server_default=db.FetchedValue(), info='实际成单佣金')
    onboard_on_reward = db.Column(db.Float, nullable=False, server_default=db.FetchedValue(), info='实际到岗佣金')
    onboard_over_reward = db.Column(db.Float, nullable=False, server_default=db.FetchedValue(), info='实际过保佣金')
    publish_position_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='发布职位数')
    closed_position_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='关闭职位数')
    open_position_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开放职位数')
    candidate_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='推荐数')
    interview_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='面试数')
    placement_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='成单数')
    onboard_on_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='到岗数')
    onboard_over_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='过保数')
    count_date = db.Column(db.Date, nullable=False, info='统计时间')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')



class TbEnterpriseResumeField(db.Model):
    __tablename__ = 'tb_enterprise_resume_field'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    template_code = db.Column(db.String(20), index=True, info='模板Code')
    field_code = db.Column(db.String(255), info='字段Code')
    field_group_code = db.Column(db.String(255), info='字段分组Code')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否删除')
    show_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='字段显示类型：1：显示且必填；2：仅显示')
    remark = db.Column(db.String(255))
    if_parent = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否根目录（1：根目录；0：子目录）')
    name = db.Column(db.String(255), info='字段名')
    sort = db.Column(db.Integer, info='排序')
    update_time = db.Column(db.DateTime, info='最后修改时间')
    update_user_id = db.Column(db.BigInteger, info='最后修改用户')
    create_time = db.Column(db.DateTime, info='创建时间')
    create_user_id = db.Column(db.BigInteger, info='创建用户ID')
    export_show_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='TDC导出展示类型 1: 强制展示 2: 无内容时隐藏 3: 强制隐藏')



class TbEnterpriseResumeTemplateFile(db.Model):
    __tablename__ = 'tb_enterprise_resume_template_file'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否删除')
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue(), info='创建时间')
    create_user_id = db.Column(db.BigInteger, info='创建用户ID')
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue(), info='最后修改时间')
    update_user_id = db.Column(db.BigInteger, info='最后修改用户')
    template_code = db.Column(db.String(20), index=True, info='模板Code')
    web_url = db.Column(db.String(500), info='全地址路径')
    relative_url = db.Column(db.String(500), info='相对地址路径')
    file_name = db.Column(db.String(50), info='上传时文件名')



class TbEnterpriseResumeTip(db.Model):
    __tablename__ = 'tb_enterprise_resume_tips'

    id = db.Column(db.BigInteger, primary_key=True, info='配置ID')
    template_code = db.Column(db.String(20), unique=True, info='模板Code')
    tips = db.Column(db.String, info='提示')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_user_id = db.Column(db.BigInteger, info='修改人')
    update_time = db.Column(db.DateTime, info='修改时间')



class TbEnterpriseSupplier(db.Model):
    __tablename__ = 'tb_enterprise_supplier'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    enterprise_id = db.Column(db.BigInteger, nullable=False, index=True, info='当前雇主ID')
    company_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='猎企ID，线下未审核的，为0')
    company_name = db.Column(db.String(127), nullable=False, info='猎企名称')
    display_name = db.Column(db.String(63))
    address = db.Column(db.String(255), info='office地址')
    direction_industry_ids = db.Column(db.String(63))
    direction_function_ids = db.Column(db.String(63))
    direction_city_ids = db.Column(db.String(63))
    cooperation_time = db.Column(db.DateTime, info='合作时间')
    cooperation_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='合作类型：1：普通合作；2：深度合作')
    supplier_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='供应商状态：0：审核中；1：通过；2：不通过；3：取消合作')
    supplier_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='供应商类型：1：线上（猎上平台已有账号）；2：线下')
    invite_code = db.Column(db.String(63), info='邀请随机码，可以为空')
    assign_hr_id = db.Column(db.BigInteger, nullable=False, info='添加供应商的HRID')
    assign_hunter_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='录入信息的猎头ID')
    pay_rate = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='分成比例；佣金分给猎头的比例，统一 90')
    priority_level = db.Column(db.Integer, server_default=db.FetchedValue(), info='合作优先级，雇主设置不同供应商的优先级')
    recommend_warning_day = db.Column(db.Integer, info='推荐预警-预警天数')
    recommend_last_warning_date = db.Column(db.DateTime, info='推荐预警-最后预警时间')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False)



class TbEnterpriseSupplierHunter(db.Model):
    __tablename__ = 'tb_enterprise_supplier_hunter'

    id = db.Column(db.BigInteger, primary_key=True)
    supplier_id = db.Column(db.BigInteger, nullable=False)
    hunter_id = db.Column(db.BigInteger, server_default=db.FetchedValue())
    company_id = db.Column(db.BigInteger, server_default=db.FetchedValue())
    hunter_name = db.Column(db.String(31))
    cell_phone = db.Column(db.String(31), nullable=False)
    email = db.Column(db.String(63), info='猎头邮箱')
    direction_industry_ids = db.Column(db.String(63))
    direction_function_ids = db.Column(db.String(63))
    supplier_hunter_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='合作状态：0：审核中；1：通过；2：不通过；3：取消合作')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)



class TbEnterpriseSupplierLog(db.Model):
    __tablename__ = 'tb_enterprise_supplier_log'

    id = db.Column(db.BigInteger, primary_key=True)
    supplier_id = db.Column(db.BigInteger, nullable=False)
    operate_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='操作类型')
    operate_name = db.Column(db.String(31), nullable=False, info='操作名称')
    operate_msg = db.Column(db.String(127), nullable=False, info='操作内容描述')
    operate_time = db.Column(db.DateTime, nullable=False)
    operate_user_id = db.Column(db.BigInteger)
    operate_user_type = db.Column(db.Integer)
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)



class TbEnterpriseSurvey(db.Model):
    __tablename__ = 'tb_enterprise_survey'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    enterprise_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='雇主ID')
    social_security_benefits = db.Column(db.String(200), info='社保福利')
    housing_benefits = db.Column(db.String(200), info='住房福利')
    holiday_benefits = db.Column(db.String(200), info='假期福利')
    phone_traffic_benefits = db.Column(db.String(200), info='通讯交通')
    private_other_required = db.Column(db.Text, info='（隐性要求）其他项说明')
    interview_address = db.Column(db.String(200), info='面试地点')
    work_address = db.Column(db.String(200), info='工作地点')
    if_other_place_reimbursement = db.Column(db.Integer, info='异地面试报销')
    reimbursement_process = db.Column(db.Text, info='报销流程')
    resume_template_attachment = db.Column(db.String(500), info='专用简历模板')
    company_introduction_attachment = db.Column(db.String(500), info='公司介绍')
    product_introduction_attachment = db.Column(db.String(500), info='产品介绍')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbEnterpriseSurveyPloy(db.Model):
    __tablename__ = 'tb_enterprise_survey_ploy'

    id = db.Column(db.BigInteger, primary_key=True)
    enterprise_survey_id = db.Column(db.BigInteger, nullable=False, index=True)
    enterprise_id = db.Column(db.BigInteger, nullable=False, index=True)
    property_key = db.Column(db.String(200), nullable=False, info='属性KEY')
    property_value = db.Column(db.String(200), info='属性值')
    property_value_min = db.Column(db.Float(20, True), info='属性最小值')
    property_value_max = db.Column(db.Float(20, True), info='属性最大值')
    property_weight = db.Column(db.Integer, nullable=False, info='属性权重 0 不限 1 必须 2优先')
    if_inner_display = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否只有内部可见')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    temp_defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class TbEnterpriseTagDic(db.Model):
    __tablename__ = 'tb_enterprise_tag_dic'

    id = db.Column(db.BigInteger, primary_key=True, info='主键，系统生成')
    tag_rule_key = db.Column(db.String(63), nullable=False, index=True, server_default=db.FetchedValue(), info='标签code，不可重复；主要用于系统预定义标签与规则代码对应；人工标签则没什么意义')
    inner_name = db.Column(db.String(31), nullable=False, info='标签的内部显示名称；可重复')
    hh_display_name = db.Column(db.String(31), info='标签的HH端显示名称，可重复，展示前去重复')
    tdc_display_name = db.Column(db.String(31), info='TDC端显示名称')
    show_message = db.Column(db.String(255), info='弹窗提示文案')
    tag_type = db.Column(db.Integer, info='标签类型；1 系统标签：预定义，不可选择；2 人工标签：人工打标签使用；3 系统定义人工打标签')
    pay_rate = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='分成比例')
    start_time = db.Column(db.DateTime, info='标签有效时间的开始时间，可以为空，表示立即生效；')
    end_time = db.Column(db.DateTime, info='标签有效时间的结束时间，可以为空，表示不限时；')
    priority = db.Column(db.Integer, server_default=db.FetchedValue(), info='标签优先级，也就是排序值，越大越靠前')
    is_mutex = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否互斥；互斥的标签，只展示优先级最高的；职位中有一个是互斥标签，则不展示其它标签')
    is_filter = db.Column(db.Integer, server_default=db.FetchedValue(), info='所有标签在职位搜索都可以搜索；这个标记为是否展示给HH用户')
    is_hh_display = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否在HH端职位上展示这个标签')
    is_tdc_dispaly = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否在TDC端职位上展示这个标签')
    tag_style = db.Column(db.String(31), info='标签样式class')
    tag_rule_json = db.Column(db.String(1023), info='标签规则json')
    mutex_calculate_tags = db.Column(db.String(255), info='互斥可计算标签，为空则互斥所有')
    calculate_type = db.Column(db.Integer, info='标签计算类型：1：按天；2：实时')
    defunct = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='逻辑删除')
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_user_id = db.Column(db.BigInteger)



class TbEnterpriseTagRelation(db.Model):
    __tablename__ = 'tb_enterprise_tag_relation'
    __table_args__ = (
        db.Index('enterprise_id_tag_id', 'enterprise_id', 'tag_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    enterprise_id = db.Column(db.BigInteger, info='职位ID')
    tag_id = db.Column(db.BigInteger, info='关联的标签主键')
    calculate_type = db.Column(db.Integer, info='从tb_enterprise_tag_dic表冗余过来')
    tag_type = db.Column(db.Integer, index=True, info='从标签表冗余过来的字段')
    start_time = db.Column(db.DateTime, info='具体在职位上的有效时间开始')
    end_time = db.Column(db.DateTime, info='标签在职位上的有效时间的结束时间')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='逻辑删除；1 已删除')
    show_message = db.Column(db.String(255), info='标签文案，部分职位的文案跟职位信息相关')
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_user_id = db.Column(db.BigInteger)



class TbEnterpriseTag(db.Model):
    __tablename__ = 'tb_enterprise_tags'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    name = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='标签名称')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbEnterpriseUser(db.Model):
    __tablename__ = 'tb_enterprise_user'

    id = db.Column(db.BigInteger, primary_key=True)
    enterprise_id = db.Column(db.BigInteger, nullable=False, index=True)
    user_id = db.Column(db.BigInteger, nullable=False)
    root = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否删除0:正常 1:已删除')
    defunct_time = db.Column(db.DateTime, info='删除时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False, index=True)



class TbEnterpriseVisit(db.Model):
    __tablename__ = 'tb_enterprise_visit'
    __table_args__ = (
        db.Index('idx_visitorid_enterpriseid_visittime', 'visitor_id', 'enterprise_id', 'visit_time'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
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



class TbEnterpriseWhiteList(db.Model):
    __tablename__ = 'tb_enterprise_white_list'

    id = db.Column(db.BigInteger, primary_key=True)
    app_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0:HR;1:HD;2:C;')
    enterprise_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='企业编号')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())



class TbEvaluationRecord(db.Model):
    __tablename__ = 'tb_evaluation_record'
    __table_args__ = (
        db.Index('idx_hrid_hasevaluate', 'hr_id', 'has_evaluated'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    candidate_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='候选人id')
    headhunter_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='猎头ID')
    headhunter_company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎头公司ID')
    hr_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    position_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职位ID')
    has_evaluated = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否评价 0,未评价 1,已评价')
    if_anonymous = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否匿名 0,公开 1,匿名')
    level = db.Column(db.Integer, info='1,好评  2，中评  3，差评')
    content = db.Column(db.String(500), info='评价内容')
    candidate_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='候选人状态 0,拒绝 1,到岗 2，放弃到岗')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, info='更新者')
    update_time = db.Column(db.DateTime, info='更新时间')



class TbEventClock(db.Model):
    __tablename__ = 'tb_event_clock'
    __table_args__ = (
        db.Index('idx_event_clock_target_data_id_type', 'target_data_id', 'target_data_type'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    ps = db.Column(db.String(256), server_default=db.FetchedValue(), info='备注')
    event = db.Column(db.String(256), info='事件')
    event_url = db.Column(db.String(256), info='链接地址')
    user_id = db.Column(db.BigInteger, nullable=False, info='user_id')
    user_type = db.Column(db.Integer, nullable=False, info='user_type')
    event_date = db.Column(db.DateTime, nullable=False, info='提醒时间')
    create_date = db.Column(db.DateTime, nullable=False)
    update_date = db.Column(db.DateTime)
    task_type = db.Column(db.Integer, info='任务类型 1待沟通 2待推荐')
    target_type = db.Column(db.Integer, info='对象类型 1人才 2职位 3订单 5其他')
    status = db.Column(db.Integer, server_default=db.FetchedValue(), info='1完成 2待办')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除')
    target_name = db.Column(db.String(50), info='对象名字')
    is_notify = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否提醒')
    target_data_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='目标id')
    target_data_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='目标类型(1.职位2人才3,订单)')



class TbEventClockInput(db.Model):
    __tablename__ = 'tb_event_clock_input'

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, nullable=False)
    user_type = db.Column(db.Integer, nullable=False)
    record = db.Column(db.String(256), nullable=False, info='记录输入历史')
    ps = db.Column(db.String(256))
    create_date = db.Column(db.DateTime, nullable=False)



class TbFeedback(db.Model):
    __tablename__ = 'tb_feedback'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='反馈类型 0：建议， 1：Bug; 2: HH 职位搜索反馈')
    description = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='描述')
    attachment = db.Column(db.String(2000), info='附件，支持多个 json格式')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbFundAccount(db.Model):
    __tablename__ = 'tb_fund_account'

    id = db.Column(db.BigInteger, primary_key=True)
    account_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1:企业；2:个人')
    account_funds = db.Column(db.Numeric(10, 2), nullable=False, server_default=db.FetchedValue(), info='账户金额')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1:生效')
    last_modify_time = db.Column(db.DateTime, info='最后更新时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)



class TbFundAccountDetail(db.Model):
    __tablename__ = 'tb_fund_account_detail'

    id = db.Column(db.BigInteger, primary_key=True)
    account_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='账户编号')
    funds_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='资金变更人')
    funds_user_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='用户类型')
    funds_user_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='用户名称')
    trade_no = db.Column(db.BigInteger, info='商户订单号')
    account_action_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='操作类型；1:充值；2：消费；3：退款、4：提现')
    account_channel_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='行为类型1:支付宝充值;2:微信充值;3:背调购买服务;4：佣金服务')
    funds = db.Column(db.Numeric(10, 2), nullable=False, server_default=db.FetchedValue(), info='金额')
    after_funds = db.Column(db.Numeric(10, 2), nullable=False, server_default=db.FetchedValue(), info='变动后资金余额')
    remark = db.Column(db.String(500), info='备注')
    create_time = db.Column(db.DateTime, nullable=False)



class TbGrabDispatchMatch(db.Model):
    __tablename__ = 'tb_grab_dispatch_match'

    id = db.Column(db.BigInteger, primary_key=True, info='唯一编号')
    version_id = db.Column(db.String(50), info='匹配记录版本号')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='职位编号')
    candidate_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='订单编号')
    hunter_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎头编号')
    talent_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='人才编号')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0：已分配（今日派单）；1:待派单；2：已指派；3：派单成功（已推荐）')
    fail_status = db.Column(db.Integer, server_default=db.FetchedValue(), info='0：正常；1：pa拒绝；2猎头拒绝；3：PA超时失效；4：猎头超时失效；5：未首推失效；')
    fail_time = db.Column(db.DateTime)
    expire_time = db.Column(db.DateTime, info='派单任务失效时间')
    undetermined_time = db.Column(db.DateTime, info='待派单时间')
    dispatch_time = db.Column(db.DateTime, info='指派时间')
    reject_type = db.Column(db.Integer, info='1：pa；2：猎头')
    reject_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='操作拒绝人')
    reject_reason = db.Column(db.String(200), info='拒绝原因')
    reject_reason_expend = db.Column(db.String(200), info='拒绝理由扩展')
    matching_rate = db.Column(db.Float, info='匹配度')
    defunct_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='软删类型 1 派单上限 2 职位公开转私密  3 数据分析，职位下架')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    update_user_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='派单用户类型 1:HR,3:CRM')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbGrabDispatchOrder(db.Model):
    __tablename__ = 'tb_grab_dispatch_order'
    __table_args__ = (
        db.Index('idx_position_hh_company', 'position_id', 'headhunter_id', 'company_id'),
        db.Index('idx_headhunterid_companyid_defunct_dispatchordertime', 'headhunter_id', 'company_id', 'defunct', 'dispatch_order_time')
    )

    id = db.Column(db.BigInteger, primary_key=True, info='唯一主键')
    position_id = db.Column(db.BigInteger, nullable=False, info='职位id')
    headhunter_id = db.Column(db.BigInteger, nullable=False, info='猎头id')
    company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='公司编号')
    team = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1：个人，2：团队')
    received = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='1：已接收，0：未接受')
    is_reject = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否拒绝接受 0 否 1是')
    if_collect = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0:未收藏;1:已收藏')
    reject_reason = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='猎头端忽略原因')
    grab_order_time = db.Column(db.DateTime, info='抢单时间')
    dispatch_order_time = db.Column(db.DateTime, index=True, info='派单时间')
    extra_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='额外状态;0:正常;1:立项')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='是否删除 -> 1 : true 已删除；0 : false 有效')
    dispatch_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='派单人')
    dispatch_user_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='派单用户类型 1:HR,3:CRM')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    is_remove = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否移除 0 否 1 移除')
    remove_reason = db.Column(db.String(255), info='移除理由')
    expire_time = db.Column(db.DateTime, info='过期时间')
    complete_expire_time = db.Column(db.DateTime, info='完成过期时间')
    first_recommend_time = db.Column(db.DateTime, info='首次推荐的时间')
    dispatch_type = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='派单类型；0：人肉派单；1：机器匹配派单')
    match_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='匹配派单编号')
    recommend_status = db.Column(db.Integer, server_default=db.FetchedValue(), info='推荐状态 0:正常;1:已推荐')
    first_read_time = db.Column(db.DateTime, info='首次阅读时间')



class TbGrabDispatchOrderPosition(db.Model):
    __tablename__ = 'tb_grab_dispatch_order_position'

    id = db.Column(db.BigInteger, primary_key=True, info='唯一主键')
    position_id = db.Column(db.BigInteger, nullable=False)
    grab_hh_total = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='抢单猎头数')
    position_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info=' 0：需要申请 1：不需要申请 2：不能申请3:暂停申请,4:抢单职位')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False)



class TbGrabDispatchProgres(db.Model):
    __tablename__ = 'tb_grab_dispatch_progress'

    id = db.Column(db.BigInteger, primary_key=True, info='唯一编号')
    version_id = db.Column(db.String(50), index=True, info='版本号')
    sequence_id = db.Column(db.Integer, info='序号')
    match_type = db.Column(db.Integer, index=True, info='匹配类型;0:职位匹配订单；1:订单匹配职位')
    progress_type = db.Column(db.Integer, info='进程类型')
    progress_desc = db.Column(db.String(200), info='进程类型描述')
    position_id = db.Column(db.String(2047), info='职位编号')
    candidate_id = db.Column(db.String(14400), info='订单编号')
    talent_id = db.Column(db.String(4095), info='人才编号')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, index=True)
    update_time = db.Column(db.DateTime, nullable=False)



class TbGrabDispatchRemark(db.Model):
    __tablename__ = 'tb_grab_dispatch_remark'

    id = db.Column(db.BigInteger, primary_key=True, info='唯一编号')
    match_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='派单匹配编号')
    remark = db.Column(db.String(500), info='备注')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbGrabOrder(db.Model):
    __tablename__ = 'tb_grab_order'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='用户编号')
    position_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职位编号')
    seq_no = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='序列号')
    is_appoint = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否指定 -> 1 : true 已删除；0 : false 有效')
    is_certainly = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否使用抢比得 -> 1 : true 已删除；0 : false 有效')
    enroll_time = db.Column(db.DateTime, nullable=False, info='报名时间')
    grab_order_time = db.Column(db.DateTime, info='抢单时间')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0：预定中；1：抢单成功；2：抢单失败 ')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否无效 -> 1 : true 已删除；0 : false 有效')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbGrabOrderPosition(db.Model):
    __tablename__ = 'tb_grab_order_position'

    position_id = db.Column(db.BigInteger, primary_key=True, info='职位编号')
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='用户编号')
    user_grade = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='抢单猎头等级:0无等级,1:铜牌,2:银牌,3:金牌,4:钻,5:皇冠')
    valid_recommend_total = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='有效推荐数')
    task_cycle_day = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='任务周期 前端可能显示为1周、2周；后端需转换为天数')
    grab_order_total = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='抢单总数')
    enroll_begin_time = db.Column(db.DateTime, info='报名开始时间')
    task_begin_time = db.Column(db.DateTime, info='任务开始时间')
    task_end_time = db.Column(db.DateTime, info='任务结束时间')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0:新建；1：报名中；2：任务中；3：结束（任务周期结束）；4：结束（暂停职位）；5：结束（职位关闭）；6：结束（报名人数不足）')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbGrabOrderSchedule(db.Model):
    __tablename__ = 'tb_grab_order_schedule'

    user_id = db.Column(db.BigInteger, primary_key=True, info='用户编号')
    max_grab_total = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='可抢职位数量')
    already_grab_total = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='已抢职位数量')
    punish_expire_time = db.Column(db.DateTime, info='惩罚到期时间（可以为null)')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbGradeConfig(db.Model):
    __tablename__ = 'tb_grade_config'

    id = db.Column(db.BigInteger, primary_key=True)
    user_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='hd or hr')
    grade = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='等级')
    next_grade = db.Column(db.Integer, info='下一等级')
    min_value = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='所需最小值')
    max_value = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='所需最大值')
    upgrade_condition_id = db.Column(db.BigInteger, info='升级必要条件编号')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbGradeEnterprise(db.Model):
    __tablename__ = 'tb_grade_enterprise'

    id = db.Column(db.BigInteger, primary_key=True)
    enterprise_id = db.Column(db.BigInteger, nullable=False, index=True, info='雇主公司ID')
    total_reward = db.Column(db.Float(asdecimal=True), nullable=False, info='累计佣金')
    year_begin = db.Column(db.DateTime, nullable=False, index=True, info='年度时间范围，开始；2017-01-01')
    year_end = db.Column(db.DateTime, nullable=False, index=True, info='年度时间范围，开始；2017-12-31')
    operation_grade = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='运营等级')
    real_grade = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='实际等级')
    is_intervene = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否人工干预了等级；0：未干预，1：干预')
    create_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())



class TbGradeEnterpriseHistory(db.Model):
    __tablename__ = 'tb_grade_enterprise_history'

    id = db.Column(db.BigInteger, primary_key=True)
    enterprise_id = db.Column(db.BigInteger, nullable=False, index=True, info='雇主id')
    year_begin = db.Column(db.DateTime, nullable=False)
    year_end = db.Column(db.DateTime, nullable=False)
    total_reward = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='累计总佣金')
    operation_grade = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    real_grade = db.Column(db.Integer, nullable=False)
    grade_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info="等级类型：1：真实年度数据；2：截止统计'")
    create_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())



class TbGradeHeadhunter(db.Model):
    __tablename__ = 'tb_grade_headhunter'

    id = db.Column(db.BigInteger, primary_key=True)
    hh_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue())
    real_grade = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='真实猎头等级')
    operations_grade = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='人工运营等级')
    intervene = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否人工干预')
    calculate_begin_time = db.Column(db.DateTime, nullable=False)
    calculate_end_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())



class TbGradeHeadhunterFlowingRecord(db.Model):
    __tablename__ = 'tb_grade_headhunter_flowing_record'

    id = db.Column(db.BigInteger, primary_key=True)
    hh_id = db.Column(db.BigInteger, nullable=False)
    grade = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='猎头等级')
    onboard_commission = db.Column(db.Float(asdecimal=True), nullable=False, info='到岗佣金')
    valid_recommend_count = db.Column(db.BigInteger, nullable=False, info='有效推荐数')
    interview_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='面试率')
    offer_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='offer率')
    onboard_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='到岗率')
    calculate_begin_time = db.Column(db.DateTime, nullable=False)
    calculate_end_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())



class TbGradeHeadhunterHistory(db.Model):
    __tablename__ = 'tb_grade_headhunter_history'

    id = db.Column(db.BigInteger, primary_key=True)
    hh_id = db.Column(db.BigInteger, nullable=False, index=True)
    grade = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='猎头等级')
    onboard_commission = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='到岗佣金')
    valid_recommend_count = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='有效推荐数')
    interview_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='面试率')
    offer_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='offer率')
    onboard_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='到岗率')
    grade_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='任务执行类型：0:每天执行(下期)   1:季末执行(历史、当期) ')
    calculate_begin_time = db.Column(db.DateTime, nullable=False, index=True)
    calculate_end_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    get_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    effective_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    current_quarter = db.Column(db.String(200))
    next_quarter = db.Column(db.String(200))



class TbGradeHeadhunterPrivilege(db.Model):
    __tablename__ = 'tb_grade_headhunter_privilege'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    hh_id = db.Column(db.BigInteger, index=True, info='猎头ID')
    enterprise_id = db.Column(db.BigInteger, info='猎头企业ID')
    grade = db.Column(db.Integer, info='猎头等级')
    privilege_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='特权类型：1,免申请；2,抢单')
    operate_receive_count = db.Column(db.Integer, info='操作领取次数,即领取特权的次数')
    receive_count = db.Column(db.Integer, info='领取后总使用次数（周期内）')
    remainder_count = db.Column(db.Integer, info='余额次数:-1代表无数次')
    start_time = db.Column(db.DateTime, info='特权开始时间')
    expire_time = db.Column(db.DateTime, info='过期时间')
    cycle_key = db.Column(db.String(20), info='特权周期值')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否删除0:false 1:true')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='修改时间')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    update_user_id = db.Column(db.BigInteger, info='修改人')



class TbGradeHeadhunterPrivilegeRecord(db.Model):
    __tablename__ = 'tb_grade_headhunter_privilege_record'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    hh_id = db.Column(db.BigInteger, nullable=False, info='猎头ID')
    position_id = db.Column(db.BigInteger, nullable=False, info='职位id')
    enterprise_id = db.Column(db.BigInteger, nullable=False, info='企业id')
    privilege_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='特权类型：1,免申请；2,抢单')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除 0:未删除 1:已删除')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())



class TbGradeHhCompany(db.Model):
    __tablename__ = 'tb_grade_hh_company'

    id = db.Column(db.BigInteger, primary_key=True)
    company_id = db.Column(db.BigInteger, nullable=False, index=True)
    real_grade = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='真实猎企等级')
    operations_grade = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='人工运营等级')
    intervene = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否人工干预')
    calculate_begin_time = db.Column(db.DateTime, nullable=False)
    calculate_end_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())



class TbGradeHhCompanyFlowingRecord(db.Model):
    __tablename__ = 'tb_grade_hh_company_flowing_record'

    id = db.Column(db.BigInteger, primary_key=True)
    company_id = db.Column(db.BigInteger, nullable=False)
    grade = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='猎企等级')
    onboard_commission = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='到岗佣金总额')
    crown_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='皇冠顾问数量 ')
    diamond_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='钻石顾问数量 ')
    platinum_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='铂金顾问数量 ')
    gold_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='金牌顾问数量 ')
    silver_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='银牌顾问数量 ')
    cuprum_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='皇冠顾问数量 ')
    calculate_begin_time = db.Column(db.DateTime, nullable=False)
    calculate_end_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())



class TbGradeHhCompanyHistory(db.Model):
    __tablename__ = 'tb_grade_hh_company_history'

    id = db.Column(db.BigInteger, primary_key=True)
    company_id = db.Column(db.BigInteger, nullable=False)
    grade = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='猎企等级')
    onboard_commission = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='到岗佣金总额')
    crown_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='皇冠顾问数量 ')
    diamond_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='钻石顾问数量 ')
    platinum_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='铂金顾问数量 ')
    gold_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='金牌顾问数量 ')
    silver_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='银牌顾问数量 ')
    cuprum_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='皇冠顾问数量 ')
    grade_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='任务执行类型：0:每天执行(下期)   1:季末执行(历史、当期) ')
    calculate_begin_time = db.Column(db.DateTime, nullable=False)
    calculate_end_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    headhunter_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='公司猎头数量 ')



class TbGradeHr(db.Model):
    __tablename__ = 'tb_grade_hr'

    id = db.Column(db.BigInteger, primary_key=True)
    hr_id = db.Column(db.BigInteger, nullable=False, index=True, info='hrid')
    quarter_begin = db.Column(db.DateTime, nullable=False, info='等级有效时间，开始；2017-01-01')
    quarter_end = db.Column(db.DateTime, nullable=False, info='等级有效时间的，结束；2017-03-31')
    total_integral = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    operation_grade = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='运营等级，作为后续资源依据')
    real_grade = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='系统计算的实际等级')
    is_intervene = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否人工干预了等级配置；0：未干预，1：干预')
    create_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())



class TbGradeHrHistory(db.Model):
    __tablename__ = 'tb_grade_hr_history'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    hr_id = db.Column(db.BigInteger, nullable=False, index=True)
    quarter_begin = db.Column(db.DateTime, nullable=False, info='等级有效时间的，开始；2017-01-01')
    quarter_end = db.Column(db.DateTime, nullable=False, info='等级有效时间的，结束；2017-03-31')
    total_integral = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    operation_grade = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    real_grade = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='实际计算的等级')
    grade_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='等级类型：1：真实季度；2：截止统计')
    create_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())



class TbGroup(db.Model):
    __tablename__ = 'tb_group'
    __table_args__ = (
        db.Index('idx_status_company_id_app_id', 'status', 'company_id', 'app_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键Id')
    group_name = db.Column(db.String(256), nullable=False, info='组名称')
    parent_id = db.Column(db.BigInteger, nullable=False, info='父组Id')
    status = db.Column(db.Integer, nullable=False, info='1:有效,0:删除')
    company_id = db.Column(db.BigInteger, nullable=False, info='公司Id')
    app_id = db.Column(db.Integer, nullable=False, info='应用Id 0:hr 1:hd')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, info='修改用户Id')



class TbGroupEnterprise(db.Model):
    __tablename__ = 'tb_group_enterprise'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    name = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='集团名称')
    remark = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='备注')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    root_user_id = db.Column(db.BigInteger, nullable=False, info='集团hrId')
    exclusion_current_repeat_status = db.Column(db.String(255), info='过滤集团本公司排序状态')
    exclusion_other_repeat_status = db.Column(db.String(255), info='过滤集团其它公司排序状态')



class TbGroupEnterpriseRelation(db.Model):
    __tablename__ = 'tb_group_enterprise_relation'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    group_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='集团id')
    enterprise_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='企业id')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    recommend_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='推荐筛选:0:否,1:是')
    report_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='报表筛选:0:否,1:是')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='逻辑删除 0：未删除，1：已删除')



class TbGroupLeader(db.Model):
    __tablename__ = 'tb_group_leader'

    id = db.Column(db.BigInteger, primary_key=True)
    group_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue())
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    company_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue())
    app_id = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())



class TbGroupMenu(db.Model):
    __tablename__ = 'tb_group_menu'
    __table_args__ = (
        db.Index('idx_group_id_company_id_app_id', 'group_id', 'company_id', 'app_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键Id')
    group_id = db.Column(db.BigInteger, nullable=False, info='组Id')
    menu_id = db.Column(db.BigInteger, nullable=False, info='菜单Id')
    company_id = db.Column(db.BigInteger, nullable=False, info='公司Id')
    app_id = db.Column(db.Integer, nullable=False, info='应用Id 0:hr 1:hd')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, info='修改人')



class TbGroupOperation(db.Model):
    __tablename__ = 'tb_group_operation'
    __table_args__ = (
        db.Index('idx_group_id_company_id_app_id', 'group_id', 'company_id', 'app_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键Id')
    operation_id = db.Column(db.BigInteger, nullable=False, info='操作Id')
    group_id = db.Column(db.BigInteger, nullable=False, info='组Id')
    company_id = db.Column(db.BigInteger, nullable=False, info='公司Id')
    app_id = db.Column(db.Integer, nullable=False, info='应用Id 0:hr 1:hd')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, info='修改人')



class TbGroupUser(db.Model):
    __tablename__ = 'tb_group_user'
    __table_args__ = (
        db.Index('idx_company_id_app_id', 'company_id', 'app_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键Id')
    group_id = db.Column(db.BigInteger, nullable=False, index=True, info='组Id')
    user_id = db.Column(db.BigInteger, nullable=False, info='用户Id')
    company_id = db.Column(db.BigInteger, nullable=False, info='公司Id')
    app_id = db.Column(db.Integer, nullable=False, info='应用Id ')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建者的Id')
    update_time = db.Column(db.DateTime, nullable=False, info='修改的时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, info='最后一次修改的用户Id')
    is_leader = db.Column(db.Integer, nullable=False, info='角色Id')



class TbHd3BetatestUser(db.Model):
    __tablename__ = 'tb_hd3_betatest_user'
    __table_args__ = (
        db.Index('idx_userid_defunct', 'user_id', 'defunct'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue())
    company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    soho = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)



class TbHdBetaTestCompany(db.Model):
    __tablename__ = 'tb_hd_beta_test_company'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='公司ID')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbHeadhunterBadge(db.Model):
    __tablename__ = 'tb_headhunter_badge'

    id = db.Column(db.BigInteger, primary_key=True)
    headhunter_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎头id')
    badge_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='徽章类型，1：超级猎头，2：高薪必配，3：使命必达，4：每月杰出，7：手动推荐')
    badge_source = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='数据来源，0：系统筛选，1：CRM编辑')
    sort_no = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='排序顺序，CRM编辑的数据从1000000000开始')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人ID')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新人ID')



class TbHeadhunterBlack(db.Model):
    __tablename__ = 'tb_headhunter_black'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    headhunter_id = db.Column(db.BigInteger, nullable=False, index=True, info='猎头Id')
    scope = db.Column(db.Integer, server_default=db.FetchedValue(), info='小黑屋范围1HR,2雇主,3.派系,4全平台')
    scope_id = db.Column(db.BigInteger, info='被关对象Id')
    scope_description = db.Column(db.String(50), info='范围描述')
    day = db.Column(db.Integer, server_default=db.FetchedValue(), info='被关天数,999为永久')
    begin_time = db.Column(db.DateTime, info='被关开始时间')
    end_time = db.Column(db.DateTime, info='被关结束时间')
    opera_user_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='操作用户类型 1:HR,2:HH,3:CRM')
    opera_user_id = db.Column(db.BigInteger, nullable=False, info='操作用户')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='逻辑删除')
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue())



class TbHeadhunterCommunicationRecord(db.Model):
    __tablename__ = 'tb_headhunter_communication_record'

    id = db.Column(db.BigInteger, primary_key=True, info='唯一主键')
    communicate_time = db.Column(db.DateTime, info='沟通时间')
    headhunter_id = db.Column(db.BigInteger, info='跟进人id')
    company_id = db.Column(db.BigInteger, index=True, info='公司id')
    target_data_id = db.Column(db.BigInteger, index=True, info='目标id')
    target_data_type = db.Column(db.Integer, info='沟通目标类型（1.职位2人才）')
    headhunter_name = db.Column(db.String(30), info='跟进人')
    communicate_id = db.Column(db.BigInteger, info='沟通对象id')
    communicate_type = db.Column(db.Integer, info='沟通对象类型（1.HR2.PA3.其他）')
    communicate_name = db.Column(db.String(30), info='沟通对象')
    communicate_content = db.Column(db.String(3000), server_default=db.FetchedValue(), info='沟通内容')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除')
    createUserId = db.Column(db.BigInteger)
    createTime = db.Column(db.DateTime)
    updateUserId = db.Column(db.BigInteger)
    updateTime = db.Column(db.DateTime)
    contact_type = db.Column(db.Integer, info='联系类型（1.陌生寻访 2.跟踪联系 3.面试联系 4.背景调查 5.跟踪服务 6.备注）')
    contact_way = db.Column(db.Integer, info='联系方式（1.电话、2.微信QQ、3.Email、4.面谈）')
    followup_status = db.Column(db.Integer, info='跟进状态（1.在跟进2不在跟进）')
    commnunicate_number = db.Column(db.String(30), info='联系电话')



class TbHeadhunterCompanyPosition(db.Model):
    __tablename__ = 'tb_headhunter_company_position'

    id = db.Column(db.BigInteger, primary_key=True)
    company_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='猎头公司id')
    enterprise_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='企业id')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='职位id')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除 0:未删除 1:已删除')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改者')
    source_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='数据来源类型')



class TbHeadhunterCompetence(db.Model):
    __tablename__ = 'tb_headhunter_competence'
    __table_args__ = (
        db.Index('index_1', 'headhunter_id', 'company_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    headhunter_id = db.Column(db.BigInteger, nullable=False, info='猎头id')
    company_id = db.Column(db.BigInteger, nullable=False, info='公司id')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='做单状态,0为无权限,1为正常,2为离职')
    title = db.Column(db.Integer, info='猎头头衔')
    industry_scope = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='做单行业范围 多个逗号隔开')
    function_scope = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='做单职能范围 多个逗号隔开')
    city_scope = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='做单城市范围 多个逗号隔开')
    position_level_scope = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='做单职级范围 多个逗号隔开')
    company_develop_status_scope = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='做单范围公司阶段 多个逗号隔开')
    function_original_ids = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='原始职能ID 多个逗号隔开')
    function_keywords = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue(), info='职能关键字（由职能ID转换而来）')
    function_keyword_ids = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='职能关键字ID 多个逗号隔开')
    create_user_id = db.Column(db.BigInteger, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbHeadhunterConcernTalent(db.Model):
    __tablename__ = 'tb_headhunter_concern_talent'

    id = db.Column(db.BigInteger, primary_key=True)
    headhunter_id = db.Column(db.BigInteger, nullable=False, info='猎头id')
    company_id = db.Column(db.BigInteger, nullable=False, info='猎企id')
    talent_id = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='外部人才id')
    source = db.Column(db.Integer, nullable=False, info='关注来源，1：孵化器；2：人才市场')
    create_time = db.Column(db.DateTime, nullable=False, index=True)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())



class TbHeadhunterDimissionSnapshot(db.Model):
    __tablename__ = 'tb_headhunter_dimission_snapshot'

    id = db.Column(db.BigInteger, primary_key=True)
    headhunter_id = db.Column(db.BigInteger, nullable=False, info='猎头id')
    company_id = db.Column(db.BigInteger, nullable=False, info='公司id')
    portrait_snapshot = db.Column(db.MEDIUMBLOB, nullable=False, info='快照json字符串')
    create_user_id = db.Column(db.BigInteger, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbHeadhunterDistribution(db.Model):
    __tablename__ = 'tb_headhunter_distribution'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    jobhunter_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='c端用户id')
    position_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职位id')
    jobhunter_record_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='投递记录id')
    headhunter_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎头id')
    company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎头所在公司ID')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0:待抢,1:已抢,2:已被抢')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    headhunter_delete = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='猎头删除，默认为false')
    readed = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否已读，默认为false未读')
    handle_time = db.Column(db.DateTime, info='抢单时间')
    first_readed = db.Column(db.Integer, server_default=db.FetchedValue(), info='猎头第一次进入抢人才界面读')
    c_read = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='c是否已读')
    c_send_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0:自动，1:手动')
    source = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0:C,1:HD')
    entrust_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='委托类型，默认主动委托，1被动委托')



class TbHeadhunterEvaluatePosition(db.Model):
    __tablename__ = 'tb_headhunter_evaluate_position'

    id = db.Column(db.BigInteger, primary_key=True)
    headhunter_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎头id')
    position_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职位id')
    score = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='分数')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除,0:false,1:true')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbHeadhunterOperationUser(db.Model):
    __tablename__ = 'tb_headhunter_operation_user'
    __table_args__ = (
        db.Index('idx_user_hh_id', 'user_id', 'headhunter_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='自增编号')
    user_id = db.Column(db.BigInteger, nullable=False, info='用户编号（运营PA）')
    headhunter_id = db.Column(db.BigInteger, nullable=False, index=True, info='猎头编号')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='逻辑删除 0：未删除，1：已删除')



class TbHeadhunterPloy(db.Model):
    __tablename__ = 'tb_headhunter_ploy'

    headhunter_id = db.Column(db.BigInteger, primary_key=True, server_default=db.FetchedValue(), info='猎头ID')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建者')
    update_time = db.Column(db.DateTime, info='更新时间')
    update_user_id = db.Column(db.BigInteger, info='更新者')
    yingyan_count = db.Column(db.Integer, server_default=db.FetchedValue(), info='鹰眼可用次数')
    service_start_time = db.Column(db.BigInteger, info='服务开始时间')
    service_end_time = db.Column(db.BigInteger, info='服务结束时间')
    service_switch = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='服务开关  0:关闭  1 开启')
    refresh_time = db.Column(db.DateTime, info='刷新时间')



class TbHeadhunterPosition(db.Model):
    __tablename__ = 'tb_headhunter_position'

    id = db.Column(db.BigInteger, primary_key=True)
    headhunter_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='猎头id')
    enterprise_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='企业id')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='职位id')
    is_important = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否重要职位,0:false,1:true')
    is_grab_order = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否抢单职位,0:false,1:true')
    grab_order_reserve_time = db.Column(db.DateTime, info='抢单预定时间')
    grab_order_time = db.Column(db.DateTime, info='抢单时间')
    grab_order_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='抢单状态0:默认状态；1:申请中；2:成功；3:失败；')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除 0:未删除 1:已删除')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    source_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='数据来源类型')
    color_tag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0不限， 1红， 2蓝， 3绿， 4黄， 5紫')



class TbHeadhunterRecruitSpecial(db.Model):
    __tablename__ = 'tb_headhunter_recruit_special'

    id = db.Column(db.BigInteger, primary_key=True)
    recruit_special_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='专场id')
    headhunter_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎头id')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除 0:未删除 1:已删除')



class TbHeadhunterSubordinateApply(db.Model):
    __tablename__ = 'tb_headhunter_subordinate_apply'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    name = db.Column(db.String(128), index=True, info='姓名')
    mobile = db.Column(db.String(64), index=True, info='手机')
    industry_id = db.Column(db.String(256), info='行业')
    function_id = db.Column(db.String(256), info='职能')
    performance = db.Column(db.String(1024), info='年化业绩')
    expect_proportion = db.Column(db.Integer, info='期望分成比例')
    defunct = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='是否删除0:false 1:true')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='修改时间')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    update_user_id = db.Column(db.BigInteger, info='修改人')



class TbHeadhunterSystemTag(db.Model):
    __tablename__ = 'tb_headhunter_system_tag'
    __table_args__ = (
        db.Index('idx_hh_system_tag_industry_function_city_ids_annual_salary', 'industry_ids', 'position_title_ids', 'annual_salary_levels', 'city_ids', 'defunct'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='自增ID')
    hh_id = db.Column(db.BigInteger, index=True, info='猎头ID')
    industry_ids = db.Column(db.String(128), info='行业')
    position_title_ids = db.Column(db.String(128), info='职能')
    annual_salary_levels = db.Column(db.String(64), info='年薪职级 1: 30万以下, 2: 30-50万, 3: 50-100万, 4: 100-200万, 5: 200万以上')
    city_ids = db.Column(db.String(128), info='城市ID')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='更新时间')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否删除 0 否 1 是')



class TbHeadhunterValid(db.Model):
    __tablename__ = 'tb_headhunter_valid'

    id = db.Column(db.BigInteger, primary_key=True)
    headhunter_id = db.Column(db.BigInteger, nullable=False, info='headhunter id')
    pa_id = db.Column(db.BigInteger, nullable=False, info='pa id')
    sys_assian = db.Column(db.Integer, server_default=db.FetchedValue(), info='系统设置 0 无效 1 有效')
    user_assian = db.Column(db.Integer, server_default=db.FetchedValue(), info='用户设置  0 无效 1 有效')
    create_time = db.Column(db.DateTime, info='创建时间')
    create_user = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime, info='修改时间')
    update_user = db.Column(db.BigInteger)
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class TbHeadhunterWorkApply(db.Model):
    __tablename__ = 'tb_headhunter_work_apply'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    name = db.Column(db.String(128), index=True, info='姓名')
    mobile = db.Column(db.String(64), index=True, info='手机')
    industry_id = db.Column(db.String(256), info='行业')
    function_id = db.Column(db.String(256), info='职能')
    recently_company_name = db.Column(db.String(128), index=True, info='最近猎企名字')
    current_basic_salary = db.Column(db.Integer, info='目前底薪')
    expect_basic_salary = db.Column(db.Integer, info='期望底薪')
    performance = db.Column(db.String(1024), info='年化业绩')
    purpose_city_id = db.Column(db.String(256), info='意向城市ID')
    defunct = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='是否删除0:false 1:true')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='修改时间')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    update_user_id = db.Column(db.BigInteger, info='修改人')



class TbHeadline(db.Model):
    __tablename__ = 'tb_headlines'

    id = db.Column(db.BigInteger, primary_key=True, info='猎上头条id')
    item_logo_path = db.Column(db.String(1024), nullable=False, server_default=db.FetchedValue(), info='猎上头条logo')
    item_title = db.Column(db.String(512), nullable=False, server_default=db.FetchedValue(), info='猎上头条标题')
    item_sub_title = db.Column(db.String(512), nullable=False, server_default=db.FetchedValue(), info='猎上头条次标题')
    item_link = db.Column(db.String(1024), nullable=False, server_default=db.FetchedValue(), info='猎上头条功能连接（单条详情连接）')
    home_link = db.Column(db.String(1024), nullable=False, server_default=db.FetchedValue(), info='首页链接')
    platform = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='平台： 1 : HR; 2 : HD; 3 : HC;')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否无效：1,已删除；0,有效')
    sort_no = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序index')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)



class TbHelpFeedback(db.Model):
    __tablename__ = 'tb_help_feedback'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    platform_type = db.Column(db.Integer, info='展示的平台类型，1：HR，2：HH，3：C，4：all;')
    user_id = db.Column(db.BigInteger, info='用户ID')
    user_name = db.Column(db.String(255), info='用户名称')
    user_code = db.Column(db.String(255), info='用户Code、手机号')
    help_link_id = db.Column(db.BigInteger, info='帮忙中心帖子ID')
    help_link_code = db.Column(db.String(255), info='帮忙中心帖子Code')
    operate_type = db.Column(db.Integer, info='操作类型(1：解决与否；2：评分)')
    operate_value = db.Column(db.String(255), info='操作值')
    operate_ip = db.Column(db.String(255), server_default=db.FetchedValue(), info='操作IP')
    remark = db.Column(db.String(255), info='备注')
    update_user_id = db.Column(db.BigInteger, info='修改人')
    update_time = db.Column(db.DateTime, info='修改时间')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    create_time = db.Column(db.DateTime, info='创建时间')



class TbHh(db.Model):
    __tablename__ = 'tb_hh'

    user_id = db.Column(db.BigInteger, primary_key=True)



class TbHhCategoryLog(db.Model):
    __tablename__ = 'tb_hh_category_log'

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, nullable=False, info='猎头id')
    service_admin = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='对应ho.user表中的service_admin')
    hh_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='猎头类型:1:Named类猎头, 2:A类猎头, 3:B类猎头,4:C类猎头,5:D类猎头,6:E类猎头')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')



class TbHhCompanyStatistic(db.Model):
    __tablename__ = 'tb_hh_company_statistics'

    company_id = db.Column(db.BigInteger, primary_key=True)
    activeness = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='活跃度')
    offer_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='offer率')
    interview_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='面试率')
    integration = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='综合')
    recommand_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='推荐数')
    interview_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='面试数')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    placement_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='近三个月成单')
    revoke_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='撤销数')
    revoke_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='撤销率')
    recommend_quality = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='推荐质量')
    server_quality = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='服务质量')
    industry_preference = db.Column(db.String(5000), nullable=False, server_default=db.FetchedValue(), info='行业偏好json格式')
    area_preference = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='地区偏好json格式')
    jobtitle_preference = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='职能偏好json格式')
    phase_preference = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='公司阶段偏好json格式')
    domian_preference = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='领域偏好json格式')
    level_preference = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='职级偏好json格式')
    enterprise_level = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='客户类型')



class TbHhDataLog(db.Model):
    __tablename__ = 'tb_hh_data_log'

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, nullable=False, index=True, info='猎头id')
    em_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    bdh_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎企id')
    placement_reward = db.Column(db.Float, nullable=False, server_default=db.FetchedValue(), info='实际成单佣金')
    candidate_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='推荐数')
    interview_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='面试数')
    placement_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='成单数')
    onboard_on_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='到岗数')
    onboard_left_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='离岗数')
    count_date = db.Column(db.Date, nullable=False, index=True, info='统计时间')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbHhNamed(db.Model):
    __tablename__ = 'tb_hh_named'

    user_id = db.Column(db.BigInteger, primary_key=True, info='猎头id')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbHhPortrait(db.Model):
    __tablename__ = 'tb_hh_portrait'

    user_id = db.Column(db.BigInteger, primary_key=True, info='猎头id')
    recommand_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='推荐数')
    interview_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='面试数')
    placement_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='成单数')
    offer_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='offer率')
    interview_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='面试率')
    revoke_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='撤销率')
    recommend_quality = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='推荐质量')
    server_quality = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='服务质量')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    login_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='登录次数')
    last_recommend_time = db.Column(db.DateTime, info='最后一次推荐时间')
    hh_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='猎头类型:1:Named类猎头, 2:A类猎头, 3:B类猎头,4:C类猎头,5:D类猎头,6:E类猎头')
    month_placement_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='月成单数')
    month_interview_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='月面试数')
    is_by_recommend = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否通过满足推荐条件统计')
    industry_preference = db.Column(db.String(5000), nullable=False, server_default=db.FetchedValue(), info='行业偏好json格式')
    area_preference = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='地区偏好json格式')
    jobtitle_preference = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='职能偏好json格式')
    phase_preference = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='公司阶段偏好json格式')
    domian_preference = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='领域偏好json格式')
    level_preference = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='职级偏好json格式')
    enterprise_level = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='客户类型')



class TbHhStatistic(db.Model):
    __tablename__ = 'tb_hh_statistics'

    user_id = db.Column(db.BigInteger, primary_key=True)
    activeness = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='活跃度')
    offer_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='offer率')
    interview_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='面试率')
    integration = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='综合')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    recommand_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='推荐数')
    interview_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='面试数')
    placement_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='近三个月成单')
    recommend_quality = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='推荐质量')
    server_quality = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='服务质量')



class TbHhType(db.Model):
    __tablename__ = 'tb_hh_type'

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, nullable=False, index=True, info='用户id')
    bdh_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    em_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    hh_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='用户类型 1：新用户，2：僵尸用户，3：沉默用户，4：菜鸟用户，5：碎片用户，6：重度活跃，7：中度活跃，8：轻度活跃')
    count_date = db.Column(db.Date, nullable=False, index=True, info='统计时间')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbHhType20180101(db.Model):
    __tablename__ = 'tb_hh_type_20180101'

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, nullable=False, index=True, info='用户id')
    bdh_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    em_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    hh_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='用户类型 1：新用户，2：僵尸用户，3：沉默用户，4：菜鸟用户，5：碎片用户，6：重度活跃，7：中度活跃，8：轻度活跃')
    count_date = db.Column(db.Date, nullable=False, info='统计时间')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbHhTypeCurrent(db.Model):
    __tablename__ = 'tb_hh_type_current'

    user_id = db.Column(db.BigInteger, primary_key=True, info='猎头id')
    hh_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='猎头类型')
    count_date = db.Column(db.Date, nullable=False, info='统计日期')
    create_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())



class TbHighCvContact(db.Model):
    __tablename__ = 'tb_high_cv_contact'
    __table_args__ = (
        db.Index('idx_high_cv_contact_high_cv_id_talent_id_contact_id_defunct', 'talent_id', 'high_cv_id', 'contact_id', 'defunct'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    high_cv_id = db.Column(db.BigInteger, nullable=False, info='高端cvid')
    talent_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='简历id')
    contact_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='联系人id')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class TbHighQualityCompany(db.Model):
    __tablename__ = 'tb_high_quality_company'

    id = db.Column(db.BigInteger, primary_key=True)
    company_id = db.Column(db.BigInteger, nullable=False, info='企业id')
    company_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='企业名称')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0未删除，1 删除')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbHistoryLog(db.Model):
    __tablename__ = 'tb_history_log'

    id = db.Column(db.BigInteger, primary_key=True, info='pk')
    table_id = db.Column(db.Integer, nullable=False, index=True, info='表名')
    table_pk = db.Column(db.BigInteger, nullable=False, index=True)
    min_data = db.Column(db.String(500), info='存json格式数据、长度最大500')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建者Id')
    user_type = db.Column(db.Integer, nullable=False, info='创建者类型')
    operate_type = db.Column(db.Integer, index=True, info='操作类型')
    after_data = db.Column(db.String(500), info='修改之后数据json')



class TbHoliday(db.Model):
    __tablename__ = 'tb_holiday'

    id = db.Column(db.BigInteger, primary_key=True)
    day = db.Column(db.String(8), nullable=False, info='日期 yyyyMMdd')
    type = db.Column(db.Integer, nullable=False, info='1：休息日；2：节假日')



class TbHomailActionLog(db.Model):
    __tablename__ = 'tb_homail_action_log'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    scheduler_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='任务编号')
    send_total = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='发送人数')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='逻辑删除')
    create_user_id = db.Column(db.BigInteger, info='创建数据的用户ID')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_user_id = db.Column(db.BigInteger, info='更新数据的用户ID')
    update_time = db.Column(db.DateTime, info='更新时间')



class TbHomailDataTemplate(db.Model):
    __tablename__ = 'tb_homail_data_templates'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    bean_name = db.Column(db.String(127), nullable=False, info='数据模板对应springbean的名字')
    title = db.Column(db.String(127), info='数据模板对应的场景名称')
    info = db.Column(db.String(255), info='场景描述')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='逻辑删除')
    create_user_id = db.Column(db.BigInteger, info='创建数据的用户ID')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_user_id = db.Column(db.BigInteger, info='更新数据的用户ID')
    update_time = db.Column(db.DateTime, info='更新时间')



class TbHomailDisplayTemplate(db.Model):
    __tablename__ = 'tb_homail_display_templates'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    name = db.Column(db.String(127), info='名称')
    title = db.Column(db.String(255), info='邮件主题')
    content = db.Column(db.String, info='邮件内容')
    data_template_id = db.Column(db.BigInteger, index=True, info='数据模板表主键')
    data_template_bean = db.Column(db.String(127), info='数据模板表，bean_name，冗余')
    template_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='模板类型；1:人工模板；2：系统模板')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='逻辑删除')
    create_user_id = db.Column(db.BigInteger, info='创建数据的用户ID')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_user_id = db.Column(db.BigInteger, info='更新数据的用户ID')
    update_time = db.Column(db.DateTime, info='更新时间')



class TbHomailDisplayTemplatesSnapshot(db.Model):
    __tablename__ = 'tb_homail_display_templates_snapshot'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    name = db.Column(db.String(127), info='名称')
    title = db.Column(db.String(255), info='邮件主题')
    content = db.Column(db.String, info='邮件内容')
    data_template_id = db.Column(db.BigInteger, index=True, info='数据模板表主键')
    data_template_bean = db.Column(db.String(127), info='数据模板表，bean_name，冗余')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='逻辑删除')
    create_user_id = db.Column(db.BigInteger, info='创建数据的用户ID')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_user_id = db.Column(db.BigInteger, info='更新数据的用户ID')
    update_time = db.Column(db.DateTime, info='更新时间')



class TbHomailSchedulerData(db.Model):
    __tablename__ = 'tb_homail_scheduler_datas'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    scheduler_id = db.Column(db.BigInteger, index=True, info='邮件任务表主键')
    data_type = db.Column(db.Integer, info='数据源类型（1:职位）')
    data_id = db.Column(db.BigInteger, info='数据源id')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='逻辑删除')
    create_user_id = db.Column(db.BigInteger, info='创建数据的用户ID')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_user_id = db.Column(db.BigInteger, info='更新数据的用户ID')
    update_time = db.Column(db.DateTime, info='更新时间')



class TbHomailSchedulerUser(db.Model):
    __tablename__ = 'tb_homail_scheduler_users'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    scheduler_id = db.Column(db.BigInteger, index=True, info='邮件任务表主键')
    user_id = db.Column(db.BigInteger, info='用户ID')
    email = db.Column(db.String(50), info='指定邮箱')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='逻辑删除')
    create_user_id = db.Column(db.BigInteger, info='创建数据的用户ID')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_user_id = db.Column(db.BigInteger, info='更新数据的用户ID')
    update_time = db.Column(db.DateTime, info='更新时间')



class TbHomailScheduler(db.Model):
    __tablename__ = 'tb_homail_schedulers'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    name = db.Column(db.String(127), info='邮件任务名称')
    data_template_id = db.Column(db.BigInteger, info='数据模板表主键')
    display_template_id = db.Column(db.BigInteger, info='显示模板snapshot表主键')
    user_template_id = db.Column(db.BigInteger, info='第三方用户数据模板表主键')
    user_template_types = db.Column(db.String(127), info='第三方用户数据源子类型表主键')
    user_type = db.Column(db.Integer, info='邮件任务中，用户数据源类型；1：数据模板指定；2：用户手动导入；3：第三方数据源指定')
    task_type = db.Column(db.Integer, info='任务触发类型：手动执行；2：自动执行')
    cron = db.Column(db.String(31), info='任务的时间表达式')
    task_status = db.Column(db.Integer, info='任务的状态；1：正常；2：停止')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='逻辑删除')
    create_user_id = db.Column(db.BigInteger, info='创建数据的用户ID')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_user_id = db.Column(db.BigInteger, info='更新数据的用户ID')
    update_time = db.Column(db.DateTime, info='更新时间')
    max_send_count = db.Column(db.Integer, info='最大发送数量')



class TbHomailSendBdMatch(db.Model):
    __tablename__ = 'tb_homail_send_bd_match'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    send_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='发送邮件记录编号：tb_homail_send_log.id')
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='用户编号')
    enterpid_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='雇主编号')
    match_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='人职包编号')
    create_user_id = db.Column(db.BigInteger, info='创建数据的用户ID')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_user_id = db.Column(db.BigInteger, info='更新数据的用户ID')
    update_time = db.Column(db.DateTime, info='更新时间')



class TbHomailSendLog(db.Model):
    __tablename__ = 'tb_homail_send_log'
    __table_args__ = (
        db.Index('HOMAIL_SEND_LOG_ACTION_ID_UU_ID', 'action_id', 'uu_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    action_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='操作id,tb_homail_action_log的主键')
    uu_id = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='uuId,用于邮件拼接链接参数识别邮件发送记录')
    scheduler_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='任务编号')
    data_template_id = db.Column(db.BigInteger, info='数据模板表主键')
    snapshot_display_template_id = db.Column(db.BigInteger, info='显示模板snapshot表主键')
    user_id = db.Column(db.BigInteger, info='用户ID')
    email = db.Column(db.String(50), info='邮箱')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='逻辑删除')
    create_user_id = db.Column(db.BigInteger, info='创建数据的用户ID')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_user_id = db.Column(db.BigInteger, info='更新数据的用户ID')
    update_time = db.Column(db.DateTime, info='更新时间')
    if_open = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='邮件是否打开')
    open_time = db.Column(db.DateTime, info='邮件打开时间')



class TbHomailUserTemplateType(db.Model):
    __tablename__ = 'tb_homail_user_template_types'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    user_template_id = db.Column(db.BigInteger, info='用户数据模板表主键')
    title = db.Column(db.String(63), info='数据模板对应子分类')
    type_key = db.Column(db.VARBINARY(63), info='分类key')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='逻辑删除')
    create_user_id = db.Column(db.BigInteger, info='创建数据的用户ID')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_user_id = db.Column(db.BigInteger, info='更新数据的用户ID')
    update_time = db.Column(db.DateTime, info='更新时间')



class TbHomailUserTemplate(db.Model):
    __tablename__ = 'tb_homail_user_templates'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    bean_name = db.Column(db.String(127), info='springbean的名称')
    title = db.Column(db.String(127), info='数据模板名称，或者说渠道')
    info = db.Column(db.String(255), info='描述')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='逻辑删除')
    create_user_id = db.Column(db.BigInteger, info='创建数据的用户ID')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_user_id = db.Column(db.BigInteger, info='更新数据的用户ID')
    update_time = db.Column(db.DateTime, info='更新时间')



class TbHomologousPosition(db.Model):
    __tablename__ = 'tb_homologous_position'
    __table_args__ = (
        db.Index('source_type_enid', 'source_id', 'source_type', 'enterprise_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键编号')
    source_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='同质化来源职位')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='同质化职位')
    enterprise_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='企业编号')
    publish_time = db.Column(db.DateTime, info='职位发布时间')
    expire_time = db.Column(db.DateTime, nullable=False, index=True)
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    source_type = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='来源类型;0:职职;1:人职')
    has_read = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0:未读 1:已读')



class TbHomologousPositionReview(db.Model):
    __tablename__ = 'tb_homologous_position_review'

    id = db.Column(db.BigInteger, primary_key=True, info='主键编号')
    source_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='原始id')
    target_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='同质化目标id')
    review_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='点评人')
    review_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='点评类型(踩/赞)')
    reason = db.Column(db.String(200), info='原因')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    source_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='来源类型;0:职职;1:人职')



class TbHopApp(db.Model):
    __tablename__ = 'tb_hop_app'

    app_id = db.Column(db.String(200), primary_key=True, server_default=db.FetchedValue(), info='APP ID')
    user_id = db.Column(db.BigInteger, nullable=False, info='用户ID')
    app_name = db.Column(db.String(100), nullable=False, info='APP名称')
    app_key = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='APP KEY')
    app_secret = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='APP SECTET')
    service_id = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='service id')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建用户ID')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改用户ID')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, info='修改时间')
    app_state = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='app 审核状态 0：待审核 1：审核通过 2：打回')



class TbHopAppInform(db.Model):
    __tablename__ = 'tb_hop_app_inform'

    id = db.Column(db.BigInteger, primary_key=True, info='id')
    app_id = db.Column(db.String(200), nullable=False, index=True, server_default=db.FetchedValue(), info='APP ID')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='服务通知类型')
    inform_url = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='通知服务地址')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='状态0:启用;1:禁止')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbHopService(db.Model):
    __tablename__ = 'tb_hop_service'

    id = db.Column(db.BigInteger, primary_key=True, info='ID')
    service_url = db.Column(db.String(100), nullable=False, info='服务路径')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    service_name = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='服务名称')
    service_state = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0：未开发，1：免费；2：付费，需申请')
    update_time = db.Column(db.DateTime, info='修改时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建用户ID')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改用户ID')



class TbHopUser(db.Model):
    __tablename__ = 'tb_hop_user'

    id = db.Column(db.BigInteger, primary_key=True, info='用户唯一ID')
    user_name = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='用户姓名')
    province_id = db.Column(db.BigInteger)
    city_id = db.Column(db.BigInteger)
    address = db.Column(db.String(255))
    password = db.Column(db.String(100), nullable=False, info='用户密码')
    company_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='公司名称')
    mobile = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue(), info='手机号码')
    email = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='邮箱')
    user_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建用户ID')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改用户ID')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, info='修改时间')



class TbHopUserRelation(db.Model):
    __tablename__ = 'tb_hop_user_relation'
    __table_args__ = (
        db.Index('INDEX_HOP_INFORM_APPID_HOPUSERID_USERID', 'app_id', 'hop_user_id', 'user_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='id')
    app_id = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='APP ID')
    hop_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='开放平台用户ID')
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎上产品用户id')
    user_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='用户类型')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbHotArea(db.Model):
    __tablename__ = 'tb_hot_area'

    area_id = db.Column(db.BigInteger, primary_key=True, info='地区id，省或城市的id')
    area_name = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='地区名称')
    sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='修改时间')



class TbHotFunction(db.Model):
    __tablename__ = 'tb_hot_function'

    function_id = db.Column(db.BigInteger, primary_key=True, info='职能id')
    function_name = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='职能名称')
    sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='修改时间')



class TbHotIndustry(db.Model):
    __tablename__ = 'tb_hot_industry'

    industry_id = db.Column(db.BigInteger, primary_key=True, info='行业id')
    industry_name = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='行业名称')
    sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='修改时间')



class TbHotPosition(db.Model):
    __tablename__ = 'tb_hot_position'

    id = db.Column(db.BigInteger, primary_key=True)
    position_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职位id')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')



class TbHotProject(db.Model):
    __tablename__ = 'tb_hot_project'

    id = db.Column(db.BigInteger, primary_key=True, info='主键Id')
    project_name = db.Column(db.String(400), info='项目名称')
    project_introduction = db.Column(db.String(4000), info='项目介绍')
    project_highlight = db.Column(db.String(4000), info='项目亮点')
    project_start_time = db.Column(db.DateTime, index=True, info='项目开始时间')
    project_end_time = db.Column(db.DateTime, index=True, info='项目结束时间')
    project_status = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='项目状态 0:初始 ')
    share_url = db.Column(db.String(400), info='分享链接')
    created_user_id = db.Column(db.BigInteger, nullable=False, index=True, info='创建用户ID')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_user_id = db.Column(db.BigInteger, nullable=False, info='修改用户ID')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='修改时间')
    defunct = db.Column(db.Integer, nullable=False, index=True, info='是否删除 0 否 1是')



class TbHotProjectPosition(db.Model):
    __tablename__ = 'tb_hot_project_position'

    id = db.Column(db.BigInteger, primary_key=True, info='主键Id')
    project_id = db.Column(db.BigInteger, nullable=False, index=True, info='项目Id')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, info='职位Id')
    created_user_id = db.Column(db.BigInteger, nullable=False, info='创建用户ID')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_user_id = db.Column(db.BigInteger, nullable=False, info='修改用户ID')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='修改时间')
    defunct = db.Column(db.Integer, nullable=False, index=True, info='是否删除 0 否 1是')



class TbHotSearch(db.Model):
    __tablename__ = 'tb_hot_search'

    id = db.Column(db.BigInteger, primary_key=True)
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='类型')
    appType = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='App类型')
    word = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='搜索词')
    location = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='位置')
    style = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='样式')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否无效 -> 1 : true 已删除；0 : false 有效')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbHr(db.Model):
    __tablename__ = 'tb_hr'

    user_id = db.Column(db.BigInteger, primary_key=True)
    enterprise_id = db.Column(db.BigInteger, nullable=False, index=True)
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否无效 -> 1 : true 已删除；0 : false 有效')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1 true 正常用户; 0 false 非正常用户; 这个status和defunct一起结合决定了三种用户 -> status 1 defunct 0 正常和系统录入; status 0 defunct 0 待审核; status 1 defunct 1 已删除和已注销;')
    service_admin = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='对应PA的id')
    warm_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='hr配合度1:较差,2:配合,3:积极')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue(), info='更新时间')
    next_publist_grab_order_time = db.Column(db.DateTime, info='下次发布抢单职位时间')
    job_sharing_settings = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='面试官操作权限 0：备注反馈，1：直接反馈')
    am = db.Column(db.Integer, server_default=db.FetchedValue(), info='hr对应的企业的am')
    login_app = db.Column(db.Integer, server_default=db.FetchedValue(), info='0:无登录过app   1：登录过app')
    login_app_time = db.Column(db.DateTime, info='登录APP时间')
    register_source = db.Column(db.String(20), server_default=db.FetchedValue(), info='注册来源;该字段为0、1、2的组合(0:hr和hrsaas;1:sasshr;2:saashr销售版)')
    trial_time = db.Column(db.DateTime, info='SAAS试用版开始时间')
    os_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='对应OS的id')
    pas_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='对应PAS的id')
    pa_grade = db.Column(db.Integer, server_default=db.FetchedValue(), info='PA评分')
    wait_grade = db.Column(db.Integer, server_default=db.FetchedValue(), info='待打分 0:未打分 1:已打分')



class TbHrBlacklist(db.Model):
    __tablename__ = 'tb_hr_blacklist'

    id = db.Column(db.BigInteger, primary_key=True)
    hr_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='hrid')
    hh_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎头id')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0未删除，1 删除')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='类型,1:猎头,2:猎企')
    opera_user_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='操作用户类型 1:HR,2:HH,3:CRM')
    begin_time = db.Column(db.DateTime, info='被关开始时间')
    end_time = db.Column(db.DateTime, info='被关结束时间')
    hh_black_id = db.Column(db.BigInteger, info='关联tb_headhunter_black表id')



class TbHrCandidate(db.Model):
    __tablename__ = 'tb_hr_candidate'

    id = db.Column(db.BigInteger, primary_key=True, info='HR收藏人才记录主键')
    hr_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='HR的主键')
    candidate_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='候选人主键')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除 0:未删除 1:已删除')
    create_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())



class TbHrCooperationHh(db.Model):
    __tablename__ = 'tb_hr_cooperation_hh'
    __table_args__ = (
        db.Index('index_hr_id_headhunter_id', 'hr_id', 'headhunter_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    hr_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='hrid')
    headhunter_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎头ID')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1：申请合作；2：合作中；3：取消合作')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')



class TbHrCooperationIntention(db.Model):
    __tablename__ = 'tb_hr_cooperation_intention'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    intention_type = db.Column(db.String(20))
    hr_id = db.Column(db.BigInteger, nullable=False, info='HR ID')
    enterprise_id = db.Column(db.BigInteger, nullable=False, info='雇主ID')
    remark = db.Column(db.String(2000))
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='修改时间')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    update_user_id = db.Column(db.BigInteger, info='修改人')



class TbHrEmailRemind(db.Model):
    __tablename__ = 'tb_hr_email_remind'

    id = db.Column(db.BigInteger, primary_key=True, info='自增主键')
    hr_id = db.Column(db.BigInteger, nullable=False)
    email_to = db.Column(db.String(500), nullable=False, info='收件人')
    email_cc = db.Column(db.String(500), info='抄送')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class TbHrEnterpriseApply(db.Model):
    __tablename__ = 'tb_hr_enterprise_apply'

    id = db.Column(db.BigInteger, primary_key=True, info='唯一编号')
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='用户id')
    enterprise_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='企业id')
    apply_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='申请状态')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbHrGradeRecord(db.Model):
    __tablename__ = 'tb_hr_grade_record'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    hr_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='hrId')
    user_type = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='用户类型 pa 1 ')
    user_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='用户ID')
    pa_grade = db.Column(db.Integer, server_default=db.FetchedValue(), info='PA评分')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='是否删除0false 1true')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, index=True, info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbHrHeadhunterCompany(db.Model):
    __tablename__ = 'tb_hr_headhunter_company'

    id = db.Column(db.BigInteger, primary_key=True)
    hr_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='hr id')
    company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎头公司id')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除 0:未删除 1:已删除')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')



class TbHrPortrait(db.Model):
    __tablename__ = 'tb_hr_portrait'

    hr_id = db.Column(db.BigInteger, primary_key=True)
    login_time = db.Column(db.DateTime, info='登录时间')
    open_position_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开放的职位数量')
    server_quality = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='服务质量')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbHunterBrowseTalend(db.Model):
    __tablename__ = 'tb_hunter_browse_talend'

    id = db.Column(db.BigInteger, primary_key=True)
    hunter_id = db.Column(db.BigInteger, nullable=False)
    talent_id = db.Column(db.String(32), nullable=False)
    browse_type = db.Column(db.Integer, nullable=False, info='1 孵化器  2人才市场')
    create_time = db.Column(db.DateTime, nullable=False)



class TbHunterInvoiceDetail(db.Model):
    __tablename__ = 'tb_hunter_invoice_detail'

    id = db.Column(db.BigInteger, primary_key=True)
    invoice_no = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='开票编号')
    invoice_title = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='开票抬头')
    payment_id = db.Column(db.BigInteger, nullable=False, info='对应收款单ID')
    placement_id = db.Column(db.BigInteger, nullable=False, info='placement成单表ID ')
    invoice_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='发票类型')
    invoice_amount = db.Column(db.Float(12, True), nullable=False, server_default=db.FetchedValue(), info='开票金额')
    invoice_date = db.Column(db.DateTime, nullable=False, info='开票日期')
    retrun_invoice_date = db.Column(db.DateTime, info='退票时间')
    comment = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='开票备注')
    return_comment = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='退票备注')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    bounce_status = db.Column(db.Integer, server_default=db.FetchedValue(), info="'1:已开票,2:需退票,3:已退票'")



class TbHunterPayment(db.Model):
    __tablename__ = 'tb_hunter_payment'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    placement_id = db.Column(db.BigInteger, nullable=False, index=True, info='placement成单表ID ')
    pay_rate = db.Column(db.Float(12, True), nullable=False, server_default=db.FetchedValue(), info='猎企佣金比例')
    total_pay_amount = db.Column(db.Float(12, True), nullable=False, server_default=db.FetchedValue(), info='总应付金额')
    had_pay_amount = db.Column(db.Float(12, True), nullable=False, server_default=db.FetchedValue(), info='已付金额')
    pay_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='付款状态：未付款，部分付款，已付款，已完结')
    refund_pay_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='退款状态:1:需退款,2:已退款,3:结束')
    refund_pay_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='退款支付类型；1：冲抵；2：退款')
    refund_progress_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='退款流程状态 0:默认；1：待猎企处理；2：待猎企确认；3：待猎上确认；4：完成退款')
    preact_amount = db.Column(db.Float(12, True), nullable=False, server_default=db.FetchedValue(), info='应提前付金额：针对到岗付和到岗预付；是否退款根据产品类型product_type来确定')
    total_refund = db.Column(db.Float(12, True), nullable=False, server_default=db.FetchedValue(), info='总应退款金额')
    had_refund = db.Column(db.Float(12, True), nullable=False, server_default=db.FetchedValue(), info='已退款金额')
    total_invoice_amount = db.Column(db.Float(12, True), nullable=False, server_default=db.FetchedValue(), info='总开票金额')
    had_invoice_amount = db.Column(db.Float(12, True), nullable=False, server_default=db.FetchedValue(), info='已开票金额')
    invoice_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开票状态：未开票，部分开票，已开票')
    refund_invoice_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='退票状态:1:需退票,2:已退票,3:结束')
    product_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='产品类型：过保付，到岗付，到岗快')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新人')
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue(), info='更新时间')



class TbHunterPositionTag(db.Model):
    __tablename__ = 'tb_hunter_position_tag'

    id = db.Column(db.BigInteger, primary_key=True, info='唯一编号')
    hunter_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='猎头编号')
    company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='公司编号')
    tag_content = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='标签内容')
    first_letter = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue(), info='首字母')
    phonetic = db.Column(db.String(400), nullable=False, server_default=db.FetchedValue(), info='拼音')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbHunterPositionTagRelation(db.Model):
    __tablename__ = 'tb_hunter_position_tag_relation'
    __table_args__ = (
        db.Index('INDEX_HUNTER_POSITION_ID', 'hunter_id', 'position_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='唯一编号')
    tag_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='标签id')
    hunter_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎头编号')
    company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='公司编号')
    position_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职位编号')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbHunterReport(db.Model):
    __tablename__ = 'tb_hunter_report'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    headhunter_id = db.Column(db.BigInteger, index=True, info='猎头ID')
    candidate_count = db.Column(db.Integer, server_default=db.FetchedValue(), info='推荐数')
    interview_count = db.Column(db.Integer, server_default=db.FetchedValue(), info='面试数')
    interview_onetime = db.Column(db.Integer, server_default=db.FetchedValue(), info='1面数')
    placement_count = db.Column(db.Integer, server_default=db.FetchedValue(), info='成单数')
    placement_amount = db.Column(db.Numeric(20, 4), server_default=db.FetchedValue(), info='成单总金额')
    create_time = db.Column(db.DateTime, info='创建时间')



class TbHunteronTalent(db.Model):
    __tablename__ = 'tb_hunteron_talent'

    talent_id = db.Column(db.String(50), primary_key=True, server_default=db.FetchedValue(), info='外部人才id')
    expect_industry_ids = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='期望行业，多个以逗号分隔')
    expect_function_ids = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='期望职能，多个以逗号分隔')
    expect_city_ids = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='期望城市，多个以逗号分隔')
    expect_annualsalary_min = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='最小期望年薪')
    expect_annualsalary_max = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='最大期望年薪')
    keywords = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='关键字')
    degree = db.Column(db.Integer, info='学历')
    apply_status_fresh_date = db.Column(db.DateTime, nullable=False, info='求职状态最后更新时间')
    resume_last_fresh_date = db.Column(db.DateTime, nullable=False, info='简历最后刷新时间')
    into_incubator_date = db.Column(db.DateTime, info='进入孵化器时间')
    into_market_date = db.Column(db.DateTime, info='进入人才市场时间')
    create_time = db.Column(db.DateTime, nullable=False)



class TbImUploadLog(db.Model):
    __tablename__ = 'tb_im_upload_log'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    file_key = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='文件key')
    from_user = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='发送方')
    to_user = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='接收方')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbImportantPosition(db.Model):
    __tablename__ = 'tb_important_position'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    headhunter_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='猎头ID')
    headhunter_company_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='猎企ID')
    position_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职位ID')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')



class TbIncubatorGroupConnection(db.Model):
    __tablename__ = 'tb_incubator_group_connection'

    id = db.Column(db.BigInteger, primary_key=True)
    create_user_id = db.Column(db.BigInteger, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    update_date = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    tag_id = db.Column(db.BigInteger, nullable=False, info='tb_incubator_headhunter_tag')
    company_id = db.Column(db.BigInteger, nullable=False)
    headhunter_id = db.Column(db.BigInteger, nullable=False, info='猎头Id')
    label = db.Column(db.String(50), nullable=False, info='猎头标签')



class TbIncubatorHeadhunterTag(db.Model):
    __tablename__ = 'tb_incubator_headhunter_tag'

    id = db.Column(db.BigInteger, primary_key=True)
    tag_name = db.Column(db.String(100), info='标签名')
    tag_desc = db.Column(db.String(500), server_default=db.FetchedValue(), info='标签描述')
    skilled_industry_ids = db.Column(db.String(100), server_default=db.FetchedValue(), info='擅长行业，多个以逗号分隔')
    skilled_function_ids = db.Column(db.String(100), server_default=db.FetchedValue(), info='擅长职能，多个以逗号分隔')
    skilled_city_ids = db.Column(db.String(100), server_default=db.FetchedValue(), info='擅长城市，多个以逗号分隔')
    skilled_annualsalary_min = db.Column(db.Float(asdecimal=True), server_default=db.FetchedValue(), info='最小擅长年薪')
    skilled_annualsalary_max = db.Column(db.Float(asdecimal=True), server_default=db.FetchedValue(), info='最大擅长年薪')
    keywords = db.Column(db.String(200), server_default=db.FetchedValue(), info='关键字')
    create_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue())



class TbIncubatorTagPosition(db.Model):
    __tablename__ = 'tb_incubator_tag_position'

    id = db.Column(db.BigInteger, primary_key=True)
    position_id = db.Column(db.BigInteger, nullable=False)
    tag_id = db.Column(db.BigInteger, nullable=False, info='tag 标签Id，（group Id）')
    create_date = db.Column(db.DateTime, nullable=False)
    update_date = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    create_user_id = db.Column(db.BigInteger, nullable=False)
    defunct = db.Column(db.Integer, server_default=db.FetchedValue())
    push_time = db.Column(db.DateTime, info='推送职位时间')
    enterprise_id = db.Column(db.BigInteger, nullable=False)
    company_id = db.Column(db.BigInteger, nullable=False)



class TbIncubatorTalent(db.Model):
    __tablename__ = 'tb_incubator_talent'

    talent_id = db.Column(db.String(50), primary_key=True, server_default=db.FetchedValue(), info='外部人才id')
    create_time = db.Column(db.DateTime, nullable=False)



class TbIncubatorWhiteCompany(db.Model):
    __tablename__ = 'tb_incubator_white_company'

    id = db.Column(db.BigInteger, primary_key=True, server_default=db.FetchedValue())
    enterprise_id = db.Column(db.BigInteger, nullable=False)
    company_id = db.Column(db.BigInteger, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    update_date = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    create_user_id = db.Column(db.BigInteger, nullable=False)
    ps = db.Column(db.String(200), info='备注')



class TbIncubatorWhiteHeadhunter(db.Model):
    __tablename__ = 'tb_incubator_white_headhunter'

    id = db.Column(db.BigInteger, primary_key=True)
    company_id = db.Column(db.BigInteger, nullable=False)
    headhunter_id = db.Column(db.BigInteger, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, nullable=False)
    tag_name = db.Column(db.String(100), info='标签名')
    tag_desc = db.Column(db.String(500), server_default=db.FetchedValue(), info='标签描述')
    skilled_industry_ids = db.Column(db.String(100), server_default=db.FetchedValue(), info='擅长行业，多个以逗号分隔')
    skilled_function_ids = db.Column(db.String(100), server_default=db.FetchedValue(), info='擅长职能，多个以逗号分隔')
    skilled_city_ids = db.Column(db.String(100), server_default=db.FetchedValue(), info='擅长城市，多个以逗号分隔')
    skilled_annualsalary_min = db.Column(db.Float(asdecimal=True), server_default=db.FetchedValue(), info='最小擅长年薪')
    skilled_annualsalary_max = db.Column(db.Float(asdecimal=True), server_default=db.FetchedValue(), info='最大擅长年薪')
    keywords = db.Column(db.String(200), server_default=db.FetchedValue(), info='关键字')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    white_list = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否是孵化器猎头；0：不是；1：是孵化器猎头')
    update_offset_days = db.Column(db.Integer, server_default=db.FetchedValue(), info='允许查看人才市场更新的简历的更新天数；0，表示看到当天的数据；1：表示只看到一天前的数据；2：表示只看到2天前的数据')
    talent_source_type = db.Column(db.String(20), info='人才来源')



class TbIndexUpdated(db.Model):
    __tablename__ = 'tb_index_updated'

    id = db.Column(db.BigInteger, primary_key=True)
    obj_id = db.Column(db.BigInteger, nullable=False)
    obj_type = db.Column(db.Integer, nullable=False, info='1.position 2.candidate 3.hh')
    create_time = db.Column(db.DateTime, nullable=False)



class TbIndustryBaseConvertTag(db.Model):
    __tablename__ = 'tb_industry_base_convert_tag'

    id = db.Column(db.BigInteger, primary_key=True, info='自增ID')
    industry_id = db.Column(db.BigInteger, info='行业ID')
    tag_industry_id = db.Column(db.BigInteger, info='标签行业ID')
    user_id = db.Column(db.BigInteger, info='操作人')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='更新时间')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否删除 0 否 1 是')



class TbIntegralExtractRecord(db.Model):
    __tablename__ = 'tb_integral_extract_record'

    user_id = db.Column(db.BigInteger, primary_key=True)
    cont_sign_in_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='连续签到次数，中断清0')
    cont_work_sign_in_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='连续工作日签到次数，中断清0')
    cont_sign_in_point = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='连续签到获取的总积分')
    last_sign_in_time = db.Column(db.DateTime, info='最后签到时间')
    last_work_sign_in_time = db.Column(db.DateTime, info='最后工作日签到时间')
    cont_work_recommend_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='连续工作日推荐次数，中断清0')
    last_work_recommend_time = db.Column(db.DateTime, info='最后推荐时间')



class TbIntegralHr(db.Model):
    __tablename__ = 'tb_integral_hr'

    hr_id = db.Column(db.BigInteger, primary_key=True, info='hr_id')
    quarter_begin = db.Column(db.DateTime, nullable=False)
    quarter_end = db.Column(db.DateTime, nullable=False)
    quarter_total_integral = db.Column(db.BigInteger, nullable=False, info='季度累计积分值')
    current_total_integral = db.Column(db.BigInteger, nullable=False, info='当前剩余的有效积分')
    create_time = db.Column(db.DateTime, nullable=False, info='记录创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='记录更新时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='记录创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='记录的最后更新人')



class TbIntegralHrChangeLog(db.Model):
    __tablename__ = 'tb_integral_hr_change_log'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    hr_id = db.Column(db.BigInteger, nullable=False, index=True, info='积分对应的hrid')
    repeat_key = db.Column(db.BigInteger, index=True)
    operate_type = db.Column(db.Integer, nullable=False, info='积分对应的操作手段')
    operate_name = db.Column(db.String(63))
    changed_integral = db.Column(db.Integer, nullable=False, info='变动的积分，有正负值；正表示加积分，负数表示扣积分')
    changed_info = db.Column(db.String(255), info='积分变动说明')
    create_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, info='0')



class TbIntegralHrQuarterHistory(db.Model):
    __tablename__ = 'tb_integral_hr_quarter_history'
    __table_args__ = (
        db.Index('quartertime', 'quarter_begin', 'quarter_end'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    hr_id = db.Column(db.BigInteger, nullable=False, index=True, info='hrid')
    quarter_begin = db.Column(db.DateTime, nullable=False, info='季度时间范围，开始；2017-01-01')
    quarter_end = db.Column(db.DateTime, nullable=False, info='季度时间范围，开始；2017-03-31')
    total_integral = db.Column(db.BigInteger, nullable=False, info='累计积分值')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='删除标志位')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())



class TbInterfaceAccessRecord(db.Model):
    __tablename__ = 'tb_interface_access_record'
    __table_args__ = (
        db.Index('idx_requrl_platformtype_isdeprecated', 'req_url', 'platform_type', 'is_deprecated'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    req_url = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='请求URL')
    req_method = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='请求方式：0，GET;1，POST')
    platform_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='平台类型Platform：1，HR；2，HD；3，C；4，CRM；5，HR_WEB；6，HD_WEB；7，C_WEB；8，CRM_WEB')
    is_deprecated = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否过时接口: 0，不是；1，是')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除0:false 1:true')
    access_time = db.Column(db.DateTime, info='接口访问时间')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbInterfaceAuthority(db.Model):
    __tablename__ = 'tb_interface_authority'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    interface_id = db.Column(db.BigInteger, nullable=False, index=True, info='接口ID')
    authority_keys = db.Column(db.String(1024), nullable=False, info='操作权限key,逗号分隔')
    auth_transfer = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='权限是否需要透传')
    invoke_if_no_transfer_auth = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='用户不存在指定透传的权限Key，是否继续调用后续方法')
    need_all_auth = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否需要所有权限才可访问接口：0,不需要，1,需要')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbInvalidCollect(db.Model):
    __tablename__ = 'tb_invalid_collect'
    __table_args__ = (
        db.Index('idx_objtype_status_objid', 'obj_type', 'status', 'obj_id'),
        db.Index('idx_invalid_collect_obj_type_status', 'obj_type', 'status'),
        db.Index('idx_invalid_obj_type_id', 'obj_type', 'obj_id')
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键Id')
    obj_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='对象类型:1猎头/2猎企/3HR/4雇主客户')
    obj_id = db.Column(db.BigInteger, nullable=False, info='对象Id')
    obj_title = db.Column(db.String(255), info='对象标题')
    obj_keyword = db.Column(db.String(255), info='供搜索的关键字')
    reason_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='原因类型:0未定义/1不做猎头/2联系不上/3无合作意向/4其他')
    reason_desc = db.Column(db.String(500), info='失效原因')
    re_cooperation = db.Column(db.String(127), info='合作可能性')
    status = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否生效:1生效/0失效')
    create_user_id = db.Column(db.Integer, info='创建人id')
    create_user_name = db.Column(db.String(255), info='创建人姓名')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_user_id = db.Column(db.Integer, info='更新人id')
    update_user_name = db.Column(db.String(255), info='更新人名字')
    update_time = db.Column(db.DateTime)



class TbInvite(db.Model):
    __tablename__ = 'tb_invite'
    __table_args__ = (
        db.Index('idx_inviterid_status_exchange_createtime', 'inviter_id', 'status', 'exchange', 'create_time'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    inviter_id = db.Column(db.BigInteger, nullable=False, info='邀请ID')
    invite_code = db.Column(db.String(100), nullable=False, unique=True, info='邀请码')
    invitee_identity = db.Column(db.String(200), nullable=False, info='邮箱或者手机号码')
    invitee_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='被邀请者的用户id')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0.邀请已发出未注册\\n1.已经注册但是未通过审核\\n2.通过审核正式成为客户')
    exchange = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否兑换 0false 1true')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')



class TbInvoiceApply(db.Model):
    __tablename__ = 'tb_invoice_apply'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    apply_number = db.Column(db.String(20), index=True, info='申请编号')
    apply_amount = db.Column(db.Float(10, True), server_default=db.FetchedValue(), info='申请金额，开票金额税费计算之前的金额')
    apply_user_id = db.Column(db.BigInteger, nullable=False, info='申请人')
    apply_time = db.Column(db.DateTime, nullable=False, info='申请时间')
    expected_payment_time = db.Column(db.DateTime, info='预计付款时间')
    actual_payment_time = db.Column(db.DateTime, info='实际付款时间')
    status = db.Column(db.Integer, nullable=False, info='状态：0 新建; 1 申请通过; 2 审核未通过; 3 审核通过，准备付款; 4 已付款; 5已收款;')
    refuse_reason = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='拒绝理由')
    modify_reason = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='修改原因')
    invoice_type = db.Column(db.Integer, nullable=False, info='发票类型,1：普通增值税。2：专用增值税6%。3：专用增值税3%')
    actual_collection_amounts = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='实际收款金额（含税）')
    actual_invoice_amounts = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='实际开票金额（含税）')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    invoice_number = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='发票编码')
    invoice_url = db.Column(db.String(10000), nullable=False, server_default=db.FetchedValue(), info='发票地址')
    audit_user_id = db.Column(db.BigInteger, info='审核用户ID')
    audit_time = db.Column(db.DateTime, info='最后审核时间')
    invoice_tax_amounts = db.Column(db.Float(asdecimal=True), server_default=db.FetchedValue(), info='发票税费')
    business_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='业务类型,0：候选人 1：简历服务')
    tax_well = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否使用了税优；0：未使用；1：使用了税优')
    company_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='申请开票的猎企')
    apply_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='开票申请类型：1：订单开票申请；2：余额开票申请')
    invoice_mgr_version = db.Column(db.Integer, server_default=db.FetchedValue(), info='开票管理版本号；1：旧版本；2：账期版本')
    process_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='订单的处理类型；0：常规订单；1：RPO职位订单；2：猎享付订单。从tb_candidate_ploy表冗余')
    refund_status = db.Column(db.Integer, server_default=db.FetchedValue(), info='退款状态；0：无需退款；1：需退款；2：已退款')
    bounce_status = db.Column(db.Integer, server_default=db.FetchedValue(), info='退票状态；0：无需退票；1：需退票；2：已退票')
    refund_date = db.Column(db.DateTime, info='退款时间')
    bounce_date = db.Column(db.DateTime, info='退票时间')
    info_confirm_status = db.Column(db.Integer, server_default=db.FetchedValue(), info='开票申请信息确认状态；0：未确认；1：已确认')
    invoice_stage = db.Column(db.Integer, server_default=db.FetchedValue(), info='开票申请中订单开票申请的子类型；1：首付款申请；2：普通申请')
    pay_process_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='支付处理类型 1：超级支付')



class TbInvoiceApplyConfirmInfo(db.Model):
    __tablename__ = 'tb_invoice_apply_confirm_info'

    id = db.Column(db.BigInteger, primary_key=True)
    apply_id = db.Column(db.BigInteger, nullable=False, index=True)
    company_id = db.Column(db.BigInteger, index=True, info='开票公司名称')
    invoice_company_name = db.Column(db.String(127))
    invoice_bank_name = db.Column(db.String(127), info='开户行，到支行')
    invoice_bank_no = db.Column(db.String(63), info='银行账号')
    contact_name = db.Column(db.String(31), info='联系人姓名')
    contact_phone = db.Column(db.String(31), info='联系人电话')
    contact_email = db.Column(db.String(63), info='联系人邮箱')
    create_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)



class TbInvoiceApplyGroup(db.Model):
    __tablename__ = 'tb_invoice_apply_group'

    id = db.Column(db.BigInteger, primary_key=True)
    group_number = db.Column(db.String(32), nullable=False, info='开票组编号')
    apply_type = db.Column(db.Integer)
    defunct = db.Column(db.Integer, index=True)
    create_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)



class TbInvoiceApplyGroupRelation(db.Model):
    __tablename__ = 'tb_invoice_apply_group_relation'

    id = db.Column(db.BigInteger, primary_key=True)
    group_id = db.Column(db.BigInteger, nullable=False, index=True, info='tb_invoice_group表主键')
    apply_id = db.Column(db.BigInteger, nullable=False, index=True, info='tb_invoice_apply表主键')
    stage_type = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='关联时的类型；1：首款；2：尾款')
    defunct = db.Column(db.Integer, index=True)
    create_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)



class TbInvoiceApplyHunter(db.Model):
    __tablename__ = 'tb_invoice_apply_hunter'

    id = db.Column(db.BigInteger, primary_key=True)
    hunter_id = db.Column(db.BigInteger, index=True, info='顾问ID')
    company_id = db.Column(db.BigInteger, info='顾问公司ID')
    hunter_name = db.Column(db.String(31))
    bank_no = db.Column(db.String(63), info='银行账户')
    bank_name = db.Column(db.String(63), info='银行名称')
    mobile = db.Column(db.String(31))
    id_card_no = db.Column(db.String(31), index=True, info='身份证号')
    defunct = db.Column(db.Integer, index=True, info='逻辑删除')
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)
    verification = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否验证 0 未验证  1 已经验证')
    id_card_front = db.Column(db.String(256), info='身份证正面')
    id_card_reverse = db.Column(db.String(256), info='身份证反面')



class TbInvoiceApplyImage(db.Model):
    __tablename__ = 'tb_invoice_apply_image'

    id = db.Column(db.BigInteger, primary_key=True)
    apply_number = db.Column(db.String(20), nullable=False, info='申请编号')
    apply_user_id = db.Column(db.BigInteger, nullable=False, info='申请人')
    invoice_url = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='发票地址')
    is_upload = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='发票图片是否已提交')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime)
    image_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='附件类型；1：发票；2：税优凭证')



class TbInvoiceApplyInstalment(db.Model):
    __tablename__ = 'tb_invoice_apply_instalment'

    id = db.Column(db.BigInteger, primary_key=True)
    apply_id = db.Column(db.BigInteger, nullable=False, index=True, info='开票主表主键')
    taxwell_apply_id = db.Column(db.BigInteger, index=True, server_default=db.FetchedValue(), info='如果本次开票使用了税优，则这里关联的税优配置信息')
    src_amount = db.Column(db.Float(12, True), nullable=False, info='账期的原始金额')
    instalment_type = db.Column(db.Integer, nullable=False, info='账期类型')
    instalment_date = db.Column(db.DateTime, info='账期对应的预计付款时间')
    instalment_pay_rate = db.Column(db.Integer, nullable=False, info='账期对应分成比例')
    instalment_pay_amount = db.Column(db.Float(12, True), nullable=False, info='账期对应实际金额，账期原始金额x分成比例之后的金额，税前')
    stage_type = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='账期对应的首付款阶段；1：首款；2：尾款')
    actual_collection_amount = db.Column(db.Float(12, True), info='仅作记录：猎头实际的收款金额，需要扣除欠款')
    actual_invoice_amount = db.Column(db.Float(12, True), info='仅作记录： 分摊到账期上的开票金额')
    can_pay_status = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否可付款状态；0：不可付款；1：可以付款')
    pay_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='账期付款状态；0：未付款；1：已付款；2：已退款')
    pay_date = db.Column(db.DateTime)
    coment = db.Column(db.String(255), info='付款备注')
    refund_coment = db.Column(db.String(255), info='退款备注')
    defunct = db.Column(db.Integer, index=True)
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)
    pay_process_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='支付类型 0:普通支付；1:超级支付；2:无条件支付')



class TbInvoiceApplyInstalmentOrderTaxwell(db.Model):
    __tablename__ = 'tb_invoice_apply_instalment_order_taxwell'

    id = db.Column(db.BigInteger, primary_key=True)
    apply_id = db.Column(db.BigInteger, nullable=False, info='开票申请主键')
    placement_id = db.Column(db.BigInteger, nullable=False, info='placement主键')
    instalment_id = db.Column(db.BigInteger, nullable=False, info='账期主表主键')
    taxwell_id = db.Column(db.BigInteger, nullable=False, info='税优主表主键')
    amount = db.Column(db.Float(12, True), nullable=False, info='分配的金额')
    defunct = db.Column(db.Integer, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False)
    payload_type = db.Column(db.Integer, nullable=False, info='税优金额类型；1：企业金额；2：猎头分配金额')
    payload_id = db.Column(db.BigInteger, info='税优的主键，type是1，表示税优主表的主键；2表示税优分配猎头表主键')



class TbInvoiceApplyLog(db.Model):
    __tablename__ = 'tb_invoice_apply_log'

    id = db.Column(db.BigInteger, primary_key=True)
    apply_id = db.Column(db.BigInteger, index=True)
    action_type = db.Column(db.Integer)
    action_date = db.Column(db.DateTime)
    coment = db.Column(db.String(255))
    data_json = db.Column(db.String)
    defunct = db.Column(db.Integer)
    create_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    stage_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='账期对应的首付款阶段；1：首款；2：尾款')



class TbInvoiceApplyOrder(db.Model):
    __tablename__ = 'tb_invoice_apply_order'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    apply_number = db.Column(db.String(20), nullable=False, index=True, info='申请编号')
    placement_id = db.Column(db.BigInteger, nullable=False, index=True, info='支付订单id')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='逻辑删除')
    apply_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='订单对应的开票申请类型，枚举同apply_type')



class TbInvoiceApplyOrderInstalmentDetail(db.Model):
    __tablename__ = 'tb_invoice_apply_order_instalment_detail'

    id = db.Column(db.BigInteger, primary_key=True)
    apply_id = db.Column(db.BigInteger, index=True, info='开票申请主表的主键')
    placement_id = db.Column(db.BigInteger, index=True, info='指定的成单表主键')
    instalment_id = db.Column(db.BigInteger, index=True, info='成单关联某个账期的主键')
    src_amount = db.Column(db.Float(12, True), info='原始金额；在账期中，当前成单分配的金额')
    pay_rate = db.Column(db.Integer, info='对应账期的分成比例')
    pay_amount = db.Column(db.Float(12, True), info='对应账期的分成金额；原始金额x分成比例')
    actual_invoice_amount = db.Column(db.Float(12, True), info='仅作记录：猎头实际应该开票金额；扣除猎上代缴税费')
    actual_collection_amount = db.Column(db.Float(12, True), info='仅作记录：猎头实际收款的金额，含税')
    defunct = db.Column(db.Integer, index=True)
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)
    collection_amount_after_tax = db.Column(db.Float(14, True), server_default=db.FetchedValue(), info='税后付款金额；企业金额+个人金额')
    invoice_amount_after_tax = db.Column(db.Float(14, True), server_default=db.FetchedValue(), info='实际开票金额；企业开票部分')
    hunter_income = db.Column(db.Float(14, True), server_default=db.FetchedValue(), info='猎头到手金额')
    company_income = db.Column(db.Float(14, True), server_default=db.FetchedValue(), info='猎企收入金额')



class TbInvoiceApplyPloy(db.Model):
    __tablename__ = 'tb_invoice_apply_ploy'

    id = db.Column(db.BigInteger, primary_key=True)
    apply_id = db.Column(db.BigInteger, nullable=False, index=True)
    account_freeze_trans_id = db.Column(db.BigInteger, info='资金账户冻结操作交易主键')
    create_time = db.Column(db.DateTime)
    company_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue())
    company_name = db.Column(db.String(255))
    bank_name = db.Column(db.String(255))
    bank_no = db.Column(db.String(63))
    contact_name = db.Column(db.String(63))
    contact_phone = db.Column(db.String(63))
    contact_mail = db.Column(db.VARBINARY(127))
    defunct = db.Column(db.Integer, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_user_id = db.Column(db.BigInteger)



class TbInvoiceApplyResume(db.Model):
    __tablename__ = 'tb_invoice_apply_resume'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    apply_number = db.Column(db.String(20), nullable=False, info='申请编号')
    withdrawal = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='提现金额')
    pay_rate = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='分成比例')
    withdrawal_reward = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='提现分成后金额')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbInvoiceApplySnapshot(db.Model):
    __tablename__ = 'tb_invoice_apply_snapshot'

    id = db.Column(db.BigInteger, primary_key=True)
    apply_id = db.Column(db.BigInteger, nullable=False, index=True)
    invoice_stage = db.Column(db.Integer, nullable=False, index=True)
    apply_json = db.Column(db.String)
    instalment_json = db.Column(db.String)
    create_time = db.Column(db.DateTime)



class TbInvoiceApplyTaxwell(db.Model):
    __tablename__ = 'tb_invoice_apply_taxwell'

    id = db.Column(db.BigInteger, primary_key=True)
    apply_id = db.Column(db.BigInteger, nullable=False, index=True, info='tb_invoice_apply表主键')
    total_amount = db.Column(db.Float(9, True), info='总金额，含税，即申请金额')
    company_amount = db.Column(db.Float(9, True), info='猎企金额，含税，即在tb_invoice_apply表的收款金额actual_collection_amounts未扣税之前')
    taxwell_amount = db.Column(db.Float(9, True), info='税优总金额')
    retrench_amount = db.Column(db.Float(9, True), info='大约节约的成本')
    hunter_more_amount = db.Column(db.Float(9, True), info='猎头到手多的金额')
    company_id = db.Column(db.BigInteger, info='猎企ID')
    company_name = db.Column(db.String(127), info='猎企名称')
    company_bank_no = db.Column(db.String(63), info='猎企的银行账户')
    company_bank_name = db.Column(db.String(63), info='猎企的银行账户开户行名称')
    invoice_ein = db.Column(db.String(63), info='税号')
    invoice_phone = db.Column(db.String(31), info='发票联系电话')
    invoice_address = db.Column(db.String(255), info='发票地址')
    receipt_name = db.Column(db.String(31), info='收件人')
    receipt_phone = db.Column(db.String(31), info='收件人联系电话')
    receipt_address = db.Column(db.String(255), info='联系地址')
    apply_user_id = db.Column(db.BigInteger, info='申请人')
    apply_time = db.Column(db.DateTime, info='申请时间')
    audit_time = db.Column(db.DateTime, info='审核时间')
    audit_user_id = db.Column(db.BigInteger, info='审核人')
    defunct = db.Column(db.Integer, info='逻辑删除')
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)
    invoice_tax_amounts = db.Column(db.Float(9, True), server_default=db.FetchedValue(), info='发票税费差')
    company_income_amount = db.Column(db.Float(9, True), server_default=db.FetchedValue(), info='猎企实际收款金额，含税，旧版本逻辑')
    hunter_income_amounts = db.Column(db.Float(9, True), server_default=db.FetchedValue(), info='猎头个人实际到手金额总和')



class TbInvoiceApplyTaxwellHunter(db.Model):
    __tablename__ = 'tb_invoice_apply_taxwell_hunter'

    id = db.Column(db.BigInteger, primary_key=True)
    taxwell_apply_id = db.Column(db.BigInteger, index=True)
    hunter_id = db.Column(db.BigInteger, info='关联的顾问ID')
    company_id = db.Column(db.BigInteger, info='顾问公司ID')
    hunter_name = db.Column(db.String(31))
    amount = db.Column(db.Float(9, True), info='税优给该顾问的金额')
    bank_no = db.Column(db.String(63), info='银行账户')
    bank_name = db.Column(db.String(63), info='银行名称')
    mobile = db.Column(db.String(31))
    id_card_no = db.Column(db.String(31), index=True, info='身份证号')
    defunct = db.Column(db.Integer, index=True, info='逻辑删除')
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)
    invoice_tax_amounts = db.Column(db.Float(9, True), server_default=db.FetchedValue(), info='税费差')
    income_amounts = db.Column(db.Float(9, True), server_default=db.FetchedValue(), info='猎头实际到手金额')
    income_tax_amounts = db.Column(db.Float(9, True), server_default=db.FetchedValue(), info='猎头个人所得税')



class TbInvoiceApplyWithdrawDetail(db.Model):
    __tablename__ = 'tb_invoice_apply_withdraw_detail'

    id = db.Column(db.String(63), primary_key=True, info='主键（taxwell_hunter_id的md5）')
    withdarw_account_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='税优付款账户主体；1：猎上网；2：亨得昂')
    task_no = db.Column(db.String(63))
    taxwell_hunter_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎头个人税优信息表主键')
    hunter_name = db.Column(db.String(31))
    mobile = db.Column(db.String(15))
    id_card_no = db.Column(db.String(31))
    bank_no = db.Column(db.String(31), info='银行卡号')
    apply_amount = db.Column(db.Float(10, True), nullable=False, info='猎头个人税优申请金额，税前')
    income_amount = db.Column(db.Float(10, True), nullable=False, info='猎头个人税优的实际收入金额')
    tax_amount = db.Column(db.Float(10, True), nullable=False, info='个税')
    invoice_tax_amount = db.Column(db.Float(10, True), nullable=False, info='税费差')
    apply_id = db.Column(db.BigInteger, nullable=False, info='税优配置信息所属开票申请')
    instalment_id = db.Column(db.BigInteger, nullable=False, info='税优配置所属账期主键')
    instalment_date = db.Column(db.DateTime, nullable=False, info='账期的预计付款时间')
    placement_id = db.Column(db.BigInteger, nullable=False, info='关联成单表主键')
    withdraw_time = db.Column(db.DateTime, info='申请提现时间，猎上网发起提现任务的时间')
    withdraw_status = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='提现任务状态；状态:1-已受理，2-已付款(可结算)，3-不存在，4-结算中，5-已结算，98-结算失败，99-已关闭\\n')
    process_status = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='是否可处理；1：可处理；0：不再处理')
    create_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)



class TbInvoiceApplyWithdrawLog(db.Model):
    __tablename__ = 'tb_invoice_apply_withdraw_log'

    id = db.Column(db.BigInteger, primary_key=True)
    action_type = db.Column(db.Integer, info='动作类型')
    detail_id = db.Column(db.String(63), index=True, info='提现详细表主键')
    withdraw_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='提现任务状态；状态:0-创建，1-已受理，2-已付款(可结算)，3-不存在，4-结算中，5-已结算，98-结算失败，99-已关闭\\n')
    info = db.Column(db.String(255), info='信息描述')
    create_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)



class TbInvoiceRefusePlacement(db.Model):
    __tablename__ = 'tb_invoice_refuse_placements'
    __table_args__ = (
        db.Index('placementId_defunct', 'placement_id', 'defunct'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    placement_id = db.Column(db.BigInteger, nullable=False)
    refuse_reason = db.Column(db.String(255), info='拒绝原因')
    refuse_time = db.Column(db.DateTime, info='拒绝时间')
    operate_user_id = db.Column(db.BigInteger)
    company_id = db.Column(db.BigInteger, index=True)
    apply_id = db.Column(db.BigInteger, info='冗余开票主键')
    defunct = db.Column(db.Integer, info='逻辑删除；打回时为0；重新开票之后为1')
    create_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)



class TbJobhunter(db.Model):
    __tablename__ = 'tb_jobhunter'

    user_id = db.Column(db.BigInteger, primary_key=True, info='用户id，使用passport的id')
    resume_email = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='邮箱')
    birthday = db.Column(db.DateTime, info='生日')
    start_work_year = db.Column(db.Integer, info='开始工作年份')
    current_annual_salary = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='当前年薪')
    work_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1.在职，看看机会\\n2.在职，急寻新工作\\n3.在职，暂无跳槽打算\\n4.离职，正在找工作')
    self_introduction = db.Column(db.String(800), nullable=False, server_default=db.FetchedValue(), info='自我介绍')
    additional_info = db.Column(db.String(800), nullable=False, server_default=db.FetchedValue())
    expect_position_titles = db.Column(db.String(800), nullable=False, server_default=db.FetchedValue(), info='期望职位')
    expect_functions = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue(), info='期望职能 多个逗号隔开')
    expect_industrys = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue(), info='期望行业 多个逗号隔开')
    expect_citys = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue(), info='期望城市 多个逗号隔开')
    expect_annual_salary = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='期望年薪')
    expect_enterprise_styles = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='期望的公司类型 多个逗号隔开\\n1.初创型\\n2.成长型\\n3.成熟型\\n4.已上市\\n5.国企\\n6.外企')
    expect_requirement = db.Column(db.String(600), nullable=False, server_default=db.FetchedValue(), info='职位要求')
    salary_secret = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='年薪隐藏\\n0.不隐藏\\n1.隐藏')
    contact_secret = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='联系方式隐藏\\n0.不隐藏\\n1.隐藏')
    current_work_company = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='当前公司')
    current_work_position = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='当前职位')
    dispatch = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    edu_exp_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='教育经历条数')
    work_exp_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='工作经历条数')
    project_exp_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='项目经验条数')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='逻辑删除')
    contact_period = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1.不限\\n2.工作日(10:00-18:00)\\n3.工作日(18:00-21:00)\\n4.节假日')
    last_dispatch_time = db.Column(db.DateTime, info='最后派单时间')
    refresh_time = db.Column(db.DateTime, nullable=False, info='刷新时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='C端用户表')
    update_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)



class TbJobhunterActivityInviteRecord(db.Model):
    __tablename__ = 'tb_jobhunter_activity_invite_record'

    id = db.Column(db.BigInteger, primary_key=True)
    invite_code = db.Column(db.String(200), nullable=False, unique=True, server_default=db.FetchedValue(), info='邀请码')
    invite_time = db.Column(db.DateTime, nullable=False, info='邀请时间')
    invite_phone = db.Column(db.String(200), server_default=db.FetchedValue(), info='邀请手机')
    invite_active_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='邀请链接对应的活动类型')
    invite_attacheinfo = db.Column(db.String(5000), nullable=False, server_default=db.FetchedValue(), info='附加信息，json格式')
    jobhunter_id = db.Column(db.BigInteger, nullable=False, info='注册成功后id')
    register_time = db.Column(db.DateTime, nullable=False, info='注册时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbJobhunterCooperate(db.Model):
    __tablename__ = 'tb_jobhunter_cooperate'
    __table_args__ = (
        db.Index('uidx_jobhunterid_headhunterid', 'jobhunter_id', 'headhunter_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    jobhunter_id = db.Column(db.BigInteger, nullable=False, info='求职者id')
    headhunter_id = db.Column(db.BigInteger, nullable=False, info='猎头id')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1.推荐职位自动产生合作')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_uesr_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')



class TbJobhunterDispatch(db.Model):
    __tablename__ = 'tb_jobhunter_dispatch'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    jobhunter_id = db.Column(db.BigInteger, nullable=False, index=True, info='求职者id')
    dispatch_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='当前分发的数量')
    max_receive_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='可以接单的数量')
    expiry_date = db.Column(db.DateTime, info='有效期')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')



class TbJobhunterDispatchLog(db.Model):
    __tablename__ = 'tb_jobhunter_dispatch_log'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    jobhunter_id = db.Column(db.BigInteger, nullable=False, info='求职者id')
    dispatched = db.Column(db.Integer, nullable=False)
    message = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue())
    headhunter_ids = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')



class TbJobhunterDispatchParameter(db.Model):
    __tablename__ = 'tb_jobhunter_dispatch_parameter'

    name = db.Column(db.String(100), primary_key=True, info='参数名')
    value = db.Column(db.String(100), nullable=False, info='参数值')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    description = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='描述')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')



class TbJobhunterEduExp(db.Model):
    __tablename__ = 'tb_jobhunter_edu_exp'
    __table_args__ = (
        db.Index('idx_jobhunterid_startyear_startmonth', 'jobhunter_id', 'start_year', 'start_month'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    jobhunter_id = db.Column(db.BigInteger, nullable=False, info='求职者id')
    school = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='学校')
    profession = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='专业')
    degree_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='学历id')
    degree = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='学历名称')
    start_year = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开始年份')
    end_year = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='结束年份')
    start_month = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开始月')
    end_month = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='结束月')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')



class TbJobhunterEvent(db.Model):
    __tablename__ = 'tb_jobhunter_event'
    __table_args__ = (
        db.Index('idx_headhunterid_createtime', 'headhunter_id', 'create_time'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    dispatch_id = db.Column(db.BigInteger, nullable=False, info='派单id')
    jobhunter_id = db.Column(db.BigInteger, nullable=False, info='C端用户id')
    headhunter_id = db.Column(db.BigInteger, nullable=False, info='猎头id')
    type = db.Column(db.Integer, nullable=False, info='1.自动派单')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1.新建\\n2.同意\\n3.拒绝\\n4.被抢了\\n5.过期')
    jobhunter_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1.TA有换工作的想法\\n2.TA是来捣乱的\\n3.未联系上人才')
    viewed = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否已读')
    receive_time = db.Column(db.DateTime, info='接单时间')
    expiry_date = db.Column(db.DateTime, info='到期时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbJobhunterPosition(db.Model):
    __tablename__ = 'tb_jobhunter_position'
    __table_args__ = (
        db.Index('uidx_jobhunterid_positionid', 'jobhunter_id', 'position_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    jobhunter_id = db.Column(db.BigInteger, nullable=False, info='求职者id')
    position_id = db.Column(db.BigInteger, nullable=False, info='职位id')
    type = db.Column(db.Integer, nullable=False, info='1.感兴趣的')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')



class TbJobhunterProjectExp(db.Model):
    __tablename__ = 'tb_jobhunter_project_exp'
    __table_args__ = (
        db.Index('idx_jobhunterid_startyear_startmonth', 'jobhunter_id', 'start_year', 'start_month'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    jobhunter_id = db.Column(db.BigInteger, nullable=False, info='求职者id')
    company_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='公司名字')
    project_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='项目名字\\n')
    description = db.Column(db.String(3000), nullable=False, server_default=db.FetchedValue(), info='项目描述')
    start_year = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开始年份')
    end_year = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='结束年份')
    start_month = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开始月')
    end_month = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='结束月')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新人')



class TbJobhunterRecommend(db.Model):
    __tablename__ = 'tb_jobhunter_recommend'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    jobhunter_id = db.Column(db.BigInteger, nullable=False, index=True, info='求职者id')
    headhunter_id = db.Column(db.BigInteger, nullable=False, info='猎头id')
    position_id = db.Column(db.BigInteger, nullable=False, info='职位id')
    candidate_id = db.Column(db.BigInteger, nullable=False, info='候选人id（订单id）')
    feedback = db.Column(db.String(300), info='结果反馈')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')



class TbJobhunterShield(db.Model):
    __tablename__ = 'tb_jobhunter_shield'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    jobhunter_id = db.Column(db.BigInteger, nullable=False, info='求职者id')
    company_name = db.Column(db.String(300), nullable=False, info='公司名称')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='状态')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbJobhunterWorkExp(db.Model):
    __tablename__ = 'tb_jobhunter_work_exp'
    __table_args__ = (
        db.Index('idx_jobhunterid_startyear_startmonth', 'jobhunter_id', 'start_year', 'start_month'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    jobhunter_id = db.Column(db.BigInteger, nullable=False, info='求职者id')
    company_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='公司名称')
    position = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='职位')
    description = db.Column(db.String(3000), nullable=False, server_default=db.FetchedValue(), info='工作描述')
    start_year = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开始年份')
    end_year = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='结束年份')
    start_month = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开始月')
    end_month = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='结束月')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')



class TbLeaveOffice(db.Model):
    __tablename__ = 'tb_leave_office'

    id = db.Column(db.BigInteger, primary_key=True, info='离职用户Id/copy identity')
    create_time = db.Column(db.DateTime, nullable=False, info='离职时间')
    identity = db.Column(db.String(100), nullable=False, info='唯一凭证')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='离职状态0有效、1无效')
    type = db.Column(db.String(1), nullable=False, info='E:email, M:mobile, O:others')
    user_id = db.Column(db.BigInteger, nullable=False, info='离职用户id')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建者id')
    user_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1 : hr; 2 : hh; 3: admin; 4: agent')



class TbLeaveOfficeHandover(db.Model):
    __tablename__ = 'tb_leave_office_handover'

    id = db.Column(db.BigInteger, primary_key=True)
    headhunter_id = db.Column(db.BigInteger, nullable=False, info='猎头id')
    company_id = db.Column(db.BigInteger, nullable=False, info='猎企id')
    candidate_sendee = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='订单交接人')
    position_sendee = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职位交接人')
    talent_sendee = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='私密人才交接人')
    remove_secret_talent = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否解除私密人才')
    update_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    finish_handover = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否完成交接')



class TbLevel(db.Model):
    __tablename__ = 'tb_level'
    __table_args__ = (
        db.Index('idx_tb_level_code_type', 'code', 'type'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    code = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='级别代码')
    name = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue(), info='级别名称')
    description = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='级别描述')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='级别类型，1：企业级别，2：职位级别')
    sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序值')
    star = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='该等级对应星级')
    coefficient = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='系数，对应的是百分比的值')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除,0:false,1:true')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbLieyingCandidateCommission(db.Model):
    __tablename__ = 'tb_lieying_candidate_commission'
    __table_args__ = (
        db.Index('idx_lieying_candidate_id_defunct_state', 'candidate_id', 'defunct', 'state'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    candidate_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='候选人id')
    reward_type = db.Column(db.Integer, info='0：固定佣金  1：年薪百分比')
    fixed_reward_amount = db.Column(db.Float(asdecimal=True), info='固定佣金的 金额   ')
    percentage_numbric = db.Column(db.Float(asdecimal=True), info='百分比 数字 20 表示 年薪* 20%')
    updated_commission = db.Column(db.Numeric(11, 4), server_default=db.FetchedValue(), info='修改佣金')
    state = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='状态 0 新增 1 通过 -1 打回')
    remarks = db.Column(db.Text, info='补充说明')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False)
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class TbLieyingCandidateCommissionImg(db.Model):
    __tablename__ = 'tb_lieying_candidate_commission_img'
    __table_args__ = (
        db.Index('idx_lieying_commission_id_defunct', 'commission_id', 'defunct'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    commission_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改佣金审核id')
    img_url = db.Column(db.String(256), nullable=False, info='图片地址')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False)
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class TbLieyingCompany(db.Model):
    __tablename__ = 'tb_lieying_company'
    __table_args__ = (
        db.Index('idx_company_id_defunct', 'company_id', 'defunct'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    company_id = db.Column(db.BigInteger, nullable=False, info='猎英企业ID')
    is_lieying = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否为猎英,0:非猎英,1:猎英')
    collateral = db.Column(db.Numeric(20, 4), server_default=db.FetchedValue(), info='保证金')
    resume_balance = db.Column(db.Numeric(20, 4), server_default=db.FetchedValue(), info='简历宝余额')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False)
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    withdraw = db.Column(db.Numeric(20, 4), server_default=db.FetchedValue(), info='可以提现金额')
    hr_company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎英关联的HR公司ID')



class TbLieyingCompanyCollateralInfo(db.Model):
    __tablename__ = 'tb_lieying_company_collateral_info'
    __table_args__ = (
        db.Index('idx_company_id_defunct', 'company_id', 'defunct'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    company_id = db.Column(db.BigInteger, nullable=False, info='猎英企业ID')
    collateral = db.Column(db.Numeric(20, 4), server_default=db.FetchedValue(), info='保证金扣除金额  正数为加 负数为减')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False)
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class TbLieyingCompanyResumeBalanceInfo(db.Model):
    __tablename__ = 'tb_lieying_company_resume_balance_info'
    __table_args__ = (
        db.Index('idx_company_id_defunct', 'company_id', 'defunct'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    company_id = db.Column(db.BigInteger, nullable=False, info='猎英企业ID')
    resume_balance = db.Column(db.Numeric(20, 4), server_default=db.FetchedValue(), info='简历宝余额扣除金额  正数为加 负数为减')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False)
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class TbLieyingCompanyUser(db.Model):
    __tablename__ = 'tb_lieying_company_user'
    __table_args__ = (
        db.Index('idx_tb_lieying_company_user_headhunter_id_defunct', 'headhunter_id', 'defunct'),
        db.Index('idx_lieying_company_id_defunct_headhunter_hr_id', 'company_id', 'defunct', 'headhunter_id', 'hr_id')
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    company_id = db.Column(db.BigInteger, nullable=False, info='猎英企业ID')
    headhunter_id = db.Column(db.BigInteger, nullable=False, info='猎头ID')
    hr_id = db.Column(db.BigInteger, nullable=False, info='hrID')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False)
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class TbLieyingHighCvRemind(db.Model):
    __tablename__ = 'tb_lieying_high_cv_remind'
    __table_args__ = (
        db.Index('idx_tb_lieying_high_cv_remind_headhunter_company_id_defunct', 'headhunter_id', 'company_id', 'defunct'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    headhunter_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎头id')
    company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎头公司id')
    num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='数量')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class TbLoginSource(db.Model):
    __tablename__ = 'tb_login_source'
    __table_args__ = (
        db.Index('user_id', 'user_id', 'user_type'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    identity = db.Column(db.String(50), nullable=False, info='登录code')
    user_id = db.Column(db.BigInteger, nullable=False, info='用户Id')
    type = db.Column(db.String(1), info='E:M:O')
    channel = db.Column(db.String(20), info='来源渠道（pp助手，应用宝）')
    user_type = db.Column(db.Integer, nullable=False, info='1 : hr; 2 : hh; 3: admin; 4: agent;5:C端')
    client_type = db.Column(db.Integer, info='客户端类型；0：PC，1：安卓，2：iOS，3：其它，4：H5')
    system_version = db.Column(db.String(50), info='操作系统：win7，ios10')
    mobile_model = db.Column(db.String(50), info='设备型号')
    client_version = db.Column(db.String(50), info='客户端版本：hr2.1,hr2.2/pc(浏览器版本号)')
    create_time = db.Column(db.DateTime, nullable=False, index=True, info='创建时间')
    ip = db.Column(db.BigInteger, info='IP')
    mac = db.Column(db.String(50), info='mac 地址')
    subtype = db.Column(db.String(50), info='网络类型')
    province = db.Column(db.String(50), info='省份')
    city = db.Column(db.String(50), info='城市')
    country = db.Column(db.String(50), info='国家')
    useragent = db.Column(db.String(200), info='userAgent')
    unique_token = db.Column(db.String(65), nullable=False, unique=True, info='唯一标识')
    source_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='来源类型')
    inner_ip = db.Column(db.BigInteger, info='inner_ip内网ip')



class TbMagicClubPositionHunter(db.Model):
    __tablename__ = 'tb_magic_club_position_hunter'
    __table_args__ = (
        db.Index('IDX_SUPPLIER_LEVEL_AND_ID', 'id', 'supplier_level'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    enterprise_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue())
    hr_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    position_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue())
    hunter_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue())
    company_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue())
    match_score = db.Column(db.Float(16, True), server_default=db.FetchedValue(), info='匹配得分')
    supplier_level = db.Column(db.Integer, index=True, server_default=db.FetchedValue())
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbMagicClubRule(db.Model):
    __tablename__ = 'tb_magic_club_rule'

    rule_key = db.Column(db.String(60), primary_key=True, server_default=db.FetchedValue(), info='规则唯一key，全局唯一')
    rule_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='规则适用类型：1：简历-职位匹配；2：猎头-职位匹配；3：猎头-简历匹配')
    rule_name = db.Column(db.String(127), nullable=False, info='规则名称')
    rule_info = db.Column(db.String(255), info='规则描述')
    is_open = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='规则是否生效；1：生效；0：关闭(不生效）')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='数据是否删除；0：未删除；1：删除')
    create_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue())



class TbMagicClubTestCase(db.Model):
    __tablename__ = 'tb_magic_club_test_case'

    case_id = db.Column(db.BigInteger, primary_key=True, info='测试用例ID')
    case_name = db.Column(db.String(63), nullable=False, info='测试用例名称')
    rule_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='用例对应规则的类型；1：简历-职位匹配；2：猎头-职位匹配；3：猎头-简历匹配；')
    info = db.Column(db.String(255))
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='逻辑删除字段')
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_user_id = db.Column(db.BigInteger)



class TbMagicClubTestCaseRule(db.Model):
    __tablename__ = 'tb_magic_club_test_case_rule'

    id = db.Column(db.BigInteger, primary_key=True, info='测试用例和规则关联表的主键')
    case_id = db.Column(db.BigInteger, nullable=False, info='测试用例关联的规则')
    rule_key = db.Column(db.String(60))
    is_open_enforce = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否强制开启规则；0：不强制开启；1：强制开启，覆盖系统配置的开关')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='逻辑删除字段')
    create_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)



class TbMagicClubTestDatum(db.Model):
    __tablename__ = 'tb_magic_club_test_data'

    id = db.Column(db.BigInteger, primary_key=True)
    position_id = db.Column(db.BigInteger, nullable=False, info='职位ID')
    talent_id = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='人才编号')
    case_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='对应的用例')
    data_target_id = db.Column(db.BigInteger, nullable=False, info='数据对应目标id；用例id（case_id）或者规则关系id（case_rule_id）')
    data_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='测试数据管理目标类型：1：测试用例；2：测试用例关联的规则')
    match_expect = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='测试数据期望的匹配结果；1：匹配；0：不匹配')
    match_actual = db.Column(db.Integer, server_default=db.FetchedValue(), info='测试数据实际的匹配结果；-1：未计算；1：匹配；0：不匹配。')
    match_log_version_id = db.Column(db.String(63), info='最后一次测试用例执行，对应的执行日志')
    last_match_time = db.Column(db.DateTime, info='最后一次匹配验证时间')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='逻辑删除')
    create_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)



class TbMailSendLimit(db.Model):
    __tablename__ = 'tb_mail_send_limit'
    __table_args__ = (
        db.Index('defucnt_email_status', 'defunct', 'to_address', 'status'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='唯一编号')
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='用户编号 可以没有 退订时候冗余字段')
    from_address = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='发件邮箱')
    to_address = db.Column(db.String(100), nullable=False, index=True, server_default=db.FetchedValue(), info='收件邮箱')
    error_code = db.Column(db.String(100), info='错误编号')
    error_message = db.Column(db.String(2048), info='错误信息')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='投递状态 2:无效地址;3:垃圾邮件;4;失败;10:退订')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbMarketTalent(db.Model):
    __tablename__ = 'tb_market_talent'

    talent_id = db.Column(db.String(50), primary_key=True, server_default=db.FetchedValue(), info='外部人才id')
    create_time = db.Column(db.DateTime, nullable=False)



class TbMatchAnalysisRecord(db.Model):
    __tablename__ = 'tb_match_analysis_record'
    __table_args__ = (
        db.Index('index_match_analysis_position_id_score', 'position_id', 'match_score'),
        db.Index('index_match_analysis_unique_indx', 'talent_id', 'position_id')
    )

    id = db.Column(db.BigInteger, primary_key=True, info='匹配主键')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='职位编号')
    talent_id = db.Column(db.String(50), nullable=False, index=True, server_default=db.FetchedValue(), info='简历编号')
    match_score = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='匹配得分')
    position_analysis_match = db.Column(db.Text, info='职位解析结果')
    resume_analysis_match = db.Column(db.Text, info='简历解析结果')
    recommend_reason = db.Column(db.Text, info='推荐理由')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbMatchAnalysisRecordSnapshot(db.Model):
    __tablename__ = 'tb_match_analysis_record_snapshot'
    __table_args__ = (
        db.Index('index_match_analysis_position_id_score', 'position_id', 'match_score'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='匹配主键')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='职位编号')
    talent_id = db.Column(db.String(50), nullable=False, index=True, server_default=db.FetchedValue(), info='简历编号')
    match_score = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='匹配得分')
    position_analysis_match = db.Column(db.Text, info='职位解析结果')
    resume_analysis_match = db.Column(db.Text, info='简历解析结果')
    recommend_reason = db.Column(db.Text, info='推荐理由')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbMatchDispatchOrder(db.Model):
    __tablename__ = 'tb_match_dispatch_order'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    position_id = db.Column(db.BigInteger, index=True, info='职位ID')
    enterprise_id = db.Column(db.BigInteger, info='雇主id')
    talent_id = db.Column(db.String(63), index=True, info='简历id，mongodb表talentModel主键')
    package_status = db.Column(db.Integer, info='人职包派单状态：1：新派；2：接收；3：拒绝；4：收藏')
    reject_reason = db.Column(db.String(255), info='如果是拒绝，这里天拒绝理由')
    hunter_id = db.Column(db.BigInteger, info='猎头')
    company_id = db.Column(db.BigInteger, info='猎企')
    dispatch_type = db.Column(db.Integer, info='派单类型：0：人工；1：机器')
    snapshot_match_id = db.Column(db.BigInteger, info='派单时明细表tb_match_analysis_record_snapshot主键')
    match_score = db.Column(db.Float(asdecimal=True), info='匹配得分')
    hd_talent_id = db.Column(db.BigInteger, info='HD人才ID')
    accept_time = db.Column(db.DateTime, info='接受派单时间')
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_user_id = db.Column(db.BigInteger)
    first_read_time = db.Column(db.DateTime, info='首次阅读时间')



class TbMatchExpectRecord(db.Model):
    __tablename__ = 'tb_match_expect_record'

    id = db.Column(db.BigInteger, primary_key=True, info='主键编号')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='职位编号')
    talent_id = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='简历编号')
    create_time = db.Column(db.DateTime, nullable=False)



class TbMatchPriorityConfig(db.Model):
    __tablename__ = 'tb_match_priority_config'

    id = db.Column(db.BigInteger, primary_key=True, info='主键编号')
    enterprise_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='企业编号')
    first_position_title_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='一级职能')
    second_position_title_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='二级职能')
    third_position_title_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='三级职能')
    min_annual_salary = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='最小年薪')
    max_annual_salary = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='最大年薪')
    dispatch_priority_time = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='派单优先时间(小时/单位)')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbMatchSimilarityPosition(db.Model):
    __tablename__ = 'tb_match_similarity_position'

    id = db.Column(db.BigInteger, primary_key=True)
    source_position_id = db.Column(db.BigInteger, index=True)
    target_position_id = db.Column(db.BigInteger, index=True)
    match_score = db.Column(db.Float(asdecimal=True))
    skill_score = db.Column(db.Float(asdecimal=True))
    field_score = db.Column(db.Float(asdecimal=True))
    create_time = db.Column(db.BigInteger)
    update_time = db.Column(db.BigInteger)
    target_position_faction = db.Column(db.String(100))
    match_info = db.Column(db.Text, info='匹配明细信息')
    is_deleted = db.Column(db.Integer, server_default=db.FetchedValue(), info='0-有效，1-失效')



class TbMemberInviteRecord(db.Model):
    __tablename__ = 'tb_member_invite_record'

    id = db.Column(db.BigInteger, primary_key=True)
    operate_user_id = db.Column(db.BigInteger, nullable=False)
    company_id = db.Column(db.BigInteger, nullable=False)
    email = db.Column(db.String(200))
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0.邀请中；2.已注册')
    register_time = db.Column(db.DateTime, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())



class TbMenu(db.Model):
    __tablename__ = 'tb_menu'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    menu_name = db.Column(db.String(256), nullable=False, info='菜单名称')
    parent_id = db.Column(db.BigInteger, nullable=False, info='父菜单Id')
    app_id = db.Column(db.Integer, nullable=False, index=True, info='应用Id 0:hr 1:hd')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='修改时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, info='修改人')



class TbMessage(db.Model):
    __tablename__ = 'tb_message'
    __table_args__ = (
        db.Index('idx_receiverid_type_defunct_createtime', 'receiver_id', 'type', 'receiver_defunct', 'create_time'),
        db.Index('idx_message_type', 'type', 'sub_type'),
        db.Index('idx_senderid_type_defunct_createtime', 'sender_id', 'sender_defunct', 'create_time')
    )

    id = db.Column(db.BigInteger, primary_key=True)
    sender_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    receiver_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    subject = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    content = db.Column(db.String, nullable=False)
    position_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue())
    candidate_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue())
    read_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    sub_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='消息详细分类')
    message_data = db.Column(db.String(1024), nullable=False, server_default=db.FetchedValue(), info='消息关联的Json结构数据')
    sender_defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    receiver_defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    last_modify_time = db.Column(db.DateTime, nullable=False)
    reply_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())



class TbMessageBrowseRecord(db.Model):
    __tablename__ = 'tb_message_browse_record'
    __table_args__ = (
        db.Index('IDX_MESSAGE_ID_USER_ID', 'message_id', 'user_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    message_id = db.Column(db.BigInteger, info='消息ID')
    user_id = db.Column(db.BigInteger, index=True, info='用户ID')
    create_user_id = db.Column(db.BigInteger, info='创建用户ID')
    create_time = db.Column(db.DateTime, info='创建时间')



class TbMobileUser(db.Model):
    __tablename__ = 'tb_mobile_user'

    uid = db.Column(db.BigInteger, primary_key=True)
    android_token = db.Column(db.String(100), info='android notification token')
    ios_token = db.Column(db.String(100), info='iOS notification token')
    wx_open_id = db.Column(db.String(100), unique=True, info='wechat bind open id\\n')
    create_time = db.Column(db.DateTime, nullable=False, info='row create time')
    last_modify_time = db.Column(db.DateTime, nullable=False, info='row last modify time')



class TbModifyGuaranteeTimeRecord(db.Model):
    __tablename__ = 'tb_modify_guarantee_time_record'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    operator_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='操作人Id')
    candidate_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='候选人ID')
    old_guarantee_time = db.Column(db.Integer, info='老的保证期')
    new_guarantee_time = db.Column(db.Integer, info='新的保证期')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')



class TbModifyRewardRecord(db.Model):
    __tablename__ = 'tb_modify_reward_record'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    operator_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='操作人Id')
    candidate_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='候选人ID')
    old_reward = db.Column(db.Float(asdecimal=True), info='老的佣金(固定佣金/百分比佣金)')
    new_reward = db.Column(db.Float(asdecimal=True), info='新的佣金(固定佣金/百分比佣金)')
    old_placement_reward = db.Column(db.Float, info='老的成单佣金')
    new_placement_reward = db.Column(db.Float, info='新的成单佣金')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')



class TbNotice(db.Model):
    __tablename__ = 'tb_notice'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='用户编号')
    notice_type = db.Column(db.Integer, nullable=False, info='1:邮件')
    option_type = db.Column(db.Integer, nullable=False, info='1:新推荐;2:反馈逾期;3:不新鲜职位')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbOfferModifyLog(db.Model):
    __tablename__ = 'tb_offer_modify_log'

    id = db.Column(db.BigInteger, primary_key=True)
    candidate_id = db.Column(db.BigInteger, index=True, server_default=db.FetchedValue())
    placement_id = db.Column(db.BigInteger, index=True, server_default=db.FetchedValue())
    annual_salary = db.Column(db.Integer, info='实际年薪')
    onboard_date = db.Column(db.DateTime, info='到岗时间')
    onboard_address = db.Column(db.String(300), info='入职地址')
    guarantee_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='职位保证期类型；1：月数；2：天数')
    reward = db.Column(db.Float(15), info='实际成单佣金')
    percentage_numbric = db.Column(db.Float(asdecimal=True), info='百分比 数字 20 表示 年薪* 20%')
    guarantee_month = db.Column(db.Integer, info='保证期存、月数')
    reward_type = db.Column(db.Integer, info='佣金类型')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='0未删除，1 删除')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue(), info='更新时间')
    month_salary_multiple = db.Column(db.Float(5, True), server_default=db.FetchedValue(), info='佣金类型为月薪倍数时，记录比例计算之后的月薪倍数')
    first_read_time = db.Column(db.DateTime, info='首次已读时间')



class TbOperateCandidateRecord(db.Model):
    __tablename__ = 'tb_operate_candidate_record'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    candidate_id = db.Column(db.BigInteger, nullable=False, index=True, info='候选人id')
    user_id = db.Column(db.BigInteger, nullable=False, info='操作人id')
    user_role_code = db.Column(db.Integer, server_default=db.FetchedValue(), info='操作人的角色ID，主要针对user_type=3')
    user_type = db.Column(db.Integer, nullable=False, info='操作人类型')
    record_level = db.Column(db.Integer, server_default=db.FetchedValue(), info='日志级别；1：流程日志；2：系统修改日志')
    operate_type = db.Column(db.Integer, nullable=False, index=True, info='操作类型')
    original_value = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='操作前的值')
    new_value = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='操作后的值')
    operate_desc = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='操作描述')
    create_time = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    invisible = db.Column(db.Integer, server_default=db.FetchedValue(), info='不可见性，-1：不做隐藏，所有人可见，1：猎头不可见，2：hr不可见')
    has_next_interview = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否有下轮面试 0:没有  1：有')
    record_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='0：订单操作记录  1：面试记录')
    feedback_status = db.Column(db.Integer, info='反馈状态')
    feedback_desc = db.Column(db.String(200), server_default=db.FetchedValue(), info='反馈状态描述')
    reason = db.Column(db.Integer, server_default=db.FetchedValue(), info='原因：0：主观 1：客观')
    is_hh_display = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='猎头端是否可见')
    is_tdc_display = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='tdc端是否可见')
    is_hr_display = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='hr端是否可见')



class TbOperateCandidateRecordImg(db.Model):
    __tablename__ = 'tb_operate_candidate_record_img'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    operate_candidate_record_id = db.Column(db.BigInteger, index=True, info='操作记录id')
    url = db.Column(db.String(256), nullable=False, info='图片地址')
    candidate_id = db.Column(db.BigInteger, nullable=False, index=True, info='候选人id')
    operate_type = db.Column(db.Integer, nullable=False, index=True, info='操作类型')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, index=True, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False)



class TbOperatePositionRecord(db.Model):
    __tablename__ = 'tb_operate_position_record'
    __table_args__ = (
        db.Index('idx_user_id_infoId', 'user_id', 'user_info_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    position_id = db.Column(db.BigInteger, nullable=False, index=True)
    process_type = db.Column(db.Integer, nullable=False, info='职位修改类型')
    operate_desc = db.Column(db.String(255), nullable=False, info='日志文本')
    user_id = db.Column(db.BigInteger, nullable=False)
    user_info_id = db.Column(db.BigInteger)
    user_type = db.Column(db.Integer)
    role_code = db.Column(db.Integer)
    record_level = db.Column(db.Integer)
    tdc_display = db.Column(db.Integer)
    hh_display = db.Column(db.Integer)
    hr_display = db.Column(db.Integer)
    defunct = db.Column(db.Integer, index=True)
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_user_id = db.Column(db.BigInteger)



class TbOperation(db.Model):
    __tablename__ = 'tb_operation'
    __table_args__ = (
        db.Index('idx_app_id_status', 'app_id', 'status'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键Id')
    operation_name = db.Column(db.String(256), nullable=False, info='操作名称')
    app_id = db.Column(db.Integer, nullable=False, info='应用Id 0:hr 1:hd')
    status = db.Column(db.Integer, nullable=False, info='状态 1:正常 2:删除')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建用户Id')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, info='修改用户Id')
    type = db.Column(db.Integer, nullable=False, info='操作组')



class TbOrderMapped(db.Model):
    __tablename__ = 'tb_order_mapped'

    id = db.Column(db.BigInteger, primary_key=True, info='pk')
    tab_key = db.Column(db.String(200), nullable=False, info='显示按钮的key')
    tab_value = db.Column(db.String(200), nullable=False, info='中文按钮名称')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    group_id = db.Column(db.Integer, nullable=False, info='列表id,candidate1,position2,talent3')
    status = db.Column(db.Integer, nullable=False, info='状态下应该显示的按钮,如果是Candidate 对应allStatus')
    tab_sort = db.Column(db.Integer, nullable=False, info='状态显示排序')
    show_value = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0页面和列表都显示，1，列表，2，详情')



class TbOrsProcessRecord(db.Model):
    __tablename__ = 'tb_ors_process_records'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_id = db.Column(db.String(50), nullable=False, info='用户唯一编号')
    outer_talent_id = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='对方人才ID')
    outer_talent_key = db.Column(db.String(200), server_default=db.FetchedValue(), info='对方人才特征值')
    outer_time_limit = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='对方时间限制，1:7天， 2:14天  3：一个月')
    inner_talent_id = db.Column(db.String(200), server_default=db.FetchedValue(), info='猎上人才库人才ID')
    updated = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0:没有更新过，1：更新过')
    updated_use_time = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='更新用时（单位：分钟）')
    tpr_talent_id = db.Column(db.String(200), server_default=db.FetchedValue(), info='第三方简历ID')
    tpr_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1:猎上，2:feiwa 3:youben')
    query_time = db.Column(db.DateTime, nullable=False, info='用户查询时间')
    query_use_ip = db.Column(db.String(20), server_default=db.FetchedValue(), info='用户查询所用IP')
    forward = db.Column(db.Integer, info='是否转发查询')
    forward_target = db.Column(db.Integer, info='1:qiaoda 暂时只有一种情况')
    create_user_id = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='创建用户ID')
    update_user_id = db.Column(db.String(100), server_default=db.FetchedValue(), info='修改用户ID')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, info='修改时间')



class TbOrsPushRecord(db.Model):
    __tablename__ = 'tb_ors_push_records'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_id = db.Column(db.String(50), nullable=False, info='用户唯一编号')
    outer_talent_id = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='对方人才ID')
    outer_time_limit = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='对方时间限制，1:7天， 2:14天  3：一个月')
    inner_talent_id = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='猎上人才库人才ID')
    update_fields = db.Column(db.String(200), info='更新项')
    updated = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0:没有更新过，1：更新过')
    updated_use_time = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='更新用时（单位：分钟）')
    source = db.Column(db.Integer, server_default=db.FetchedValue(), info='1:qiaoda 2: hunteron')
    create_user_id = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='创建用户ID')
    update_user_id = db.Column(db.String(100), server_default=db.FetchedValue(), info='修改用户ID')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, info='修改时间')



class TbOrsUserLimit(db.Model):
    __tablename__ = 'tb_ors_user_limit'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_id = db.Column(db.String(50), nullable=False, info='用户唯一编号')
    user_surplus_money = db.Column(db.Float(asdecimal=True), server_default=db.FetchedValue(), info='用户剩余套餐金额')
    user_surplus_count = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='用户剩余套餐次数')
    last_query_time = db.Column(db.DateTime, info='创建时间')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    create_user_id = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='创建用户ID')
    update_user_id = db.Column(db.String(100), server_default=db.FetchedValue(), info='修改用户ID')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, info='修改时间')



class TbOutsideEnterprise(db.Model):
    __tablename__ = 'tb_outside_enterprise'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    outside_id = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='外部的企业id')
    name = db.Column(db.String(200), nullable=False, info='企业名')
    display_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='企业显示名')
    logo = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='企业logo')
    temptation = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue(), info='企业诱惑')
    tags = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue(), info='企业标签')
    highlights = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='企业亮点')
    industry_ids = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue(), info='行业id列表')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='公司性质：0：其他性质，1：外资 欧美，2：外资非欧美，3：合资，4：国企，5：民营公司，6：国内上市公司，7：外企代表处，8：政府机关，9：事业单位，10：非营利机构')
    establish_year = db.Column(db.Integer, info='企业成立年份')
    scale = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='公司规模：0：1-49，1：50-99，2：100-499，3：500-999，4：1000-4999，5：5000-9999，6：10000+')
    industry_rank = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='行业排名')
    website = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='公司网站')
    introduce = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='公司简介')
    advantage = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='竞争优势')
    culture = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='企业文化')
    address = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='公司地址')
    source = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='职位来源')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    develop_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='企业发展状态：0:默认，1：未融资，2：天使轮，3：A轮，4：B轮，5：C轮，6：D轮及以上，7：上市公司')
    city_id = db.Column(db.BigInteger, info='城市id')



class TbOutsideEnterpriseImgDatum(db.Model):
    __tablename__ = 'tb_outside_enterprise_img_data'

    id = db.Column(db.BigInteger, primary_key=True)
    enterprise_id = db.Column(db.BigInteger, nullable=False, info='企业id')
    link_id = db.Column(db.BigInteger, nullable=False, info='关联企业调研数据表中的id，比如企业产品id；管理团队id等')
    img = db.Column(db.MEDIUMBLOB, info='企业logo二进制图片')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='图片类型，1：企业logo，2：企业介绍图片，3：产品图片，4：管理团队头像')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')



class TbOutsideEnterpriseInvestigateImage(db.Model):
    __tablename__ = 'tb_outside_enterprise_investigate_image'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    enterprise_id = db.Column(db.BigInteger, nullable=False, info='企业id')
    image = db.Column(db.String(500), nullable=False, info='公司图片')
    sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbOutsideEnterpriseInvestigateManager(db.Model):
    __tablename__ = 'tb_outside_enterprise_investigate_manager'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    enterprise_id = db.Column(db.BigInteger, nullable=False, info='企业id')
    name = db.Column(db.String(100), nullable=False, info='管理者姓名')
    duty = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='管理者的职务')
    weibo = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='微博')
    logo = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='头像')
    introduce = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='管理者个人信息介绍')
    sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbOutsideEnterpriseInvestigateProduct(db.Model):
    __tablename__ = 'tb_outside_enterprise_investigate_product'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    enterprise_id = db.Column(db.BigInteger, nullable=False, info='企业id')
    name = db.Column(db.String(100), nullable=False, info='产品名')
    website = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='产品网址')
    logo = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='产品logo')
    introduce = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='产品介绍')
    sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbOutsidePosition(db.Model):
    __tablename__ = 'tb_outside_position'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    outside_id = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='外部的职位id')
    title = db.Column(db.String(200), nullable=False, info='职位名')
    publish_time = db.Column(db.DateTime, nullable=False, info='发布时间')
    min_annual_salary = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='最小年薪')
    max_annual_salary = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='最大年薪')
    city_id = db.Column(db.BigInteger, info='工作城市id')
    location = db.Column(db.String(1000), info='上班详细地址')
    degree_required = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='学历要求 0:不限 1：大专及以上 2：本科及以上 3：硕士及以上 4：博士及以上')
    work_exp_required = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='工作经验要求 ：0:不限 1:1年以上  2:2年以上 3:3年以上 4：4年以上 (这个直接存要求工作年薪的数字即可，如果是范围取最小值)')
    gender_required = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='性别要求 0：不限  1：男  2：女')
    temptation = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='职位诱惑')
    department = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='所属部门')
    reportpo = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='汇报对象')
    subordinate = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='下属团队')
    head_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='招聘人数')
    job_description = db.Column(db.Text, info='职位描述')
    job_requirement = db.Column(db.Text, info='任职要求')
    enterprise_id = db.Column(db.BigInteger, nullable=False, info='企业id')
    enterprise_name = db.Column(db.String(200), nullable=False, info='企业名（冗余字段，用于职位排重）')
    source = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='职位来源')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')



class TbPaCollection(db.Model):
    __tablename__ = 'tb_pa_collection'
    __table_args__ = (
        db.Index('idx_headhunter__id', 'headhunter_id', 'company_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    headhunter_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎头id')
    company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎头公司id')
    pa_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='pa_id')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())



class TbPaFunctionIndustry(db.Model):
    __tablename__ = 'tb_pa_function_industry'

    pa_id = db.Column(db.Integer, primary_key=True, info='pa_id')
    position_id = db.Column(db.BigInteger, info='职位ID')
    industry_id1 = db.Column(db.String(2200), info='行业一级,逗号分隔ID')
    industry_id2 = db.Column(db.String(2200), info='行业二级,逗号分隔ID')
    position_title1 = db.Column(db.String(2200), info='职能一级,逗号分隔ID')
    position_title2 = db.Column(db.String(2200), info='职能二级,逗号分隔ID')
    position_title3 = db.Column(db.String(5200), info='职能三级,逗号分隔ID')
    city_id = db.Column(db.String(2200))
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='更新时间')



class TbPaHeadhunter(db.Model):
    __tablename__ = 'tb_pa_headhunter'

    id = db.Column(db.BigInteger, primary_key=True)
    pa_id = db.Column(db.BigInteger, nullable=False, info='PA Id')
    headhunter_id = db.Column(db.BigInteger, nullable=False, info='hunter Id')
    create_time = db.Column(db.DateTime, info='创建时间')
    create_user = db.Column(db.BigInteger, info='创建用户')
    update_time = db.Column(db.DateTime, info='更新时间')
    update_user = db.Column(db.BigInteger, info='更新用户')
    status = db.Column(db.Integer, server_default=db.FetchedValue(), info='状态：0 无效；1 有效')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否删除，0 未删除 ；1已删除')



class TbPairPositionTalent(db.Model):
    __tablename__ = 'tb_pair_position_talent'
    __table_args__ = (
        db.Index('pair_key', 'position_id', 'talent_id', 'is_manul'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    pair_unique_key = db.Column(db.String(40), info='position_id+talent_id+hunter_id的唯一标识')
    position_id = db.Column(db.BigInteger, nullable=False, info='职位ID')
    talent_id = db.Column(db.BigInteger, nullable=False, info='人才ID')
    hunter_id = db.Column(db.BigInteger, nullable=False, info='猎头ID')
    is_manul = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否人工指定')
    is_system = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否系统指定')
    is_view_list = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否列表查看过')
    view_list_time = db.Column(db.DateTime, info='列表时间')
    is_view_detail = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否查看过详情')
    view_detail_time = db.Column(db.DateTime, info='浏览详情时间')
    create_time = db.Column(db.DateTime, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建用户')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='逻辑删除')



class TbParameterConfig(db.Model):
    __tablename__ = 'tb_parameter_config'

    id = db.Column(db.BigInteger, primary_key=True, info='唯一编号')
    config_key = db.Column(db.Integer, nullable=False)
    config_value = db.Column(db.String, info='参数值')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)



class TbParamsTypeConfig(db.Model):
    __tablename__ = 'tb_params_type_config'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='参数类型')
    value = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='参数名称')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, info='修改时间')



class TbParamsValueConfig(db.Model):
    __tablename__ = 'tb_params_value_config'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='参数类型')
    num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='参数key')
    value = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='参数value')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, info='修改时间')



class TbPassport(db.Model):
    __tablename__ = 'tb_passport'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    member_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    login_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    password = db.Column(db.String(200), nullable=False)
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否无效 -> 1 : true 已删除；0 : false 有效')
    user_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1 : hr; 2 : hh; 3: admin; 4: agent')
    account_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='账户类型 0：个人；1：集团')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    last_login_time = db.Column(db.DateTime, info='最后登陆时间')
    mobile_verified = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='该用户的手机号码是否被验证过 0:false, 1 true')
    email_verified = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='该用户的email是否被验证过 0:false, 1 true')
    ip = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='IP地址')
    user_agent = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='用户代理')
    is_reset_password = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否需要重置密码:1:是,0:否')
    App_Login_Status = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否通过APP登录，0未登录，1已登录')
    tip_status = db.Column(db.Integer, server_default=db.FetchedValue(), info='提示状态、0未提示、1已提示')
    authentication_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='认证状态：默认0，未提交；1，审核通过；2，审核不通过；3，审核中')
    leave_office = db.Column(db.Integer, server_default=db.FetchedValue(), info='离职状态，0正常、1已离职')
    certificates_authentication_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='认证状态：默认0:未提交申请；1：审核中；2：审核通过；3：审核不通过')
    certificates_not_through_reason = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='审核不通过原因')
    certificates_user_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0:新用户；1：老用户。上线后，已经注册的猎头为老用户，以后注册的为新用户')
    certificates_is_force = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否强制0:不强制；1：强制(移动端需要根据该字段提示用户是否强制去提交认证信息)')
    has_chang_pwd = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否修改过密码  0  没有修改过 1 改过')



class TbPaymentDetail(db.Model):
    __tablename__ = 'tb_payment_detail'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    placement_id = db.Column(db.BigInteger, nullable=False, info='placement成单表ID ')
    payment_id = db.Column(db.BigInteger, nullable=False, info='对应收款单ID')
    detail_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='明细类型：向猎头付款，猎头退款')
    refund_pay_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='退款支付类型；1：冲抵；2：退款')
    amount = db.Column(db.Float(12, True), nullable=False, server_default=db.FetchedValue(), info='金额')
    amount_date = db.Column(db.DateTime, index=True, info='金额日期')
    amount_channel = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='收款或退款途径,1:线下,2:通过总账')
    comment = db.Column(db.String(1000), server_default=db.FetchedValue(), info='收款或退款备注')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='更新人')
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue(), info='更新时间')



class TbPermissionMenu(db.Model):
    __tablename__ = 'tb_permission_menu'

    id = db.Column(db.BigInteger, primary_key=True)
    user_type = db.Column(db.Integer, nullable=False, info='所属类型;1:hr;2:hd')
    remark = db.Column(db.String(200), info='备注')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    menu_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='菜单名称')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')



class TbPermissionOperation(db.Model):
    __tablename__ = 'tb_permission_operation'

    id = db.Column(db.BigInteger, primary_key=True)
    user_type = db.Column(db.Integer, nullable=False, info='所属类型;1:hr;2:hd')
    remark = db.Column(db.String(200), info='备注')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    authority_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='权限名称')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    menu_id = db.Column(db.BigInteger, nullable=False, info='菜单id')
    authority_key = db.Column(db.String(200), nullable=False, info='操作权限key')
    operation_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0 ，物理菜单在菜单栏显示，1虚拟菜单，菜单栏不显示')
    authority_sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序')
    ps = db.Column(db.String(500), info='备注')



class TbPermissionUser(db.Model):
    __tablename__ = 'tb_permission_user'

    id = db.Column(db.BigInteger, primary_key=True)
    user_type = db.Column(db.Integer, nullable=False, index=True, info='所属类型;1:hr;2:hd')
    user_id = db.Column(db.BigInteger, nullable=False, index=True, info='用户id')
    authority_key = db.Column(db.String(200), nullable=False, index=True, info='操作权限key')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, info='更新时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建者id')
    update_user_id = db.Column(db.BigInteger, info='更新者id')



class TbPlacementComment(db.Model):
    __tablename__ = 'tb_placement_comment'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    placement_id = db.Column(db.BigInteger, nullable=False, info='成单id')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='备注类型:1:企业销账')
    comment = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新人')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='更新时间')



class TbPlacementInvoiceRemind(db.Model):
    __tablename__ = 'tb_placement_invoice_remind'

    id = db.Column(db.BigInteger, primary_key=True)
    placement_id = db.Column(db.BigInteger, nullable=False, index=True)
    pay_rate = db.Column(db.Float, nullable=False, server_default=db.FetchedValue(), info='付款比例(占佣金的比例)')
    should_amount = db.Column(db.Numeric(12, 2), nullable=False, server_default=db.FetchedValue(), info='应开票金额')
    had_amount = db.Column(db.Numeric(12, 2), nullable=False, server_default=db.FetchedValue(), info='已开票金额')
    invoice_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='应开票次序')
    should_date = db.Column(db.DateTime, info='应开票的时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbPlacementPloy(db.Model):
    __tablename__ = 'tb_placement_ploy'
    __table_args__ = (
        db.Index('commision', 'commision_owner_company_id', 'commision_owner_status'),
    )

    placement_id = db.Column(db.BigInteger, primary_key=True, server_default=db.FetchedValue(), info='placementId')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建者')
    update_time = db.Column(db.DateTime, info='更新时间')
    update_user_id = db.Column(db.BigInteger, info='更新者')
    hunteron_reward_type = db.Column(db.Integer, info='佣金类型（猎上设置）0：固定佣金   1：年薪百分比')
    hunteron_fixed_reward_amount = db.Column(db.Float(asdecimal=True), info='固定佣金（猎上设置）')
    hunteron_percentage = db.Column(db.Float(asdecimal=True), info='佣金比例（猎上设置）')
    pay_rate_type = db.Column(db.Integer, info='offer时，最终佣金分成比例类型；来源于candidate_ploy表的pay_rate_type和min_pay_rate_type的综合计算')
    offer_certificate = db.Column(db.String(256), info='offer凭证')
    has_certificate = db.Column(db.Integer, info='是否有凭证')
    invoice_mgr_version = db.Column(db.Integer, server_default=db.FetchedValue(), info='开票管理版本号；1：旧版本；2：账期版本')
    src_reward = db.Column(db.Float(10, True), server_default=db.FetchedValue(), info='原始佣金，未乘以显示比例，主要用于向雇主收款时使用')
    src_percent = db.Column(db.Float(10, True), server_default=db.FetchedValue())
    process_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='订单的处理类型；0：常规订单；1：RPO职位订单')
    src_month_salary_multiple = db.Column(db.Float(5, True), server_default=db.FetchedValue(), info='佣金类型为月薪倍数时，记录原始的月薪倍数')
    month_salary_multiple = db.Column(db.Float(5, True), server_default=db.FetchedValue(), info='佣金类型为月薪倍数时，记录比例计算之后的月薪倍数')
    guarantee_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='职位保证期类型；1：月数；2：天数')
    invoice_apply_status = db.Column(db.Integer, server_default=db.FetchedValue(), info='0：不可开票；1：可开票；2：已开票；3：不能开票；4：可申请首付款；5：已申请首付款')
    modify_offer = db.Column(db.Integer, server_default=db.FetchedValue(), info='待打分 0:未修改 1:已修改')
    pay_process_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='支付处理类型 1：超级支付')
    commision_pay_rate = db.Column(db.Float(6, True), server_default=db.FetchedValue(), info='分佣的比例')
    invoice_apply_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='订单对应的开票申请类型，枚举同apply_type')
    commision_owner_status = db.Column(db.Integer, server_default=db.FetchedValue(), info='可分佣状态；0：不可申请；1：可申请；2：已申请分佣')
    commision_owner_company_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='分佣收益猎头，0表示不分佣')
    pay_date_type = db.Column(db.Integer, info='付款时间类型 1:开票前；2:到岗后；3:收款后；4:过保后')
    pay_date = db.Column(db.Integer, info='支付天数,单位为天数')
    position_client_type = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='发布职位的客户端类型；1：旧版本hr，包括saas版本；2：新版本OnWork')
    reward_version = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='佣金计算版本号；默认1；1：当前版本；2：合伙人佣金规则版本')
    reward_snapshot_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='合伙人佣金版本对应的快照ID')
    withhold_hunteron_rate = db.Column(db.Float(6, True), nullable=False, server_default=db.FetchedValue(), info='猎上作为平台的预扣百分比')
    withhold_enterprise_rate = db.Column(db.Float(6, True), nullable=False, server_default=db.FetchedValue(), info='预扣-雇主的比例')
    withhold_pa_operate_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='预扣-PA运营类型')
    withhold_bd_operate_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='预扣-BD运营类型')
    withhold_pa_company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='预扣-PA是合伙人的情况下，对应合伙人猎企ID')
    withhold_pa_rate = db.Column(db.Float(6, True), nullable=False, server_default=db.FetchedValue(), info='预扣-PA是合伙人，对应预扣百分比')
    withhold_bd_company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='预扣-BD是合伙人的情况下，对应合伙人猎企ID')
    withhold_bd_rate = db.Column(db.Float(6, True), nullable=False, server_default=db.FetchedValue(), info='预扣-BD是合伙人，对应预扣百分比')
    commission_enterprise_rate = db.Column(db.Float(6, True), nullable=False, server_default=db.FetchedValue(), info='分佣-雇主的比例')
    commission_pa_operate_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='分佣-PA运营类型')
    commission_bd_operate_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='分佣-BD运营类型')
    commission_pa_company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='分佣-PA是合伙人的情况下，对应合伙人猎企ID；这是职位当前的PA信息')
    commission_pa_rate = db.Column(db.Float(6, True), nullable=False, server_default=db.FetchedValue(), info='分佣-PA是合伙人，对应分佣百分比')
    commission_bd_company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='分佣-BD是合伙人的情况下，对应合伙人猎企ID；这是职位当前的BD信息')
    commission_bd_rate = db.Column(db.Float(2, True), nullable=False, server_default=db.FetchedValue(), info='分佣-BD是合伙人，对应分佣百分比')
    commission_pa_owner_status = db.Column(db.Integer, server_default=db.FetchedValue(), info='pa可分佣状态；0：不可申请；1：可申请开票；2：已申请开票；3：已退款不可申请；4：可首款；5：已申请首款')
    commission_bd_owner_status = db.Column(db.Integer, server_default=db.FetchedValue(), info='bd可分佣状态；0：不可申请；1：可申请开票；2：已申请开票；3：已退款不可申请；4：可首款；5：已申请首款')
    receipt_reward = db.Column(db.Float(12, True), server_default=db.FetchedValue(), info='收款-订单实际收款佣金')
    receipt_percent = db.Column(db.Float(6, True), server_default=db.FetchedValue(), info='收款-收款方向的实际比例')
    receipt_month_multiple = db.Column(db.Float(6, True), server_default=db.FetchedValue(), info='收款-收款方向的月薪倍数')
    receipt_pa_rate = db.Column(db.Float(6, True), server_default=db.FetchedValue(), info='先结-pa的分佣比例')
    receipt_bd_rate = db.Column(db.Float(6, True), server_default=db.FetchedValue(), info='先结-bd的分佣比例')
    settle_mode_pa = db.Column(db.Integer, server_default=db.FetchedValue(), info='合伙人pa的结算方式；1：先结；2：后结')
    settle_mode_bd = db.Column(db.Integer, server_default=db.FetchedValue(), info='合伙人bd的结算方式；1：先结；2：后结')



class TbPlacementReceiptsRemind(db.Model):
    __tablename__ = 'tb_placement_receipts_remind'

    id = db.Column(db.BigInteger, primary_key=True)
    placement_id = db.Column(db.BigInteger, nullable=False, index=True)
    should_amount = db.Column(db.Numeric(12, 2), nullable=False, server_default=db.FetchedValue(), info='应收款金额')
    had_amount = db.Column(db.Numeric(12, 2), nullable=False, server_default=db.FetchedValue(), info='已收款款金额')
    receipts_num = db.Column(db.Integer, info='应收款次序')
    should_date = db.Column(db.DateTime, info='应收款时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue(), info='更新时间')



class TbPlacementRecord(db.Model):
    __tablename__ = 'tb_placement_record'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    candidate_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='候选人id')
    placement_id = db.Column(db.BigInteger, nullable=False, index=True, info='成单id')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='状态:1申请2驳回3通过')
    reason = db.Column(db.String(800), nullable=False, server_default=db.FetchedValue(), info='驳回原因')
    approve_time = db.Column(db.DateTime, nullable=False, info='操作时间')
    leave_reason = db.Column(db.String(800), nullable=False, server_default=db.FetchedValue(), info='离职原因')
    leave_time = db.Column(db.DateTime, nullable=False, info='离职时间')
    attachment = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='未过保申请附件')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0未删除，1 删除')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbPlanActivity(db.Model):
    __tablename__ = 'tb_plan_activity'

    id = db.Column(db.BigInteger, primary_key=True, info='唯一编号')
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='用户编号')
    plan_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='策划类型；1:人才市场运营引流活动')
    link_url = db.Column(db.String(100), info='链接地址')
    step = db.Column(db.Integer, info='步骤；1:初始化；2：已通知；3：已完成')
    is_read = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否已读；0:false;1:true')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbPlatformConfig(db.Model):
    __tablename__ = 'tb_platform_config'

    config_key = db.Column(db.Integer, primary_key=True)
    config_value = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    remark = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())



class TbPlatformRewardConfig(db.Model):
    __tablename__ = 'tb_platform_reward_config'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    max_reward = db.Column(db.BigInteger, nullable=False, info='规则，佣金范围下限；-1表示无上限；单位：元')
    min_reward = db.Column(db.BigInteger, info='佣金范围下限；-1：表示无下限；单位元')
    pay_rate = db.Column(db.Float(6, True), info='分成比例')
    update_time = db.Column(db.DateTime, info='更新或者创建时间')
    update_user_id = db.Column(db.BigInteger, info='更新或者创建的用户')



class TbPlatformRewardConfigLog(db.Model):
    __tablename__ = 'tb_platform_reward_config_log'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    conf_id = db.Column(db.BigInteger, info='对应tb_platform_reward_config主键')
    min_reward = db.Column(db.BigInteger, info='当时的最小值')
    max_reward = db.Column(db.BigInteger, info='最大值')
    pay_rate = db.Column(db.Float(6, True), info='分成比例')
    conf_type = db.Column(db.Integer, info='操作类型；1：插入；2：更新；3：删除')
    operate_user_id = db.Column(db.BigInteger, info='操作人')
    operate_time = db.Column(db.DateTime, info='操作时间')



class TbPlatformRewardConfigSnapshot(db.Model):
    __tablename__ = 'tb_platform_reward_config_snapshot'

    id = db.Column(db.BigInteger, primary_key=True)
    rule_json = db.Column(db.String(2047), info='规则json字符串')
    spanshot_time = db.Column(db.DateTime, index=True, info='规则修改的缓存时间')
    user_id = db.Column(db.BigInteger, info='保存这个快照的用户')
    defunct = db.Column(db.Integer, info='逻辑删除')



class TbPortraitCrmPa(db.Model):
    __tablename__ = 'tb_portrait_crm_pa'

    pa_id = db.Column(db.BigInteger, primary_key=True)
    industry_preference = db.Column(db.String(1000), info='行业偏好')
    function_preference = db.Column(db.String(1000), info='职能偏好')
    city_preference = db.Column(db.String(1000), info='城市偏好')
    work_year_preference = db.Column(db.String(1000), info='工作时间偏好')
    annual_level_preference = db.Column(db.String(1000), info='薪资偏好')
    enterprise_develop_preference = db.Column(db.String(1000), info='企业发展偏好')
    enterprise_type_preference = db.Column(db.String(1000), info='企业类型偏好')
    enterprise_scale__preference = db.Column(db.String(1000), info='企业规模')
    feedback_time = db.Column(db.Integer, info='反馈时间')
    interview_rate = db.Column(db.Float(asdecimal=True), info='面试率')
    offer_rate = db.Column(db.Float(asdecimal=True), info='offer率')
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)



class TbPortraitEnterprise(db.Model):
    __tablename__ = 'tb_portrait_enterprise'

    enterprise_id = db.Column(db.BigInteger, primary_key=True, info='企业id作为主键')
    interview_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='面试数')
    recommend_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='推荐数')
    offer_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='offer数')
    over_guarantee_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='过保数')
    interview_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='面试率')
    offer_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='offer率')
    over_guarantee_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='过保率')
    current_position_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='当前职位数')
    new_position_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='新发职位数')
    last_publish_time = db.Column(db.DateTime, info='最后发布职位时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    feedback_time = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='平均反馈时长（分钟）')
    onboard_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='到岗率')
    hr_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='hr人数')



class TbPortraitHeadhunter(db.Model):
    __tablename__ = 'tb_portrait_headhunter'

    headhunter_id = db.Column(db.BigInteger, primary_key=True, index=True, info='猎头id作为主键')
    recommend_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='推荐数')
    interview_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='面试数')
    offer_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='offer数')
    revoke_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='撤销数')
    interview_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='面试率')
    arrive_interview_rate = db.Column(db.Float(asdecimal=True), server_default=db.FetchedValue(), info='到面率')
    offer_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='offer率')
    onboard_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='到岗率')
    revoke_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='撤销率')
    recommend_quality = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='推荐质量')
    server_quality = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='服务质量')
    last_recommend_time = db.Column(db.DateTime, info='最后推荐时间')
    deal_order_trend = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='做单趋势')
    industry_preference = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='行业偏好json格式')
    area_preference = db.Column(db.String(5000), nullable=False, server_default=db.FetchedValue(), info='城市偏好json格式')
    jobtitle_preference = db.Column(db.String(5000), nullable=False, server_default=db.FetchedValue(), info='职能偏好json格式')
    phase_preference = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='公司阶段偏好json格式')
    annualsalary_preference = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='年薪偏好')
    position_level_preference = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='职位等级偏好json格式')
    enterprise_level = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='客户等级json格式')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    onboard_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='到岗数')
    over_guarantee_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='过保数')
    recent_recommend_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='近30日推荐数')
    interviewing_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='面试中的数量')
    enterprise_preference = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='面试企业偏好')
    over_guarantee_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='过保率')
    area_fucos_score = db.Column(db.Integer, info='城市专注度得分')
    industry_fucos_score = db.Column(db.Integer, info='行业专注度得分')
    jobtitle_focus_score = db.Column(db.Integer, info='职能专注度得分')
    annualsalary_focus_score = db.Column(db.Integer, info='年薪专注度得分')
    scale_focus_score = db.Column(db.Integer, info='公司规模专注度得分')
    style_focus_score = db.Column(db.Integer, info='公司类型专注度得分')
    develop_focus_score = db.Column(db.Integer, info='公司发展阶段专注度得分')
    position_level_focus_score = db.Column(db.Integer, info='职位等级专职度得分')
    enterprise_level_focus_score = db.Column(db.Integer, info='企业等级专专注度得分')
    last_visit_recommend_position_time = db.Column(db.DateTime, info='最后一次浏览推荐给他的职位的时间')
    recommend_position_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='猎头推荐职位数')
    last_operation_time = db.Column(db.DateTime, info='猎头最后活跃时间')
    onboard_commission = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='到岗佣金')
    valid_recommend_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='有效推荐数')
    position_browse_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位浏览数量')
    position_collect_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位收藏数量')



class TbPortraitHhCompany(db.Model):
    __tablename__ = 'tb_portrait_hh_company'

    company_id = db.Column(db.BigInteger, primary_key=True, info='猎企id作为主键')
    headhunter_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='猎头顾问数')
    recommend_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='推荐数')
    interview_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='面试数')
    offer_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='offer数')
    revoke_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='撤销数')
    interview_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='面试率')
    offer_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='offer率')
    onboard_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='到岗率')
    revoke_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='撤销率')
    recommend_quality = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='推荐质量')
    server_quality = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='服务质量')
    last_recommend_time = db.Column(db.DateTime, info='最后推荐时间')
    deal_order_trend = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='做单趋势')
    industry_preference = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='行业偏好json格式')
    area_preference = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='区域偏好json格式')
    jobtitle_preference = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='职能偏好json格式')
    phase_preference = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='公司阶段偏好json格式')
    annualsalary_preference = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='年薪偏好')
    position_level_preference = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='职位等级偏好json格式')
    enterprise_level = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='客户等级json格式')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    onboard_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='到岗数')
    over_guarantee_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='过保数')
    recent_recommend_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='近30日推荐数')
    enterprise_preference = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='面试企业偏好')
    over_guarantee_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='过保率')
    valid_user_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='有效猎头数：3个月有做单的猎头数')
    invalid_user_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='无效猎头数：3个月无做单的猎头数')
    have_tags_user_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='有标签猎头数')



class TbPortraitHr(db.Model):
    __tablename__ = 'tb_portrait_hr'

    hr_id = db.Column(db.BigInteger, primary_key=True)
    feedback_time = db.Column(db.BigInteger, info='反馈时长')
    feedback_rate = db.Column(db.Float(asdecimal=True), info='反馈率')
    feedback_statistics = db.Column(db.String(1000), info='反馈统计')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime)
    feedback_overdue_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='反馈逾期数')
    stale_position_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='不新鲜职位数')
    first_publish_position_time = db.Column(db.DateTime, info='hr首次发布职位时间')
    last_publish_position_time = db.Column(db.DateTime, info='hr最后发布职位时间')
    last_feedback_time = db.Column(db.DateTime, info='hr最后反馈时间')
    position_hc_total_count = db.Column(db.BigInteger, info='职位HC总数')
    online_position_hc_total_count = db.Column(db.BigInteger, info='在线职位HC总数')
    online_position_count = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='hr在线职位数')
    this_month_online_position_count = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='hr本月上线职位数')
    history_position_count = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='hr历史职位数')
    three_month_placement_count = db.Column(db.BigInteger, info='最近三个月成单数量')
    six_month_placement_count = db.Column(db.BigInteger, info='最近五个月成单数量')
    year_placement_count = db.Column(db.BigInteger, info='最近一年成单数量')
    all_placement_count = db.Column(db.BigInteger, info='历史总成单数量')
    three_month_placement_reward = db.Column(db.Float(asdecimal=True), info='最近三个月成单额度')
    six_month_placement_reward = db.Column(db.Float(asdecimal=True), info='最近五个月成单额度')
    year_placement_reward = db.Column(db.Float(asdecimal=True), info='最近一年成单额度')
    all_placement_reward = db.Column(db.Float(asdecimal=True), info='历史总成单额度')
    online_total_reward = db.Column(db.Float(asdecimal=True), info='在线总佣金数')
    history_total_reward = db.Column(db.Float(asdecimal=True), info='历史总佣金数')
    online_avg_position_reward = db.Column(db.Float(asdecimal=True), info='在线职位平均佣金')
    history_avg_reward = db.Column(db.Float(asdecimal=True), info='历史职位平均佣金')
    placement_transformed_rate = db.Column(db.Float(asdecimal=True), info='成单转化率')
    active = db.Column(db.Integer, server_default=db.FetchedValue(), info='hr是否活跃 0：非活跃  1：活跃')



class TbPortraitPosition(db.Model):
    __tablename__ = 'tb_portrait_position'

    position_id = db.Column(db.BigInteger, primary_key=True, info='职位id作为主键')
    recommend_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='推荐数')
    interview_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='面试数')
    offer_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='offer数')
    revoke_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='撤销数')
    interview_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='面试率')
    estimate_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='评估数')
    underway_order_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='进行中的订单数')
    deal_order_hh_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='做单猎头数')
    feedback_time = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='反馈时长（单位分钟）')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    feedback_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='反馈率')
    feedback_statistics = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='反馈统计')
    interviewing_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='面试中的数量')
    onboard_count = db.Column(db.Integer, server_default=db.FetchedValue())
    onboard_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='到岗率')
    offer_rate = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='offer率')
    collect_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位收藏数')
    browse_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位浏览数')
    estimate_reject_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='评估未通过数')
    interview_arrive_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='面试到达数')
    interview_pass_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='面试通过数')



class TbPositionAbility(db.Model):
    __tablename__ = 'tb_position_ability'

    id = db.Column(db.BigInteger, primary_key=True)
    ability_name = db.Column(db.String(127), nullable=False, info='能力描述词')
    defunct = db.Column(db.Integer)
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_user_id = db.Column(db.BigInteger)



class TbPositionAbilityRelation(db.Model):
    __tablename__ = 'tb_position_ability_relation'

    id = db.Column(db.BigInteger, primary_key=True)
    position_id = db.Column(db.BigInteger, nullable=False, index=True)
    ability_id = db.Column(db.BigInteger, nullable=False)
    ability_name = db.Column(db.String(127))
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_user_id = db.Column(db.BigInteger)



class TbPositionActiveList(db.Model):
    __tablename__ = 'tb_position_active_list'

    id = db.Column(db.BigInteger, primary_key=True, info='pk')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, info='职位ID')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位有效性true 有效、false 无效')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, info='更新时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建者')
    update_user_id = db.Column(db.BigInteger, info='更新时间')
    active_type = db.Column(db.Integer, info='活动类型，1到岗预付')
    enterprise_id = db.Column(db.BigInteger, nullable=False, info='企业id')
    credit_rate = db.Column(db.Integer, server_default=db.FetchedValue(), info='企业信用（比例）')
    start_time = db.Column(db.DateTime, info='开始时间')
    end_time = db.Column(db.DateTime, info='结束时间')
    static_over_guarantee_rate = db.Column(db.Float(asdecimal=True), server_default=db.FetchedValue(), info='静态过保率')
    pre_pay_rate = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='预付比例')



class TbPositionActivity(db.Model):
    __tablename__ = 'tb_position_activity'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    remark = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue())
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除;0:false 1:true')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbPositionActivityCandidate(db.Model):
    __tablename__ = 'tb_position_activity_candidate'

    id = db.Column(db.BigInteger, primary_key=True)
    position_activity_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    position_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    candidate_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除;0:false 1:true')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)



class TbPositionActivityPlacement(db.Model):
    __tablename__ = 'tb_position_activity_placement'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    position_activity_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    position_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    placement_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除;0:false 1:true')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbPositionActivityRelationship(db.Model):
    __tablename__ = 'tb_position_activity_relationship'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    position_activity_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    position_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除;0:false 1:true')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    score = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='推荐指数')
    remark = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='推荐说明')



class TbPositionAnswer(db.Model):
    __tablename__ = 'tb_position_answer'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    question_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='问题id')
    answer_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='回答者的id')
    answer_user_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='回答者的类型   1:hr,2:hh 3:admin')
    content = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='回答内容')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除 0:未删除 1:已删除')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新人')
    read_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0:未读  1:已读')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue())
    ask_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())



class TbPositionApply(db.Model):
    __tablename__ = 'tb_position_apply'

    id = db.Column(db.BigInteger, primary_key=True, info='主键自增')
    position_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位类型:1非猎头职位')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, info='职位Id')
    enterprise_id = db.Column(db.BigInteger, info='雇主企业id')
    hr_id = db.Column(db.BigInteger, nullable=False, info='HR用户Id')
    yypa_id = db.Column(db.BigInteger, info='运营pa')
    fwpa_id = db.Column(db.BigInteger, info='服务pa')
    feiwa_id = db.Column(db.String(65), info='飞蛙数字字符串Id')
    resume_obj_id = db.Column(db.String(65), info='mongoDB简历Id')
    resume_id = db.Column(db.BigInteger, info='简历Id')
    talent_obj_id = db.Column(db.String(65), info='mongoDB人才id')
    talent_id = db.Column(db.BigInteger, info='人才id')
    now_process_code = db.Column(db.Integer, info='当前流程编号')
    now_process_desc = db.Column(db.String(255), info='当前流程描述')
    now_process_time = db.Column(db.DateTime, info='当前流程时间')
    expect_interview_time = db.Column(db.DateTime, info='下一个流程预期面试时间')
    expect_onboard_time = db.Column(db.DateTime, info='下一个流程时间预期到岗')
    expect_guarantee_time = db.Column(db.DateTime, info='下一个流程时间预期过保')
    actual_onboard_time = db.Column(db.DateTime, info='下一个流程时间实际到岗')
    pay_status = db.Column(db.Integer, server_default=db.FetchedValue(), info='订单支付状态：0未支付/1已支付成功/2已支付失败')
    remote_invoke_status = db.Column(db.Integer, server_default=db.FetchedValue(), info='调用远程接口：0未调用/1调用成功/2调用失败')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_user_id = db.Column(db.BigInteger, info='更新人')
    update_time = db.Column(db.DateTime)



class TbPositionApplyOperateRecord(db.Model):
    __tablename__ = 'tb_position_apply_operate_record'

    id = db.Column(db.BigInteger, primary_key=True, info='主键Id')
    position_apply_id = db.Column(db.BigInteger, nullable=False, info='投递Id')
    operate_type = db.Column(db.Integer, info='操作类型')
    process_code = db.Column(db.Integer, info='当前流程编号')
    process_desc = db.Column(db.String(255), info='当前流程描述')
    process_time = db.Column(db.DateTime, info='当前流程时间')
    hr_id = db.Column(db.BigInteger, nullable=False, info='HR用户Id')
    yypa_id = db.Column(db.BigInteger, info='运营pa')
    feiwa_id = db.Column(db.String(20))
    fwpa_id = db.Column(db.BigInteger, info='服务pa')
    talent_id = db.Column(db.BigInteger, info='人才id')
    talent_obj_id = db.Column(db.String(65), info='mongoDB人才id')
    resume_obj_id = db.Column(db.String(65), info='mongoDB简历Id')
    resume_id = db.Column(db.BigInteger, info='简历Id')
    record_desc = db.Column(db.String(255), info='记录日志说明')
    param_json = db.Column(db.Text, info='附加参数JSON')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_user_id = db.Column(db.BigInteger, info='更新人')
    update_time = db.Column(db.DateTime)



class TbPositionApplyRestrained(db.Model):
    __tablename__ = 'tb_position_apply_restrained'

    id = db.Column(db.BigInteger, primary_key=True)
    headhunter_id = db.Column(db.BigInteger, nullable=False, info='猎头Id')
    obj_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='限制申请职位或者企业ID')
    obj_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='限制的类型：1企业2猎头')
    restrained_reason = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='限制理由')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除 0:未删除 1:已删除')
    create_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())



class TbPositionArea(db.Model):
    __tablename__ = 'tb_position_area'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    name = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='专区名称')
    description = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue(), info='描述')
    min_annual_salary = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='最小年薪')
    max_annual_salary = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='最大年薪')
    industry = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue(), info='行业')
    min_reward_amount = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='最小佣金')
    max_reward_amount = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='最大佣金')
    position_title_keywords = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue(), info='职位名称关键字')
    company_tags = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue(), info='公司标签（多个按照,分割）')
    sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0未删除，1 删除')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbPositionAreaRelationship(db.Model):
    __tablename__ = 'tb_position_area_relationship'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    position_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职位id')
    position_area_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职位专区id')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0未删除，1 删除')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbPositionAutoApply(db.Model):
    __tablename__ = 'tb_position_auto_apply'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    position_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职位id ')
    user_grade_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='抢单猎头等级')
    user_interviewrate_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='面试率')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    apply_type = db.Column(db.Integer, info='职位审核状态:1:自动拒绝,2：自动通过')



class TbPositionBag(db.Model):
    __tablename__ = 'tb_position_bag'
    __table_args__ = (
        db.Index('source_type_time', 'source_type', 'already_time', 'finish_time'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    headhunter_id = db.Column(db.BigInteger, index=True, server_default=db.FetchedValue(), info='猎头id')
    headhunter_company_id = db.Column(db.BigInteger, index=True, server_default=db.FetchedValue(), info='猎头所在的公司id')
    position_id = db.Column(db.BigInteger, index=True, server_default=db.FetchedValue(), info='职位ID')
    source_id = db.Column(db.BigInteger, index=True, server_default=db.FetchedValue(), info='简历ID/职位ID')
    source_type = db.Column(db.Integer, index=True, info='0 简历 ,1职位')
    status = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='0 人职派单  1人职打包 2职职打包  3职职派单')
    candidate_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='订单ID')
    received = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='1：已接收，0：未接受')
    is_reject = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否拒绝接受 0 否 1是')
    reject_reason = db.Column(db.String(500), info='猎头端忽略原因')
    dispatch_user_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='派单人')
    dispatch_user_type = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='派单用户类型 1:HR,2:HH,3:CRM')
    recommend_status = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='推荐状态 0:正常;1:已推荐')
    first_read_time = db.Column(db.DateTime, info='首次阅读时间')
    dispatch_order_id = db.Column(db.BigInteger, info='原派单表ID')
    remark = db.Column(db.String(500), info='备注')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='逻辑删除')
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime, index=True, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    state = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='状态 0:待接单 1:已经接单 2:已经拒绝 3 已经结束')
    delay_take_time = db.Column(db.DateTime, server_default=db.FetchedValue(), info='待接单时间')
    already_time = db.Column(db.DateTime, info='已经接单时间')
    reject_time = db.Column(db.DateTime, info='已经拒绝时间')
    finish_time = db.Column(db.DateTime, info='已经结束时间')
    important_level = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='重要标示0:无;1:重要（暂定）')
    first_already_time = db.Column(db.DateTime, info='首次接单时间')
    first_reject_time = db.Column(db.DateTime, info='首次拒绝时间')
    first_finish_time = db.Column(db.DateTime, info='首次结束时间')
    position_reward_snapshot_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='职位佣金快照')



t_tb_position_bag_2019_12_16 = db.Table(
    'tb_position_bag_2019_12_16',
    db.Column('id', db.BigInteger, nullable=False, info='主键'),
    db.Column('headhunter_id', db.BigInteger, server_default=db.FetchedValue(), info='猎头id'),
    db.Column('headhunter_company_id', db.BigInteger, server_default=db.FetchedValue(), info='猎头所在的公司id'),
    db.Column('position_id', db.BigInteger, server_default=db.FetchedValue(), info='职位ID'),
    db.Column('source_id', db.BigInteger, server_default=db.FetchedValue(), info='简历ID/职位ID'),
    db.Column('source_type', db.Integer, info='0 简历 ,1职位'),
    db.Column('status', db.Integer, server_default=db.FetchedValue(), info='0 人职派单  1人职打包 2职职打包  3职职派单'),
    db.Column('candidate_id', db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='订单ID'),
    db.Column('received', db.Integer, nullable=False, server_default=db.FetchedValue(), info='1：已接收，0：未接受'),
    db.Column('is_reject', db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否拒绝接受 0 否 1是'),
    db.Column('reject_reason', db.String(500), info='猎头端忽略原因'),
    db.Column('dispatch_user_id', db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='派单人'),
    db.Column('dispatch_user_type', db.Integer, nullable=False, server_default=db.FetchedValue(), info='派单用户类型 1:HR,2:HH,3:CRM'),
    db.Column('recommend_status', db.Integer, server_default=db.FetchedValue(), info='推荐状态 0:正常;1:已推荐'),
    db.Column('first_read_time', db.DateTime, info='首次阅读时间'),
    db.Column('dispatch_order_id', db.BigInteger, info='原派单表ID'),
    db.Column('remark', db.String(500), info='备注'),
    db.Column('defunct', db.Integer, nullable=False, server_default=db.FetchedValue(), info='逻辑删除'),
    db.Column('create_user_id', db.BigInteger),
    db.Column('create_time', db.DateTime, server_default=db.FetchedValue()),
    db.Column('update_user_id', db.BigInteger),
    db.Column('update_time', db.DateTime, server_default=db.FetchedValue())
)



class TbPositionBagReject(db.Model):
    __tablename__ = 'tb_position_bag_reject'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    position_bag_id = db.Column(db.BigInteger, nullable=False, index=True, info='职位包ID')
    content_status = db.Column(db.String(50), info='拒绝理由key')
    content = db.Column(db.String(500), info='拒绝原因描述')
    opera_user_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='操作用户类型 1:HR,2:HH,3:CRM')
    opera_user_id = db.Column(db.BigInteger, nullable=False, info='操作用户')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='逻辑删除')
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue())



class TbPositionBlack(db.Model):
    __tablename__ = 'tb_position_black'

    id = db.Column(db.BigInteger, primary_key=True)
    position_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职位编号')
    obj_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='项目编号/猎头编号')
    obj_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='类型：0:项目;1:猎头')
    remark = db.Column(db.String(100), server_default=db.FetchedValue(), info='备注')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbPositionBrowseHistory(db.Model):
    __tablename__ = 'tb_position_browse_history'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='用户编号')
    position_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职位编号')
    browse_time = db.Column(db.DateTime, nullable=False)
    ip = db.Column(db.String(50), info='ip')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbPositionBrowseRecord(db.Model):
    __tablename__ = 'tb_position_browse_record'
    __table_args__ = (
        db.Index('idx_userid_positionid_createtime', 'user_id', 'position_id', 'create_time'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='用户编号')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='职位编号')
    client_type = db.Column(db.Integer, info='客户端类型')
    scene_type = db.Column(db.Integer, info='场景类型')
    scene_code = db.Column(db.String(128), info='场景Code')
    referer = db.Column(db.String(2048), info='请求Referer')
    scene_source_code = db.Column(db.String(255), info='场景来源Code：ai 智能推荐')
    create_time = db.Column(db.DateTime, nullable=False, index=True, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')



class TbPositionCancel(db.Model):
    __tablename__ = 'tb_position_cancel'

    id = db.Column(db.BigInteger, primary_key=True)
    position_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职位id')
    company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='公司id')
    hr_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='HRid')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')



class TbPositionComment(db.Model):
    __tablename__ = 'tb_position_comment'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    position_Id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职位编号')
    reply_comment_Id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='如果为回复记录，则该字段记录评论编号，否则为空')
    reply_user_Id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='回复用户编号')
    user_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='用户类型')
    commenter = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='评论人')
    replyer = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='回复人')
    content = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='评论内容')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否无效 -> 1 : true 已删除；0 : false 有效')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbPositionCommissionRule(db.Model):
    __tablename__ = 'tb_position_commission_rule'

    position_id = db.Column(db.BigInteger, primary_key=True, info='职位表主键；必须是简历职位')
    rule = db.Column(db.Text, info='佣金规则')
    instruction = db.Column(db.Text, info='佣金规则补充说明')
    defunct = db.Column(db.Integer, index=True)
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)



class TbPositionCondition(db.Model):
    __tablename__ = 'tb_position_conditions'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    company_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue())
    conditions = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='职位筛选条件 json字符串类型')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除0false, 1true')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbPositionContactCofig(db.Model):
    __tablename__ = 'tb_position_contact_cofig'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    option_type = db.Column(db.Integer, nullable=False, info='设置类型')
    option_child_type = db.Column(db.Integer, info='子类型')
    option_value = db.Column(db.Integer, info='设置要求值')
    description = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='描述')
    location = db.Column(db.Integer, info='顺序')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbPositionContactOption(db.Model):
    __tablename__ = 'tb_position_contact_option'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, info='职位id')
    contact_config_id = db.Column(db.BigInteger, nullable=False, info='联系规则id')
    contact_value = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='联系方式1：手机；2：座机；3：IM')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbPositionCooperation(db.Model):
    __tablename__ = 'tb_position_cooperation'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='职位id')
    enterprise_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='企业id')
    obj_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎头或猎企Id')
    obj_type = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='对象类型：1猎头2猎企')
    apply_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='申请用户Id')
    position_assign_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职位负责人Id')
    type = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='合作类型：1：指定，2：申请')
    status = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='合作状态0：申请中1：拒绝2：通过')
    extra_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='额外状态;0:正常;1:立项')
    is_inquiry = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否预审；0:false;1:true')
    apply_way = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='申请方式1:推面比申请；2：候选人画像申请；3：免申请特权申请；4：抢单特权申请')
    request_reason = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='申请理由')
    rejected_reason = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='拒绝理由')
    request_time = db.Column(db.DateTime, nullable=False, info='申请时间')
    operate_time = db.Column(db.DateTime, info='拒绝或通过的操作时间')
    accept_time = db.Column(db.DateTime, info='批准时间')
    reject_times = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='拒绝申请次数')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='是否删除 0:未删除 1:已删除')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    hh_defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否猎头删除')
    source_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='数据来源类型')
    option_ids = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='拒绝选项id')
    appy_user_company_id = db.Column(db.BigInteger, nullable=False, info='申请人公司ID')
    recommend_status = db.Column(db.Integer, server_default=db.FetchedValue(), info='推荐状态 0:正常;1:已推荐')
    pa_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='pa id')



class TbPositionDataLog(db.Model):
    __tablename__ = 'tb_position_data_log'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, info='猎头id')
    bdo_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    pa_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    enterprise_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='企业id')
    placement_reward = db.Column(db.Float, nullable=False, server_default=db.FetchedValue(), info='实际成单佣金')
    onboard_on_reward = db.Column(db.Float, nullable=False, server_default=db.FetchedValue(), info='实际到岗佣金')
    onboard_over_reward = db.Column(db.Float, nullable=False, server_default=db.FetchedValue(), info='实际过保佣金')
    candidate_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='推荐数')
    interview_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='面试数')
    placement_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='成单数')
    onboard_on_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='到岗数')
    onboard_left_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='离岗数')
    count_date = db.Column(db.Date, nullable=False, index=True, info='统计时间')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbPositionDispatchHunter(db.Model):
    __tablename__ = 'tb_position_dispatch_hunter'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, info='职位ID')
    hunter_id = db.Column(db.BigInteger, nullable=False, index=True, info='猎头ID')
    operation_id = db.Column(db.BigInteger, nullable=False, info='操作人ID')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    user_type = db.Column(db.Integer, nullable=False, info='用户类型 1 hr   2 crm用户')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='状态 0.未浏览 1.浏览  2.收藏  3.做单')
    source_type = db.Column(db.Integer, nullable=False, info='来源 ： 1 推荐 2 搜索')
    massage = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='通知猎头的次数')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1.给职位推猎头  2.给猎头推职位')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')



class TbPositionEditLog(db.Model):
    __tablename__ = 'tb_position_edit_log'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    position_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职位编号')
    original = db.Column(db.String(5000), nullable=False, server_default=db.FetchedValue())
    target = db.Column(db.String(5000), nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')



class TbPositionFree(db.Model):
    __tablename__ = 'tb_position_free'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    title = db.Column(db.String(500), info='职位标题')
    enterprise_id = db.Column(db.BigInteger, info='企业Id')
    position_type = db.Column(db.Integer, info='职位(公开)类型:1公开/2私密')
    work_country_id = db.Column(db.BigInteger, info='国家')
    work_province_id = db.Column(db.BigInteger, info='省份')
    work_city_id = db.Column(db.BigInteger, info='城市')
    work_area_id = db.Column(db.BigInteger, info='地区')
    work_address = db.Column(db.String(255), info='工作地址')
    place = db.Column(db.String(255), info='交通说明')
    profession_type_id = db.Column(db.BigInteger, info='职能类别')
    profession_type_parent_id = db.Column(db.BigInteger, info='职能父级Id')
    industry_id = db.Column(db.BigInteger, info='行业Id')
    month_salary_rule = db.Column(db.Integer, info='月薪制度')
    min_show_annual_salary = db.Column(db.Float(10, True), info='最小年薪')
    max_show_annual_salary = db.Column(db.Float(10, True), info='最大年薪')
    min_show_month_salary = db.Column(db.Float(10, True), info='最小月薪')
    max_show_month_salary = db.Column(db.Float(10, True), info='最大月薪')
    work_exp_required = db.Column(db.Integer, info='工作年限要求')
    work_exp_start = db.Column(db.Integer, info='最低工作年限')
    work_exp_end = db.Column(db.Integer, info='最大工作年限')
    work_exp_year_desc = db.Column(db.String(255), info='工作年限描述')
    age_start = db.Column(db.Integer, info='最低年龄')
    age_end = db.Column(db.Integer, info='最大年龄')
    age_required = db.Column(db.String(65), info='年龄要求')
    gender_required = db.Column(db.Integer, info='性别要求')
    degree_required = db.Column(db.Integer, info='学历要求')
    certificate = db.Column(db.String(255), info='证书要求')
    language_required = db.Column(db.String(255), info='语言要求')
    language_string_required = db.Column(db.String(255), info='语言要求字符串')
    college_req = db.Column(db.String(255), info='院校要求')
    job_description = db.Column(db.Text, info='职位描述')
    job_requirement = db.Column(db.Text, info='职位需求')
    welfare = db.Column(db.Text, info='职位亮点')
    position_label = db.Column(db.Text, info='职位标签关键字')
    status = db.Column(db.Integer, info='状态:0:发布/1草稿/2关闭/3关闭中/4暂停/7删除')
    head_count = db.Column(db.Integer, info='招聘人数')
    position_assign_id = db.Column(db.BigInteger, info='负责的HRId')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_user_id = db.Column(db.BigInteger, info='更新人')
    update_time = db.Column(db.DateTime)
    publish_user_id = db.Column(db.BigInteger, info='发布人')
    publish_time = db.Column(db.DateTime, info='发布时间')
    is_trial = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否试用版')
    position_classification_code = db.Column(db.String(10), info='职位职能Code（算法计算）')



class TbPositionFreeConf(db.Model):
    __tablename__ = 'tb_position_free_conf'

    position_free_id = db.Column(db.BigInteger, primary_key=True, unique=True, info='非猎头职位Id')
    is_recruitment = db.Column(db.Integer, info='是否招聘 1:招聘/0:不招聘')
    is_receive_resume = db.Column(db.Integer, info='是否接收简历 1接收/0不接收')
    match_resume_count = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='符合职位的简历匹配数量')
    interest_resume_count = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='对次简历感兴趣数量')
    receive_resume_count = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='收到的简历数量')
    forward_qrcode = db.Column(db.String(255), info='转发二维码信息')
    responsible_pa_id = db.Column(db.BigInteger, info='当前负责PA')
    create_with_position_id = db.Column(db.BigInteger, info='从某份JD导入')
    pa_remark = db.Column(db.String(500), info='pa备注')
    accurate_resume_count = db.Column(db.BigInteger, info='精准人才数量')
    invite_count = db.Column(db.BigInteger, server_default=db.FetchedValue())
    invite_success_count = db.Column(db.BigInteger, server_default=db.FetchedValue())
    interview_count = db.Column(db.BigInteger, server_default=db.FetchedValue())
    offer_count = db.Column(db.BigInteger, server_default=db.FetchedValue())
    onboard_count = db.Column(db.BigInteger, server_default=db.FetchedValue())
    position_edit_count = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='职位编辑次数')



class TbPositionInvestigate(db.Model):
    __tablename__ = 'tb_position_investigate'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    position_id = db.Column(db.BigInteger, nullable=False, info='职位编号')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1:问答类,2:select,3:radio,4checkbox')
    issue = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='问题')
    statement = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='答案')
    sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0未删除，1 删除')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbPositionLabel(db.Model):
    __tablename__ = 'tb_position_label'

    id = db.Column(db.BigInteger, primary_key=True)
    position_id = db.Column(db.BigInteger, nullable=False)
    label_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class TbPositionLibrary(db.Model):
    __tablename__ = 'tb_position_library'
    __table_args__ = (
        db.Index('position_id_company_id', 'company_id', 'position_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    user_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='猎头id')
    company_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='猎头公司id')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='职位id')
    tag_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='标签类型')
    mark_tag_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='标记标签操作人')
    is_assign = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否已分配')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='状态 0:正常；1:异常')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除 0:未删除 1:已删除')
    remark = db.Column(db.String(50), info='备注')
    first_scene_type = db.Column(db.Integer, info='首次场景类型')
    first_scene_code = db.Column(db.String(128), info='首次场景Code')
    first_scene_source_code = db.Column(db.String(255), info='首次场景来源Code')
    create_scene_type = db.Column(db.Integer, info='创建时场景类型')
    create_scene_code = db.Column(db.String(128), info='创建时场景Code')
    create_scene_source_code = db.Column(db.String(255), info='创建时间场景来源Code')
    create_time = db.Column(db.DateTime, nullable=False, index=True)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())



class TbPositionLocation(db.Model):
    __tablename__ = 'tb_position_locations'

    id = db.Column(db.BigInteger, primary_key=True)
    position_id = db.Column(db.BigInteger, nullable=False, index=True, info='职位ID')
    province_id = db.Column(db.BigInteger, info='省份')
    city_id = db.Column(db.BigInteger, info='城市')
    address = db.Column(db.String(255), info='详细工作地址')
    create_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)



class TbPositionMatchTalent(db.Model):
    __tablename__ = 'tb_position_match_talent'

    id = db.Column(db.BigInteger, primary_key=True)
    position_id = db.Column(db.BigInteger, nullable=False, index=True, info='职位ID')
    talent_md5 = db.Column(db.String(50), nullable=False, index=True, server_default=db.FetchedValue(), info='外部人才id')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    match_degree = db.Column(db.Integer, nullable=False, info='匹配度')
    source_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='用户来源类型 1.巧达 2.hd 3.jobhunter')
    match_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='匹配类型  1.系统匹配 2.c端我要面试职位')



class TbPositionOperationClassifyRank(db.Model):
    __tablename__ = 'tb_position_operation_classify_rank'

    id = db.Column(db.BigInteger, primary_key=True, info='主键编号')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, info='职位编号')
    position_type = db.Column(db.Integer, nullable=False, info='职位类型')
    rank_type = db.Column(db.Integer, nullable=False, info='职位等级类型 1 第一阶段 2 第二阶段 3 第三阶段 4 第三阶段')
    rank_start_time = db.Column(db.DateTime, nullable=False, info='职位分类阶段开始时间')
    rank_end_time = db.Column(db.DateTime, nullable=False, info='职位分类阶段结束时间')
    is_apply = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否有申请阶段')
    dispatch_start_time = db.Column(db.DateTime, info='派单开始时间')
    dispatch_end_time = db.Column(db.DateTime, info='派单结束时间')
    apply_start_time = db.Column(db.DateTime, info='申请开始时间')
    apply_end_time = db.Column(db.DateTime, info='申请结束时间')
    is_expire = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否失效 0 否 1 是')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除 0 否 1 是')



class TbPositionOperationPhase(db.Model):
    __tablename__ = 'tb_position_operation_phase'

    id = db.Column(db.BigInteger, primary_key=True, info='主键编号')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, info='职位编号')
    phase_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='阶段类型 1 指派阶段 2 申请阶段')
    start_time = db.Column(db.DateTime, info='开始时间')
    end_time = db.Column(db.DateTime, info='结束时间')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, info='更新人')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除 0 否 1 是')



class TbPositionOperationPhaseLog(db.Model):
    __tablename__ = 'tb_position_operation_phase_log'

    id = db.Column(db.BigInteger, primary_key=True, info='主键编号')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, info='职位编号')
    position_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位类型 1 公开 2 私密')
    phase_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='阶段类型 1 指派阶段 2 申请阶段')
    start_time = db.Column(db.DateTime, info='开始时间')
    end_time = db.Column(db.DateTime, info='结束时间')
    is_pre = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否预设 0 否 1 是')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建人')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除 0 否 1 是')



class TbPositionOperationPhasePre(db.Model):
    __tablename__ = 'tb_position_operation_phase_pre'

    id = db.Column(db.BigInteger, primary_key=True, info='主键编号')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, info='职位编号')
    phase_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='阶段类型 1 指派阶段 2 申请阶段')
    start_time = db.Column(db.DateTime, info='开始时间')
    end_time = db.Column(db.DateTime, info='结束时间')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, info='更新人')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除 0 否 1 是')



class TbPositionOperationPre(db.Model):
    __tablename__ = 'tb_position_operation_pre'

    id = db.Column(db.BigInteger, primary_key=True, info='主键编号')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, info='职位编号')
    hh_total = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='做单猎头数')
    auto_apply_interview_ratio = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='申请条件%')
    auto_reject_interview_ratio = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='自动通过条件%')
    apply_required = db.Column(db.String(500), info='申请须知')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, info='更新人')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除 0 否 1 是')



class TbPositionOperationUser(db.Model):
    __tablename__ = 'tb_position_operation_user'
    __table_args__ = (
        db.Index('user_id', 'user_id', 'position_id'),
        db.Index('idx_positionid_userid', 'position_id', 'user_id')
    )

    id = db.Column(db.BigInteger, primary_key=True, info='自增编号')
    user_id = db.Column(db.BigInteger, nullable=False, info='用户编号（运营PA）')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, info='职位编号')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbPositionOperationUser20180621(db.Model):
    __tablename__ = 'tb_position_operation_user_20180621'
    __table_args__ = (
        db.Index('idx_user_position_id', 'user_id', 'position_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='自增编号')
    user_id = db.Column(db.BigInteger, nullable=False, info='用户编号（运营PA）')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, info='职位编号')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbPositionOperationUserDic(db.Model):
    __tablename__ = 'tb_position_operation_user_dic'

    id = db.Column(db.BigInteger, primary_key=True, info='自增编号')
    user_id = db.Column(db.BigInteger, nullable=False, info='用户编号')
    position_titile_ids = db.Column(db.String(255), info='职能编号，多个","隔开')
    custom_ids = db.Column(db.String(255), info='自定义职能ID，多个","隔开')
    city_ids = db.Column(db.String(255), info='地区编号，多个","隔开')
    org_ids = db.Column(db.String(255), info='组织架构编号，多个","隔开')
    po_ids = db.Column(db.String(255), info='PO编号，多个","隔开')
    spa_ids = db.Column(db.String(255), info='运营PA，多个","隔开')
    exclude_spa_ids = db.Column(db.String(255), info='排除运营PA，多个","隔开')
    enterprise_system_ids = db.Column(db.String(255), info='企业派系，多个","隔开')
    is_clear = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否清理数据 0 否 1是')
    create_time = db.Column(db.DateTime, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, info='更新时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())



class TbPositionOptimizationDescription(db.Model):
    __tablename__ = 'tb_position_optimization_description'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='职位编号')
    description = db.Column(db.String(256), info='描述')
    state = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='状态 1 有效  0 无效')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False)



class TbPositionPackage(db.Model):
    __tablename__ = 'tb_position_package'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(200), nullable=False, info='职位包名称')
    description = db.Column(db.String(800), nullable=False, server_default=db.FetchedValue(), info='专场描述')
    share_key = db.Column(db.String(100), nullable=False, index=True, server_default=db.FetchedValue(), info='专场的key')
    contact_id = db.Column(db.String(800), nullable=False, server_default=db.FetchedValue(), info='联系人id')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位包状态:1:开放,2:暂停')
    end_time = db.Column(db.DateTime, info='可分享的失效时间')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    ower_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='所有者id')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    target_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='打包目标id')
    package_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位包类型:0:线上,1:线下')
    address = db.Column(db.String(800), nullable=False, server_default=db.FetchedValue(), info='专场地点')
    start_time = db.Column(db.DateTime, info='专场开始日期')
    over_time = db.Column(db.DateTime, info='专场结束日期')
    pic_path = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='图片')



class TbPositionPackageRelation(db.Model):
    __tablename__ = 'tb_position_package_relation'

    id = db.Column(db.BigInteger, primary_key=True)
    position_package_id = db.Column(db.BigInteger, nullable=False, info='职位包外键id')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, info='职位id')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    sort_number = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='序号')



class TbPositionPauseRule(db.Model):
    __tablename__ = 'tb_position_pause_rule'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    rule_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='暂停规则类型 0：候选人数达到限制  1：总面试数达到限制  2：职位未操作天数 3：职位N天未处理的候选人N数')
    candidate_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='候选人数')
    interview_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='面试数')
    position_days_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位天数')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除 0:未删除 1:已删除')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')



class TbPositionPkgBrowse(db.Model):
    __tablename__ = 'tb_position_pkg_browse'

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, nullable=False, index=True)
    position_pkg_key = db.Column(db.String(50), nullable=False, index=True, info='职位包唯一key')
    source = db.Column(db.String(20), nullable=False, info='点击来源')
    browse_time = db.Column(db.DateTime, nullable=False, info='浏览时间')



class TbPositionPkgPosition(db.Model):
    __tablename__ = 'tb_position_pkg_position'

    id = db.Column(db.BigInteger, primary_key=True)
    position_id = db.Column(db.BigInteger, nullable=False, info='职位id')
    user_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='用户id')
    user_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='用户类型')
    position_pkg_key = db.Column(db.String(50), nullable=False, index=True, info='职位包唯一key')
    source = db.Column(db.String(20), nullable=False, info='点击来源')
    action_type = db.Column(db.Integer, nullable=False, info='动作类型，0:浏览，1：收藏')
    create_time = db.Column(db.DateTime, nullable=False, info='浏览时间')



class TbPositionPloy(db.Model):
    __tablename__ = 'tb_position_ploy'
    __table_args__ = (
        db.Index('outer_s_t_id', 'outer_enterprise_source', 'outer_position_type', 'outer_position_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='职位编号')
    position_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位类型:0:申请,1公开,2:私密,3:暂停,4:抢单')
    auto_apply_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='自动申请状态:0:否，1:是')
    auto_reject_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='自动拒绝状态:0:否，1:是')
    user_grade_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='抢单猎头等级:0无等级,1:铜牌,2:银牌,3:金牌,4:钻,5:皇冠')
    is_grab_order = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否是抢单职位:0不是,1:是')
    grab_order_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='抢单职位数量')
    surplus_grab_order_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='剩余抢单职位数量')
    effective_recommend_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='抢单猎头有效推荐数')
    effective_interview_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='抢单猎头面试数')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue(), info='更新时间')
    publish_grab_order_time = db.Column(db.DateTime, info='发布抢单职位时间')
    task_grab_order_time = db.Column(db.DateTime, info='抢单任务开始时间')
    update_grab_position_time = db.Column(db.DateTime, info='抢单职位更新为公开职位时的时间')
    accept_order_days = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='做单天数')
    position_assign_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='职位负责人')
    task_date = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='抢单任务周期,1:1周,2:2周,3:3周,4:1个月,8:2个月,12:3个月')
    publish_user_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='发布职位的用户类型、默认HR发布')
    grab_order_reserve_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='抢单预定状态;0:默认状态；1:预定中；2:预定结束')
    value = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='价值积分')
    product_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='职位产品类型:1:标准版,2：佣金宝，3：到岗快')
    product_pay_rate = db.Column(db.Integer, info='产品到岗时付的佣金比例')
    position_title_subid = db.Column(db.BigInteger)
    position_title_subname = db.Column(db.String(1000))
    hunteron_reward_type = db.Column(db.Integer, info='佣金类型（猎上设置）0：固定佣金   1：年薪百分比')
    hunteron_fixed_reward_amount = db.Column(db.Float(asdecimal=True), info='固定佣金（猎上设置）')
    hunteron_max_reward_amount = db.Column(db.Float(asdecimal=True), info='最高佣金（猎上设置）')
    hunteron_percentage = db.Column(db.Float(asdecimal=True), info='佣金比例（猎上设置）')
    hunteron_min_reward_amount = db.Column(db.Float(asdecimal=True), info='最小佣金（猎上设置）')
    hunteron_operate_time = db.Column(db.DateTime, info='操作时间（猎上设置）')
    position_modify_reward_time = db.Column(db.DateTime, info='职位佣金修改时间（HR）')
    familiar_skills = db.Column(db.String(1000), info='熟悉技能')
    master_skills = db.Column(db.String(1000), info='精通技能')
    survey_result = db.Column(db.String(1000), info='调研结果')
    feed_back_type = db.Column(db.Integer, info='反馈类型')
    feed_back_time = db.Column(db.DateTime, info='反馈时间')
    submit_audit_time = db.Column(db.DateTime, info='提交审核时间')
    audit_time = db.Column(db.DateTime, info='审核时间')
    requirement_type = db.Column(db.Integer, info='需求类型1.公开需求2.特殊需求')
    requirement_desc = db.Column(db.Text, info='需求补充说明')
    sys_valid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='系统判断是否有效 0 无效 1 有效')
    manual_valid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='人工判断是否有效 0 无效 1 有效')
    first_po_valid_time = db.Column(db.DateTime, info='po首次设置职位有效的时间')
    po_audit_time = db.Column(db.DateTime, info='po审核时间')
    specific_items = db.Column(db.String(2000), info='特殊条款')
    operation_classify_type = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='职位运营分类类型 1 骨 2 铜 3 银 4 金')
    operation_rank_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='职位当前阶段 1 第一阶段 2 第二阶段 3 第三阶段 4 第四阶段')
    recommend_new_status_count = db.Column(db.Integer, server_default=db.FetchedValue(), info='新推状态数')
    open_reason_info = db.Column(db.Text, info='开放原因')
    submit_audit_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='调研人')
    audit_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='审核人')
    related_description = db.Column(db.String(2047), nullable=False, server_default=db.FetchedValue(), info='汇报对象介绍')
    position_attribute = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位属性 1 普通职位 2 RPO职位')
    interview_process_json = db.Column(db.Text, info='面试流程JSON')
    position_star = db.Column(db.String(2), info='职位定级（A级、B级、C级）')
    position_pay_rate90 = db.Column(db.Integer, info='职位-分成比例-19猎企')
    position_pay_rate80 = db.Column(db.Integer, info='职位-分成比例-28猎企')
    pay_rate = db.Column(db.Integer, info='分成比例')
    position_introduction_attachment = db.Column(db.String(1000), info='职位附件')
    position_introduction_attachment_name = db.Column(db.String(1000), info='职位附件-名称')
    position_description_recording = db.Column(db.String(1000), info='职位说明录音')
    dispatch_priority_time = db.Column(db.Float(asdecimal=True), nullable=False, index=True, server_default=db.FetchedValue(), info='派单优先时间')
    dispatch_priority_visible_time = db.Column(db.DateTime, info='派单可见时间')
    outer_position_type = db.Column(db.Integer, info='外部平台，职位类型；例如开放猎场、定向职位')
    outer_channel_account_id = db.Column(db.BigInteger, info='外部渠道-账号ID')
    outer_position_id = db.Column(db.String(63), info='外部平台，职位ID')
    outer_enterprise_source = db.Column(db.Integer, info='外部平台，类型，比如平安')
    position_client_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='发布职位的客户端类型；1：旧版本hr，包括saas版本；2：新版本OnWork')
    max_hunter_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='该职位的做单猎头数限制；-1：不限')
    normal_price = db.Column(db.Float(6, True), info='普通职位的定价，单位：元')
    publish_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='职位的发布类型；1：猎头职位；2：普通职位；默认1')
    reward_display_rate = db.Column(db.Integer, server_default=db.FetchedValue(), info='职位佣金显示比例，0~100，100表示100%')
    reward_display_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='显示比例对应类型；1：默认；2：预扣')
    month_salary_multiple = db.Column(db.Float(5, True), server_default=db.FetchedValue(), info='佣金类型为月薪倍数时，记录月薪倍数')
    guarantee_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='职位保证期类型；1：月数；2：天数')
    ai_screening = db.Column(db.Integer, server_default=db.FetchedValue(), info='ai初筛项；1:未设置初筛  2 设置初筛 3:不适用初筛')
    position_owner = db.Column(db.Integer, server_default=db.FetchedValue(), info='职位发布者类型；1：猎上发布；2：合伙人发布')
    implicit_requirement = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='隐性要求:0无,1:有')
    provide_make_material = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='提供做单资料:0无,1:有')
    position_assign_company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职位负责人猎企id')
    market_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位上下架状态；0：未上架；1：已上架；2：已下架')
    underline_count = db.Column(db.Integer, info='管理职能的下属人数')
    difficult_score = db.Column(db.Float(6, True), server_default=db.FetchedValue(), info='难度分')
    emphasis_position_switch = db.Column(db.Integer, server_default=db.FetchedValue(), info='重点职位开关')
    emphasis_position_chang_time = db.Column(db.DateTime, info='重点职位变更时间')
    withhold_hunteron_rate = db.Column(db.Float(6, True), nullable=False, server_default=db.FetchedValue(), info='猎上作为平台的预扣百分比')
    withhold_enterprise_rate = db.Column(db.Float(6, True), nullable=False, server_default=db.FetchedValue(), info='预扣-雇主的比例')
    withhold_pa_operate_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='预扣-PA运营类型')
    withhold_bd_operate_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='预扣-BD运营类型')
    withhold_pa_company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='预扣-PA是合伙人的情况下，对应合伙人猎企ID')
    withhold_pa_rate = db.Column(db.Float(6, True), nullable=False, server_default=db.FetchedValue(), info='预扣-PA是合伙人，对应预扣百分比')
    withhold_bd_company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='预扣-BD是合伙人的情况下，对应合伙人猎企ID')
    withhold_bd_rate = db.Column(db.Float(6, True), nullable=False, server_default=db.FetchedValue(), info='预扣-BD是合伙人，对应预扣百分比')
    commission_enterprise_rate = db.Column(db.Float(6, True), nullable=False, server_default=db.FetchedValue(), info='分佣-雇主的比例')
    commission_pa_operate_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='分佣-PA运营类型')
    commission_bd_operate_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='分佣-BD运营类型')
    commission_pa_company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='分佣-PA是合伙人的情况下，对应合伙人猎企ID；这是职位当前的PA信息')
    commission_pa_rate = db.Column(db.Float(6, True), nullable=False, server_default=db.FetchedValue(), info='分佣-PA是合伙人，对应分佣百分比')
    commission_bd_company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='分佣-BD是合伙人的情况下，对应合伙人猎企ID；这是职位当前的BD信息')
    commission_bd_rate = db.Column(db.Float(2, True), nullable=False, server_default=db.FetchedValue(), info='分佣-BD是合伙人，对应分佣百分比')



class TbPositionPortrait(db.Model):
    __tablename__ = 'tb_position_portrait'

    position_id = db.Column(db.BigInteger, primary_key=True, info='职位编号')
    offer_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='offer总数')
    candidate_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='候选人总数')
    interviewer_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='面试人数')
    feedback_time = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='反馈时长（单位分钟）')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbPositionPreemption(db.Model):
    __tablename__ = 'tb_position_preemption'

    position_id = db.Column(db.BigInteger, primary_key=True, server_default=db.FetchedValue(), info='职位id')
    hh_title_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='头衔id')
    preemption_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位抢单数量')
    preemption_remain_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位剩余抢单数量')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbPositionPreemptionHh(db.Model):
    __tablename__ = 'tb_position_preemption_hh'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    position_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职位id')
    hh_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎头id')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0未删除，1 删除')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbPositionPreemptionHhBlacklist(db.Model):
    __tablename__ = 'tb_position_preemption_hh_blacklist'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    hh_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎头id')
    expire_time = db.Column(db.DateTime, nullable=False, info='惩罚到期时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbPositionProduct(db.Model):
    __tablename__ = 'tb_position_product'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    product_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位产品类型:1:标准版,2：佣金宝，3：到岗快')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    product_desc = db.Column(db.String(1000), info='产品描述')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class TbPositionProject(db.Model):
    __tablename__ = 'tb_position_project'
    __table_args__ = (
        db.Index('position_id_company_id', 'position_id', 'company_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='唯一编号')
    project_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='项目类型;0:普通1:特殊;2:私密')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='职位编号')
    company_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='公司编号')
    max_member_total = db.Column(db.Integer, info='最大成员数量')
    max_member_recommend_total = db.Column(db.Integer, info='最大推荐成员数量')
    important_level = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='重要标示0:无;1:重要（暂定）')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位项目状态;0:正常;1:关闭;2:异常')
    extra_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位项目状态;0:正常;1:关闭')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbPositionProjectMember(db.Model):
    __tablename__ = 'tb_position_project_member'
    __table_args__ = (
        db.Index('project_id_user_id', 'project_id', 'user_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='唯一编号')
    project_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='项目编号')
    company_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='公司编号')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='职位编号')
    user_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='用户编号')
    role_type = db.Column(db.Integer, info='角色类型：1:不能推荐;2:推荐需审核;3:推荐候选人')
    is_manager = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否管理者')
    is_owner = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='是否owner')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='成员状态;0:正常;1:离职')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbPositionQuestion(db.Model):
    __tablename__ = 'tb_position_question'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='职位id')
    ask_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='提问人')
    ask_user_type = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='提问人的类型')
    question_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='问题类型')
    content = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='问题内容')
    resolved = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否解决 0:未解决 1:已解决')
    anonymity = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否匿名 0:不匿名 1:匿名')
    is_read = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否已读：0：未读，1：已读')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='是否删除 0:未删除 1:已删除')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')



class TbPositionReward(db.Model):
    __tablename__ = 'tb_position_reward'

    position_id = db.Column(db.BigInteger, primary_key=True, server_default=db.FetchedValue(), info='职位编号')
    custom_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    reward = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    description = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, info='修改时间')



class TbPositionRewardSnapshot(db.Model):
    __tablename__ = 'tb_position_reward_snapshot'
    __table_args__ = (
        db.Index('idx_position_id_version', 'position_id', 'snapshot_version'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    position_id = db.Column(db.BigInteger, nullable=False)
    snapshot_version = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='快照是否是当前值；1：当前值；0：历史快照')
    withhold_hunteron_rate = db.Column(db.Float(6, True), nullable=False, server_default=db.FetchedValue(), info='猎上作为平台的预扣百分比')
    withhold_enterprise_rate = db.Column(db.Float(6, True), nullable=False, server_default=db.FetchedValue(), info='预扣-雇主的比例')
    withhold_pa_operate_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='预扣-PA运营类型')
    withhold_bd_operate_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='预扣-BD运营类型')
    withhold_pa_company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='预扣-PA是合伙人的情况下，对应合伙人猎企ID')
    withhold_pa_rate = db.Column(db.Float(6, True), nullable=False, server_default=db.FetchedValue(), info='预扣-PA是合伙人，对应预扣百分比')
    withhold_bd_company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='预扣-BD是合伙人的情况下，对应合伙人猎企ID')
    withhold_bd_rate = db.Column(db.Float(6, True), nullable=False, server_default=db.FetchedValue(), info='预扣-BD是合伙人，对应预扣百分比')
    commission_enterprise_rate = db.Column(db.Float(6, True), nullable=False, server_default=db.FetchedValue(), info='分佣-雇主的比例')
    commission_pa_operate_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='分佣-PA运营类型')
    commission_bd_operate_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='分佣-BD运营类型')
    commission_pa_company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='分佣-PA是合伙人的情况下，对应合伙人猎企ID；这是职位当前的PA信息')
    commission_pa_rate = db.Column(db.Float(6, True), nullable=False, server_default=db.FetchedValue(), info='分佣-PA是合伙人，对应分佣百分比')
    commission_bd_company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='分佣-BD是合伙人的情况下，对应合伙人猎企ID；这是职位当前的BD信息')
    commission_bd_rate = db.Column(db.Float(2, True), nullable=False, server_default=db.FetchedValue(), info='分佣-BD是合伙人，对应分佣百分比')
    message = db.Column(db.String(255), info='快照信息备注')
    defunct = db.Column(db.Integer, index=True, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    reward_display_rate = db.Column(db.Integer, server_default=db.FetchedValue(), info='职位佣金显示比例，0~100，100表示100%')
    reward_display_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='显示比例对应类型；1：默认；2：预扣')



class TbPositionRightArrived(db.Model):
    __tablename__ = 'tb_position_right_arrived'

    id = db.Column(db.BigInteger, primary_key=True)
    position_id = db.Column(db.BigInteger, nullable=False, index=True)
    cycle_interval_day = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='发送短信的周期间隔,单位天')
    end_time = db.Column(db.DateTime, index=True, info='巧达活动的结束时间')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1:同步,2:取消同步')
    syn_operator_time = db.Column(db.DateTime, info='同步的操作时间')
    syn_operator_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='同步操作人的id')
    cancel_syn_operator_time = db.Column(db.DateTime, info='取消同步的操作时间')
    cancel_syn_operator_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='取消同步的操作人id')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否已删除  1 : true 已删除；0 : false 有效')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)



class TbPositionShare(db.Model):
    __tablename__ = 'tb_position_share'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    internal_name = db.Column(db.String(256), nullable=False, info='内部名称')
    project_name = db.Column(db.String(256), info='项目名称')
    qq_link = db.Column(db.String(256), info='QQ链接')
    wx_link = db.Column(db.String(256), info='微信链接')
    dd_link = db.Column(db.String(256), info='微信链接')
    created_user_id = db.Column(db.BigInteger, nullable=False, index=True, info='创建用户ID')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='修改时间')
    updated_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改用户ID')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='修改时间')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='逻辑删除')



class TbPositionShareCode(db.Model):
    __tablename__ = 'tb_position_share_code'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    code = db.Column(db.String(32), nullable=False, info='职位ids的对应码')
    position_ids = db.Column(db.String(500), nullable=False, info='职位id字符串，以逗号分隔')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    hh_id = db.Column(db.BigInteger, nullable=False, info='分享的猎头ID')
    qr_code = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='二维码地址')



class TbPositionShareEnterprise(db.Model):
    __tablename__ = 'tb_position_share_enterprise'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    position_share_id = db.Column(db.BigInteger, nullable=False, index=True, info='主键')
    enterprise_name = db.Column(db.String(256), nullable=False, info='雇主名称')
    project_backdrop = db.Column(db.Text, nullable=False, info='项目背景')
    position_id = db.Column(db.Text, nullable=False, info='职位ID列表')
    position_description = db.Column(db.Text, nullable=False, info='职位描述做单要求')
    created_user_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='创建用户ID')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='修改时间')
    updated_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改用户ID')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='修改时间')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='逻辑删除')



class TbPositionShareStatistic(db.Model):
    __tablename__ = 'tb_position_share_statistics'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    position_share_id = db.Column(db.BigInteger, nullable=False, index=True, info='主键')
    qq_browse_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='QQ浏览统计')
    qq_share_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='QQ分享统计')
    wx_browse_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='微信浏览统计')
    wx_share_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='微信分享统计')
    dd_browse_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='钉钉浏览统计')
    dd_share_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='钉钉分享统计')
    created_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建用户ID')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='修改时间')
    updated_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改用户ID')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='修改时间')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='逻辑删除')



class TbPositionSkill(db.Model):
    __tablename__ = 'tb_position_skills'

    group_id = db.Column(db.BigInteger, primary_key=True)
    skills = db.Column(db.String(2000), nullable=False)



class TbPositionSubscribeRecord(db.Model):
    __tablename__ = 'tb_position_subscribe_record'

    id = db.Column(db.BigInteger, primary_key=True, info='唯一编号')
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='用户id')
    name = db.Column(db.String(50), info='名称')
    subscribe_value = db.Column(db.String, info='订阅条件json')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbPositionSurvey(db.Model):
    __tablename__ = 'tb_position_survey'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='职位id')
    feedback_time = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='反馈周期')
    related_description = db.Column(db.String(1024), nullable=False, server_default=db.FetchedValue(), info='相关介绍')
    priority_conditions = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='优先条件')
    welfare = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='福利')
    interview_process = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='面试流程')
    place = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue(), info='面试地点说明')
    supplement_info = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='补充信息')
    is_complete = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否完成')
    complete_time = db.Column(db.DateTime, info='完成时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    degree_is_required = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='学历要求是否必须')
    gender_is_required = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='性别要求是否必须')
    gender_is_private = db.Column(db.Integer, server_default=db.FetchedValue(), info='性别是否私密，0：否，1：是')
    work_exp_is_required = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='工作年限是否必须')
    language_is_required = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='语言要求是否必须')
    age_is_required = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='年龄要求是否必须')
    age_is_private = db.Column(db.Integer, server_default=db.FetchedValue(), info='年龄是否私密，0：否，1：是')
    certificate_is_required = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='证书要求是否必须')
    target_company = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='目标公司')
    target_position = db.Column(db.String(100), info='目标职能')
    company_advantage = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='公司优势')
    background_required = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='背景要求')
    exp_required = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='经验要求')
    hr_is_contact = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='hr是否愿意联系猎头')
    architect_info = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='架构介绍')
    hr_is_contact_desc = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='hr是否愿意联系猎头描述')
    reporting_object = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='汇报对象')
    team_size = db.Column(db.Integer, info='团队人数')
    age_start = db.Column(db.Integer, info='年龄最小')
    age_end = db.Column(db.Integer, info='年龄最大')
    work_exp_start = db.Column(db.Integer, info='工作经验最小')
    work_exp_end = db.Column(db.Integer, info='工作经验最大')
    special_work_exp_start = db.Column(db.Integer, info='特定工作经验最小')
    special_work_exp_end = db.Column(db.Integer, info='特定工作经验最大')
    hunteron_attention = db.Column(db.String(300), info='特定注意事项,仅供猎上网使用')
    hr_dislike = db.Column(db.String(255), server_default=db.FetchedValue(), info='HR不喜欢的')
    salary_supplement = db.Column(db.String(255), server_default=db.FetchedValue(), info='薪资补充说明')
    management_exp_req_start = db.Column(db.Integer, info='管理经验最小')
    management_exp_req_end = db.Column(db.Integer, info='管理经验最大')
    management_exp_desc = db.Column(db.String(1023), info='管理经验描述')
    college_req = db.Column(db.String(1000), info='学院要求')
    sub_content_type_req = db.Column(db.String(1000), info='内容类型')
    product_type_req = db.Column(db.String(1000), info='产品类型')
    operation_type_req = db.Column(db.String(1000), info='运营类型')
    special_experience_req = db.Column(db.String(1000), info='特定经验')
    is_urgent = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否紧急，0：否，1：是')
    marry_child_required = db.Column(db.Integer, server_default=db.FetchedValue(), info='婚育排除项：1.已婚已育，2.已婚未育，3.未婚已育，4.未婚未育')
    marry_child_is_private = db.Column(db.Integer, server_default=db.FetchedValue(), info='婚育排除项是否私密，0：否，1：是')
    open_reason_type = db.Column(db.Integer, info='开放原因')
    open_reason_info = db.Column(db.Text, info='开放原因说明')
    responsible_product_project_area = db.Column(db.Text, info='负责产品/项目/区域')
    leader_position_title = db.Column(db.String(200), info='上级岗位&背景')
    leader_position_title_desc = db.Column(db.Text, info='上级岗位&背景说明')
    department = db.Column(db.String(200), info='所属部门')
    team_size_type = db.Column(db.Integer, info='所属部门人数')
    function_type = db.Column(db.Integer, info='职能类型')
    onboard_day_num = db.Column(db.Integer, info='最快到岗天数')
    resume_feed_back_day_num = db.Column(db.Integer, index=True, info='简历反馈周期')
    interview_day_num = db.Column(db.Integer, index=True, info='面试周期')
    annual_salary_before_tax_min = db.Column(db.Integer, info='税前年薪（小）')
    annual_salary_before_tax_max = db.Column(db.Integer, info='税前年薪（大）')
    salary_rule_month = db.Column(db.Integer, info='基本薪资')
    salary_rule_constitute = db.Column(db.Text, info='薪资构成')
    social_security_benefits = db.Column(db.String(200), info='社保福利')
    housing_benefits = db.Column(db.String(200), info='住房福利')
    holiday_benefits = db.Column(db.String(200), info='假期福利')
    phone_traffic_benefits = db.Column(db.String(200), info='通讯交通')
    subordinates_num = db.Column(db.Integer, info='下属人数')
    other_required = db.Column(db.Text, info='（人选要求）其他项说明')
    private_other_required = db.Column(db.Text, info='（隐性要求）其他项说明')
    interview_address = db.Column(db.String(200), info='面试地点')
    work_address = db.Column(db.String(200), info='工作地点')
    interview_rotation_num = db.Column(db.Integer, info='面试轮次')
    interview_process_json = db.Column(db.Text, info='面试流程')
    if_other_place = db.Column(db.Integer, info='异地面试')
    if_other_place_reimbursement = db.Column(db.Integer, info='异地面试报销')
    reimbursement_process = db.Column(db.Text, info='报销流程')
    resume_template_attachment = db.Column(db.String(500), info='专用简历模板')
    company_introduction_attachment = db.Column(db.String(500), info='公司介绍')
    product_introduction_attachment = db.Column(db.String(500), info='产品介绍')
    skill_lang_exp_tool_req = db.Column(db.String(500), info='技术语言/产品/运营类型')
    field_direction_bg_req = db.Column(db.String(500), info='领域/方向/背景')
    field_direction_bg_weight = db.Column(db.Integer, server_default=db.FetchedValue(), info='领域/方向/背景 权重')
    skill_lang_exp_tool_weight = db.Column(db.Integer, server_default=db.FetchedValue(), info='技能/语言/经验/工具 权重')
    product_type_weight = db.Column(db.Integer, server_default=db.FetchedValue(), info='产品类型 权重')
    operation_type_weight = db.Column(db.Integer, server_default=db.FetchedValue(), info='运营类型 权重')
    function_type_description = db.Column(db.String(1000), info='职能类型描述')
    work_hours_am = db.Column(db.BigInteger, info='上班时间')
    work_hours_pm = db.Column(db.BigInteger, info='下班时间')
    punch_card = db.Column(db.Integer, info='是否打卡 0:不打卡 1:打卡')
    annual_salary_before_tax_description = db.Column(db.String(1000), info='税前年薪描述')
    interview_other_place_description = db.Column(db.String(255), info='异地面试补充说明')
    survey_rest = db.Column(db.Integer, info='休息情况')
    background_survey_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='背调')
    background_survey_description = db.Column(db.String(255), info='背调说明')



t_tb_position_survey_20190829 = db.Table(
    'tb_position_survey_20190829',
    db.Column('id', db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='主键ID'),
    db.Column('position_id', db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职位id'),
    db.Column('feedback_time', db.String(100), nullable=False, server_default=db.FetchedValue(), info='反馈周期'),
    db.Column('related_description', db.String(100), nullable=False, server_default=db.FetchedValue(), info='相关介绍'),
    db.Column('priority_conditions', db.String(100), nullable=False, server_default=db.FetchedValue(), info='优先条件'),
    db.Column('welfare', db.String(200), nullable=False, server_default=db.FetchedValue(), info='福利'),
    db.Column('interview_process', db.String(100), nullable=False, server_default=db.FetchedValue(), info='面试流程'),
    db.Column('place', db.String(255), nullable=False, server_default=db.FetchedValue(), info='面试地点说明'),
    db.Column('supplement_info', db.String(2000), nullable=False, server_default=db.FetchedValue(), info='补充信息'),
    db.Column('is_complete', db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否完成'),
    db.Column('complete_time', db.DateTime, info='完成时间'),
    db.Column('create_user_id', db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人'),
    db.Column('create_time', db.DateTime, nullable=False, info='创建时间'),
    db.Column('update_user_id', db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人'),
    db.Column('update_time', db.DateTime, nullable=False, info='修改时间'),
    db.Column('degree_is_required', db.Integer, nullable=False, server_default=db.FetchedValue(), info='学历要求是否必须'),
    db.Column('gender_is_required', db.Integer, nullable=False, server_default=db.FetchedValue(), info='性别要求是否必须'),
    db.Column('gender_is_private', db.Integer, server_default=db.FetchedValue(), info='性别是否私密，0：否，1：是'),
    db.Column('work_exp_is_required', db.Integer, nullable=False, server_default=db.FetchedValue(), info='工作年限是否必须'),
    db.Column('language_is_required', db.Integer, nullable=False, server_default=db.FetchedValue(), info='语言要求是否必须'),
    db.Column('age_is_required', db.Integer, nullable=False, server_default=db.FetchedValue(), info='年龄要求是否必须'),
    db.Column('age_is_private', db.Integer, server_default=db.FetchedValue(), info='年龄是否私密，0：否，1：是'),
    db.Column('certificate_is_required', db.Integer, nullable=False, server_default=db.FetchedValue(), info='证书要求是否必须'),
    db.Column('target_company', db.String(1000), nullable=False, server_default=db.FetchedValue(), info='目标公司'),
    db.Column('target_position', db.String(100), info='目标职能'),
    db.Column('company_advantage', db.String(500), nullable=False, server_default=db.FetchedValue(), info='公司优势'),
    db.Column('background_required', db.String(200), nullable=False, server_default=db.FetchedValue(), info='背景要求'),
    db.Column('exp_required', db.String(100), nullable=False, server_default=db.FetchedValue(), info='经验要求'),
    db.Column('hr_is_contact', db.Integer, nullable=False, server_default=db.FetchedValue(), info='hr是否愿意联系猎头'),
    db.Column('architect_info', db.String(2000), nullable=False, server_default=db.FetchedValue(), info='架构介绍'),
    db.Column('hr_is_contact_desc', db.String(100), nullable=False, server_default=db.FetchedValue(), info='hr是否愿意联系猎头描述'),
    db.Column('reporting_object', db.String(100), nullable=False, server_default=db.FetchedValue(), info='汇报对象'),
    db.Column('team_size', db.Integer, info='团队人数'),
    db.Column('age_start', db.Integer, info='年龄最小'),
    db.Column('age_end', db.Integer, info='年龄最大'),
    db.Column('work_exp_start', db.Integer, info='工作经验最小'),
    db.Column('work_exp_end', db.Integer, info='工作经验最大'),
    db.Column('special_work_exp_start', db.Integer, info='特定工作经验最小'),
    db.Column('special_work_exp_end', db.Integer, info='特定工作经验最大'),
    db.Column('hunteron_attention', db.String(300), info='特定注意事项,仅供猎上网使用'),
    db.Column('hr_dislike', db.String(255), server_default=db.FetchedValue(), info='HR不喜欢的'),
    db.Column('salary_supplement', db.String(255), server_default=db.FetchedValue(), info='薪资补充说明'),
    db.Column('management_exp_req_start', db.Integer, info='管理经验最小'),
    db.Column('management_exp_req_end', db.Integer, info='管理经验最大'),
    db.Column('management_exp_desc', db.String(300), info='管理经验描述'),
    db.Column('college_req', db.String(1000), info='学院要求'),
    db.Column('sub_content_type_req', db.String(1000), info='内容类型'),
    db.Column('product_type_req', db.String(1000), info='产品类型'),
    db.Column('operation_type_req', db.String(1000), info='运营类型'),
    db.Column('special_experience_req', db.String(1000), info='特定经验'),
    db.Column('is_urgent', db.Integer, server_default=db.FetchedValue(), info='是否紧急，0：否，1：是'),
    db.Column('marry_child_required', db.Integer, server_default=db.FetchedValue(), info='婚育排除项：1.已婚已育，2.已婚未育，3.未婚已育，4.未婚未育'),
    db.Column('marry_child_is_private', db.Integer, server_default=db.FetchedValue(), info='婚育排除项是否私密，0：否，1：是'),
    db.Column('open_reason_type', db.Integer, info='开放原因'),
    db.Column('open_reason_info', db.Text, info='开放原因说明'),
    db.Column('responsible_product_project_area', db.Text, info='负责产品/项目/区域'),
    db.Column('leader_position_title', db.String(200), info='上级岗位&背景'),
    db.Column('leader_position_title_desc', db.Text, info='上级岗位&背景说明'),
    db.Column('department', db.String(200), info='所属部门'),
    db.Column('team_size_type', db.Integer, info='所属部门人数'),
    db.Column('function_type', db.Integer, info='职能类型'),
    db.Column('onboard_day_num', db.Integer, info='最快到岗天数'),
    db.Column('resume_feed_back_day_num', db.Integer, info='简历反馈周期'),
    db.Column('interview_day_num', db.Integer, info='面试周期'),
    db.Column('annual_salary_before_tax_min', db.Integer, info='税前年薪（小）'),
    db.Column('annual_salary_before_tax_max', db.Integer, info='税前年薪（大）'),
    db.Column('salary_rule_month', db.Integer, info='基本薪资'),
    db.Column('salary_rule_constitute', db.Text, info='薪资构成'),
    db.Column('social_security_benefits', db.String(200), info='社保福利'),
    db.Column('housing_benefits', db.String(200), info='住房福利'),
    db.Column('holiday_benefits', db.String(200), info='假期福利'),
    db.Column('phone_traffic_benefits', db.String(200), info='通讯交通'),
    db.Column('subordinates_num', db.Integer, info='下属人数'),
    db.Column('other_required', db.Text, info='（人选要求）其他项说明'),
    db.Column('private_other_required', db.Text, info='（隐性要求）其他项说明'),
    db.Column('interview_address', db.String(200), info='面试地点'),
    db.Column('work_address', db.String(200), info='工作地点'),
    db.Column('interview_rotation_num', db.Integer, info='面试轮次'),
    db.Column('interview_process_json', db.Text, info='面试流程'),
    db.Column('if_other_place', db.Integer, info='异地面试'),
    db.Column('if_other_place_reimbursement', db.Integer, info='异地面试报销'),
    db.Column('reimbursement_process', db.Text, info='报销流程'),
    db.Column('resume_template_attachment', db.String(500), info='专用简历模板'),
    db.Column('company_introduction_attachment', db.String(500), info='公司介绍'),
    db.Column('product_introduction_attachment', db.String(500), info='产品介绍'),
    db.Column('skill_lang_exp_tool_req', db.String(500), info='技术语言/产品/运营类型'),
    db.Column('field_direction_bg_req', db.String(500), info='领域/方向/背景'),
    db.Column('field_direction_bg_weight', db.Integer, server_default=db.FetchedValue(), info='领域/方向/背景 权重'),
    db.Column('skill_lang_exp_tool_weight', db.Integer, server_default=db.FetchedValue(), info='技能/语言/经验/工具 权重'),
    db.Column('product_type_weight', db.Integer, server_default=db.FetchedValue(), info='产品类型 权重'),
    db.Column('operation_type_weight', db.Integer, server_default=db.FetchedValue(), info='运营类型 权重')
)



class TbPositionSurveyAudit(db.Model):
    __tablename__ = 'tb_position_survey_audit'

    id = db.Column(db.BigInteger, primary_key=True)
    position_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='职位id')
    audit_type = db.Column(db.Integer, info='审核结果：1：通过，0：不通过')
    remark = db.Column(db.String(1000), info='备注')
    investigation_time = db.Column(db.DateTime, info='职位调研时间')
    position_snapshot = db.Column(db.String(5000))
    position_survey_snapshot = db.Column(db.String(5000))
    position_survey_extra_option_snapshot = db.Column(db.String(5000))
    position_survey_extra_object_snapshot = db.Column(db.String(5000))
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime)
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='删除标识 0  否 1 是')



class TbPositionSurveyExtraObject(db.Model):
    __tablename__ = 'tb_position_survey_extra_object'

    id = db.Column(db.BigInteger, primary_key=True)
    position_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='职位id')
    object_required = db.Column(db.String(1000), info='参考项值')
    object_required_weight = db.Column(db.Integer, server_default=db.FetchedValue(), info='参考项_权重1/2/3/4 对应必须、重要、优先、必须满足其一')
    object_name = db.Column(db.String(1000), info='参考项名称')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime)



class TbPositionSurveyExtraOption(db.Model):
    __tablename__ = 'tb_position_survey_extra_option'

    id = db.Column(db.BigInteger, primary_key=True)
    position_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='职位id')
    college_required = db.Column(db.String(1000), info='毕业院校')
    college_required_weight = db.Column(db.Integer, server_default=db.FetchedValue(), info='毕业院校_权重')
    degree_required = db.Column(db.Integer, server_default=db.FetchedValue(), info='学历要求 0:不限 1：大专及以上 2：本科及以上 3：硕士及以上 4：博士及以上')
    degree_required_weight = db.Column(db.Integer, server_default=db.FetchedValue(), info='学历要求_权重')
    gender_required = db.Column(db.Integer, server_default=db.FetchedValue(), info='性别要求 0：不限  1：男  2：女')
    gender_required_weight = db.Column(db.Integer, server_default=db.FetchedValue(), info='性别要求_权重')
    target_company = db.Column(db.String(1000), server_default=db.FetchedValue(), info='目标公司')
    target_company_weight = db.Column(db.Integer, server_default=db.FetchedValue(), info='目标公司_权重')
    age_start = db.Column(db.Integer, info='年龄最小')
    age_end = db.Column(db.Integer, info='年龄最大')
    age_required_weight = db.Column(db.Integer, server_default=db.FetchedValue(), info='年龄_权重')
    work_exp_start = db.Column(db.Integer, info='工作总年限最小')
    work_exp_end = db.Column(db.Integer, info='工作总年限最大')
    work_exp_weight = db.Column(db.Integer, server_default=db.FetchedValue(), info='工作总年限_权重')
    special_experience_req = db.Column(db.String(1000), info='特定经验')
    special_experience_weight = db.Column(db.Integer, server_default=db.FetchedValue(), info='特定经验_权重')
    special_work_exp_start = db.Column(db.Integer, info='特定工作经验最小')
    special_work_exp_end = db.Column(db.Integer, info='特定工作经验最大')
    special_work_exp_weight = db.Column(db.Integer, server_default=db.FetchedValue(), info='特定工作经验_权重')
    skill_lang_exp_tool_req = db.Column(db.String(1000), info='技能/语言/经验/工具')
    skill_lang_exp_tool_weight = db.Column(db.Integer, server_default=db.FetchedValue(), info='技能/语言/经验/工具_权重')
    field_direction_bg_req = db.Column(db.String(1000), info='领域/方向/背景')
    field_direction_bg_weight = db.Column(db.Integer, server_default=db.FetchedValue(), info='领域/方向/背景_权重')
    product_type_req = db.Column(db.String(1000), info='产品类型')
    product_type_weight = db.Column(db.Integer, server_default=db.FetchedValue(), info='产品类型_权重')
    operation_type_req = db.Column(db.String(1000), info='运营类型')
    operation_type_weight = db.Column(db.Integer, server_default=db.FetchedValue(), info='运营类型_权重')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime)



class TbPositionSurveyFeedback(db.Model):
    __tablename__ = 'tb_position_survey_feedback'

    id = db.Column(db.BigInteger, primary_key=True, info='自增主键')
    position_id = db.Column(db.BigInteger, nullable=False)
    user_id = db.Column(db.BigInteger, nullable=False, info='反馈用户')
    user_type = db.Column(db.Integer, nullable=False, info='反馈用户类型')
    type = db.Column(db.Integer, nullable=False, info='反馈类型 1 赞 2踩')
    content = db.Column(db.String(500), info='反馈内容')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='删除标识 0  否 1 是')



class TbPositionSurveyPloy(db.Model):
    __tablename__ = 'tb_position_survey_ploy'

    id = db.Column(db.BigInteger, primary_key=True)
    position_survey_id = db.Column(db.BigInteger, nullable=False, index=True)
    position_id = db.Column(db.BigInteger, nullable=False, index=True)
    property_key = db.Column(db.String(200), nullable=False, info='属性KEY')
    property_value = db.Column(db.String(200), info='属性值')
    property_value_min = db.Column(db.Float(20, True), info='属性最小值')
    property_value_max = db.Column(db.Float(20, True), info='属性最大值')
    property_weight = db.Column(db.Integer, nullable=False, info='属性权重 0 不限 1 必须 2优先')
    if_inner_display = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否只有内部可见')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    temp_defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class TbPositionTag(db.Model):
    __tablename__ = 'tb_position_tag'
    __table_args__ = (
        db.Index('uidx_positionid_tagid_createuserid', 'position_id', 'tag_content', 'create_user_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue())
    tag_content = db.Column(db.String(30), nullable=False, index=True, server_default=db.FetchedValue())
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除0false1true')
    create_user_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')



class TbPositionTagDic(db.Model):
    __tablename__ = 'tb_position_tag_dic'

    id = db.Column(db.BigInteger, primary_key=True, info='主键，系统生成')
    tag_rule_key = db.Column(db.String(63), nullable=False, index=True, server_default=db.FetchedValue(), info='标签code，不可重复；主要用于系统预定义标签与规则代码对应；人工标签则没什么意义')
    inner_name = db.Column(db.String(31), nullable=False, info='标签的内部显示名称；可重复')
    hh_display_name = db.Column(db.String(31), info='标签的HH端显示名称，可重复，展示前去重复')
    tdc_display_name = db.Column(db.String(31), info='TDC端显示名称')
    show_message = db.Column(db.String(255), info='弹窗提示文案')
    tag_type = db.Column(db.Integer, info='标签类型；1 系统标签：预定义，不可选择；2 人工标签：人工打标签使用；')
    pay_rate = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='分成比例')
    start_time = db.Column(db.DateTime, info='标签有效时间的开始时间，可以为空，表示立即生效；')
    end_time = db.Column(db.DateTime, info='标签有效时间的结束时间，可以为空，表示不限时；')
    priority = db.Column(db.Integer, server_default=db.FetchedValue(), info='标签优先级，也就是排序值，越大越靠前')
    is_mutex = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否互斥；互斥的标签，只展示优先级最高的；职位中有一个是互斥标签，则不展示其它标签')
    is_filter = db.Column(db.Integer, server_default=db.FetchedValue(), info='所有标签在职位搜索都可以搜索；这个标记为是否展示给HH用户')
    is_hh_display = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否在HH端职位上展示这个标签')
    is_tdc_dispaly = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否在TDC端职位上展示这个标签')
    tag_style = db.Column(db.String(31), info='标签样式class')
    tag_rule_json = db.Column(db.String(1023), info='标签规则json')
    mutex_calculate_tags = db.Column(db.String(255), info='互斥可计算标签，为空则互斥所有')
    calculate_type = db.Column(db.Integer, info='标签计算类型：1：按天；2：实时')
    defunct = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='逻辑删除')
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_user_id = db.Column(db.BigInteger)



class TbPositionTagRelation(db.Model):
    __tablename__ = 'tb_position_tag_relation'
    __table_args__ = (
        db.Index('position_id_tag_id', 'position_id', 'tag_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    position_id = db.Column(db.BigInteger, info='职位ID')
    tag_id = db.Column(db.BigInteger, info='关联的标签主键')
    calculate_type = db.Column(db.Integer, info='从tb_position_tag_dic表冗余过来')
    start_time = db.Column(db.DateTime, info='具体在职位上的有效时间开始')
    end_time = db.Column(db.DateTime, info='标签在职位上的有效时间的结束时间')
    defunct = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='逻辑删除；1 已删除')
    show_message = db.Column(db.String(255), info='标签文案，部分职位的文案跟职位信息相关')
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_user_id = db.Column(db.BigInteger)
    tag_type = db.Column(db.Integer, index=True, info='从标签表冗余过来的字段')



class TbPositionTagRelationCopy(db.Model):
    __tablename__ = 'tb_position_tag_relation_copy'
    __table_args__ = (
        db.Index('position_id_tag_id', 'position_id', 'tag_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    position_id = db.Column(db.BigInteger, info='职位ID')
    tag_id = db.Column(db.BigInteger, info='关联的标签主键')
    calculate_type = db.Column(db.Integer, info='从tb_position_tag_dic表冗余过来')
    start_time = db.Column(db.DateTime, info='具体在职位上的有效时间开始')
    end_time = db.Column(db.DateTime, info='标签在职位上的有效时间的结束时间')
    defunct = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='逻辑删除；1 已删除')
    show_message = db.Column(db.String(255), info='标签文案，部分职位的文案跟职位信息相关')
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_user_id = db.Column(db.BigInteger)
    tag_type = db.Column(db.Integer, index=True, info='从标签表冗余过来的字段')



class TbPositionTalentAlternativeRelation(db.Model):
    __tablename__ = 'tb_position_talent_alternative_relation'
    __table_args__ = (
        db.Index('idx_talentid_defunct_positionid', 'talent_id', 'defunct', 'position_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    headhunter_id = db.Column(db.BigInteger, nullable=False, info='猎头id')
    company_id = db.Column(db.BigInteger, nullable=False, index=True, info='猎头公司id')
    talent_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='人才id')
    outer_talent_id = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='外部人才id')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, info='职位id')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='备选名单状态1：初选2：有意向3：待推荐4：已推荐5：移除')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除 -> 1 : true 已删除；0 : false 有效')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    project_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='项目编号')
    source_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='来源类型；0：手动添加；1：机器匹配派单')



class TbPositionTalentPair(db.Model):
    __tablename__ = 'tb_position_talent_pair'

    id = db.Column(db.BigInteger, primary_key=True)
    headhunter_id = db.Column(db.BigInteger, nullable=False)
    position_id = db.Column(db.BigInteger, nullable=False)
    talent_id = db.Column(db.BigInteger, nullable=False)
    type = db.Column(db.Integer, nullable=False, info='配对类型，1：longlist, 2:shortlist')
    create_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class TbPositionTitle(db.Model):
    __tablename__ = 'tb_position_title'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    name = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='名称')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='类型；0:标题；1:职位')
    parent_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='父id')
    order_by = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序')
    industry_id = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='行业id')
    hot = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='标记 0：原有，1：新增')
    hd_sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='hd端排序，为0不显示')
    hr_sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='hr端排序，为0不显示')
    c_sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='c端排序，为0不显示')
    group_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='技能id')



class TbPositionTitle2Bak(db.Model):
    __tablename__ = 'tb_position_title2-bak'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    name = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='名称')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='类型；0:标题；1:职位')
    parent_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='父id')
    order_by = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序')
    industry_id = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='行业id')
    hot = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='标记 0：原有，1：新增')
    hd_sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='hd端排序，为0不显示')
    hr_sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='hr端排序，为0不显示')
    c_sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='c端排序，为0不显示')
    group_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='技能id')



class TbPositionTitleTag(db.Model):
    __tablename__ = 'tb_position_title_tag'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='名称')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='类型；0:标题；1:职位')
    parent_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='父id')
    order_by = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序')
    industry_id = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='行业id')
    hot = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='标记 0：原有，1：新增')
    hd_sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='hd端排序，为0不显示')
    hr_sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='hr端排序，为0不显示')
    c_sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='c端排序，为0不显示')
    group_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='技能id')



class TbPositionTitleTag2Bak(db.Model):
    __tablename__ = 'tb_position_title_tag2-bak'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='名称')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='类型；0:标题；1:职位')
    parent_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='父id')
    order_by = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='排序')
    industry_id = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='行业id')
    hot = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='标记 0：原有，1：新增')
    hd_sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='hd端排序，为0不显示')
    hr_sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='hr端排序，为0不显示')
    c_sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='c端排序，为0不显示')
    group_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='技能id')



class TbPositionUrgentRule(db.Model):
    __tablename__ = 'tb_position_urgent_rule'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    rule_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='个人职位1：公司职位2')
    revoke_times = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='被撤销次数')
    revoke_days = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='被撤销的接下来多少天内')
    tf_urgent = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否可以发送24小时紧急职位')
    fe_urgent = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否可以发送48小时紧急职位')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除 0:未删除 1:已删除')
    priority = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='优先级排序')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')



class TbPositionValid(db.Model):
    __tablename__ = 'tb_position_valid'

    id = db.Column(db.BigInteger, primary_key=True, info='主键id')
    industry_ids = db.Column(db.String(255), nullable=False)
    function_ids = db.Column(db.String(255), nullable=False)
    city_ids = db.Column(db.String(255), info='城市ids')
    yearly_salary_mix = db.Column(db.Float(20, True), info='年薪区间（小）')
    yearly_salary_max = db.Column(db.Float(20, True), info='年薪区间（大）')
    commission = db.Column(db.Float(20, True), info='佣金')
    po_id = db.Column(db.Integer, info='创建者（PO）')
    create_user_id = db.Column(db.Integer, info='更新者')
    create_time = db.Column(db.DateTime, info='创建时间')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='删除标识')



class TbPositionValueBase(db.Model):
    __tablename__ = 'tb_position_value_base'

    level_code = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue(), info='级别CODE')
    base_value = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='基础积分')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbPositionValueConfig(db.Model):
    __tablename__ = 'tb_position_value_config'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    level_code = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='级别CODE')
    value_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1:职能;2:佣金比例;3:年薪;4:保证期')
    rank = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='级别类型')
    conditions = db.Column(db.String(200), info='条件')
    value = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue(), info='获取积分')
    description = db.Column(db.String(200), info='描述')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbPositionWeightConfig(db.Model):
    __tablename__ = 'tb_position_weight_config'

    id = db.Column(db.BigInteger, primary_key=True, info='主键自增')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, info='职位编号')
    work_exp = db.Column(db.Integer, server_default=db.FetchedValue(), info='工作年限_权重')
    special_work_exp = db.Column(db.Integer, server_default=db.FetchedValue(), info='特殊工作年限_权重')
    management_exp = db.Column(db.Integer, server_default=db.FetchedValue(), info='管理经验描述_权重')
    team_size = db.Column(db.Integer, server_default=db.FetchedValue(), info='团队人数_权重')
    management_exp_req = db.Column(db.Integer, server_default=db.FetchedValue(), info='管理经验年限_权重')
    degree_req = db.Column(db.Integer, server_default=db.FetchedValue(), info='学历_权重')
    colleage_req = db.Column(db.Integer, server_default=db.FetchedValue(), info='学院权重')
    content_type_req = db.Column(db.Integer, server_default=db.FetchedValue(), info='内容类型权重')
    language_req = db.Column(db.Integer, server_default=db.FetchedValue(), info='语言_权重')
    skill_lang_exp_tool = db.Column(db.Integer, server_default=db.FetchedValue(), info='技能语言经验工具_权重')
    field_direction_bg = db.Column(db.Integer, server_default=db.FetchedValue(), info='领域方向背景_权重')
    target_company = db.Column(db.Integer, server_default=db.FetchedValue(), info='目标企业_权重')
    target_position = db.Column(db.Integer, server_default=db.FetchedValue(), info='目标职能_权重')
    age_req = db.Column(db.Integer, server_default=db.FetchedValue(), info='年龄_权重')
    gender_req = db.Column(db.Integer, server_default=db.FetchedValue(), info='性别_权重')
    product_type_exp = db.Column(db.Integer, server_default=db.FetchedValue(), info='产品类型_权重')
    operation_type_exp = db.Column(db.Integer, server_default=db.FetchedValue(), info='运营类型_权重')
    special_experience_exp = db.Column(db.Integer, server_default=db.FetchedValue(), info='特定经验_权重')



class TbPrepayConf(db.Model):
    __tablename__ = 'tb_prepay_conf'

    id = db.Column(db.BigInteger, primary_key=True, info='pk')
    level_code = db.Column(db.Integer, nullable=False)
    credit_code = db.Column(db.Integer, nullable=False, info='等级')
    pre_pay_rate = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='预付比例')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, info='创建者')
    update_time = db.Column(db.DateTime, info='更新时间')
    update_user_id = db.Column(db.BigInteger, info='更新者')



class TbPrivacy(db.Model):
    __tablename__ = 'tb_privacy'

    user_id = db.Column(db.BigInteger, primary_key=True)
    real_name_hide = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    email_hide = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    office_phone_hide = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mobile_phone_hide = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbPrivacyNumberBind(db.Model):
    __tablename__ = 'tb_privacy_number_bind'

    id = db.Column(db.BigInteger, primary_key=True, info='唯一编号')
    a_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='A用户id')
    a_phone = db.Column(db.String(50), info='A号码')
    b_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='B用户id')
    b_phone = db.Column(db.String(50), info='B号码')
    expire_time = db.Column(db.DateTime, info='失效时间')
    secret_no = db.Column(db.String(50), info='隐私号码')
    extension_no = db.Column(db.String(50), info='绑定关系id')
    subs_id = db.Column(db.String(50), info='分机号码')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbProfile(db.Model):
    __tablename__ = 'tb_profile'

    user_id = db.Column(db.BigInteger, primary_key=True, info='用户ID')
    real_name = db.Column(db.String(200), nullable=False, info='真实姓名')
    first_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    last_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    user_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1 : hr; 2 : hh; 3: admin; 4: agent')
    display_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='显示名称')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否无效 -> 1 : true 已删除；0 : false 有效')
    birthday = db.Column(db.DateTime, info='生日')
    gender = db.Column(db.Integer, info='0.女 1.男')
    title = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='岗位名称')
    mobile_phone = db.Column(db.String(200), nullable=False, index=True, server_default=db.FetchedValue(), info='手机号')
    account = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='账号')
    email = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='邮箱')
    avatar = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue())
    province_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='省ID')
    city_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='城市ID')
    address = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='地址')
    office_phone = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='办公电话')
    qq = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='qq')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, index=True, info='修改时间')
    login_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='登录名')
    experience = db.Column(db.Integer, info='工作年限')
    subscription_email = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='订阅设置中可以设置的邮箱地址，注册时使用注册邮箱')
    subscription_mobile_phone = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='订阅设置时')
    industry = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='所属行业')
    industry_func = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='所属行业只能')
    birthday_cnt = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='出生日期原文YYYY.MM')
    title_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1.我是hr;2:我是用人部门负责人;3:我是老板;4:其他')
    start_contact_time = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='沟通开始时间')
    end_contact_time = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='沟通结束时间')
    customer_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='客户类型：0:普通，1:代操作')



t_tb_profile_bak2016 = db.Table(
    'tb_profile_bak2016',
    db.Column('user_id', db.BigInteger),
    db.Column('real_name', db.String(600)),
    db.Column('first_name', db.String(600)),
    db.Column('last_name', db.String(600)),
    db.Column('user_type', db.Integer),
    db.Column('display_name', db.String(600)),
    db.Column('defunct', db.Integer),
    db.Column('birthday', db.DateTime),
    db.Column('gender', db.Integer),
    db.Column('title', db.String(600)),
    db.Column('mobile_phone', db.String(600)),
    db.Column('email', db.String(600)),
    db.Column('avatar', db.String(1500)),
    db.Column('province_id', db.BigInteger),
    db.Column('city_id', db.BigInteger),
    db.Column('address', db.String(1500)),
    db.Column('office_phone', db.String(600)),
    db.Column('qq', db.String(300)),
    db.Column('create_user_id', db.BigInteger),
    db.Column('update_user_id', db.BigInteger),
    db.Column('create_time', db.DateTime),
    db.Column('update_time', db.DateTime),
    db.Column('login_name', db.String(600)),
    db.Column('experience', db.Integer),
    db.Column('subscription_email', db.String(600)),
    db.Column('subscription_mobile_phone', db.String(600))
)



class TbProfileBak20160126(db.Model):
    __tablename__ = 'tb_profile_bak20160126'

    user_id = db.Column(db.BigInteger, primary_key=True)
    real_name = db.Column(db.String(200), nullable=False)
    first_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    last_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    user_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1 : hr; 2 : hh; 3: admin; 4: agent')
    display_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否无效 -> 1 : true 已删除；0 : false 有效')
    birthday = db.Column(db.DateTime)
    gender = db.Column(db.Integer, info='0.女 1.男')
    title = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    mobile_phone = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    email = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    avatar = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue())
    province_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    city_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    address = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue())
    office_phone = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    qq = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False, index=True)
    login_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    experience = db.Column(db.Integer)
    subscription_email = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='订阅设置中可以设置的邮箱地址，注册时使用注册邮箱')
    subscription_mobile_phone = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='订阅设置时')



class TbProjectBlackList(db.Model):
    __tablename__ = 'tb_project_black_list'

    id = db.Column(db.BigInteger, primary_key=True)
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='类型：0:整个项目;1:项目个人')
    project_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='项目编号')
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='用户编号')
    remark = db.Column(db.String(100), server_default=db.FetchedValue(), info='备注')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbPullulateConfig(db.Model):
    __tablename__ = 'tb_pullulate_config'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='hd or hr')
    operate_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='操作类型:面试确认、offer等')
    min_annual = db.Column(db.Integer, info='最小年薪')
    max_annual = db.Column(db.Integer, info='最大年薪')
    recommand_quality = db.Column(db.Float(asdecimal=True), info='推荐质量')
    fetch_count = db.Column(db.Integer, info='获取次数')
    online_day = db.Column(db.Integer, info='连续在线天数')
    reply_time = db.Column(db.Integer, info='回复时间')
    min_work_year = db.Column(db.Integer, info='最小工作年限')
    max_work_year = db.Column(db.Integer, info='最大工作年限')
    ratio = db.Column(db.Float(asdecimal=True), info='比例')
    modify_time = db.Column(db.Integer, info='更新时间')
    max_modify_time = db.Column(db.Integer, info='最大更新时间')
    pullulate_value = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='贡献值')
    remark = db.Column(db.String(100), info='备注')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbReceiptsDetail(db.Model):
    __tablename__ = 'tb_receipts_detail'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    placement_id = db.Column(db.BigInteger, nullable=False, index=True, info='placement成单表ID ')
    receipts_id = db.Column(db.BigInteger, nullable=False, index=True, info='对应收款单ID')
    detail_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='明细类型：收款，退款')
    amount = db.Column(db.Float(12, True), nullable=False, server_default=db.FetchedValue(), info='金额')
    tax_amount = db.Column(db.Float(15, True), server_default=db.FetchedValue(), info='收款金额对应的税额')
    amount_date = db.Column(db.DateTime, index=True, info='金额日期')
    amount_channel = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='收款或退款途径,1:线下,2:通过总账')
    comment = db.Column(db.String(1000), server_default=db.FetchedValue(), info='收款或退款备注')
    attach = db.Column(db.String(255), info='付款时的附件文件')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue(), info='更新时间')



class TbRecommandFailed(db.Model):
    __tablename__ = 'tb_recommand_failed'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    talent_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='人才id')
    enterprise_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='企业id')
    position_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职位id')
    talent_name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='人才名称')
    email = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='人才邮件地址')
    cell_phone = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='人才手机号码')
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='用户id')
    create_time = db.Column(db.DateTime, info='创建时间')



class TbRecommendSpecial(db.Model):
    __tablename__ = 'tb_recommend_special'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    enterprise_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='企业id')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建者')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='更新者')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='逻辑删除 0：未删除，1：已删除')



class TbRecommendSuitableTalentLog(db.Model):
    __tablename__ = 'tb_recommend_suitable_talent_log'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    headhunter_id = db.Column(db.BigInteger, nullable=False, info='猎头id')
    position_id = db.Column(db.BigInteger, nullable=False, info='职位id')
    suitable_talent_ids = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='匹配的人才ids')
    screen_out_talent_ids = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='筛选后的人才ids')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbRecommendVip(db.Model):
    __tablename__ = 'tb_recommend_vip'

    id = db.Column(db.BigInteger, primary_key=True)
    enterprise_list = db.Column(db.String(500), info='特殊公司处理（判断到职位），企业id“,”分割')
    enterprise_id = db.Column(db.BigInteger, nullable=False, info='公司id')



class TbRecruitSpecial(db.Model):
    __tablename__ = 'tb_recruit_special'
    __table_args__ = (
        db.Index('idx_start_end_time', 'start_time', 'end_time'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='名称')
    logo_path = db.Column(db.String(200))
    page_link = db.Column(db.String(200), info='专场链接')
    description = db.Column(db.Text)
    is_top = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否置顶')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除0false 1true')
    service_admin = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='服务人员')
    start_time = db.Column(db.DateTime, nullable=False, info='开始时间')
    end_time = db.Column(db.DateTime, nullable=False, info='结束时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    recruit_special_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0：web端；1：手机端；2：所有(all)')
    mobile_logo_path = db.Column(db.String(200), info='手机端logo路径')
    open_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开放类型 0：所有；1：Soho；2：company')
    big_pc_logo_path = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='PC背景大图片')
    recruit_special_kind = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='专场类型：0无意义，1公司专场，2职位专场，3特殊专场')
    is_recommend = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否推荐到主页')
    big_pc_background_color = db.Column(db.String(50), info='PC背景颜色')
    platform_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='展示的平台类型，1：HR，2：HH，3：C，4：all; 因原始是HH在用，故默认2')
    expire_day_num = db.Column(db.Integer, server_default=db.FetchedValue(), info='过期天数')



class TbRedRackesOrder(db.Model):
    __tablename__ = 'tb_red_rackes_order'

    id = db.Column(db.BigInteger, primary_key=True)
    activity_lottery_id = db.Column(db.BigInteger, nullable=False, index=True, info='抽奖活动ID')
    position_id = db.Column(db.BigInteger, index=True, info='职位ID')
    candidate_id = db.Column(db.BigInteger, index=True, info='订单ID')
    headhunter_id = db.Column(db.BigInteger, index=True, info='猎头ID')
    company_id = db.Column(db.BigInteger, index=True, info='猎企ID')
    enterprise_id = db.Column(db.BigInteger, info='雇主ID')
    candidate_name = db.Column(db.String(128), info='候选人')
    position_title = db.Column(db.String(600), info='职位title')
    red_rackes_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='红包类型 0 逾期 1 现金')
    status = db.Column(db.Integer, server_default=db.FetchedValue(), info='提现状态  -2:新建 -1:逾期中, 0:未提现  1:提现中  2:已经提现')
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_user_id = db.Column(db.BigInteger)



class TbRegisterWaitHandle(db.Model):
    __tablename__ = 'tb_register_wait_handle'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    email = db.Column(db.String(100), nullable=False, info='注册人邮箱的邮箱')
    phone = db.Column(db.String(30), nullable=False, server_default=db.FetchedValue(), info='注册人的号码(手机号或座机号)')
    register_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='注册类型:1:hr注册,2:猎头注册')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')



class TbRegistrationSource(db.Model):
    __tablename__ = 'tb_registration_source'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='用户编号')
    user_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1 : hr; 2 : hh; 3: admin; 4: agent')
    client_type = db.Column(db.Integer, info='客户端类型；1：PC；2：APP；3：CRM；4：H5')
    user_name = db.Column(db.String(50), info='用户名')
    mobile_phone = db.Column(db.String(50), info='联系电话')
    referer = db.Column(db.String(1023), info='链接来源')
    invite_code = db.Column(db.String(50), info='邀请码')
    ip = db.Column(db.String(50), info='IP地址')
    location = db.Column(db.String(50), info='地址')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbRejectReasonOption(db.Model):
    __tablename__ = 'tb_reject_reason_option'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='类型, 1:猎头, 2:猎企')
    content = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='拒绝理由内容')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除,0:false,1:true')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbRemindHrConfiger(db.Model):
    __tablename__ = 'tb_remind_hr_configer'
    __table_args__ = (
        db.Index('remindKey_defunct', 'remind_key', 'user_id', 'user_type', 'defunct'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    remind_key = db.Column(db.String(63), nullable=False, index=True)
    user_id = db.Column(db.BigInteger)
    user_type = db.Column(db.Integer)
    defunct = db.Column(db.Integer)
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_user_id = db.Column(db.BigInteger)



class TbRemindHrDatum(db.Model):
    __tablename__ = 'tb_remind_hr_data'
    __table_args__ = (
        db.Index('remind_key_user', 'hr_id', 'remind_key'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    hr_id = db.Column(db.BigInteger, nullable=False)
    remind_key = db.Column(db.String(63), nullable=False)
    remind_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    remind_date = db.Column(db.BigInteger)
    create_date = db.Column(db.DateTime)



class TbRemindManager(db.Model):
    __tablename__ = 'tb_remind_manager'

    id = db.Column(db.BigInteger, primary_key=True)
    service_key = db.Column(db.String(63), info='服务key')
    menu_key = db.Column(db.String(31), info='菜单key')
    remind_key = db.Column(db.String(63), nullable=False, index=True)
    remind_name = db.Column(db.String(63), nullable=False, info='提醒信息名称')
    remind_info = db.Column(db.String(255), info='功能描述')
    app_type = db.Column(db.Integer, nullable=False, info='客户端类型；0：hr；1：hh；2：c；3：crm；4：猎大')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue())
    update_time = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)



class TbResumeMatchPosition(db.Model):
    __tablename__ = 'tb_resume_match_position'
    __table_args__ = (
        db.Index('idx_userid_positionid_positionclienttype', 'user_id', 'position_id', 'position_client_type'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, index=True, info='猎头ID')
    talent_id = db.Column(db.BigInteger, index=True, info='hdTalent表主键')
    position_id = db.Column(db.BigInteger, index=True, info='职位ID')
    match_score = db.Column(db.Float(asdecimal=True), info='匹配得分')
    recommend_reason = db.Column(db.Text, info='推荐原因')
    position_analysis_match = db.Column(db.Text, info='职位解析')
    resume_analysis_match = db.Column(db.Text, info='简历解析')
    is_read = db.Column(db.Integer, info='是否已读')
    is_ignore = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否忽略:0未忽略；1忽略')
    ignore_reason_status = db.Column(db.Integer, info='忽略原因状态字段')
    ignore_reason_desc = db.Column(db.String(255), info='忽略原因描述字段')
    create_time = db.Column(db.DateTime, index=True, info='记录创建时间')
    match_info = db.Column(db.Text, info='匹配明细信息')
    position_client_type = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='发布职位的客户端类型；1：旧版本hr，包括saas版本；2：新版本OnWork')



class TbResumePositionIntent(db.Model):
    __tablename__ = 'tb_resume_position_intent'
    __table_args__ = (
        db.Index('pid_type', 'position_id', 'sell_type', 'defunct'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    position_id = db.Column(db.BigInteger, nullable=False, info='简历职位ID')
    intent_dic_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='意向字典表主键')
    sell_type = db.Column(db.Integer, nullable=False, info='简历职位对应的面向简历类型；1：激活简历；2：意向简历；3：到面简历')
    intent_title = db.Column(db.String(255), info='简历职位自定义的意向问题；如果是自定义，则intent_dic_id是0')
    defunct = db.Column(db.Integer)
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)



class TbResumePositionIntentDic(db.Model):
    __tablename__ = 'tb_resume_position_intent_dic'

    id = db.Column(db.BigInteger, primary_key=True)
    title = db.Column(db.String(255), nullable=False, info='意向内容')
    info = db.Column(db.String(1023), nullable=False, info='意向描述')
    defunct = db.Column(db.Integer)
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)



class TbResumePositionIntentDicExplan(db.Model):
    __tablename__ = 'tb_resume_position_intent_dic_explan'
    __table_args__ = (
        db.Index('intentdicId', 'intent_dic_id', 'defunct'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    intent_dic_id = db.Column(db.BigInteger, nullable=False, info='字典表主键；因为一个字典可以对应n个扩展')
    title = db.Column(db.String(255))
    info = db.Column(db.String(255))
    value_json = db.Column(db.String(2047))
    type = db.Column(db.Integer, info='类型；1：选择；2：单选；3：复选；4：键值文本；5：日期')
    defunct = db.Column(db.Integer)
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)



class TbResumePositionPloy(db.Model):
    __tablename__ = 'tb_resume_position_ploy'

    id = db.Column(db.BigInteger, primary_key=True)
    position_id = db.Column(db.BigInteger, nullable=False, index=True, info='职位表主键；必须是简历职位')
    is_for_active = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否面向激活简历')
    is_for_intent = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否面向意向简历')
    is_for_interview = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否面向到面简历')
    active_price = db.Column(db.Float(10, True), info='如果面向激活简历，则对应价格')
    hh_active_price = db.Column(db.Float(10, True), server_default=db.FetchedValue(), info='HH端的激活简历价格')
    intent_price = db.Column(db.Float(10, True), info='面向意向简历的价格')
    hh_intent_price = db.Column(db.Float(10, True), server_default=db.FetchedValue(), info='HH端显示的意向简历价格')
    interview_price = db.Column(db.Float(10, True), info='面向到面简历的价格')
    hh_interview_price = db.Column(db.Float(10, True), server_default=db.FetchedValue(), info='HH端显示的面试服务价格')
    province_id = db.Column(db.BigInteger)
    city_id = db.Column(db.BigInteger)
    address = db.Column(db.String(255))
    defunct = db.Column(db.Integer)
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)



class TbRetransmitCandidate(db.Model):
    __tablename__ = 'tb_retransmit_candidate'

    id = db.Column(db.BigInteger, primary_key=True)
    candidate_id = db.Column(db.BigInteger, nullable=False, info='候选人id')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='面试官操作状态 0：未操作，1：面试官约面，2：面试官拒绝，3：面试通过，4：面试未通过')
    remark = db.Column(db.String(1000), info='备注')
    is_read = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否已读 0：未读，1：已读')
    resolved = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='已解决 0：未解决，1：已解决')
    agree_interview_time = db.Column(db.DateTime, info='简历通过时间')
    refuse_interview_time = db.Column(db.DateTime, info='简历拒绝时间')
    nonpass_interview_time = db.Column(db.DateTime, info='面试拒绝时间')
    pass_interview_time = db.Column(db.DateTime, info='面试通过时间')
    undet_before_interview_time = db.Column(db.DateTime, info='简历待定时间')
    undet_in_interview_time = db.Column(db.DateTime, info='面试待定时间')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='逻辑删除 0：未删除，1：已删除')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    operatortype = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='默认0面试官操作，1HR代面试官操作，3管理员操作')



class TbRetransmitPosition(db.Model):
    __tablename__ = 'tb_retransmit_position'

    id = db.Column(db.BigInteger, primary_key=True, info='id')
    position_id = db.Column(db.BigInteger, nullable=False, info='转发职位id')
    hr_id = db.Column(db.BigInteger, nullable=False, info='转发的hr id')
    operations = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='面试官操作权限 0：备注权限，1：操作权限')
    uuid = db.Column(db.String(50), nullable=False, info='对外暴露链接中使用')
    transmit_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0：转发选定候选人；1：转发职位下全部')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='逻辑删除 0：未删除，1：已删除')



class TbRetransmitPositionCandidate(db.Model):
    __tablename__ = 'tb_retransmit_position_candidate'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    retransmit_position_id = db.Column(db.BigInteger, nullable=False, info='转发批次id')
    candidate_id = db.Column(db.BigInteger, nullable=False, info='候选人id')
    is_read = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否已读，0：未读，1：已读')
    create_user_id = db.Column(db.BigInteger, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='逻辑删除 0：未删除，1：已删除')
    position_id = db.Column(db.BigInteger, nullable=False, info='职位id')



class TbRetransmitPositionResume(db.Model):
    __tablename__ = 'tb_retransmit_position_resume'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    retransmit_position_id = db.Column(db.BigInteger, nullable=False, info='转发批次id')
    position_id = db.Column(db.BigInteger, nullable=False, info='职位id')
    resume_feiwa_id = db.Column(db.String(65), nullable=False, info='飞蛙简历Id')
    resume_obj_id = db.Column(db.String(65), info='简历Id')
    is_read = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否已读，0：未读，1：已读')
    create_user_id = db.Column(db.BigInteger, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='逻辑删除 0：未删除，1：已删除')



class TbRole(db.Model):
    __tablename__ = 'tb_role'

    id = db.Column(db.BigInteger, primary_key=True, info='角色Id')
    role_name = db.Column(db.String(256), nullable=False, info='角色名称')
    app_id = db.Column(db.Integer, nullable=False, index=True, info='应用Id 0:hr 1:hd')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, info='修改人')



class TbSaleUpdateLog(db.Model):
    __tablename__ = 'tb_sale_update_log'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    obj_id = db.Column(db.BigInteger, nullable=False, info='对象id')
    obj_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='对象类型, 1:企业, 2:猎头公司, 3:黄页, 4:待跟进')
    sale_admin_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='bdo_id')
    history = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='修改对象绑定的销售历史记录')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbSalesAssignRule(db.Model):
    __tablename__ = 'tb_sales_assign_rule'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    name = db.Column(db.String(200), nullable=False, unique=True, info='名字')
    province_ids = db.Column(db.String(3000))
    city_ids = db.Column(db.String(3000))
    industry_ids = db.Column(db.String(3000))
    sales_admin = db.Column(db.BigInteger, nullable=False)
    sales_type = db.Column(db.Integer, nullable=False, info='1.企业销售\\n2.猎头公司销售')
    effect = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否生效')
    default_value = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否全站默认（当没有匹配到，就使用这个）')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbScheduleLog(db.Model):
    __tablename__ = 'tb_schedule_log'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    count_date = db.Column(db.Date, nullable=False, info='需要统计的日期')
    is_rerun = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否需要重新运行')
    schedule_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='定时器类型')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbSendMessageRecord(db.Model):
    __tablename__ = 'tb_send_message_record'

    id = db.Column(db.BigInteger, primary_key=True)
    headhunter_id = db.Column(db.BigInteger, nullable=False, info='猎头id')
    talent_id = db.Column(db.BigInteger, nullable=False, info='人才id')
    mobile_phone = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    email = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0 未发送 1 已发送')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    invite_code = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='邀请码')



class TbServiceEnterpriseConfiger(db.Model):
    __tablename__ = 'tb_service_enterprise_configer'
    __table_args__ = (
        db.Index('service_key_id', 'enterprise_id', 'service_key'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    enterprise_id = db.Column(db.BigInteger, nullable=False, info='雇主id')
    service_key = db.Column(db.String(63), info='服务唯一标识key')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime)



class TbServiceItem(db.Model):
    __tablename__ = 'tb_service_item'

    id = db.Column(db.BigInteger, primary_key=True)
    module_key = db.Column(db.String(63), nullable=False, info='所属模块')
    service_key = db.Column(db.String(63), nullable=False, info='服务项的唯一标识符')
    service_name = db.Column(db.String(63), info='服务名称')
    service_summary = db.Column(db.String(255), info='服务描述')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    is_display = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    icon_url = db.Column(db.String(255))
    service_item_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='服务类型；0：未开放；1：需要激活；2：无需激活，所有雇主默认拥有')
    enterprise_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='当前使用该服务的雇主数量')
    sort_value = db.Column(db.Integer, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime)



class TbServiceModule(db.Model):
    __tablename__ = 'tb_service_module'

    id = db.Column(db.BigInteger, primary_key=True)
    module_key = db.Column(db.String(63), nullable=False, info='服务模块唯一标识')
    module_title = db.Column(db.String(63), nullable=False, info='服务模块名称')
    module_summary = db.Column(db.String(255), nullable=False, info='服务模块简介')
    module_info = db.Column(db.String(255), info='服务模块介绍，展示在模块细则上')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='逻辑删除；0：未删除；1：删除')
    is_display = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否在首页展示；0：不展示（后端代码管理用）；1：展示')
    icon_url = db.Column(db.String(255), server_default=db.FetchedValue(), info='模块在前端展示的标志图路径')
    sort_value = db.Column(db.Integer, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime)



class TbServiceRelation(db.Model):
    __tablename__ = 'tb_service_relation'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    obj_id = db.Column(db.BigInteger, nullable=False, index=True)
    obj_type = db.Column(db.Integer, nullable=False, info='对象类型:1:猎头,2猎企')
    bdh_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    em_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbSmsList(db.Model):
    __tablename__ = 'tb_sms_list'
    __table_args__ = (
        db.Index('sms_phone_user_type_index', 'phone_number', 'user_type'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='唯一编号')
    phone_number = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='手机号码')
    user_type = db.Column(db.Integer, info='用户类型')
    list_type = db.Column(db.Integer, info='名单类型 0:黑名单；1:白名单')
    hour_limit = db.Column(db.Integer, info='小时上限')
    day_limit = db.Column(db.Integer, info='天上限')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbSobotAgent(db.Model):
    __tablename__ = 'tb_sobot_agents'

    agent_id = db.Column(db.String(50), primary_key=True, info='唯一编号')
    agent_email = db.Column(db.String(100), index=True, info='坐席邮箱')
    agent_name = db.Column(db.String(50), info='坐席真实名称')
    agent_nick = db.Column(db.String(50), info='坐席昵称')
    agent_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='启用状态（0未激活，1启用中，9停用，-1删除）')
    phone_no = db.Column(db.String(50), info='坐席手机')
    crm_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='对应的crm用户id')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    source_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='数据来源：0 智齿 1 天润')



class TbSobotCallRecord(db.Model):
    __tablename__ = 'tb_sobot_call_record'

    call_id = db.Column(db.String(50), primary_key=True, info='通话记录id')
    agent_id = db.Column(db.String(50), info='呼叫坐席id')
    call_flag = db.Column(db.Integer, info='接听标识 0：未接听；1：已接听')
    call_type = db.Column(db.Integer, index=True, info='呼叫类型')
    json_content = db.Column(db.Text, info='详细内容')
    start_time = db.Column(db.DateTime, index=True, info='拨打时间')
    reply = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否已回拨')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    source_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='数据来源：0 智齿 1 天润')



class TbSoftSkillTag(db.Model):
    __tablename__ = 'tb_soft_skill_tag'

    id = db.Column(db.BigInteger, primary_key=True, info='主键Id')
    tag_name = db.Column(db.String(1023), nullable=False, info='标签名称')
    tag_pinyin = db.Column(db.String(160), info='标签名称拼音')
    category = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='分类:0:未知/1:技能语言经验工具/2:领域方向背景/3:学院证书/4:内容分类/5:城市地区/6:产品类型/7:运营类型/8:目标公司/9:特定经验/10:语言要求')
    parent_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='父级Id，如果有。1:运营类型/2:211大学/3:985大学/4:工具/5:技能/6:技术/7:经验/8:语言/9:产品类型')
    is_validate = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否验证:0:未验证/1:已验证')
    source_industy = db.Column(db.String(100), info='产生时的行业')
    source_function = db.Column(db.String(100), info='产生时的职能')
    source_position = db.Column(db.String(100), info='产生时的职位')
    description = db.Column(db.String(255), info='描述')
    hr_sorting = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='hr端排序')
    hh_sorting = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='hh端排序')
    tdc_sorting = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='tdc端排序')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_user_id = db.Column(db.BigInteger, info='更新人')
    update_time = db.Column(db.DateTime)
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否删除 0 否 1是')



class TbSpecialEnterprise(db.Model):
    __tablename__ = 'tb_special_enterprise'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    enterprise_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    special_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='特殊类型0：不特殊1：去哪儿')



class TbSpecialHighCvFile(db.Model):
    __tablename__ = 'tb_special_high_cv_file'
    __table_args__ = (
        db.Index('idx_recruitspecialid_defunct', 'recruit_special_id', 'defunct'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    recruit_special_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='同质化专场id')
    file_name = db.Column(db.String(256), nullable=False, info='高端cv文件名称')
    file_url = db.Column(db.String(512), nullable=False, info='高端cv文件地址')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)
    expire_time = db.Column(db.DateTime, info='过期时间')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class TbSpecialHighCvInfo(db.Model):
    __tablename__ = 'tb_special_high_cv_info'
    __table_args__ = (
        db.Index('idx_recruitspecialid_special_high_cv_id_is_recommend_defunct', 'recruit_special_id', 'special_high_cv_id', 'is_recommend', 'defunct'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    recruit_special_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='同质化专场id')
    special_high_cv_id = db.Column(db.BigInteger, nullable=False, info='高端cv文件id')
    talent_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='简历id')
    name = db.Column(db.String(64), nullable=False, info='名字')
    sex = db.Column(db.String(8), nullable=False, info='性别')
    age = db.Column(db.String(32), nullable=False, info='年龄')
    city = db.Column(db.String(64), nullable=False, info='所在城市')
    highest_education = db.Column(db.String(64), nullable=False, info='最高学历')
    school = db.Column(db.String(256), nullable=False, info='毕业院校')
    is_211 = db.Column(db.String(8), nullable=False, info='是否211')
    is_985 = db.Column(db.String(8), nullable=False, info='是否985')
    is_lieying = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否为猎英,0:非猎英,1:猎英')
    current_position = db.Column(db.String(256), nullable=False, info='当前职位')
    current_annual_salary = db.Column(db.String(256), nullable=False, info='当前年薪')
    stair_function = db.Column(db.String(256), nullable=False, info='一级职能（应聘职位）')
    second_function = db.Column(db.String(256), nullable=False, info='二级职能（应聘职位）')
    established_company = db.Column(db.String(256), nullable=False, info='曾任职知名公司（最近工作过的一家知名公司）')
    take_office_time = db.Column(db.String(256), nullable=False, info='知名公司任职时长（最近这家知名公司的工作时长） ')
    job_duties = db.Column(db.String(3000), nullable=False, info='工作职责（最近这家知名公司的工作职责）')
    job_hopping_rate = db.Column(db.String(256), nullable=False, info='跳槽频率（当前时间倒推至开始工作总年数(上限10年)/公司数）')
    recommended_reason = db.Column(db.Text, nullable=False, info='推荐理由（订单中的推荐理由）')
    is_recommend = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否推荐 true 推荐  false 取消推荐')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    talent_headhunter_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='简历对应猎头id')
    talent_company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='简历对应猎头公司id')



class TbSpecialPosition(db.Model):
    __tablename__ = 'tb_special_position'
    __table_args__ = (
        db.Index('idx_recruitspecialid_positionid', 'recruit_special_id', 'position_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    recruit_special_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='同质化专场id')
    position_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='职位ID')
    priority = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='优先级')
    match_priority = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='（九宫格匹配）优先级')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    expire_time = db.Column(db.DateTime, info='过期时间')



class TbStarEnterprise(db.Model):
    __tablename__ = 'tb_star_enterprise'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    enterprise_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='企业id')
    enterprise_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='企业类型')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除,0:false,1:true')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    priority = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class TbSubscription(db.Model):
    __tablename__ = 'tb_subscription'
    __table_args__ = (
        db.Index('uidx_userid_notifytype_subtype', 'user_id', 'notify_type', 'sub_type'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_id = db.Column(db.BigInteger, nullable=False)
    notify_type = db.Column(db.Integer, nullable=False, info='1.站内信\\n2.短信\\n3.邮箱\\n4.微信')
    sub_type = db.Column(db.Integer, nullable=False, info='1.candidate\\n2.position\\n3.hunteron\\n4.hr')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')



class TbSuggestBaseNormal(db.Model):
    __tablename__ = 'tb_suggest_base_normal'

    id = db.Column(db.BigInteger, primary_key=True)
    word = db.Column(db.String(63), nullable=False, info='关键字内容')
    word_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='关键字类型；1 : 【内部】企业名称；2：【内部】职位标题；3：【内部】职能；4：【内部】行业；5：【内部】地区；6：【内部】技能关键字；7：【内部】猎企名称')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除，0：正常未删除；1：已删除')
    update_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False)



class TbSupplierInviteInfo(db.Model):
    __tablename__ = 'tb_supplier_invite_info'

    id = db.Column(db.BigInteger, primary_key=True)
    supplier_id = db.Column(db.BigInteger)
    enterprise_id = db.Column(db.BigInteger, nullable=False, info='雇主ID')
    hr_id = db.Column(db.BigInteger, nullable=False, info='生成邀请链接的HR')
    invite_code = db.Column(db.String(63), nullable=False)
    company_name = db.Column(db.String(127), info='猎企名称')
    root_hunter_name = db.Column(db.String(31), info='负责人')
    cell_phone = db.Column(db.String(31), nullable=False, info='邀请时填写的手机号，需要在提交审核信息的时候验证手机验证码')
    email = db.Column(db.String(63), info='邀请码发送的邮箱，记录用')
    company_id = db.Column(db.BigInteger, info='关联的猎企ID')
    start_time = db.Column(db.DateTime, info='邀请码，有效开始时间')
    end_time = db.Column(db.DateTime, info='邀请码有效时间，结束')
    create_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)



class TbSystemEnterprise(db.Model):
    __tablename__ = 'tb_system_enterprise'

    id = db.Column(db.BigInteger, primary_key=True)
    code = db.Column(db.BigInteger, nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='派系名称')
    remark = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='备注')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='逻辑删除 0：未删除，1：已删除')



class TbSystemEnterpriseRelation(db.Model):
    __tablename__ = 'tb_system_enterprise_relation'
    __table_args__ = (
        db.Index('enterprise_id_index', 'enterprise_id', 'system_code'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    system_code = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='派系id')
    enterprise_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='企业id')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='逻辑删除 0：未删除，1：已删除')



class TbTag(db.Model):
    __tablename__ = 'tb_tag'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    content = db.Column(db.String(30), nullable=False, unique=True, server_default=db.FetchedValue(), info='标签内容')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbTagDicCustom(db.Model):
    __tablename__ = 'tb_tag_dic_custom'

    id = db.Column(db.BigInteger, primary_key=True, info='主键编号')
    custom_industry = db.Column(db.String(200), info='自定义行业')
    custom_function = db.Column(db.String(200), info='自定义职能')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    create_time = db.Column(db.DateTime, info='创建时间')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否删除 0 否 1是')



class TbTagDicEnterprise(db.Model):
    __tablename__ = 'tb_tag_dic_enterprise'

    id = db.Column(db.BigInteger, primary_key=True, info='自增ID')
    key_id = db.Column(db.String(500), info='id拼接')
    enterprise_id = db.Column(db.BigInteger, info='企业id')
    user_id = db.Column(db.BigInteger, info='操作人')
    industry_ids = db.Column(db.String(500), info='行业(多个以逗号分隔)')
    develop_status = db.Column(db.BigInteger, info='发展阶段')
    enterprise_style = db.Column(db.BigInteger, info='企业性质')
    establish_age = db.Column(db.BigInteger, info='成立年限')
    enterprise_scale = db.Column(db.BigInteger, info='公司规模')
    enterprise_lights = db.Column(db.String(500), info='公司亮点')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='更新时间')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否删除 0 否 1 是')



class TbTagDicHeadhunter(db.Model):
    __tablename__ = 'tb_tag_dic_headhunter'
    __table_args__ = (
        db.Index('index_2', 'industry_id1', 'industry_id2', 'position_title1', 'position_title2', 'position_title3', 'city_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='自增ID')
    key_id = db.Column(db.String(500), info='id拼接')
    hh_id = db.Column(db.BigInteger, index=True, info='猎头ID')
    user_id = db.Column(db.BigInteger, info='操作人')
    industry_id1 = db.Column(db.BigInteger, info='行业一级')
    industry_id2 = db.Column(db.BigInteger, info='行业二级')
    position_title1 = db.Column(db.BigInteger, info='职能一级')
    position_title2 = db.Column(db.BigInteger, info='职能二级')
    position_title3 = db.Column(db.BigInteger, info='职能三级')
    annual_salary_level = db.Column(db.Integer, index=True, info='年薪职级 1: 30万以下, 2: 30-50万, 3: 50-100万, 4: 100-200万, 5: 200万以上')
    city_id = db.Column(db.BigInteger, info='城市ID')
    custom_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='自定义编号')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='更新时间')
    defunct = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='是否删除 0 否 1 是')



class TbTagDicHr(db.Model):
    __tablename__ = 'tb_tag_dic_hr'
    __table_args__ = (
        db.Index('index_2', 'industry_id1', 'industry_id2', 'position_title1', 'position_title2', 'position_title3', 'annual_salary_level', 'city_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='自增ID')
    key_id = db.Column(db.String(500), info='id拼接')
    hr_id = db.Column(db.BigInteger, index=True, info='HR_ID')
    user_id = db.Column(db.BigInteger, info='操作人')
    industry_id1 = db.Column(db.BigInteger, info='行业一级')
    industry_id2 = db.Column(db.BigInteger, info='行业二级')
    position_title1 = db.Column(db.BigInteger, info='职能一级')
    position_title2 = db.Column(db.BigInteger, info='职能二级')
    position_title3 = db.Column(db.BigInteger, info='职能三级')
    annual_salary_level = db.Column(db.Integer, info='年薪职级 1: 30万以下, 2: 30-50万, 3: 50-100万, 4: 100-200万, 5: 200万以上')
    city_id = db.Column(db.BigInteger, info='城市ID')
    custom_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='自定义编号')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='更新时间')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否删除 0 否 1 是')



class TbTagDicLog(db.Model):
    __tablename__ = 'tb_tag_dic_log'

    id = db.Column(db.BigInteger, primary_key=True)
    obj_id = db.Column(db.BigInteger)
    obj_type = db.Column(db.Integer, info='1 猎头， 2 HR  ，3 职位')
    operate_type = db.Column(db.Integer, info='0 增加 1 修改 2 删除')
    original = db.Column(db.String(5000))
    target = db.Column(db.String(5000))
    operate_user_id = db.Column(db.BigInteger)
    operate_user_type = db.Column(db.Integer)
    create_time = db.Column(db.DateTime)



class TbTagDicPosition(db.Model):
    __tablename__ = 'tb_tag_dic_position'
    __table_args__ = (
        db.Index('index_2', 'industry_id1', 'industry_id2', 'position_title1', 'position_title2', 'position_title3'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='自增ID')
    key_id = db.Column(db.String(500), info='id拼接')
    position_id = db.Column(db.BigInteger, index=True, info='职位ID')
    user_id = db.Column(db.BigInteger, info='操作人')
    industry_id1 = db.Column(db.BigInteger, info='行业一级')
    industry_id2 = db.Column(db.BigInteger, info='行业二级')
    position_title1 = db.Column(db.BigInteger, info='职能一级')
    position_title2 = db.Column(db.BigInteger, info='职能二级')
    position_title3 = db.Column(db.BigInteger, info='职能三级')
    annual_salary_level = db.Column(db.Integer, info='年薪职级 1: 30万以下, 2: 30-50万, 3: 50-100万, 4: 100-200万, 5: 200万以上')
    city_id = db.Column(db.BigInteger, info='城市ID')
    custom_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='自定义编号')
    tag_ids = db.Column(db.String(512), info='新标签IDS')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='更新时间')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否删除 0 否 1 是')



class TbTagExcel(db.Model):
    __tablename__ = 'tb_tag_excel'

    position_id = db.Column(db.BigInteger, primary_key=True)
    position_name = db.Column(db.String(255))
    industry_name1 = db.Column(db.String(255))
    industry_name2 = db.Column(db.String(255))
    position_title_name1 = db.Column(db.String(255))
    position_title_name2 = db.Column(db.String(255))
    position_title_name3 = db.Column(db.String(255))
    industry_id1 = db.Column(db.BigInteger)
    industry_id2 = db.Column(db.BigInteger)
    position_titile1 = db.Column(db.BigInteger)
    position_titile2 = db.Column(db.BigInteger)
    position_titile3 = db.Column(db.BigInteger)
    city_id = db.Column(db.BigInteger)
    is_handle = db.Column(db.Integer, server_default=db.FetchedValue())



t_tb_tag_hh_excel = db.Table(
    'tb_tag_hh_excel',
    db.Column('user_name', db.String(255)),
    db.Column('hh_source', db.String(255)),
    db.Column('create_time_str', db.String(255)),
    db.Column('hh_id', db.BigInteger),
    db.Column('hh_name', db.String(255)),
    db.Column('hh_tag_type', db.String(255)),
    db.Column('hh_no', db.String(255)),
    db.Column('industry_name1', db.String(255)),
    db.Column('industry_name2', db.String(255)),
    db.Column('position_titile_name1', db.String(255)),
    db.Column('position_titile_name2', db.String(255)),
    db.Column('position_titile_name3', db.String(255)),
    db.Column('annual_salarys', db.String(255)),
    db.Column('city_names', db.String(255)),
    db.Column('user_id', db.BigInteger),
    db.Column('industry_id1', db.BigInteger),
    db.Column('industry_id2', db.BigInteger),
    db.Column('position_titile1', db.BigInteger),
    db.Column('position_titile2', db.BigInteger),
    db.Column('position_titile3', db.BigInteger),
    db.Column('annual_salary_ids', db.String(255)),
    db.Column('city_ids', db.String(255)),
    db.Column('create_time', db.DateTime)
)



class TbTalentFlowLog(db.Model):
    __tablename__ = 'tb_talent_flow_log'

    id = db.Column(db.BigInteger, primary_key=True)
    talent_id = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='外部人才id')
    flow_type = db.Column(db.Integer, nullable=False, info='1：猎上库进入孵化器；2：猎上库进入人才市场；3：孵化器进入人才市场')
    flow_time = db.Column(db.DateTime, nullable=False, info='流动时间')



class TbTalentIntentReport(db.Model):
    __tablename__ = 'tb_talent_intent_report'

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



class TbTalentLookedRecord(db.Model):
    __tablename__ = 'tb_talent_looked_records'

    id = db.Column(db.BigInteger, primary_key=True)
    headhunter_id = db.Column(db.BigInteger, nullable=False, info='猎头id')
    talent_id = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='外部人才id')
    source = db.Column(db.Integer, info='查看来源，1：孵化器；2：人才市场')
    looked_time = db.Column(db.DateTime, info='查看时间')
    create_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())



class TbTalentSearchCondition(db.Model):
    __tablename__ = 'tb_talent_search_condition'

    id = db.Column(db.BigInteger, primary_key=True)
    source = db.Column(db.Integer)
    condition_json = db.Column(db.String(1500))
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    _def = db.Column('def', db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否为默认')



class TbTalentTag(db.Model):
    __tablename__ = 'tb_talent_tag'
    __table_args__ = (
        db.Index('uidx_talentid_tagid_createuserid', 'talent_id', 'tag_content', 'create_user_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    talent_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue())
    tag_content = db.Column(db.String(30), nullable=False, index=True, server_default=db.FetchedValue())
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除0false1true')
    create_user_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')



class TbTalentTagRelation(db.Model):
    __tablename__ = 'tb_talent_tag_relation'

    id = db.Column(db.BigInteger, primary_key=True)
    company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='公司ID')
    tag_id = db.Column(db.BigInteger, nullable=False, info='标签ID')
    talent_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='人才ID')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除')
    create_time = db.Column(db.DateTime, nullable=False)
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())



class TbThirdAuthUser(db.Model):
    __tablename__ = 'tb_third_auth_user'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    user_id = db.Column(db.BigInteger, info='用户id')
    open_id = db.Column(db.String(250), index=True, info='公众号openId')
    client_id = db.Column(db.String(250), info='第三方clientId')
    access_token = db.Column(db.String(1000), info='网页授权接口调用凭证')
    expires_in = db.Column(db.Integer, info='access_token接口调用凭证超时时间，单位（秒）')
    refresh_token = db.Column(db.String(1000), info='用户刷新access_token')
    scope = db.Column(db.String(50), info='用户授权的作用域，使用逗号（,）分隔')
    union_id = db.Column(db.String(100))
    type = db.Column(db.Integer, info='平台来源')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='逻辑删除')
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue())



class TbThirdAuthUserInfo(db.Model):
    __tablename__ = 'tb_third_auth_user_info'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    user_id = db.Column(db.BigInteger, info='用户id')
    open_id = db.Column(db.String(250), index=True, info='公众号openId')
    client_id = db.Column(db.String(250), info='第三方clientId')
    subscribe = db.Column(db.Integer)
    nickname = db.Column(db.String(100), info='用户昵称')
    sex_desc = db.Column(db.String(8), info='性别描述信息：男、女、未知等')
    sex = db.Column(db.Integer, info='性别表示：1，2等数字')
    language = db.Column(db.String(50), info='语言')
    city = db.Column(db.String(50), info='城市')
    province = db.Column(db.String(50), info='省份')
    country = db.Column(db.String(50), info='国家')
    headImg_url = db.Column(db.String(250), info='头像')
    subscribe_time = db.Column(db.BigInteger, info='订阅时间')
    union_id = db.Column(db.String(100))
    remark = db.Column(db.String(200), info='备注')
    group_id = db.Column(db.Integer)
    tag_ids = db.Column(db.String(200), info='以,分隔')
    privileges = db.Column(db.String(1000), info='用户特权信息,以,分隔')
    subscribe_scene = db.Column(db.String(50), info='用户关注的渠道来源')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='逻辑删除')
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue())



class TbTimeBackup(db.Model):
    __tablename__ = 'tb_time_backup'
    __table_args__ = (
        db.Index('idx_databasename_tablename_pk', 'database_name', 'table_name', 'pk'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    database_name = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue())
    table_name = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue())
    pk = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    original_create_time = db.Column(db.DateTime)
    original_update_time = db.Column(db.DateTime)
    new_create_time = db.Column(db.DateTime)
    new_update_time = db.Column(db.DateTime)



class TbTradeOrderApiLog(db.Model):
    __tablename__ = 'tb_trade_order_api_log'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    trade_no = db.Column(db.String(32), info='外部订单编号')
    user_id = db.Column(db.BigInteger, info='用户ID')
    api_type = db.Column(db.Integer, info='API 类型')
    channel_type = db.Column(db.Integer, info='渠道类型')
    api_log_type = db.Column(db.Integer, info='API日志类型')
    api_method = db.Column(db.String(512), info='API方法')
    content = db.Column(db.Text, info='内容JSON')
    create_time = db.Column(db.DateTime, info='创建时间')
    create_user_id = db.Column(db.BigInteger, info='创建用户ID')



class TbUnreadCandidate(db.Model):
    __tablename__ = 'tb_unread_candidate'
    __table_args__ = (
        db.Index('idx_userid_candidateid', 'user_id', 'candidate_id'),
        db.Index('idx_userid_type', 'user_id', 'type')
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='用户id')
    candidate_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='候选人id')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='列表类型0：已推荐1：面试中2：待筛选 3:待确认面试')
    create_time = db.Column(db.DateTime, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建用户')



class TbUnreadPayment(db.Model):
    __tablename__ = 'tb_unread_payment'
    __table_args__ = (
        db.Index('idx_userid_paymentid', 'user_id', 'payment_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='用户id')
    payment_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='支付id')
    create_time = db.Column(db.DateTime, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建用户')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除 1:true 已删除；0:false 未删除')



class TbUnreadPlacement(db.Model):
    __tablename__ = 'tb_unread_placement'
    __table_args__ = (
        db.Index('idx_userid_type', 'user_id', 'type'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='用户id')
    placement_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='成单id')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='列表类型0:offer1:到岗2：过保')
    create_time = db.Column(db.DateTime, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建用户')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除 1:true 已删除；0:false 未删除')



class TbUnreadPosition(db.Model):
    __tablename__ = 'tb_unread_position'
    __table_args__ = (
        db.Index('idx_userid_type', 'user_id', 'type'),
        db.Index('idx_userid_positionid', 'user_id', 'position_id')
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='用户id')
    position_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职位id')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='列表类型0：合作1：重要2：关注3：申请')
    create_time = db.Column(db.DateTime, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建用户')



class TbUnreadTalent(db.Model):
    __tablename__ = 'tb_unread_talent'
    __table_args__ = (
        db.Index('idx_userid_type', 'user_id', 'type'),
        db.Index('idx_userid_talentid', 'user_id', 'talent_id')
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='用户id')
    talent_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='人才id')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='列表类型0：候选人库1：需沟通待推荐')
    create_time = db.Column(db.DateTime, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建用户')



class TbUpgradeConditionConfig(db.Model):
    __tablename__ = 'tb_upgrade_condition_config'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='hd or hr')
    interviewed_rate = db.Column(db.Float(asdecimal=True), info='面试率')
    revoke_rate = db.Column(db.Float(asdecimal=True), info='撤销率')
    recommand_quality = db.Column(db.Float(asdecimal=True), info='推荐质量')
    service_quality = db.Column(db.Float(asdecimal=True), info='服务质量')
    reward = db.Column(db.Float, info='offer佣金')
    extra_reward = db.Column(db.Float, info='扩展offer佣金，如果配置了则优先判断该项')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbUserActivityBehavior(db.Model):
    __tablename__ = 'tb_user_activity_behavior'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    activity_code = db.Column(db.String(64), nullable=False, info='活动Code')
    user_id = db.Column(db.BigInteger, index=True, info='用户ID')
    user_type = db.Column(db.Integer, nullable=False, info='用户类型:1：企业，2：猎头，3：管理员，4：渠道用户，5：求职者用户')
    mobile = db.Column(db.String(16), index=True, info='用户手机号')
    mobile_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='手机号验证状态(1:已关联用户；2：未关联用户)')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除0:false 1:true')
    activity_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='活动状态(0:新录待审；1：可用；2：不可用)')
    ip = db.Column(db.String(128), info='IP')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    update_user_id = db.Column(db.BigInteger, info='修改人')



class TbUserActivityConfig(db.Model):
    __tablename__ = 'tb_user_activity_config'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    activity_code = db.Column(db.String(64), info='活动Code')
    user_id = db.Column(db.BigInteger, index=True, info='用户ID')
    user_type = db.Column(db.Integer, server_default=db.FetchedValue(), info='用户类型:1：企业，2：猎头，3：管理员，4：渠道用户，5：求职者用户')
    config_type = db.Column(db.String(50), info='设置类型')
    config_value = db.Column(db.String(50), info='设置值')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否删除0:false 1:true')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='修改时间')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    update_user_id = db.Column(db.BigInteger, info='修改人')



class TbUserActivityInviteCode(db.Model):
    __tablename__ = 'tb_user_activity_invite_code'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='用户id')
    invite_code = db.Column(db.String(20), nullable=False, unique=True, server_default=db.FetchedValue(), info='邀请码')
    share = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否分享成功；0：未分享；1：分享')
    qr_code = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='二维码图片')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbUserActivityPrizeHistory(db.Model):
    __tablename__ = 'tb_user_activity_prize_history'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_id = db.Column(db.BigInteger, index=True, info='用户ID')
    activity_code = db.Column(db.String(64), info='活动Code')
    prize_pool_id = db.Column(db.BigInteger, info='奖品池关联ID')
    prize_type = db.Column(db.String(32), info='奖品类型')
    prize_text = db.Column(db.String(2048), info='奖品文本')
    data_code1 = db.Column(db.BigInteger, info='奖品数据Code1')
    data_code2 = db.Column(db.BigInteger, info='奖品数据Code2')
    data_code3 = db.Column(db.String(128), info='奖品数据Code2')
    prize_isuse_time = db.Column(db.DateTime, info='奖品发放时间')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否删除0:false 1:true')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, info='修改时间')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    update_user_id = db.Column(db.BigInteger, info='修改人')



class TbUserAward(db.Model):
    __tablename__ = 'tb_user_award'
    __table_args__ = (
        db.Index('uidx_userid_awardtype', 'user_id', 'award_type'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_id = db.Column(db.BigInteger, nullable=False)
    award_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1.活动注册有奖\\n2.受邀请注册有奖')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0.未激活\\n1.激活\\n2.已领取')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')



class TbUserBlackList(db.Model):
    __tablename__ = 'tb_user_black_list'

    id = db.Column(db.BigInteger, primary_key=True)
    obj_id = db.Column(db.BigInteger, nullable=False, info='对象id')
    obj_type = db.Column(db.Integer, nullable=False, info='对象类型：1：猎头')
    confine_start_time = db.Column(db.DateTime, info='关小黑屋的开始执行时间')
    confine_end_time = db.Column(db.DateTime, info='关小黑屋的结束时间时间，永久在当前时间基础上加60年')
    confine_reason = db.Column(db.String(1000), info='拉黑原因')
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否删除 0 否 1是')



class TbUserCompanyApplyLeave(db.Model):
    __tablename__ = 'tb_user_company_apply_leave'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='修改时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    operation_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='操作用户ID')
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='申请人ID')
    company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='申请人所在公司')
    connect_headhunter_Id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='交接猎头ID')
    connect_company_headhunter_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='交接公司库的猎头ID')
    status = db.Column(db.Integer, server_default=db.FetchedValue(), info='申请状态 成功:1,失败:0,申请:2')
    take_public = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否带走公开候选人')
    take_private_public = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否带走私有公开候选人')



t_tb_user_delete_record = db.Table(
    'tb_user_delete_record',
    db.Column('user_id', db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='被删除的用户ID'),
    db.Column('email', db.String(100), nullable=False, server_default=db.FetchedValue(), info='用户邮箱'),
    db.Column('mobile', db.String(50), nullable=False, server_default=db.FetchedValue(), info='用户手机'),
    db.Column('user_type', db.Integer, nullable=False, server_default=db.FetchedValue(), info='被删除的用户类型：1.HR，2.HD'),
    db.Column('reason', db.String(1000), nullable=False, server_default=db.FetchedValue(), info='删除原因'),
    db.Column('deleteTime', db.DateTime, info='删除时间'),
    db.Column('createTime', db.DateTime, info='创建时间'),
    db.Column('createUserId', db.BigInteger, info='创建人'),
    db.Column('updateTime', db.DateTime, info='修改时间'),
    db.Column('updateUserId', db.BigInteger, info='修改人')
)



class TbUserIdentity(db.Model):
    __tablename__ = 'tb_user_identity'
    __table_args__ = (
        db.Index('INDEX_USER_TYPE', 'user_type', 'identity', 'type'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_id = db.Column(db.BigInteger, nullable=False, index=True, info='用户id')
    user_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1 : hr; 2 : hh; 3: admin; 4: agent')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建者id')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    type = db.Column(db.String(1), nullable=False, info='E:email, M:mobile, O:others')
    identity = db.Column(db.String(100), nullable=False, info='唯一性凭证')
    dead_time = db.Column(db.DateTime, info='账号失效时间；null表示不失效')



class TbUserIdentitySafe(db.Model):
    __tablename__ = 'tb_user_identity_safe'
    __table_args__ = (
        db.Index('conbain', 'user_id', 'user_type', 'safe_ip'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, nullable=False)
    user_type = db.Column(db.Integer, info='用户类型')
    safe_ip = db.Column(db.String(31), index=True, info='登录ip')
    pwd_login = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否允许密码登录')
    sms_login = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否允许短信登录')
    wechat_login = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否允许微信登录')
    defunct = db.Column(db.Integer)
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)



class TbUserIntegral(db.Model):
    __tablename__ = 'tb_user_integral'

    user_id = db.Column(db.BigInteger, primary_key=True)
    user_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='hd or hr')
    company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='企业/猎企')
    pullulate_value = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='贡献值')
    base_pullulate_value = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='实际贡献值')
    credit_value = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='信誉值')
    point_value = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='积分值')
    grade = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='当前等级')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbUserIntegralRecord(db.Model):
    __tablename__ = 'tb_user_integral_record'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue())
    company_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='公司编号')
    to_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='赠送人or接受人')
    user_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='hd or hr')
    integral_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='积分类型：贡献值或其他')
    operate_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='操作类型:面试确认、offer等')
    integral_value = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='积分值/贡献值')
    after_integral_value = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='之后积分值')
    candidate_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='候选人编号')
    position_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职位编号')
    talent_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='人才编号')
    qd_talent_id = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='巧达人才编号')
    jobhunter_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='求职者编号')
    before_grade = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='之前等级')
    after_grade = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='之后等级')
    is_upgrade = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否升级')
    is_complete = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否完成任务')
    is_read = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否已读')
    remark = db.Column(db.String(200), info='备注')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1 : true 已删除；0 : false 有效')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbUserIntegralTopRecord(db.Model):
    __tablename__ = 'tb_user_integral_top_record'

    id = db.Column(db.Integer, primary_key=True, info='主键ID')
    point_top_value = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='积分上线值')
    headhunter_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='猎头类型：0 非白名单 1白名单')
    update_user_id = db.Column(db.BigInteger, nullable=False, info='更新人')
    update_time = db.Column(db.DateTime, nullable=False, info='更新时间')



class TbUserInviteRecord(db.Model):
    __tablename__ = 'tb_user_invite_record'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='用户id')
    invite_code = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue(), info='邀请码')
    operation_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1：手动输入;2:通过链接带入')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbUserOperation(db.Model):
    __tablename__ = 'tb_user_operation'
    __table_args__ = (
        db.Index('idx_user_id_company_id_app_id', 'user_id', 'company_id', 'app_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键Id')
    operation_id = db.Column(db.BigInteger, nullable=False, info='操作Id')
    user_id = db.Column(db.BigInteger, nullable=False, info='用户Id')
    company_id = db.Column(db.BigInteger, nullable=False, info='公司Id')
    app_id = db.Column(db.Integer, nullable=False, info='应用Id 0:hr 1:hd')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, info='修改人')



class TbUserOperationBak20160126(db.Model):
    __tablename__ = 'tb_user_operation_bak20160126'
    __table_args__ = (
        db.Index('idx_user_id_company_id_app_id', 'user_id', 'company_id', 'app_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键Id')
    operation_id = db.Column(db.BigInteger, nullable=False, info='操作Id')
    user_id = db.Column(db.BigInteger, nullable=False, info='用户Id')
    company_id = db.Column(db.BigInteger, nullable=False, info='公司Id')
    app_id = db.Column(db.Integer, nullable=False, info='应用Id 0:hr 1:hd')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, info='创建人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, info='修改人')



class TbUserPageLastBrowse(db.Model):
    __tablename__ = 'tb_user_page_last_browse'
    __table_args__ = (
        db.Index('IDX_PAGE_CODE_USER_ID', 'page_code', 'user_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    page_code = db.Column(db.String(255), info='页面Code')
    user_id = db.Column(db.BigInteger, info='用户ID')
    last_count = db.Column(db.BigInteger, info='最后数量')
    last_browse_time = db.Column(db.DateTime, info='最后浏览时间')
    create_time = db.Column(db.DateTime, info='创建时间')



class TbUserPayInfo(db.Model):
    __tablename__ = 'tb_user_pay_info'

    user_id = db.Column(db.BigInteger, primary_key=True, server_default=db.FetchedValue(), info='用户编号')
    user_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='用户类型 1:hr 2:hd 3:admin 4:渠道用户 5:求职者')
    bank_account_number = db.Column(db.String(30), nullable=False, server_default=db.FetchedValue(), info='银行卡号')
    bank_account_name = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='银行开户名')
    deposit_bank = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='开户行')
    bank_type = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='银行类型')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='审核状态0：未提交审核；1：审核中；2：审核成功；3：审核未通过；')
    defunct = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否无效1 : true 已删除；0 : false 有效')
    operator_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='审核操作人')
    reject_reason = db.Column(db.String(500), info='拒绝理由')
    submit_verify_time = db.Column(db.DateTime, info='提交身份认证时间')
    operate_verify_time = db.Column(db.DateTime, info='操作身份认证时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbUserPositionClue(db.Model):
    __tablename__ = 'tb_user_position_clues'
    __table_args__ = (
        db.Index('idx_user_position_clues_deal_status_user_id', 'deal_user_id', 'deal_status'),
        db.Index('IDX_POSITION_ID_USER_ID', 'position_id', 'user_id')
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    clues_type = db.Column(db.Integer, info='线索类型')
    position_id = db.Column(db.BigInteger, info='职位ID')
    user_id = db.Column(db.BigInteger, info='用户ID')
    deal_user_id = db.Column(db.BigInteger, info='处理用户ID')
    deal_status = db.Column(db.Integer, server_default=db.FetchedValue(), info='处理状态(1:待处理；2：已处理)')
    deal_time = db.Column(db.DateTime, info='处理时间')
    deal_result_id = db.Column(db.BigInteger, info='沟通记录ID')
    position_health = db.Column(db.Numeric(11, 2), info='健康度')
    position_priority = db.Column(db.Integer, info='职位定级（职位紧急度）')
    last_operate_time = db.Column(db.DateTime, info='最后操作时间')
    update_time = db.Column(db.DateTime, info='修改时间')
    update_user_id = db.Column(db.BigInteger, info='修改用户ID')
    create_time = db.Column(db.DateTime, info='创建时间')
    create_user_id = db.Column(db.BigInteger, info='创建用户ID')
    position_tag_id = db.Column(db.BigInteger, info='职位标签ID')



class TbUserPositionCluesCopy20200910(db.Model):
    __tablename__ = 'tb_user_position_clues_copy20200910'
    __table_args__ = (
        db.Index('IDX_POSITION_ID_USER_ID', 'position_id', 'user_id'),
        db.Index('idx_user_position_clues_deal_status_user_id', 'deal_user_id', 'deal_status')
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    clues_type = db.Column(db.Integer, info='线索类型')
    position_id = db.Column(db.BigInteger, info='职位ID')
    user_id = db.Column(db.BigInteger, info='用户ID')
    deal_user_id = db.Column(db.BigInteger, info='处理用户ID')
    deal_status = db.Column(db.Integer, server_default=db.FetchedValue(), info='处理状态(1:待处理；2：已处理)')
    deal_time = db.Column(db.DateTime, info='处理时间')
    deal_result_id = db.Column(db.BigInteger, info='沟通记录ID')
    position_health = db.Column(db.Numeric(11, 2), info='健康度')
    position_priority = db.Column(db.Integer, info='职位定级（职位紧急度）')
    last_operate_time = db.Column(db.DateTime, info='最后操作时间')
    update_time = db.Column(db.DateTime, info='修改时间')
    update_user_id = db.Column(db.BigInteger, info='修改用户ID')
    create_time = db.Column(db.DateTime, info='创建时间')
    create_user_id = db.Column(db.BigInteger, info='创建用户ID')



class TbUserReplyLog(db.Model):
    __tablename__ = 'tb_user_reply_log'

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='用户编号')
    jobhunter_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='求职者编号')
    reply_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='回复类型：1:呼叫；2:委托')
    reply_time = db.Column(db.DateTime, info='回复时间')
    is_reply = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class TbUserScore(db.Model):
    __tablename__ = 'tb_user_score'

    user_id = db.Column(db.BigInteger, primary_key=True)
    score = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='总积分')
    contribution = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='贡献值')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    pullulate = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='成长值')



class TbUserScoreRecord(db.Model):
    __tablename__ = 'tb_user_score_record'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1：积分；2：贡献值')
    operation_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='操作类型')
    operation_value = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='操作值，积分或者贡献值')
    operation_after_value = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='操作后总值，积分或者贡献值')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    candidate_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='候选人编号')



class TbUserSearchLog(db.Model):
    __tablename__ = 'tb_user_search_log'
    __table_args__ = (
        db.Index('INDEX_SEARCH_LOG_USER_ID_TYPE', 'user_id', 'query_type'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='唯一编号')
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='用户id')
    query_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='搜索类型 1:职位')
    query_word = db.Column(db.String(255), info='关键字')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除；0:false;1:true')
    create_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, index=True)
    update_time = db.Column(db.DateTime, nullable=False)



class TbUserSignSingleConfig(db.Model):
    __tablename__ = 'tb_user_sign_single_config'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_id = db.Column(db.BigInteger, index=True, info='用户ID')
    app_type = db.Column(db.String(64), info='平台类型')
    client_type = db.Column(db.String(64), info='客户端类型')
    max_single_login_count = db.Column(db.Integer, server_default=db.FetchedValue(), info='最多单点登录次数')
    create_time = db.Column(db.DateTime, info='创建时间')
    create_user_id = db.Column(db.BigInteger, info='创建人')
    update_user_id = db.Column(db.BigInteger, info='最后修改人')
    update_time = db.Column(db.DateTime, info='最后修改时间')



class TbUserSimpleForm(db.Model):
    __tablename__ = 'tb_user_simple_form'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    form_code = db.Column(db.String(50), index=True, info='表单Code')
    user_type = db.Column(db.Integer, info='用户类型')
    user_id = db.Column(db.BigInteger, info='用户ID')
    name = db.Column(db.String(20), info='名称')
    company_name = db.Column(db.String(255), info='公司名称')
    mobile = db.Column(db.String(20), info='手机号')
    form_json = db.Column(db.Text, info='表单JSON')
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)



class TbUserSource(db.Model):
    __tablename__ = 'tb_user_source'

    user_id = db.Column(db.BigInteger, primary_key=True, info='用户Id')
    channel_referer = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='渠道的referer地址')
    channel = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='渠道')
    event_referer = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='活动的referer地址')
    event = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='活动')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')



class TbUserSurvey(db.Model):
    __tablename__ = 'tb_user_survey'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    headhunter_id = db.Column(db.BigInteger, nullable=False, info='猎头ID')
    cooperate_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='合作类型 1 全职做单，2 兼职做单，3 私单')
    work_will = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='做单意愿 1 完全线上，2 线上为主线下为辅，3 线下为主线上为辅')
    remark = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='备注')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbUserTodo(db.Model):
    __tablename__ = 'tb_user_todo'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue())
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='类型1：面试申请(hd)2：到岗前一天(hd)3：面试当天(hd)4：新推荐候选人(hr)5：评估中候选人(hr)6：待定候选人(hr)7：面试后1天(hr)8：到岗后1天(hr)10：过保后1天(hr)11：当天有面试(hr)12：到岗前1天(hr)13：过保前一天(hr), 14:longList(适合职位的人才大范围), 15: shortList(适合此职位的候选人小范围)')
    candidate_id = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue(), info='候选人id')
    position_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='职位id')
    talent_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='人才id')
    description = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='描述')
    start_time = db.Column(db.DateTime, info='开始时间')
    end_time = db.Column(db.DateTime, info='结束时间')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info=' 状态 0：新建，1：已处理，2：已删除，3：自动删除')
    channel = db.Column(db.Integer, info='来源渠道')
    show_start_time = db.Column(db.DateTime, info='列表显示的开始时间')
    show_end_time = db.Column(db.DateTime, info='列表显示的结束时间')
    custom_task_object = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='自定义任务对象')
    source_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='数据来源类型')
    position_source_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='职位数据来源类型')



class TbUserWx(db.Model):
    __tablename__ = 'tb_user_wx'

    user_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    user_type = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue(), info='用户类型;1:HR;2:HD')
    wx_open_id = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='微信用户openID')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除,0:false,1:true')



class TbVipLevelConfig(db.Model):
    __tablename__ = 'tb_vip_level_config'

    vip_level = db.Column(db.Integer, primary_key=True, info='vip等级')
    user_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='用户类型 1:hr 2:hd 3:admin 4:渠道用户 5:求职者')
    min_value = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='区间最小值')
    max_value = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='区间最大值')
    remark = db.Column(db.String(200), nullable=False, info='备注信息')



class TbWeixinSendQueue(db.Model):
    __tablename__ = 'tb_weixin_send_queue'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    source_id = db.Column(db.String(128), index=True, info='源ID')
    send_type = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='发送类型')
    stage = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='队列阶段 0 初始 1:执行中 2:完成')
    defunct = db.Column(db.Integer, index=True, server_default=db.FetchedValue(), info='是否有效')
    update_user_id = db.Column(db.BigInteger, info='修改用户')
    update_time = db.Column(db.DateTime, info='修改时间')
    create_user_id = db.Column(db.BigInteger, info='创建用户')
    create_time = db.Column(db.DateTime, info='创建时间')



class TbWeixinUserInfo(db.Model):
    __tablename__ = 'tb_weixin_user_info'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    user_id = db.Column(db.BigInteger, info='用户id')
    open_id = db.Column(db.String(250), index=True, info='公众号openId')
    subscribe = db.Column(db.Integer)
    nickname = db.Column(db.String(100), info='用户昵称')
    sex_desc = db.Column(db.String(8), info='性别描述信息：男、女、未知等')
    sex = db.Column(db.Integer, info='性别表示：1，2等数字')
    language = db.Column(db.String(50), info='语言')
    city = db.Column(db.String(50), info='城市')
    province = db.Column(db.String(50), info='省份')
    country = db.Column(db.String(50), info='国家')
    headImg_url = db.Column(db.String(250), info='头像')
    subscribe_time = db.Column(db.BigInteger, info='订阅时间')
    union_id = db.Column(db.String(100))
    remark = db.Column(db.String(200), info='备注')
    group_id = db.Column(db.Integer)
    tag_ids = db.Column(db.String(200), info='以,分隔')
    privileges = db.Column(db.String(1000), info='用户特权信息,以,分隔')
    subscribe_scene = db.Column(db.String(50), info='用户关注的渠道来源')
    defunct = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='逻辑删除')
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue())



class TbWhiteListApplyRecord(db.Model):
    __tablename__ = 'tb_white_list_apply_record'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='用户编号')
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')



class TbYellowPage(db.Model):
    __tablename__ = 'tb_yellow_page'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    name = db.Column(db.String(300), nullable=False, info='名称')
    province_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='省ID')
    city_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='市ID')
    address = db.Column(db.String(500), info='地址')
    introduce = db.Column(db.String(2000), info='介绍')
    industry_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='行业ID')
    other_industry_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    scale = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    style = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    website = db.Column(db.String(200), info='网址')
    contact_name = db.Column(db.String(200), info='联系人')
    contact_email = db.Column(db.String(200), info='联系邮箱')
    contact_mobile = db.Column(db.String(200), info='联系电话')
    contact_gender = db.Column(db.Integer, info='性别')
    contact_phone = db.Column(db.String(200), info='联系手机')
    contact_qq = db.Column(db.String(200), info='qq')
    sales_admin = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='创建人')
    update_user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='修改人')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='修改时间')
    enterprise_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='企业id')



class Timepointer(db.Model):
    __tablename__ = 'timepointer'
    __table_args__ = (
        db.Index('idx_objId_objtype_submodel', 'objId', 'objType', 'subModel'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    objId = db.Column(db.BigInteger, info='对象ID')
    objType = db.Column(db.Integer, info='模块,0 candidate,1 interview, 2 request, 3 position,4 interview')
    comment = db.Column(db.String(100), info='补充说明')
    datetime = db.Column(db.DateTime, info='响应时间')
    userId = db.Column(db.BigInteger, info='执行人')
    oldStatus = db.Column(db.Integer, info='原来状态')
    newStatus = db.Column(db.Integer, info='现在状态')
    createTime = db.Column(db.DateTime, info='创建时间')
    subModel = db.Column(db.BigInteger)
    positionId = db.Column(db.BigInteger, index=True, info='职位ID')
    employerId = db.Column(db.BigInteger, info='雇主id')
    employerCompanyId = db.Column(db.BigInteger, info='企业ID')
    headhunterId = db.Column(db.BigInteger, info='猎头id')
    headhunterCompanyId = db.Column(db.BigInteger, info='猎企ID')
    candidateId = db.Column(db.BigInteger, index=True, info='候选人编号')
    end_time = db.Column(db.DateTime)
    content = db.Column(db.Text, info='内容')



class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    firstName = db.Column(db.String(200))
    lastName = db.Column(db.String(200))
    trueName = db.Column(db.String(200), info='真名（姓名）')
    displayName = db.Column(db.String(200), info='显示名')
    nickname = db.Column(db.String(30), info='昵称')
    email = db.Column(db.String(200), index=True, info='邮箱')
    password = db.Column(db.String(200), info='密码')
    companyId = db.Column(db.BigInteger, index=True, info='公司ID')
    userTitle = db.Column(db.String(200))
    Gender = db.Column(db.Integer, info='0：先生，1：女士')
    userType = db.Column(db.Integer, index=True, info='1：企业，2：猎头，3：管理员，4：渠道用户')
    phone = db.Column(db.String(200))
    altPhone = db.Column(db.String(200))
    cellPhone = db.Column(db.String(200), index=True)
    fax = db.Column(db.String(200))
    zipCode = db.Column(db.String(200))
    idType = db.Column(db.Integer, info='证件类型：1：身份证；2：其它')
    idNumber = db.Column(db.String(50))
    idVerification = db.Column(db.Integer, info='验证 0：未验证；1：以验证')
    certificateType = db.Column(db.Integer, info='猎头用户证书类型 0：无 1：中介员 2：中介师 ')
    certificateNumber = db.Column(db.String(200))
    certificateVerification = db.Column(db.Integer, info='证书验证 0：未验证；1：以验证')
    country = db.Column(db.String(200), info='国家')
    province = db.Column(db.String(100), info='省')
    city = db.Column(db.String(100), info='市')
    address = db.Column(db.String(200), info='地址')
    securityQuestion = db.Column(db.String(200), info='密码 安全问题')
    secuityAnswer = db.Column(db.String(200), info='密码 安全答案')
    registerIP = db.Column(db.String(200), info='注册ip')
    approveDate = db.Column(db.DateTime, info='审核时间')
    lastLogin = db.Column(db.DateTime, info='最后登陆时间')
    loginTimes = db.Column(db.Integer, info='登陆次数')
    rank = db.Column(db.Integer)
    referralCode = db.Column(db.String(8), info='用来推荐别人的号')
    referredBy = db.Column(db.BigInteger, info='注册时用的推荐号')
    keepConfidential = db.Column(db.Integer, info='0：公开 1：保密名字')
    selfIntroduction = db.Column(db.String(6000), info='自我介绍（猎头）')
    activeEngagements = db.Column(db.Integer, info='当前的活动（job）')
    engagementAbility = db.Column(db.Integer, info='engagement限制')
    status = db.Column(db.Integer, index=True, info='0：未审核 1：活动 2：不活动 3：删除（审核毙了）')
    approveUserId = db.Column(db.BigInteger, info='审核人')
    approveTime = db.Column(db.DateTime, info='审核时间')
    createUserId = db.Column(db.BigInteger, info='创建人')
    createTime = db.Column(db.DateTime, index=True, info='创建时间')
    updateUserId = db.Column(db.BigInteger, info='修改人')
    updateTime = db.Column(db.DateTime, server_default=db.FetchedValue(), info='更新时间')
    experiencedIndustry = db.Column(db.Integer)
    experiencedIndustry2 = db.Column(db.Integer)
    redirectLink = db.Column(db.String(50), info='登录后的跳转link')
    forwardToEmail = db.Column(db.Integer, info='是否转发到email，0：不转发 1：转发')
    isIndependent = db.Column(db.Integer, server_default=db.FetchedValue(), info='0： 独立猎头，1：非独立猎头')
    totalCandidate = db.Column(db.Integer, info='对应猎头用户表示：所有推荐的候选人总数;对于企业用户表示，所有收到的候选人总数;')
    interviewedCandidate = db.Column(db.Integer, info='对于猎头用户表示：所有推荐的候选人中被面试的总数;对于企业用户表示，所有收到的候选人中被面试的总数')
    totalPosition = db.Column(db.Integer, info='对应企业用户是发布职位总数;对于猎头用户是完成职位总数')
    headhunterShare = db.Column(db.Float(asdecimal=True))
    epAgentShare = db.Column(db.Float(asdecimal=True))
    hhAgentShare = db.Column(db.Float(asdecimal=True))
    role = db.Column(db.Integer)
    remark = db.Column(db.String(1000))
    isShow = db.Column(db.String(200), info='按顺序0 姓名,1 电话, 2 Email, 3 公司名称, 4 公司简介')
    experience = db.Column(db.Integer, info='0,小于1年; 1,1-2年; 2,2-3年; 3,3-4年; 4,4-5年; 5,5年以上')
    hhTitle = db.Column(db.Integer, info='0,Researcher; 1,Assistant consultent; 2,Consultant; 3,Senior consultant')
    reportTo = db.Column(db.BigInteger)
    hastenCandidateTime = db.Column(db.Integer, server_default=db.FetchedValue(), info='系统通知HR催促处理候选人次数')
    assignedPosition = db.Column(db.Integer, info='企业用户负责职位数')
    showPublicPosition = db.Column(db.Integer, info='0,看不到公共职位; 1,可以看到')
    showHRContact = db.Column(db.Integer, info='0,看不到HR联系方法; 1,可以看到')
    canSubmitCandidate = db.Column(db.Integer, info='0,不能直接推荐候选人; 1,可以直接推荐')
    canAssignPosition = db.Column(db.Integer, info='0,不能分配职位给其他猎头; 1,可以分配')
    acceptRecommondPosition = db.Column(db.Integer, info='0,不接收推荐职位; 1,接收推荐职位')
    msnqq = db.Column(db.String(100), info='在线联系方式')
    forwhere = db.Column(db.Integer, info='用户从哪里注册 0自己注册，1平台用户推荐，2自己开发，3客户邀请签约猎头')
    showReward = db.Column(db.Integer, info='是否可见职位佣金')
    root = db.Column(db.Integer, info='0为root,1为branch')
    purview = db.Column(db.String(100), info='用户权限')
    bank = db.Column(db.String(50), info='开户银行')
    account = db.Column(db.String(50), info='银行账户名')
    accountNumber = db.Column(db.String(50), info='银行账号')
    integral = db.Column(db.Integer, info='社区积分')
    msn = db.Column(db.String(50), info='MSN')
    qq = db.Column(db.String(200), info='QQ')
    otherEmail = db.Column(db.String(50), info='其他邮箱')
    otherPhone = db.Column(db.String(50), info='备用电话')
    kind = db.Column(db.Integer, info='0,客服；1,销售')
    shortName = db.Column(db.String(30), info='系统设置')
    userGroup = db.Column(db.Integer, info='用户组')
    weibo = db.Column(db.String(30), info='微薄帐号')
    headhunterExperience = db.Column(db.Integer, info='猎头经验（与工作经验一样）')
    candidateSource = db.Column(db.String(100), info='候选人所在资源所在城市（文本）')
    sohoHelp = db.Column(db.String(1000), info='需要悬赏聘提供额外帮助（json ）')
    successfulCase = db.Column(db.String(2000), info='成功案例')
    otherExperiencedIndustry = db.Column(db.String(20), info='其他行业（行业选项里没有的）')
    totalSecondInterview = db.Column(db.Integer, info='二面数')
    totalInterview = db.Column(db.Integer, info='二面数')
    totalRequest = db.Column(db.Integer, info='企业 : 当前申请数；猎头：当前申请数')
    totalCollectionPosition = db.Column(db.Integer, info='企业 : 发布的职位被猎头关注数; 猎头：当前关注职位数')
    totalAssignPosition = db.Column(db.Integer, info='企业 : 发布的职位被猎头关注数; 猎头：当前关注职位数')
    totalPlacement = db.Column(db.Integer, info='成单数')
    totalOpenPosition = db.Column(db.Integer, info='开放中职位')
    avatar = db.Column(db.String(200), info='头像')
    avatar_verify = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='头像审核，0：头像未审核或者审核中；1：头像已审核通过；2；头像审核未通过')
    isNoticeMessageForMobile = db.Column(db.Integer, server_default=db.FetchedValue(), info='手机端是否推送消息设置 0，不推送，1推送')
    isCallPhoneForMobile = db.Column(db.Integer, server_default=db.FetchedValue(), info='是否可以直接按人名子拨打电话,0不可以，1可以')
    iphoneToken = db.Column(db.String(200), info='iphone 手机推送TOKEN')
    idcard_image_url = db.Column(db.String(100))
    head_image_url = db.Column(db.String(40))
    big_shot_apply_status = db.Column(db.Integer)
    weixin = db.Column(db.String(50))
    personalCompanyId = db.Column(db.BigInteger)
    secret = db.Column(db.String(100))
    badges = db.Column(db.String(100))
    companyName = db.Column(db.String(100))
    provinceId = db.Column(db.Integer)
    cityId = db.Column(db.Integer)
    permissionStatus = db.Column(db.String(10))
    rejectReason = db.Column(db.String(1000))
    total_score = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎头总分')
    idcard_image_url_back = db.Column(db.String(100), info='证件照背面')
    experiencedFunctions = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='擅长职能')
    experienced_areas = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='擅长地区')
    experienced_annual_salary = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='擅长年薪')
    experienced_industrys = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='擅长行业')
    begin_work_year = db.Column(db.SmallInteger, info='开始工作年份')
    receive_jobhunter = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否接受人才消息   0：不接收  1：接收')
    experienced_position_titles = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='擅长职位')
    experienced_develops = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='擅长发展阶段')
    experienced_domains = db.Column(db.String(400), nullable=False, server_default=db.FetchedValue(), info='擅长领域')
    experienced_position_level = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='擅长职位等级')
    talent_distribution = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='人才分布')
    settings_steps = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='设置步数')
    title_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='头衔;1:寻访员（R）,2:助理顾问（AC）,3:顾问（C）,4:资深顾问（SC）,5:合伙人 ,6:兼职猎头,7:其他')
    reject_time = db.Column(db.DateTime, info='拒绝时间')
    apply_reason = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='提交认证申请理由')
    service_admin = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='客服id')
    confine_start_time = db.Column(db.DateTime, info='关小黑屋的开始执行时间')
    confine_end_time = db.Column(db.DateTime, info='关小黑屋的结束时间时间，永久在当前时间基础上加60年')
    recommend_limit = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='猎头每日推荐量限制，默认值0为不限')
    verified_title = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='头衔是否已被猎上审核')
    need_check_recommend = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='推荐是否需要猎上审核')
    will_operate_industrys = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='意愿操作行业')
    will_operate_position_titles = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='意愿操作职能')
    work_will = db.Column(db.String(2000), nullable=False, server_default=db.FetchedValue(), info='做单意愿')
    surveyed = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='猎头是否被调研过')
    soho_recommended = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='猎头是否以soho身份做过单；0：未做过；1：做过')
    vip_level = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='vip等级 0:vip0; 1:vip1; 2:vip2; 3:vip3; 4:vip4; 5:vip5; 6:vip6; ')
    submit_verify_time = db.Column(db.DateTime, info='提交Soho认证时间')
    single_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='做单类型；1:Soho;2:公司root;3:加入公司')
    single_verify_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='做单认证状态；0:审核中;1:审核通过;2:审核拒绝3:离职')
    company_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='公司状态')
    customer_service_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='客服ID')
    invalid_register_reason = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='无效注册原因')
    single_verify_operate_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='做单审核操作人')
    single_verify_time = db.Column(db.DateTime, info='做单审核时间')
    rejected_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0：正常；打回类型 1：审核通过前打回；2：审核通过后打回')
    bdh_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='bdh id')
    contend_jobhunter_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='猎头抢单数量，每推荐一个c端人才就会清0')
    register_setting_steps = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='注册流程完成情况')
    inner_level_code = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='内部级别')



t_user_20180131 = db.Table(
    'user_20180131',
    db.Column('id', db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='主键ID'),
    db.Column('firstName', db.String(200)),
    db.Column('lastName', db.String(200)),
    db.Column('trueName', db.String(200), info='真名（姓名）'),
    db.Column('displayName', db.String(200), info='显示名'),
    db.Column('email', db.String(200), info='邮箱'),
    db.Column('password', db.String(200), info='密码'),
    db.Column('companyId', db.BigInteger, info='公司ID'),
    db.Column('userTitle', db.String(200)),
    db.Column('Gender', db.Integer, info='0：先生，1：女士'),
    db.Column('userType', db.Integer, info='1：企业，2：猎头，3：管理员，4：渠道用户'),
    db.Column('phone', db.String(200)),
    db.Column('altPhone', db.String(200)),
    db.Column('cellPhone', db.String(200)),
    db.Column('fax', db.String(200)),
    db.Column('zipCode', db.String(200)),
    db.Column('idType', db.Integer, info='证件类型：1：身份证；2：其它'),
    db.Column('idNumber', db.String(50)),
    db.Column('idVerification', db.Integer, info='验证 0：未验证；1：以验证'),
    db.Column('certificateType', db.Integer, info='猎头用户证书类型 0：无 1：中介员 2：中介师 '),
    db.Column('certificateNumber', db.String(200)),
    db.Column('certificateVerification', db.Integer, info='证书验证 0：未验证；1：以验证'),
    db.Column('country', db.String(200), info='国家'),
    db.Column('province', db.String(100), info='省'),
    db.Column('city', db.String(100), info='市'),
    db.Column('address', db.String(200), info='地址'),
    db.Column('securityQuestion', db.String(200), info='密码 安全问题'),
    db.Column('secuityAnswer', db.String(200), info='密码 安全答案'),
    db.Column('registerIP', db.String(200), info='注册ip'),
    db.Column('approveDate', db.DateTime, info='审核时间'),
    db.Column('lastLogin', db.DateTime, info='最后登陆时间'),
    db.Column('loginTimes', db.Integer, info='登陆次数'),
    db.Column('rank', db.Integer),
    db.Column('referralCode', db.String(8), info='用来推荐别人的号'),
    db.Column('referredBy', db.BigInteger, info='注册时用的推荐号'),
    db.Column('keepConfidential', db.Integer, info='0：公开 1：保密名字'),
    db.Column('selfIntroduction', db.String(6000), info='自我介绍（猎头）'),
    db.Column('activeEngagements', db.Integer, info='当前的活动（job）'),
    db.Column('engagementAbility', db.Integer, info='engagement限制'),
    db.Column('status', db.Integer, info='0：未审核 1：活动 2：不活动 3：删除（审核毙了）'),
    db.Column('approveUserId', db.BigInteger, info='审核人'),
    db.Column('approveTime', db.DateTime, info='审核时间'),
    db.Column('createUserId', db.BigInteger, info='创建人'),
    db.Column('createTime', db.DateTime, info='创建时间'),
    db.Column('updateUserId', db.BigInteger, info='修改人'),
    db.Column('updateTime', db.DateTime, server_default=db.FetchedValue(), info='更新时间'),
    db.Column('experiencedIndustry', db.Integer),
    db.Column('experiencedIndustry2', db.Integer),
    db.Column('redirectLink', db.String(50), info='登录后的跳转link'),
    db.Column('forwardToEmail', db.Integer, info='是否转发到email，0：不转发 1：转发'),
    db.Column('isIndependent', db.Integer, server_default=db.FetchedValue(), info='0： 独立猎头，1：非独立猎头'),
    db.Column('totalCandidate', db.Integer, info='对应猎头用户表示：所有推荐的候选人总数;对于企业用户表示，所有收到的候选人总数;'),
    db.Column('interviewedCandidate', db.Integer, info='对于猎头用户表示：所有推荐的候选人中被面试的总数;对于企业用户表示，所有收到的候选人中被面试的总数'),
    db.Column('totalPosition', db.Integer, info='对应企业用户是发布职位总数;对于猎头用户是完成职位总数'),
    db.Column('headhunterShare', db.Float(asdecimal=True)),
    db.Column('epAgentShare', db.Float(asdecimal=True)),
    db.Column('hhAgentShare', db.Float(asdecimal=True)),
    db.Column('role', db.Integer),
    db.Column('remark', db.String(1000)),
    db.Column('isShow', db.String(200), info='按顺序0 姓名,1 电话, 2 Email, 3 公司名称, 4 公司简介'),
    db.Column('experience', db.Integer, info='0,小于1年; 1,1-2年; 2,2-3年; 3,3-4年; 4,4-5年; 5,5年以上'),
    db.Column('hhTitle', db.Integer, info='0,Researcher; 1,Assistant consultent; 2,Consultant; 3,Senior consultant'),
    db.Column('reportTo', db.BigInteger),
    db.Column('hastenCandidateTime', db.Integer, server_default=db.FetchedValue(), info='系统通知HR催促处理候选人次数'),
    db.Column('assignedPosition', db.Integer, info='企业用户负责职位数'),
    db.Column('showPublicPosition', db.Integer, info='0,看不到公共职位; 1,可以看到'),
    db.Column('showHRContact', db.Integer, info='0,看不到HR联系方法; 1,可以看到'),
    db.Column('canSubmitCandidate', db.Integer, info='0,不能直接推荐候选人; 1,可以直接推荐'),
    db.Column('canAssignPosition', db.Integer, info='0,不能分配职位给其他猎头; 1,可以分配'),
    db.Column('acceptRecommondPosition', db.Integer, info='0,不接收推荐职位; 1,接收推荐职位'),
    db.Column('msnqq', db.String(100), info='在线联系方式'),
    db.Column('forwhere', db.Integer, info='用户从哪里注册 0自己注册，1平台用户推荐，2自己开发，3客户邀请签约猎头'),
    db.Column('showReward', db.Integer, info='是否可见职位佣金'),
    db.Column('root', db.Integer, info='0为root,1为branch'),
    db.Column('purview', db.String(100), info='用户权限'),
    db.Column('bank', db.String(50), info='开户银行'),
    db.Column('account', db.String(50), info='银行账户名'),
    db.Column('accountNumber', db.String(50), info='银行账号'),
    db.Column('integral', db.Integer, info='社区积分'),
    db.Column('msn', db.String(50), info='MSN'),
    db.Column('qq', db.String(200), info='QQ'),
    db.Column('otherEmail', db.String(50), info='其他邮箱'),
    db.Column('otherPhone', db.String(50), info='备用电话'),
    db.Column('kind', db.Integer, info='0,客服；1,销售'),
    db.Column('shortName', db.String(30), info='系统设置'),
    db.Column('userGroup', db.Integer, info='用户组'),
    db.Column('weibo', db.String(30), info='微薄帐号'),
    db.Column('headhunterExperience', db.Integer, info='猎头经验（与工作经验一样）'),
    db.Column('candidateSource', db.String(100), info='候选人所在资源所在城市（文本）'),
    db.Column('sohoHelp', db.String(1000), info='需要悬赏聘提供额外帮助（json ）'),
    db.Column('successfulCase', db.String(2000), info='成功案例'),
    db.Column('otherExperiencedIndustry', db.String(20), info='其他行业（行业选项里没有的）'),
    db.Column('totalSecondInterview', db.Integer, info='二面数'),
    db.Column('totalInterview', db.Integer, info='二面数'),
    db.Column('totalRequest', db.Integer, info='企业 : 当前申请数；猎头：当前申请数'),
    db.Column('totalCollectionPosition', db.Integer, info='企业 : 发布的职位被猎头关注数; 猎头：当前关注职位数'),
    db.Column('totalAssignPosition', db.Integer, info='企业 : 发布的职位被猎头关注数; 猎头：当前关注职位数'),
    db.Column('totalPlacement', db.Integer, info='成单数'),
    db.Column('totalOpenPosition', db.Integer, info='开放中职位'),
    db.Column('avatar', db.String(200), info='头像'),
    db.Column('avatar_verify', db.Integer, nullable=False, server_default=db.FetchedValue(), info='头像审核，0：头像未审核或者审核中；1：头像已审核通过；2；头像审核未通过'),
    db.Column('isNoticeMessageForMobile', db.Integer, server_default=db.FetchedValue(), info='手机端是否推送消息设置 0，不推送，1推送'),
    db.Column('isCallPhoneForMobile', db.Integer, server_default=db.FetchedValue(), info='是否可以直接按人名子拨打电话,0不可以，1可以'),
    db.Column('iphoneToken', db.String(200), info='iphone 手机推送TOKEN'),
    db.Column('idcard_image_url', db.String(100)),
    db.Column('head_image_url', db.String(40)),
    db.Column('big_shot_apply_status', db.Integer),
    db.Column('weixin', db.String(50)),
    db.Column('personalCompanyId', db.BigInteger),
    db.Column('secret', db.String(100)),
    db.Column('badges', db.String(100)),
    db.Column('companyName', db.String(100)),
    db.Column('provinceId', db.Integer),
    db.Column('cityId', db.Integer),
    db.Column('permissionStatus', db.String(10)),
    db.Column('rejectReason', db.String(1000)),
    db.Column('total_score', db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='猎头总分'),
    db.Column('idcard_image_url_back', db.String(100), info='证件照背面'),
    db.Column('experiencedFunctions', db.String(200), nullable=False, server_default=db.FetchedValue(), info='擅长职能'),
    db.Column('experienced_areas', db.String(200), nullable=False, server_default=db.FetchedValue(), info='擅长地区'),
    db.Column('experienced_annual_salary', db.String(200), nullable=False, server_default=db.FetchedValue(), info='擅长年薪'),
    db.Column('experienced_industrys', db.String(200), nullable=False, server_default=db.FetchedValue(), info='擅长行业'),
    db.Column('begin_work_year', db.SmallInteger, info='开始工作年份'),
    db.Column('receive_jobhunter', db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否接受人才消息   0：不接收  1：接收'),
    db.Column('experienced_position_titles', db.String(200), nullable=False, server_default=db.FetchedValue(), info='擅长职位'),
    db.Column('experienced_develops', db.String(100), nullable=False, server_default=db.FetchedValue(), info='擅长发展阶段'),
    db.Column('experienced_domains', db.String(400), nullable=False, server_default=db.FetchedValue(), info='擅长领域'),
    db.Column('experienced_position_level', db.Integer, nullable=False, server_default=db.FetchedValue(), info='擅长职位等级'),
    db.Column('talent_distribution', db.String(50), nullable=False, server_default=db.FetchedValue(), info='人才分布'),
    db.Column('settings_steps', db.Integer, nullable=False, server_default=db.FetchedValue(), info='设置步数'),
    db.Column('title_id', db.Integer, nullable=False, server_default=db.FetchedValue(), info='头衔;1:寻访员（R）,2:助理顾问（AC）,3:顾问（C）,4:资深顾问（SC）,5:合伙人 ,6:兼职猎头,7:其他'),
    db.Column('reject_time', db.DateTime, info='拒绝时间'),
    db.Column('apply_reason', db.String(200), nullable=False, server_default=db.FetchedValue(), info='提交认证申请理由'),
    db.Column('service_admin', db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='客服id'),
    db.Column('confine_start_time', db.DateTime, info='关小黑屋的开始执行时间'),
    db.Column('confine_end_time', db.DateTime, info='关小黑屋的结束时间时间，永久在当前时间基础上加60年'),
    db.Column('recommend_limit', db.Integer, nullable=False, server_default=db.FetchedValue(), info='猎头每日推荐量限制，默认值0为不限'),
    db.Column('verified_title', db.Integer, nullable=False, server_default=db.FetchedValue(), info='头衔是否已被猎上审核'),
    db.Column('need_check_recommend', db.Integer, nullable=False, server_default=db.FetchedValue(), info='推荐是否需要猎上审核'),
    db.Column('will_operate_industrys', db.String(200), nullable=False, server_default=db.FetchedValue(), info='意愿操作行业'),
    db.Column('will_operate_position_titles', db.String(200), nullable=False, server_default=db.FetchedValue(), info='意愿操作职能'),
    db.Column('work_will', db.String(2000), nullable=False, server_default=db.FetchedValue(), info='做单意愿'),
    db.Column('surveyed', db.Integer, nullable=False, server_default=db.FetchedValue(), info='猎头是否被调研过'),
    db.Column('soho_recommended', db.Integer, nullable=False, server_default=db.FetchedValue(), info='猎头是否以soho身份做过单；0：未做过；1：做过'),
    db.Column('vip_level', db.Integer, nullable=False, server_default=db.FetchedValue(), info='vip等级 0:vip0; 1:vip1; 2:vip2; 3:vip3; 4:vip4; 5:vip5; 6:vip6; '),
    db.Column('submit_verify_time', db.DateTime, info='提交Soho认证时间'),
    db.Column('single_type', db.Integer, nullable=False, server_default=db.FetchedValue(), info='做单类型；1:Soho;2:公司root;3:加入公司'),
    db.Column('single_verify_status', db.Integer, nullable=False, server_default=db.FetchedValue(), info='做单认证状态；0:审核中;1:审核通过;2:审核拒绝3:离职'),
    db.Column('company_status', db.Integer, nullable=False, server_default=db.FetchedValue(), info='公司状态'),
    db.Column('customer_service_id', db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='客服ID'),
    db.Column('invalid_register_reason', db.String(200), nullable=False, server_default=db.FetchedValue(), info='无效注册原因'),
    db.Column('single_verify_operate_id', db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='做单审核操作人'),
    db.Column('single_verify_time', db.DateTime, info='做单审核时间'),
    db.Column('rejected_type', db.Integer, nullable=False, server_default=db.FetchedValue(), info='0：正常；打回类型 1：审核通过前打回；2：审核通过后打回'),
    db.Column('bdh_id', db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='bdh id'),
    db.Column('contend_jobhunter_count', db.Integer, nullable=False, server_default=db.FetchedValue(), info='猎头抢单数量，每推荐一个c端人才就会清0'),
    db.Column('register_setting_steps', db.Integer, nullable=False, server_default=db.FetchedValue(), info='注册流程完成情况'),
    db.Column('inner_level_code', db.Integer, nullable=False, server_default=db.FetchedValue(), info='内部级别')
)



t_view1 = db.Table(
    'view1',
    db.Column('id', db.BigInteger),
    db.Column('position_id', db.BigInteger, server_default=db.FetchedValue()),
    db.Column('candidate_id', db.BigInteger, server_default=db.FetchedValue()),
    db.Column('hunter_id', db.BigInteger, server_default=db.FetchedValue()),
    db.Column('talent_id', db.BigInteger, server_default=db.FetchedValue()),
    db.Column('status', db.Integer, server_default=db.FetchedValue()),
    db.Column('fail_status', db.Integer, server_default=db.FetchedValue()),
    db.Column('fail_time', db.DateTime),
    db.Column('expire_time', db.DateTime),
    db.Column('undetermined_time', db.DateTime),
    db.Column('dispatch_time', db.DateTime),
    db.Column('reject_type', db.Integer),
    db.Column('reject_user_id', db.BigInteger, server_default=db.FetchedValue()),
    db.Column('reject_reason', db.String(200)),
    db.Column('reject_reason_expend', db.String(200)),
    db.Column('defunct', db.Integer, server_default=db.FetchedValue()),
    db.Column('create_user_id', db.BigInteger, server_default=db.FetchedValue()),
    db.Column('update_user_id', db.BigInteger, server_default=db.FetchedValue()),
    db.Column('create_time', db.DateTime),
    db.Column('update_time', db.DateTime)
)



class WorksheetDatum(db.Model):
    __tablename__ = 'worksheet_data'

    id = db.Column(db.BigInteger, primary_key=True)
    sheet_id = db.Column(db.BigInteger, nullable=False, index=True, info='工单数据关联的工单主表主键')
    old_json = db.Column(db.String(2013), info='工单修改之前数据')
    new_json = db.Column(db.String(2013), info='工单修改之后的数据')
    modify_status = db.Column(db.Integer, info='数据修改状态；0：未修改；1：已修改')
    modify_time = db.Column(db.DateTime, info='修改时间')
    defunct = db.Column(db.Integer)
    create_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)
    update_user_id = db.Column(db.BigInteger)
    update_time = db.Column(db.DateTime)



class WorksheetInfo(db.Model):
    __tablename__ = 'worksheet_info'

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, nullable=False, index=True)
    user_role_code = db.Column(db.Integer, nullable=False)
    user_info_id = db.Column(db.BigInteger, nullable=False)
    user_type = db.Column(db.Integer, info='用户类型')
    description = db.Column(db.String(511), info='工单描述')
    sheet_type = db.Column(db.Integer, nullable=False, info='工单类型')
    target_type = db.Column(db.Integer, info='关联数据类型，工单必须关联数据')
    target_id = db.Column(db.BigInteger, info='关联的数据主键')
    audit_user_id = db.Column(db.BigInteger, info='审核人')
    audit_time = db.Column(db.DateTime, info='审核时间')
    complete_time = db.Column(db.DateTime, info='完成时间')
    status = db.Column(db.Integer, info='工单状态；1：新建待审；2：审核通过；3：审核不通过；4：完成')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger, nullable=False)
    update_user_id = db.Column(db.BigInteger, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)



class WorksheetNotice(db.Model):
    __tablename__ = 'worksheet_notice'
    __table_args__ = (
        db.Index('idx_user_id_process_status', 'user_id', 'process_status'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    sheet_id = db.Column(db.BigInteger, nullable=False, index=True, info='通知关联的工单；一个工单可以通知多个人，会有多个通知单')
    user_id = db.Column(db.BigInteger, nullable=False, info='通知对应的用户角色ID')
    user_role_code = db.Column(db.Integer, nullable=False, info='用户角色')
    user_info_id = db.Column(db.BigInteger, nullable=False, info='用户信息ID')
    user_type = db.Column(db.Integer)
    notice_time = db.Column(db.DateTime, nullable=False, info='通知时间')
    finish_time = db.Column(db.DateTime, info='完成时间')
    process_status = db.Column(db.Integer, nullable=False, info='处理状态；0：未处理；1：已处理')
    read_status = db.Column(db.Integer, nullable=False, info='是否已读；0：未读；1已读')
    read_time = db.Column(db.DateTime, info='已读时间，查看详情')
    defunct = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    create_user_id = db.Column(db.BigInteger)
    update_user_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)

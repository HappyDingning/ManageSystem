from django.db import models
from django.contrib.auth.models import AbstractUser


class Login_Info(AbstractUser):
    is_teacher_choices = [('0', '否'), ('1', '是')]
    """
    用户信息表
    """
    is_teacher = models.CharField(max_length=2, default='1', null=False, verbose_name='是否是教职工', choices = is_teacher_choices)

    class Meta(object):
        db_table = 'Login_Info'
        verbose_name = '用户表'

    def __str__(self):
        return self.username


# 教职工信息
class StaffInfo(models.Model):
    staffID = models.CharField(max_length=11, primary_key=True, verbose_name='教职工工号')
    staffName = models.CharField(max_length=26, verbose_name='教职工姓名')
    staffNumber = models.CharField(max_length=12, verbose_name='教职工电话')

    class Meta(object):
        db_table = 'StaffInfo'
        verbose_name = '教职工表'

    def __str__(self):
        return self.staffName


# 本科生信息
class UndergraduateInfo(models.Model):
    gender_choices = [('0', '男'),
                      ('1', '女')]

    political_choices = [('1', '中共党员'), ('2', '中共预备党员'), ('3', '共青团员'), ('4', '民革党员'),
                         ('5', '民盟盟员'), ('6', '民建会员'), ('7', '民进会员'), ('8', '农工党党员'),
                         ('9', '致公党党员'), ('10', '九三学社社员'), ('11', '台盟盟员'),
                         ('12', '无党派人士'), ('13', '群众')]

    studentID = models.CharField(max_length=11, primary_key=True, verbose_name='学号')
    studentName = models.CharField(max_length=26, verbose_name='学生姓名')
    gender = models.CharField(max_length=2, choices=gender_choices, verbose_name='性别')
    enrollmentYear = models.IntegerField(verbose_name='入学年份')
    specialty = models.CharField(max_length=41, verbose_name='专业')
    studentClass = models.CharField(max_length=16, null=True, blank=True, verbose_name='班级', default='无')
    mobileNumber = models.CharField(max_length=12, verbose_name='手机号')
    qqNumber = models.CharField(max_length=12, verbose_name='qq号')
    politicalStatus = models.CharField(max_length=3, choices=political_choices, verbose_name='政治面貌')
    instructor = models.CharField(max_length=11, verbose_name='辅导员工号')
    position = models.CharField(max_length=21, null=True, blank=True, verbose_name='职务')

    class Meta(object):
        db_table = 'UndergraduateInfo'
        verbose_name = '本科生基础信息'

    def __str__(self):
        return self.studentName


# 本科生其它信息
class UndergraduateOtherInfo(models.Model):
    nation_choices = [('0', '汉族'), ('1', '壮族'), ('2', '满族'), ('3', '回族'), ('4', '苗族'), ('5', '维吾尔族'),
                      ('6', '土家族'), ('7', '彝族'), ('8', '蒙古族'), ('9', '藏族'), ('10', '布依族'), ('11', '侗族'),
                      ('12', '瑶族'), ('13', '朝鲜族'), ('14', '白族'), ('15', '哈尼族'), ('16', '哈萨克族'),
                      ('17', '黎族'), ('18', '傣族'), ('19', '畲族'), ('20', '傈僳族'), ('21', '仡佬族'),
                      ('22', '东乡族'), ('23', '高山族'), ('24', '拉祜族'), ('25', '水族'), ('26', '佤族'),
                      ('27', '纳西族'), ('28', '羌族'), ('29', '土族'), ('30', '仫佬族'), ('31', '锡伯族'),
                      ('32', '柯尔克孜族'), ('33', '达斡尔族'), ('34', '景颇族'), ('35', '毛南族'), ('36', '撒拉族'),
                      ('37', '布朗族'), ('38', '塔吉克族'), ('39', '阿昌族'), ('40', '普米族'), ('41', '鄂温克族'),
                      ('42', '怒族'), ('43', '京族'), ('44', '基诺族'), ('45', '德昂族'), ('46', '保安族'),
                      ('47', '俄罗斯族'), ('48', '裕固族'), ('49', '乌孜别克族'), ('50', '门巴族'), ('51', '鄂伦春族'),
                      ('52', '独龙族'), ('53', '塔塔尔族'), ('54', '赫哲族'), ('55', '珞巴族')]

    religion_choices = [('0', '否'), ('1', '是')]

    RR_choices = [('0', '农村'), ('1', '城市')]

    healthy_choices = [('0', '健康'), ('1', '良好'), ('2', '及格'), ('3', '不及格'), ('4', '优秀')]

    birthday = models.DateField(verbose_name='出生日期')
    nation = models.CharField(max_length=3, choices=nation_choices, verbose_name='民族',default="汉族")
    isReligious = models.CharField(max_length=2, choices=religion_choices, verbose_name='是否信仰宗教', default=0)
    religion = models.CharField(max_length=21, verbose_name='信仰宗教')
    dormitoryBuilding = models.CharField(max_length=3, verbose_name='宿舍楼号')
    dormitory = models.CharField(max_length=4, verbose_name='宿舍号')
    province = models.CharField(max_length=11, verbose_name='家庭所在省/自治区')
    city = models.CharField(max_length=21, verbose_name='家庭所在市')
    county = models.CharField(max_length=21, verbose_name='家庭所在县/区')
    address = models.CharField(max_length=81, verbose_name='家庭详细地址')
    registeredResidence = models.CharField(max_length=2, choices=RR_choices, verbose_name='户口性质')
    fName = models.CharField(max_length=26, verbose_name='父亲姓名')
    fWork = models.CharField(max_length=26, verbose_name='父亲工作', default='无')
    fMobileNumber = models.CharField(max_length=11, verbose_name='父亲电话')
    mName = models.CharField(max_length=26, verbose_name='母亲姓名')
    mWork = models.CharField(max_length=26, verbose_name='母亲工作', default='无')
    mMobileNumber = models.CharField(max_length=12, verbose_name='母亲电话')
    gName = models.CharField(max_length=26, verbose_name='监护人姓名')
    gMobileNumber = models.CharField(max_length=12, verbose_name='监护人电话')
    gkChinese = models.IntegerField(verbose_name='语文成绩')
    gkMath = models.IntegerField(verbose_name='数学成绩')
    gkEnglish = models.IntegerField(verbose_name='英语成绩')
    gkScience = models.IntegerField(verbose_name='理综成绩')
    healthy = models.CharField(max_length=2, choices=healthy_choices, verbose_name='健康情况')
    postalCode = models.CharField(max_length=7, verbose_name='邮政编码')
    baseInfo = models.OneToOneField(UndergraduateInfo, on_delete=models.CASCADE, related_name='BUstudentInfo', verbose_name='学生')

    class Meta(object):
        db_table = 'UndergraduateOtherInfo'
        verbose_name = '本科生其它信息'


# 课程对应表
class CourseInfo(models.Model):
    type_choices = [('0', '通识必修'), ('1', '专业选修'), ('2', '学科选修'), ('3', '实践环节'),
                    ('4', '选修')]

    courseID = models.CharField(max_length=9, primary_key=True, verbose_name='课程号')
    courseSeq = models.CharField(max_length=6, verbose_name='课序号')
    courseName = models.CharField(max_length=41, verbose_name='课程名')
    credit = models.FloatField(verbose_name='学分')
    courseType = models.CharField(max_length=2, choices=type_choices, verbose_name='课程属性')

    class Meta(object):
        db_table = 'CourseInfo'
        verbose_name = '课程对应表'

    def __str__(self):
        return self.courseName, self.credit


# 活动对应表
class ActivityInfo(models.Model):
    activityID = models.AutoField(primary_key=True, verbose_name='活动id')
    activityName = models.CharField(max_length=61, verbose_name='活动名')

    class Meta(object):
        db_table = 'ActivityInfo'
        verbose_name = '活动对应表'

    def __str__(self):
        return self.activityName


# 本科生成绩
class UndergraduateClassScore(models.Model):
    study_choice = [('0','正常'), ('1', '重修'), ('2', '补考')]

    # 学生删除后，词条消息删除
    Ustudent = models.ForeignKey(UndergraduateInfo, on_delete=models.CASCADE, related_name='UstudentInfo', verbose_name='学生')
    # 课程删除后此处依旧保留信息
    course = models.ForeignKey(CourseInfo, on_delete=models.DO_NOTHING, related_name='courseInfo', verbose_name='课程')
    score = models.IntegerField(verbose_name='成绩')
    examTime = models.DateField(verbose_name='日期')
    teacherID = models.CharField(max_length=11, null=True, blank=True, verbose_name='教师工号')
    studyMode = models.CharField(max_length=2, choices=study_choice, verbose_name='课程属性')

    class Meta(object):
        db_table = 'UndergraduateClassScore'
        verbose_name = '本科生成绩'

    def __str__(self):
        return self.score


# 本科生志愿活动
class VolunteerService(models.Model):
    Vstudent = models.ForeignKey(UndergraduateInfo, on_delete=models.CASCADE, related_name='VstudentInfo', verbose_name='学生')
    activity = models.ForeignKey(UndergraduateInfo, on_delete=models.CASCADE, related_name='activityInfo', verbose_name='活动')
    duration = models.IntegerField(null=True, blank=True, verbose_name='时长')

    class Meta(object):
        db_table = 'VolunteerService'
        verbose_name = '本科生活动时长'

    def __str__(self):
        return self.duration


# 考勤情况
class AttendenceInfo(models.Model):
    attend_choice = [('0', '全勤'), ('1', '旷课'), ('2', '迟到'), ('3', '请假'),
                     ('4', '早退')]

    Astudent = models.ForeignKey(UndergraduateInfo, on_delete=models.CASCADE, related_name='AstudentInfo', verbose_name='学生')
    date = models.DateField(verbose_name='日期')
    period = models.IntegerField(verbose_name='节次')
    attendence = models.CharField(max_length=2, choices=attend_choice, verbose_name='出勤情况')

    class Meta(object):
        db_table = 'AttendenceInfo'
        verbose_name = '考勤情况'

    def __str__(self):
        return self.period, self.attendence















# Generated by Django 2.2.7 on 2020-08-12 03:10

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityInfo',
            fields=[
                ('activityID', models.AutoField(primary_key=True, serialize=False, verbose_name='活动id')),
                ('activityName', models.CharField(max_length=61, verbose_name='活动名')),
            ],
            options={
                'verbose_name': '活动对应表',
                'db_table': 'ActivityInfo',
            },
        ),
        migrations.CreateModel(
            name='CourseInfo',
            fields=[
                ('courseID', models.CharField(max_length=9, primary_key=True, serialize=False, verbose_name='课程号')),
                ('courseSeq', models.CharField(max_length=6, verbose_name='课序号')),
                ('courseName', models.CharField(max_length=41, verbose_name='课程名')),
                ('credit', models.FloatField(verbose_name='学分')),
                ('courseType', models.CharField(choices=[('0', '通识必修'), ('1', '专业选修'), ('2', '学科选修'), ('3', '实践环节'), ('4', '选修')], max_length=2, verbose_name='课程属性')),
            ],
            options={
                'verbose_name': '课程对应表',
                'db_table': 'CourseInfo',
            },
        ),
        migrations.CreateModel(
            name='StaffInfo',
            fields=[
                ('staffID', models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='教职工工号')),
                ('staffName', models.CharField(max_length=26, verbose_name='教职工姓名')),
                ('staffNumber', models.CharField(max_length=12, verbose_name='教职工电话')),
            ],
            options={
                'verbose_name': '教职工表',
                'db_table': 'StaffInfo',
            },
        ),
        migrations.CreateModel(
            name='UndergraduateInfo',
            fields=[
                ('studentID', models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='学号')),
                ('studentName', models.CharField(max_length=26, verbose_name='学生姓名')),
                ('gender', models.CharField(choices=[('0', '男'), ('1', '女')], max_length=2, verbose_name='性别')),
                ('enrollmentYear', models.IntegerField(verbose_name='入学年份')),
                ('specialty', models.CharField(max_length=41, verbose_name='专业')),
                ('studentClass', models.CharField(blank=True, default='无', max_length=16, null=True, verbose_name='班级')),
                ('mobileNumber', models.CharField(max_length=12, verbose_name='手机号')),
                ('qqNumber', models.CharField(max_length=12, verbose_name='qq号')),
                ('politicalStatus', models.CharField(choices=[('1', '中共党员'), ('2', '中共预备党员'), ('3', '共青团员'), ('4', '民革党员'), ('5', '民盟盟员'), ('6', '民建会员'), ('7', '民进会员'), ('8', '农工党党员'), ('9', '致公党党员'), ('10', '九三学社社员'), ('11', '台盟盟员'), ('12', '无党派人士'), ('13', '群众')], max_length=3, verbose_name='政治面貌')),
                ('instructor', models.CharField(max_length=11, verbose_name='辅导员工号')),
                ('position', models.CharField(blank=True, max_length=21, null=True, verbose_name='职务')),
            ],
            options={
                'verbose_name': '本科生基础信息',
                'db_table': 'UndergraduateInfo',
            },
        ),
        migrations.CreateModel(
            name='VolunteerService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField(blank=True, null=True, verbose_name='时长')),
                ('Vstudent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='VstudentInfo', to='studentUser.UndergraduateInfo', verbose_name='学生')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activityInfo', to='studentUser.UndergraduateInfo', verbose_name='活动')),
            ],
            options={
                'verbose_name': '本科生活动时长',
                'db_table': 'VolunteerService',
            },
        ),
        migrations.CreateModel(
            name='UndergraduateOtherInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField(verbose_name='出生日期')),
                ('nation', models.CharField(choices=[('0', '汉族'), ('1', '壮族'), ('2', '满族'), ('3', '回族'), ('4', '苗族'), ('5', '维吾尔族'), ('6', '土家族'), ('7', '彝族'), ('8', '蒙古族'), ('9', '藏族'), ('10', '布依族'), ('11', '侗族'), ('12', '瑶族'), ('13', '朝鲜族'), ('14', '白族'), ('15', '哈尼族'), ('16', '哈萨克族'), ('17', '黎族'), ('18', '傣族'), ('19', '畲族'), ('20', '傈僳族'), ('21', '仡佬族'), ('22', '东乡族'), ('23', '高山族'), ('24', '拉祜族'), ('25', '水族'), ('26', '佤族'), ('27', '纳西族'), ('28', '羌族'), ('29', '土族'), ('30', '仫佬族'), ('31', '锡伯族'), ('32', '柯尔克孜族'), ('33', '达斡尔族'), ('34', '景颇族'), ('35', '毛南族'), ('36', '撒拉族'), ('37', '布朗族'), ('38', '塔吉克族'), ('39', '阿昌族'), ('40', '普米族'), ('41', '鄂温克族'), ('42', '怒族'), ('43', '京族'), ('44', '基诺族'), ('45', '德昂族'), ('46', '保安族'), ('47', '俄罗斯族'), ('48', '裕固族'), ('49', '乌孜别克族'), ('50', '门巴族'), ('51', '鄂伦春族'), ('52', '独龙族'), ('53', '塔塔尔族'), ('54', '赫哲族'), ('55', '珞巴族')], default='汉族', max_length=3, verbose_name='民族')),
                ('isReligious', models.CharField(choices=[('0', '否'), ('1', '是')], default=0, max_length=2, verbose_name='是否信仰宗教')),
                ('religion', models.CharField(max_length=21, verbose_name='信仰宗教')),
                ('dormitoryBuilding', models.CharField(max_length=3, verbose_name='宿舍楼号')),
                ('dormitory', models.CharField(max_length=4, verbose_name='宿舍号')),
                ('province', models.CharField(max_length=11, verbose_name='家庭所在省/自治区')),
                ('city', models.CharField(max_length=21, verbose_name='家庭所在市')),
                ('county', models.CharField(max_length=21, verbose_name='家庭所在县/区')),
                ('address', models.CharField(max_length=81, verbose_name='家庭详细地址')),
                ('registeredResidence', models.CharField(choices=[('0', '农村'), ('1', '城市')], max_length=2, verbose_name='户口性质')),
                ('fName', models.CharField(max_length=26, verbose_name='父亲姓名')),
                ('fWork', models.CharField(default='无', max_length=26, verbose_name='父亲工作')),
                ('fMobileNumber', models.CharField(max_length=11, verbose_name='父亲电话')),
                ('mName', models.CharField(max_length=26, verbose_name='母亲姓名')),
                ('mWork', models.CharField(default='无', max_length=26, verbose_name='母亲工作')),
                ('mMobileNumber', models.CharField(max_length=12, verbose_name='母亲电话')),
                ('gName', models.CharField(max_length=26, verbose_name='监护人姓名')),
                ('gMobileNumber', models.CharField(max_length=12, verbose_name='监护人电话')),
                ('gkChinese', models.IntegerField(verbose_name='语文成绩')),
                ('gkMath', models.IntegerField(verbose_name='数学成绩')),
                ('gkEnglish', models.IntegerField(verbose_name='英语成绩')),
                ('gkScience', models.IntegerField(verbose_name='理综成绩')),
                ('healthy', models.CharField(choices=[('0', '健康'), ('1', '良好'), ('2', '及格'), ('3', '不及格'), ('4', '优秀')], max_length=2, verbose_name='健康情况')),
                ('postalCode', models.CharField(max_length=7, verbose_name='邮政编码')),
                ('baseInfo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='BUstudentInfo', to='studentUser.UndergraduateInfo', verbose_name='学生')),
            ],
            options={
                'verbose_name': '本科生其它信息',
                'db_table': 'UndergraduateOtherInfo',
            },
        ),
        migrations.CreateModel(
            name='UndergraduateClassScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(verbose_name='成绩')),
                ('examTime', models.DateField(verbose_name='日期')),
                ('teacherID', models.CharField(blank=True, max_length=11, null=True, verbose_name='教师工号')),
                ('studyMode', models.CharField(choices=[('0', '正常'), ('1', '重修'), ('2', '补考')], max_length=2, verbose_name='课程属性')),
                ('Ustudent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UstudentInfo', to='studentUser.UndergraduateInfo', verbose_name='学生')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='courseInfo', to='studentUser.CourseInfo', verbose_name='课程')),
            ],
            options={
                'verbose_name': '本科生成绩',
                'db_table': 'UndergraduateClassScore',
            },
        ),
        migrations.CreateModel(
            name='AttendenceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='日期')),
                ('period', models.IntegerField(verbose_name='节次')),
                ('attendence', models.CharField(choices=[('0', '全勤'), ('1', '旷课'), ('2', '迟到'), ('3', '请假'), ('4', '早退')], max_length=2, verbose_name='出勤情况')),
                ('Astudent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AstudentInfo', to='studentUser.UndergraduateInfo', verbose_name='学生')),
            ],
            options={
                'verbose_name': '考勤情况',
                'db_table': 'AttendenceInfo',
            },
        ),
        migrations.CreateModel(
            name='Login_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_teacher', models.CharField(choices=[('0', '否'), ('1', '是')], default='1', max_length=2, verbose_name='是否是教职工')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户表',
                'db_table': 'Login_Info',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]

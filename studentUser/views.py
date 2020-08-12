from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
import json
from .models import UndergraduateInfo, UndergraduateOtherInfo, Login_Info, ActivityInfo, CourseInfo
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token
from django.db.models import Q
from django.contrib.auth.models import User
from rest_framework import permissions
from itertools import chain

from rest_framework.authtoken import views
from .forms import studentInfo, studentOtherInfo


# Create your views here.
def home(request):
    """Renders the home page."""
    return render(request, 'index.html')

def userInfo(reuqest):
    return JsonResponse({"code":20000,"data":{"roles":["admin"],"introduction":"I am a super administrator","avatar":"https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif","name":"Super Admin"}})

# 登录账户
def userLogin(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        token = views.obtain_auth_token(request).data
        result = {'code': 20000, 'data': token}
        return JsonResponse(result)
    else:
        return render(request,"error.html",{"message":"账户名或密码错误"})

# 退出登录
def userLogout(request):
    token = Token.objects.get(user = request.user)
    token.delete()
    logout(request)
    
    return JsonResponse({"code": 20000, "data": "success"})

# 查询安全性检查 待完善
def securityCheck(queryString):
    return True

# 自定义查询
def customQuery(request):
    if not securityCheck(request.POST.get("query")):
        return {"code": 40000, "data": "这是非法的查询"}

    query = eval(request.POST.get("query"))
    targetModule = eval(request.POST.get("module"))

    return targetModule.objects.query

# 新增学生信息
def createStudent(request):
    studentinfo = studentInfo(request.POST)
    studentotherinfo = studentOtherInfo(request.POST)

    if studentinfo.is_valid() and studentotherinfo.is_valid():
       studentinfo  = studentinfo.save()
       studentotherinfo = studentotherinfo.save(commit=False)
       studentotherinfo.baseInfo = studentinfo
       studentotherinfo.save()

    return JsonResponse({"code": 20000, "data": "success"})

#创建用户，超级管理员
# @login_required(login_url='/accounts/login/')
def register(request):
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    sex = request.POST.get("gender","")
    Login_Info.objects.create_superuser(username=username, password=password,is_teacher=sex,email=None)
    referer = request.META.get("HTTP_REFERER", reverse("home"))
    return redirect(referer)


def register1(request):
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    sex = request.POST.get("gender","")
    print(sex)
    Login_Info.objects.create_user(username=username, password=password,is_teacher=sex)
    referer = request.META.get("HTTP_REFERER", reverse("home"))
    return redirect(referer)


#检查密码
def check_password(request):
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    user = authenticate(request, username=username, password=password)
    ret = user.check_password('test123456')
    referer = request.META.get("HTTP_REFERER", reverse("home"))
    return redirect(referer)


#修改密码
def change_password(request):
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    user = authenticate(request, username=username, password="旧密码")
    user.set_password(password='新密码')
    user.save()
    referer = request.META.get("HTTP_REFERER", reverse("home"))
    return redirect(referer)


@login_required
def return_undergraduateinfo(request):
    if request.method == 'GET':
        data = UndergraduateInfo.objects.values().all()
        data = list(data)
        result = {'code':200, 'data':data}
        return JsonResponse(result)


@login_required
def updata_undergraduateinfo(request):
    if request.method == 'POST':
        pass


@login_required
def addnew_undergraduateinfo(request):
    if request.method == 'POST':
        try:
            student = UndergraduateInfo()
            student.studentID = request.POST.get("studentID", "")
            student.studentName = request.POST.get("studentName", "")
            student.gender = request.POST.get("gender", "")
            student.enrollmentYear = request.POST.get("enrollmentYear", "")
            student.specialty = request.POST.get("specialty", "")
            student.studentClass = request.POST.get("studentClass", "")
            student.instructor = request.POST.get("instructor", "")
            student.position = request.POST.get("position", "")
            student.save()

            studentOther = UndergraduateOtherInfo()
            studentOther.baseInfo = student.studentID
            studentOther.birthday = request.POST.get("birthday", "")
            studentOther.nation = request.POST.get("nation", "")
            studentOther.isReligious = request.POST.get("isReligious", "")
            studentOther.religion = request.POST.get("religion", "")
            studentOther.mobileNumber = request.POST.get("mobileNumber", "")
            studentOther.qqNumber = request.POST.get("qqNumber", "")
            studentOther.politicalStatus = request.POST.get("politicalStatus", "")
            studentOther.dormitoryBuilding = request.POST.get("dormitoryBuilding", "")
            studentOther.dormitory = request.POST.get("dormitory", "")
            studentOther.province = request.POST.get("province", "")
            studentOther.city = request.POST.get("city", "")
            studentOther.county = request.POST.get("county", "")
            studentOther.address = request.POST.get("address", "")
            studentOther.registeredResidence = request.POST.get("registeredResidence", "")
            studentOther.fName = request.POST.get("fName", "")
            studentOther.fWork = request.POST.get("fWork", "")
            studentOther.fMobileNumber = request.POST.get("fMobileNumber", "")
            studentOther.mName = request.POST.get("mName", "")
            studentOther.mWork = request.POST.get("mWork", "")
            studentOther.mMobileNumber = request.POST.get("mMobileNumber", "")
            studentOther.gName = request.POST.get("gName", "")
            studentOther.gMobileNumber = request.POST.get("gMobileNumber", "")
            studentOther.gkChinese = request.POST.get("gkChinese", "")
            studentOther.gkMath = request.POST.get("gkMath", "")
            studentOther.gkEnglish = request.POST.get("gkEnglish", "")
            studentOther.gkScience = request.POST.get("gkScience", "")
            studentOther.healthy = request.POST.get("healthy", "")
            studentOther.postalCode = request.POST.get("postalCode", "")
            studentOther.save()
        except:
            return HttpResponse(400)
        return HttpResponse(200)


# 过滤器和取列值的操作
# @login_required
def return_UndergraduateInfo_Optional(request):
    query = request.POST.get('query', None)
    fields = request.POST.get('fields', None)

    # 过滤器
    query_str = ''
    for each_query in query:
        query_str = query_str + 'Q(%s)|' % (each_query)
    query_str = query_str[:-1]
    data = UndergraduateInfo.objects.filter(eval(query_str))

    #
    data = list(data.values(*fields))

    result = {'code':200, 'data':data}

    return JsonResponse(result)

# 学生其他信息
def return_UndergraduateOtherInfo_Optional(request):
    query = request.POST.get('query', None)
    fields = request.POST.get('fields', None)

    # 过滤器
    query_str = ''
    for each_query in query:
        query_str = query_str + 'Q(%s)|' % (each_query)
    query_str = query_str[:-1]
    data = UndergraduateOtherInfo.objects.filter(eval(query_str))

    #
    data = list(data.values(*fields))

    result = {'code':200, 'data':data}

    return JsonResponse(result)

# 课程
def return_CourseInfo_Optional(request):
    query = request.POST.get('query', None)
    fields = request.POST.get('fields', None)

    # 过滤器
    query_str = ''
    for each_query in query:
        query_str = query_str + 'Q(%s)|' % (each_query)
    query_str = query_str[:-1]
    data = CourseInfo.objects.filter(eval(query_str))

    #
    data = list(data.values(*fields))

    result = {'code':200, 'data':data}

    return JsonResponse(result)

#活动
def return_ActivityInfo_Optional(request):
    query = request.POST.get('query', None)
    fields = request.POST.get('fields', None)

    # 过滤器
    query_str = ''
    for each_query in query:
        query_str = query_str + 'Q(%s)|' % (each_query)
    query_str = query_str[:-1]
    data = ActivityInfo.objects.filter(eval(query_str))

    #
    data = list(data.values(*fields))

    result = {'code':200, 'data':data}

    return JsonResponse(result)

# return_undergraduateinfo_Optional(1)

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
plt.rcParams['font.sans-serif'] = ['KaiTi'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

# 均分柱状图
def A():
    chengjis = ['gkChinese','gkMath','gkEnglish','gkScience']
    name_list  = []
    y1 = []
    y2 = []
    for chengji in chengjis:
        name_list .append(chengji)
        students_r = UndergraduateOtherInfo.objects.filter(registeredResidence='0')
        students_r_chinese = students_r.values_list(chengji)
        students_r_chinese = list(students_r_chinese)
        students_r_chinese = np.mean(students_r_chinese)
        y1.append(students_r_chinese)

        students_r = UndergraduateOtherInfo.objects.filter(registeredResidence='1')
        students_r_chinese = students_r.values_list(chengji)
        students_r_chinese = list(students_r_chinese)
        students_r_chinese = np.mean(students_r_chinese)
        y2.append(students_r_chinese)
    # print(name_list )
    # print(y1)
    # print(y2)

    x = list(range(len(name_list )))
    total_width, n = 0.8, 2
    width = total_width / n
    plt.bar(x, y1, width=width, label='农村', fc='b')
    for i in range(len(x)):
        x[i] += width
    plt.bar(x, y2, width=width, label='城镇', tick_label=name_list, fc='g')
    plt.legend()
    plt.show()

# 频率直方图
def Frequency_histogram():
    fig, ax = plt.subplots()
    chengjis = ['gkChinese','gkMath','gkEnglish','gkScience']
    name_list  = []
    y1 = []
    y2 = []
    students_r_sum = UndergraduateOtherInfo.objects.filter(registeredResidence='0')
    students_r_sum = students_r_sum.values_list('gkChinese','gkMath','gkEnglish','gkScience')
    students_r_sum = list(students_r_sum)
    students_r_sum = [sum(i) for i in students_r_sum]
    y1.append(students_r_sum)

    students_c_sum = UndergraduateOtherInfo.objects.filter(registeredResidence='1')
    students_c_sum = students_c_sum.values_list('gkChinese','gkMath','gkEnglish','gkScience')
    students_c_sum = list(students_c_sum)
    students_c_sum = [sum(i) for i in students_c_sum]
    y2.append(students_c_sum)

    sns.distplot(y1, kde=True, hist=False)
    sns.distplot(y2, kde=True, hist=False)
    plt.savefig('B.png')
    plt.show()


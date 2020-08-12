from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

def djregist(request):
    if request.method == 'GET':
        return render(request, 'day6_regist.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        # 此处的User 是 django 自带的model
        User.objects.create_user(username=name, password=password)
        return HttpResponseRedirect('/uauth/dj_login/')

def djlogin(request):
    if request.method == 'GET':
        return render(request, 'day6_login.html')

    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        # 验证用户名和密码，验证通过的话，返回user对象
        user = auth.authenticate(username=name, password=password)
        if user:
            # 验证成功 登陆
            auth.login(request, user)
            return HttpResponseRedirect('/stuapp/index/')
        else:
            return render(request, 'day6_regist.html')

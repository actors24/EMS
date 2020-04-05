import random
import string
import time

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

from user.captcha.image import ImageCaptcha
from user.models import User


# Create your views here.


def login(request):
    username = request.COOKIES.get('name')
    if username:
        username = username.encode('latin-1').decode('utf-8')
    pwd = request.COOKIES.get('password')
    user = User.objects.filter(username=username, password=pwd)
    if user:
        request.session['flag'] = 1
        return redirect('manage:main')
    return render(request, 'login.html')


def login_logic(request):
    try:
        username = request.POST.get('name')
        pwd = request.POST.get('pwd')
        rem = request.POST.get('remember')
        user = User.objects.filter(username=username, password=pwd)
        if user:
            request.session['flag'] = 1
            res = JsonResponse({"msg": "登录成功", "status": 1})
            if rem:
                res.set_cookie('name', username, max_age=7 * 24 * 3600)
                res.set_cookie('password', pwd, max_age=7 * 24 * 3600)
            return res
        else:
            return JsonResponse({"msg": "用户名或密码错误", "status": 0})
    except:
        return JsonResponse({"msg": "登录失败", "status": 0})


def register(request):
    return render(request, 'regist.html')


def register_logic(request):
    num = request.POST.get('number').lower()
    num2 = request.session.get('code').lower()
    if num == num2:
        username = request.POST.get('username')
        realname = request.POST.get('name')
        pwd = request.POST.get('pwd')
        sex = request.POST.get('sex')
        user = User.objects.filter(username='username')
        if user:
            return HttpResponse('注册失败,用户名重复')
        else:
            User.objects.create(username=username, realname=realname, password=pwd, gender=sex)
            return redirect('user:login')
    else:
        return HttpResponse('验证码错误')


def get_captcha(request):
    img = ImageCaptcha()
    code = random.sample(string.ascii_letters + string.digits, 5)
    code = ''.join(code)
    request.session['code'] = code
    data = img.generate(code)
    return HttpResponse(data, 'image/png')


def log_out(request):
    del request.session['flag']
    res = redirect('user:login')
    res.set_cookie('name', '', max_age=1)
    res.set_cookie('password', '', max_age=1)
    return res


def get_username(request):
    time.sleep(1)
    username = request.GET.get('username')
    if username == '':
        return JsonResponse({"status": 0})
    user = User.objects.filter(username=username)
    if user:
        return JsonResponse({"status": 0})
    else:
        return JsonResponse({"status": 1})


def get_code(request):
    time.sleep(1)
    code = request.GET.get('code')
    code1 = request.session.get('code')
    if code.lower() == code1.lower():
        return JsonResponse({"status": 1})
    else:
        return JsonResponse({"status": 0})

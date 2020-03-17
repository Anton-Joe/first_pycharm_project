from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import  redirect
# Create your views here.


def index(request):
    username = request.GET.get('username')
    if username:
        return HttpResponse('CMS首页')
    else:
        # 获取当前实例空间
        current_namespace = request.resolver_match.namespace
        return redirect("{namespace}:login".format(namespace=current_namespace))


def login(request):
    return HttpResponse('登录页面')

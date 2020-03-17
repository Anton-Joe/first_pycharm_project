from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, reverse


def index(request):
    return HttpResponse('练习首页')


def room_id(request, room_id):
    return redirect('practiceApp:test_name')


def room_id2(request):
    return HttpResponse("房间号：{d}".format(d=request.GET.get('room_id2')))
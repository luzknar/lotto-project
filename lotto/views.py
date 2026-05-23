from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>6/45 Lotto 웹 사이트에 오신 것을 환영합니다!</h1>")
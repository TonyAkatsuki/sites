from django.shortcuts import render
from imust.models import Student,StuArt,Article,Comment, News
from django.views.decorators import csrf
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.shortcuts import render
from django.contrib.auth import authenticate, login    


from bs4 import BeautifulSoup
import requests
from lxml import html
import time
import sys
baseurl = "https://coes-stud.must.edu.mo"
#intake  = "1809"
import requests

# Create your views here.


def login(request):
    if request.POST:
        result = Student(sid = request.POST['sid'], password =  request.POST['pw'], name = 'DEFAULT_' + request.POST['sid'])
        result.save()
    return HttpResponseRedirect('http://127.0.0.1:8000/S_Home.html/?sid=' + request.POST['sid'])

def Login(request):
    return render(request, 'imust/Login.html', context={})

def quit(request):
    result = Student.objects.get(sid=request.GET.get('sid')).delete()
    return HttpResponseRedirect('http://127.0.0.1:8000/')

def forumComment(request):
    s = request.GET.get('sid')
    aid = request.GET.get('aid')
    article = Article.objects.get(aid=aid)
    sid = StuArt.objects.get(aid=aid)
    author = Student.objects.get(sid=sid.sid)
    comment_list = Comment.objects.filter(aid=aid)
    return render(request, 'imust/S_Forum-comment.html', context={'article': article, 'author': author, 'comment_list':comment_list, 'sid':s})

def forumPublish(request):
    s = request.GET.get('sid')
    return render(request, 'imust/S_Forum-publish.html', context={'sid':s})

def submitAr(request):
    s = request.GET.get('sid')
    ctx={}
    if request.POST:
        result = Article(title = request.POST['Title'], content =  request.POST['Content'])
        result.save()
        ar = Article.objects.latest('time')
        stuart = StuArt(aid = ar.aid, sid=s)
        stuart.save()
    ctx['result'] = "Successful!"
    return render(request, 'imust/S_Forum-publish.html', context={'result':ctx, 'sid':s})

def submitCo(request):
    s = request.GET.get('sid')
    aid=request.GET.get('aid')
    ctx={}
    if request.POST:
        stu = Student.objects.get(sid=s)
        result = Comment(aid = aid, comment =  request.POST['Comment'], name=stu.name, sid=s)
        result.save()
    ctx['result'] = "Successful!"
    article = Article.objects.get(aid=aid)
    sid = StuArt.objects.get(aid=aid)
    author = Student.objects.get(sid=sid.sid)
    comment_list = Comment.objects.filter(aid=aid)
    return render(request, 'imust/S_Forum-comment.html', context={'article': article, 'author': author, 'comment_list':comment_list, 'result':ctx, 'sid':s})


def forumhome(request):
    s = request.GET.get('sid')
    article_list = Article.objects.all().order_by('-time')
    return render(request, 'imust/S_Forumhome.html', context={'article_list': article_list, 'sid':s})

def home(request):
    s = request.GET.get('sid')
    return render(request, 'imust/S_Home.html', context={'sid':s})

def news(request):
    s = request.GET.get('sid')
    result = News.objects.all().order_by('-time')
    return render(request,'imust/S_News.html', context = {'news':result, 'sid':s})

def refreshNew(request):
    a = News.objects.all().delete()
    s = request.GET.get('sid')
    a = getNews()
    result = News.objects.all().order_by('-time')
    return render(request,'imust/S_News.html', context = {'news':result, 'sid':s})

def time(request):
    s = request.GET.get('sid')
    return render(request, 'imust/S_Time.html', context={'sid':s})

def getNews():
	list_Content = []

	for page in range(1,5):
		print("------------------------------------------next page: ", page)
		urlend = '?limit=10&start='
		target = 'https://www.must.edu.mo/cn/news'
		if page != 1:
			start = page * 10
			target = target + urlend + str(start)
		req = requests.get(url = target, verify=False)
		html = req.text
		bf = BeautifulSoup(html, features="html.parser")
		must = 'https://www.must.edu.mo'

		for row in range(0,9):
			time = bf.select('#t3-content > section > div.items-row.cols-1.row-'+str(row)+' > article > div.article-content > aside')
			title = bf.select('#t3-content > section > div.items-row.cols-1.row-'+ str(row) + ' > article > div.article-content > h4 > a')
			link = bf.select('#t3-content > section > div.items-row.cols-1.row-'+ str(row) + ' > article > div.article-content > h4 > a')
			#print(time[0].text) 
			#print(title[0].text)
			for href in link:
				t = href.get('href')
				news = must + t;
				#print(news)
				req = requests.get(url = news, verify = False)
				sub = BeautifulSoup(req.text, features="html.parser")
				body = sub.find('section', class_= 'article-content clearfix')
				result = News(title=title[0].text,time=time[0].text,content=body.text)
				result.save()
				#print(body.text)
				
	return 0
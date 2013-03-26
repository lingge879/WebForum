#coding:utf8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django import forms
from wb.blog.models import *

class Log(forms.Form):
    title = forms.CharField(label='标题')
    content = forms.CharField(widget=forms.Textarea, label='内容')

def index(request):
    if request.method == 'POST':
        log = Log(request.POST)
        if log.is_valid():
            title = log.cleaned_data['title']
            content = log.cleaned_data['content']
            Note.objects.create(title=title, content=content)
            return HttpResponseRedirect('/index')
    else:
        log = Log()
    return render_to_response('index.html', {'log': log})
            

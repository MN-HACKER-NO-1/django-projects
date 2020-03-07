from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    params={'name':'naved','age':'19'}
    return render(request,'index.html',params)
def about(request):
    return HttpResponse('''<h1>HI I AM FROM about</h1>''')

def anaylayze(request):
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    print(removepunc)
    print(djtext)
    punction='''"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''
    analyzed = ""
    if anaylayze=='on':
        for  char in djtext:
            if char not in punction:
                analyzed=analyzed + char
            params={ 'purpose':'Remove punction','analyze_text':analyzed }

        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Error")

def capitalizefirst(request):
    return HttpResponse("<h1>HI I AM FROM capitalizefirst</h1>")

def newlineremove(request):
    return HttpResponse("<h1>HI I AM FROM newlineremove</h1>")

def spaceremove(request):
    return HttpResponse("<h1>HI I AM FROM spaceremove</h1>")
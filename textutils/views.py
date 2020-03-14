from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analyze(request):
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    print(removepunc)
    print(djtext)
    punction='''"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''
    analyzed = ""
    if removepunc=='on':
        for  char in djtext:
            if char not in punction:
                analyzed=analyzed + char
            params={ 'purpose':'Remove punctuaion','analyze_text':analyzed }

        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Error")

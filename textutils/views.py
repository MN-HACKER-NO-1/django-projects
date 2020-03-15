from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analyze(request):
    # get the text
    djtext=request.GET.get('text','default')
    # check checkboxes values
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')
    wordscounter=request.GET.get('wordscounter','off')
    punction='''"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''
    analyzed = ""
    # check which checkbox in on
    if removepunc=='on':
        for  char in djtext:
            if char not in punction:
                analyzed=analyzed + char
        params={ 'purpose':'Remove punctuaion','analyze_text':analyzed }

        return render(request,'analyze.html',params)
    elif fullcaps=='on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'for capitilization', 'analyze_text': analyzed}

        return render(request, 'analyze.html', params)
    elif newlineremover=='on':
        analyzed=""
        for char in djtext:
            if char!='\n':
                analyzed=analyzed+char
        params = {'purpose': 'for remove new line', 'analyze_text': analyzed}

        return render(request, 'analyze.html', params)
    elif extraspaceremover=='on':
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
        params = {'purpose': 'for remove extra space', 'analyze_text': analyzed}

        return render(request, 'analyze.html', params)
    elif wordscounter=='on':
        analyzed=0
        for char in djtext:
            if char==" ":
                analyzed+=1

        params = {'purpose': 'for count the words', 'analyze_text': analyzed}

        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")

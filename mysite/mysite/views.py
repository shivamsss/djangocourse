# I have created this file by my own
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    # return HttpResponse("hello Shivam")
      return render(request,'index.html')
def about(request):
    return HttpResponse("about Shivam")

def newwebsite(request):
    return HttpResponse('''<a href="https://www.google.com/">Click To Open Google</a>''')

def analyze(request):
    djtext = request.GET.get('textarea1','default')
    removepunc1=request.GET.get('removepunc','default')
    uppercase1=request.GET.get('fullcaps','default')
    newline1=request.GET.get('newline','default')
    charcount1=request.GET.get('charcount','default')

    if removepunc1 =='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed1=""
        for char in djtext:
            if char not in punctuations:
                analyzed1=analyzed1+char

        params = {
            'purpose': 'remove Punctuations',
            'analyzed_text': analyzed1
        }
        djtext=analyzed1
        # return render(request, 'analyze.html', params)

    if(uppercase1 == 'on'):
        upcase=""
        for char in djtext:
            upcase=upcase+char.upper()
        params = {
        'purpose': 'Move To Uppercase',
        'analyzed_text': upcase
              }
        djtext=upcase
        # return render(request, 'analyze.html', params)
    if(newline1=='on'):
        new=""
        for char in djtext:
            if char !='\n':
                new=new+char
        params = {
            'purpose': 'New Line Remove',
            'analyzed_text': new
        }
        djtext=new
        # return render(request,'analyze.html',params)
    if(charcount1=='on'):
        count=0
        for char in djtext:
            count=count+1
        params = {
            'purpose': 'Char Count ',
            'analyzed_text': count
        }
        djtext=count
        # return render(request, 'analyze.html', params)


    if(removepunc1 != "on" and newline1!="on" and charcount1!="on" and uppercase1!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)
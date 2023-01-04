# I have created this file on my own (views.py)
from django.http import HttpResponse
from django.shortcuts import render
from simple_colors import *

#CODE FOR MAKING WEBSITES NAVIGATION PAGES

# def index(request):
#     with open("one.txt","r") as f:
#         content=f.read()
#     return HttpResponse(content)
# def about(request):
#     return HttpResponse("This is the about section")

# def nav(request):
#     return HttpResponse('''<h1>Navigate to various pages</h1><br><br><h2><a href="https://www.youtube.com">Youtube</a></h2><br><h2><a href="https://www.facebook.com">Facebook</a></h2><br><h2><a href="https://www.instagram.com">Instagram</a></h2><br><h2><a href="https://www.google.com">Google</a></h2><br><h2><a href="https://www.amazon.in">Amazon</a></h2><br>''')



# def removepunc(request):
#     #get the text
#     djtext=request.POST.get('text','default')
#     print(djtext)
#     #anaylse the text
#     return HttpResponse("Remove punc" '''<br><br><h2><a href="http://127.0.0.1:8000/home">back</a></h2>''')

# def capfirst(request):
#     return HttpResponse("Capitalize first" '''<br><br><h2><a href="http://127.0.0.1:8000/home">back</a></h2>''')

# def newlineremove(request):
#     return HttpResponse("Newline remover" '''<br><br><h2><a href="http://127.0.0.1:8000/home">back</a></h2>''')

# def spaceremove(request):
#     return HttpResponse("spaceremover" '''<br><br><h2><a href="http://127.0.0.1:8000/home">back</a></h2>''')

# def charcount(request):
#     return HttpResponse("charcount" '''<br><br><h2><a href="http://127.0.0.1:8000/home">back</a></h2>''')

def index(request):
    return render(request, "index.html")

def contactus(request):
        return render(request,'contactus.html')
def aboutus(request):
        return render(request,'aboutus.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    # check the check boxes
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    allspaceremover=request.POST.get('allspaceremover','off')
    boldtext=request.POST.get('boldtext','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcounter=request.POST.get('charcounter','off')
    punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed=""

    # check which checkbox is on
    if removepunc=="on":
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        parameter={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html',parameter)
    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        parameter={'purpose':'Changed to upper Case','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html',parameter)
    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char !="\n":
                analyzed=analyzed+char
        parameter={'purpose':'No new line char','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html',parameter)
    if allspaceremover=="on":
        analyzed=""
        for char in djtext:
            if ord(char) != 32:
                analyzed=analyzed+char
        parameter={'purpose':'All spaces Removed','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html',parameter)
    if (extraspaceremover=="on"):
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
        parameter={'purpose':'Extra spaces Removed','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html',parameter)
    if charcounter=="on":
        analyzed=""
        x=len(djtext)
        analyzed=x
        parameter={'purpose':'All spaces Removed','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html',parameter)

    if boldtext=="on":
        analyzed=""
        parameter={'purpose':'Text made bold','analyzed_text1':djtext}
        djtext=analyzed

    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and allspaceremover!="on" and extraspaceremover !="on" and charcounter!="on" and boldtext!="on"):
        return render(request,'error_page.html')
    # else:
    #     return HttpResponse("Error")
    
    return render(request, 'analyze.html',parameter)


    
    


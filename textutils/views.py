#Python code for text utils
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    #get the text
    djtext = request.POST.get('text','default')

    #Checkbox values
    removepunc = request.POST.get('removepunc','off')
    capitalize = request.POST.get('capitalize','off')
    space_remove = request.POST.get('space_remove', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    #check which checkbox is on
    if removepunc=='on' or capitalize=='on' or space_remove=='on' or newlineremover == 'on' or charcount=='on':
        if removepunc=='on':
            punctuations ='''.?!,:;-~_(){}[]<>""'/\...*&#@^|'''
            analyzed=""
            for char in djtext:
                if char not in punctuations:
                    analyzed = analyzed + char
            para ={'purpose':'Remove Punctuation','analyzed_text':analyzed}
            djtext=analyzed
        if capitalize == 'on':
            analyzed =""
            for char in djtext:
                analyzed = analyzed + char.upper()
            para = {'purpose': 'CAPITALIZE', 'analyzed_text': analyzed}
            djtext = analyzed

        if space_remove == 'on':
            analyzed =""
            space=' '
            for char in djtext:
                if char not in space:
                    analyzed = analyzed + char
            para = {'purpose': 'RemoveSpaces', 'analyzed_text': analyzed}
            djtext = analyzed
        if newlineremover == 'on':
            analyzed =""

            for char in djtext:
                if char != "\n" and char !="\r":
                    analyzed = analyzed + char
            para = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
            djtext = analyzed
        if charcount=='on':
            c=0
            for char in djtext:
                c=c+1

            analyzed= djtext + "\nThe number of Characters are : "+ str(c)
            para = {'purpose': 'Character Counter', 'analyzed_text': analyzed}
            djtext = analyzed
        return render(request, 'analyze.html', para)
    else :
        analyzed=djtext
        para = {'purpose': 'No Operations Performed', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', para)


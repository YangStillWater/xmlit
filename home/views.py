# -*- coding: UTF-8 -*-

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView

from update.models import Image,Text,SlideImage


def index(request):
    textlist=Text.objects.all()
    imglist=Image.objects.all()
    slideimglist=SlideImage.objects.all()
    if request.user.is_authenticated():
        loginned=True
        username=request.user.get_username()
    else:
        loginned=False
    #print(textlist[0].content)
    return render_to_response('index.html',locals(),
        context_instance=RequestContext(request))

def show_textlist(request):
    textlist=Text.objects.all()
    imglist=Image.objects.all()
    slideimglist=SlideImage.objects.all()
    return HttpResponse(textlist)

class TextList(ListView):
    model = Text

def hello(request):
    return HttpResponse("Hello,  You're at the index.")

def default(request):
    return HttpResponseRedirect('/home')

def test(request):
    return HttpResponseNotFound('<h1>Page not found</h1>')


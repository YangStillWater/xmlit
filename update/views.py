# -*- coding: UTF-8 -*-

import os
import uuid
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from xmlit.settings import BASE_DIR
from update.models import Image,Text,SlideImage

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

@login_required
def upload(request):
    """
    upload image
    """
    imgId = request.GET.get('id','1')
    hasUpload="wait"
    i=Image.objects.get(pk=imgId)
    filename=i.filename
    imgURL="/static/Image/"+filename
    if request.method == 'POST':
        image = request.FILES.get("img","")
        if image:
            fn, ext = os.path.splitext(image.name)#这个方法是将每个文件名分割为名字跟扩展名
            filename = str(uuid.uuid1()) + ext
            if 1 == handle_uploaded_file(image,filename):
                hasUpload="上传成功！"
                imgURL="/static/Image/"+filename
                #i=Image.objects.get(pk=imgId)
                i=Image(position='1',filename=filename,upd_person=request.user.get_username(),upd_date=timezone.now())
                i.save()
            else:
                hasUpload="上传失败！"

    return render_to_response('upload.django.html',locals(),
        context_instance=RequestContext(request))


@login_required
def upload_slide(request):
    """
    upload slideimage
    """
    hasUpload="wait"

    slideimglist=SlideImage.objects.all()
    if request.method == 'POST':
        filename=request.POST.get('filename','')
        option=request.POST.get('option')
        if request.POST.get('delete','') != '':
            remove_file(BASE_DIR+'/static/assets/slide/'+filename)
            q=SlideImage.objects.filter(filename=filename).delete()
            return HttpResponse("<script>top.window.location.href='/'</script>")
    
        if option == 'add':
            imgdata=SlideImage()
        if option == 'overwrite':
            q=SlideImage.objects.filter(filename=filename)
            if q.count()>0:
                imgdata=q[0]
            else:
                imgdata=SlideImage()

        image = request.FILES.get("img","")
        if image:
            if filename=='':
                filename=image.name
            if 1 == handle_uploaded_file(image,'slide/'+filename):
                hasUpload="上传成功！"
                imgdata.filename=filename
                imgdata.upd_person=request.user.get_username()
                imgdata.upd_date=timezone.now()
                imgdata.save()
            else:
                hasUpload="上传失败！"

        return HttpResponse("<script>top.window.location.href='/'</script>")

    return render_to_response('upload_slide.django.html',locals(),
        context_instance=RequestContext(request))

def remove_file(filename):
    os.remove(filename)
    
def handle_uploaded_file(f,name):
    path=BASE_DIR+'/static/assets/'
    if not os.path.exists(path):
        os.makedirs(path)
    destination = open(path+'/'+name, 'wb+')
    try:
        for chunk in f.chunks():
            destination.write(chunk)
        destination.close()
        return 1
    except:
        return 0

@login_required
def edit(request,txt_id):
    '''
    update text
    '''
    if int(txt_id) > Text.objects.count():
        t=Text(position='',content='',upd_person='')
    else:
        t=Text.objects.get(pk=txt_id)
    if request.method == 'POST':
        t.content=request.POST.get('value','')
        t.upd_person=request.user.get_username()
        t.upd_date=timezone.now()
        t.save()
    return render_to_response('edit.django.html',locals(),
        context_instance=RequestContext(request))

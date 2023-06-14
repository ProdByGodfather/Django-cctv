from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import cv2
from .camera import *
from django.http import StreamingHttpResponse
from django.views.decorators.gzip import gzip_page

#Show Camera
# @login_required
# @gzip_page
def livefe(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad!
        pass

@login_required
def index(request, *args, **kwargs):

    return render(request, 'camera.html')

def home(request):
    return render(request,'home.html')





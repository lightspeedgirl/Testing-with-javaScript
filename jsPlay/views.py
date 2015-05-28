from django.shortcuts import render
from django.shortcuts import  get_object_or_404, render_to_response
def index(request):

    return render_to_response('jsPlay/test.html')
    
def test2(request):

    return render_to_response('jsPlay/test2.html')
    
def can(request):

    return render_to_response('jsPlay/can.html')
    
def followMouse(request):

    return render_to_response('jsPlay/followMouse.html')
    
def lines(request):

    return render_to_response('jsPlay/lines.html')
    
def nirvash(request):

    return render_to_response('jsPlay/nirvash.html')
    
def rombasimiltion(request):

    return render_to_response('jsPlay/rombasimilation.html')
    

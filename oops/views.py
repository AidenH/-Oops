from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    tileindex = [0] * 3
    return render_to_response('index.html', locals())

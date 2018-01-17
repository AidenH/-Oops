import re
from django.http import HttpResponse
from django.shortcuts import render_to_response
from oops.models import Tile

def index(request):
    tileindex = Tile.objects.all()

    # saved in case tile_container's style="width: {{ width }}%;" is needed
    # widthint = 26 * len(tileindex)
    # width = str(widthint) + "%"

    return render_to_response('index.html', locals())

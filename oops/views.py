from django.http import HttpResponse
from django.shortcuts import render_to_response
from oops.models import Tile

def index(request):
    tileindex = Tile.objects.all()

    # saved in case tile_container's style="width: {{ width }}%;" is needed
    # widthint = 26 * len(tileindex)
    # width = str(widthint) + "%"

    return render_to_response('index.html', locals())

def tile_update(request):
    def strip_content(a):
        out = a.replace('&nbsp;', ' ').replace('<br>', '\n')
        return out

    tile_id = request.GET["id"]
    content_updated = request.GET["content"]

    if tile_id == '':
        tile_id = 0

    try:
        print("Id: %s" % tile_id)
        print("Content: %s" % content_updated)
        Tile.objects.filter(id=tile_id).update(content=strip_content(content_updated))
        return HttpResponse(status=200)
    except:
        return HttpResponse(status=403)

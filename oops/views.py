from django.http import HttpResponse
from django.shortcuts import render
from oops.models import Tile

def index(request):
    tileindex = Tile.objects.all()

    # saved in case tile_container's style="width: {{ width }}%;" is needed
    # widthint = 26 * len(tileindex)
    # width = str(widthint) + "%"

    return render(request, 'index.html', locals())

def tile_update(request):
    tile_id = request.GET["id"]
    content_updated = request.GET["content"]

    if tile_id == '': tile_id = 0 #Check tile id is not null

    try:
        print("Id: %s" % tile_id)
        print("Content: %s" % content_updated)
        Tile.objects.filter(id=tile_id).update(content=content_updated) #strip_content would go here around content_updated

        return HttpResponse(status=200)
    except:
        return HttpResponse(status=403)

def tile_add(request):
    try:
        t = Tile(title="Title")
        t.save()

        return HttpResponse(status=200)
    except:
        return HttpResponse(status=403)

def tile_delete(request):
    try:
        tile_id = request.GET["id"]
        Tile.objects.filter(id=tile_id).delete()

        return HttpResponse(status=200)
    except:
        return HttpResponse(status=403)

import re
from django.http import HttpResponse
from django.shortcuts import render_to_response
from oops.models import Tile

def index(request):
    tileindex = []
    for i in range(1, len(Tile.objects.all())+1):
        tile_title = str(Tile.objects.filter(id=i)
            .values_list('title', flat=True).get())
        tile_date = re.findall(r'20..-..-.. ..:..:..', str(Tile.objects.filter(id=i)
            .values_list('date', flat=True).get()))[0]
        tile_content = str(Tile.objects.filter(id=i)
            .values_list('content', flat=True).get())
        tileindex.append(int(i))

    # saved in case tile_container's style="width: {{ width }}%;" is needed
    # widthint = 26 * len(tileindex)
    # width = str(widthint) + "%"

    return render_to_response('index.html', locals())

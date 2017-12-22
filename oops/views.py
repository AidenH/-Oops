from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    tileindex = []
    for i in range(1, 11):
        tileindex.append(int(i))

    # saved in case tile_container's style="width: {{ width }}%;" is needed
    # widthint = 26 * len(tileindex)
    # width = str(widthint) + "%"

    return render_to_response('index.html', locals())

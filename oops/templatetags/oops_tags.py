from django import template
from oops.models import Tile

register = template.Library()

@register.simple_tag
def pytileUpdate(content_new, tile_id):
    if tile_id == '':
        tile_id = 0
    Tile.objects.filter(id=tile_id).update(content=content_new)
    print("test")
    return 1

from django import template
from oops.models import Tile

register = template.Library()

@register.simple_tag
def pytileUpdate(tile_id, content_new):
    Tile.objects.filter(id=tile_id).update(content=content_new)

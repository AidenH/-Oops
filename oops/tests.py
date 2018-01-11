from django.test import TestCase
from oops.models import Tile

class Tile_Tests(TestCase):
    def test_tile_content(self):
        for i in range(1, len(Tile.objects.all())+1):
            content = "<QuerySet [<Tile: My day: Jan 11th, 2018-01-11 20:02:49.724751+00:00 - -Shopping\n -Cinema\n -Dinner"
            self.assertEqual(Tile.objects.filter(id=i), content)

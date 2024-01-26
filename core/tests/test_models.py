
from django.test import TestCase
from django.contrib.gis.geos import Point

from core.models import GeoPoint

class ModelsTest(TestCase):

    def setUp(self):

        self.lat = 9.913990 # a random lat
        self.long = 8.889590 # a random long
        self.name = "John Doe"
        

    def test_geo_point_model(self):
        """Test create GeoPoint instance"""

        geo_point = GeoPoint.objects.create(
            name=self.name,
            location=Point(self.long, self.lat),
            
        )
        self.assertTrue(isinstance(geo_point, GeoPoint))
        self.assertEqual(GeoPoint.objects.count(), 1)
        self.assertEqual(self.name, geo_point.name)
       
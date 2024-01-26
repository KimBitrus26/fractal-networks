
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point


class GeoPoint(models.Model):
    """
    A model to utilize postgis
    
    """
    name = models.CharField(max_length=255)
    location = models.PointField()

    def save(self, *args, **kwargs):

        if not self.pk:
            # Access latitude and longitude from the location field
            longitude, latitude = self.location.coords

            # Create a Point object from the provided coordinates
            point = Point(longitude, latitude)

            # Set the location field with the Point object
            self.location = point

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
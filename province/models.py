from django.db import models
from island.models import Island

class Province(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    image_url = models.URLField(blank=True, null=True)
    island = models.ForeignKey(Island, related_name='provinces' , null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.province

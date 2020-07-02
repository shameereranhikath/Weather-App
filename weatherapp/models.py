from django.db import models


# Create your models here.
class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='cities'

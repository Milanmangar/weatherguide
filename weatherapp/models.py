from django.db import models
from django.utils import timezone

class City(models.Model):
    name = models.CharField(max_length=50)
    pub_date = models.DateField(default=timezone.now)
    user_name = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'

class CityUser(models.Model):
    name = models.CharField(max_length=50)
    pub_date = models.DateField(default=timezone.now)
    user_name = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'citiesuser'

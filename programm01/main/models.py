from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=15)

    class Meta :
        db_table = 'citys'
        managed = False

    def __str__(self):
        return self.name

class Institution(models.Model):
    name = models.CharField(max_length=25)
    city = models.ForeignKey(City,on_delete=models.CASCADE,db_column='city_id')
    type = models.CharField(max_length=15)
    description = models.CharField(max_length=200,db_column='discriptions')
    adress = models.CharField(max_length=25)
    website = models.CharField(max_length=35)

    class Meta:
        db_table = 'institutions'
        managed = False

    def __str__(self):
        return self.name







from django.db import models

# Create your models here.
class MyModel(models.Model):
    Rank = models.IntegerField()
    Name = models.CharField()
    Platform = models.CharField()
    Year = models.IntegerField()
    Genre = models.CharField()
    Publisher = models.CharField()
    NA_Sales = models.FloatField()
    EU_Sales = models.FloatField()
    JP_Sales = models.FloatField()
    Other_Sales = models.FloatField()
    Global_Sales = models.FloatField()


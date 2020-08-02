from django.db import models

# Create your models here.
class Stock_prediction(models.Model):
   title = models.CharField(max_length=140)
   uuid = models.CharField(max_length=36)
   start_month = models.IntegerField()
   start_day = models.IntegerField()
   start_year = models.IntegerField()
   end_month = models.IntegerField()
   end_day = models.IntegerField()
   end_year = models.IntegerField()
   ticker_symbol = models.CharField(max_length=20)




class Balance_sheet(models.Model):
   title = models.CharField(max_length=140)
   uuid = models.CharField(max_length=36)
   upload = models.FileField(upload_to='uploads/')

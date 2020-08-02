from django.contrib import admin
from .models import Stock_prediction, Balance_sheet

# Register your models here.
admin.site.register(Stock_prediction)
admin.site.register(Balance_sheet)

from django import forms
from.import models

class SearchStock(forms.ModelForm):
    class Meta:
        model = models.Stock_prediction
        fields = ['title', 'uuid', 'start_month', 'start_day', 'start_year', 'end_month', 'end_day', 'end_year', 'ticker_symbol']





class BalanceSheet(forms.ModelForm):
    class Meta:
        model = models.Balance_sheet
        fields = ['title', 'uuid', 'upload']
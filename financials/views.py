from django.shortcuts import render
from django.http import HttpResponse
from.import forms
from .models import Stock_prediction, Balance_sheet
#from .util import randomUUID

import pandas as pd
import pandas_datareader.data as web
import yfinance as yf
yf.pdr_override()
"""
from sklearn import linear_model
import matplotlib.pyplot as plt
import io
import urllib, base64
"""
import datetime


# Create your views here.

def balance(request):
    if request.method == 'POST':
        form = forms.BalanceSheet(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            """
            instance = form.save(commit=False)
            instance.uuid = randomUUID
            instance.save()
            """
    else:
        form = forms.BalanceSheet()

    return render(request, 'balance.html', locals())

def balance_list(request):
    articles = Balance_sheet.objects.all().order_by('id');

    return render(request, 'balance_list.html', locals())

def balance_detail(request, slug):
    sheet = Balance_sheet.objects.get(title=slug)
    link = str(sheet.upload)
    file = open('media/' + link, 'rt')
    file_content = file.read()
    file.close()
    return HttpResponse(file_content, content_type="text/plain")



def cashflow(request):
    if request.method == 'POST':
        form = forms.SearchStock()
    else:
        form = forms.SearchStock()

    return render(request, 'stockpredict.html', locals())

def cashflow_list(request):
    articles = Stock_prediction.objects.all().order_by('id');
    return render(request, 'stockpredict_list.html', locals())

def cashflow_detail(request, slug):
    stock = Stock_prediction.objects.get(title=slug)

    title = str(stock.ticker_symbol)

    a = int(stock.start_year)
    b =int(stock.start_month)
    c = int(stock.start_day)

    d = int(stock.end_year)
    e = int(stock.end_month)
    f = int(stock.end_day)
    start = datetime.datetime(a, b, c)
    end = datetime.datetime(d, e, f)

    stock_pick = web.DataReader(title, start, end)
    df = pd.DataFrame(stock_pick)
    #web.seoption('display.max_columns', 500)
    html = df.to_html
    #html.head()

    return HttpResponse(html, content_type="text/plain")



def income(request):
    """
    dataframe = pd.read_fwf('media/uploads/brain_body')  # .txt file
    x_values = dataframe[['Brain']]
    y_values = dataframe[['Body']]

    # plt.plot(range(12))
    plt.scatter(x_values, y_values)
    plt.plot(x_values, x_values)
    fig = plt.gcf()

    buffer = io.BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)
    string = base64.b64encode(buffer.read())
    uric = urllib.parse.quote(string)

    form = forms.SearchStock()

    if request.method == 'POST':
        form = forms.SearchStock()

        new_stock_serach = Stock_prediction()
        """
    start = datetime.datetime(2010, 1, 1)
    end = datetime.datetime(2017, 1, 11)

    df = web.DataReader("AAPL",  start, end)
    html = df.to_html



    return HttpResponse(html, content_type="text/plain")
    #return render(request, 'buysellhold.html', locals())
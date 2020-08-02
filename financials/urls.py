from django.conf.urls import url
from . import views
from mindbalance import views as main_views


app_name = 'finance'

urlpatterns = [
    url(r'^balance/', views.balance, name='balance'),
    url(r'^balance_list/', views.balance_list, name='balance_list'),
    url(r'^balance_detail/(?P<slug>[\w-]+)/$', views.balance_detail, name='balance_detail'),
    url(r'^cashflow/', views.cashflow, name='cashflow'),
    url(r'^cashflow_list/', views.cashflow_list, name='cashflow_list'),
    url(r'^cashflow_detail/(?P<slug>[\w-]+)/$', views.cashflow_detail, name='cashflow_detail'),
    url(r'^income/', views.income, name='income'),
    url(r'^index/', main_views.index, name='index'),
]

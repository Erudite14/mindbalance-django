from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.balance),
    url(r'^cash/', views.about),
    #url(r'^$'),flow
]

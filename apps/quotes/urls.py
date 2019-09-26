from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^myaccount/(?P<id>\d+)$', views.myaccount),
    url(r'^quotes$', views.quotes),
    url(r'^quotes/add$', views.addQuote),
    url(r'^quotes/new$', views.createQuote),
    url(r'^quotes/(?P<id>\d+)$', views.showQuote)
    # url(r'^user/(?P<user_id>\d+)$', views.showUser),
]

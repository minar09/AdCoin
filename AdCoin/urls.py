import os

from django.conf.urls import *  # @UnusedWildImport 
from django.conf.urls import patterns, url
from AdCoin.views import *  # @UnusedWildImport

static = os.path.join(os.path.dirname(__file__), 'static')


urlpatterns = patterns('',

    url(r'^$', HomePage),
    url(r'^Home/$', HomePage),
)
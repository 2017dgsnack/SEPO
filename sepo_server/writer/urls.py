#from django.urls import path
from django.conf.urls import include,url
from community.views import post_community
from . import views
from writer.views import test_writer


urlpatterns = [
#	path('', views.index, name = 'index'),
	url(r'^$',test_writer),
]


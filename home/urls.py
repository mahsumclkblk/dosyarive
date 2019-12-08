from django.conf.urls import url
from home.views import *
app_name="home"

urlpatterns = [
    url(r'^/$',home_page,name="home"),
]
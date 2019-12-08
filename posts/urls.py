from django.conf.urls import url
from posts.views import *
app_name="post"

urlpatterns = [
    url(r'^index/$',post_index,name="index"),
    url(r'^create/$',post_create,name="create"),
    url(r'^detail/(?P<id>\d+)/$',post_detail,name="detail"),
    url(r'^update/(?P<id>\d+)/$',post_update,name="update"),
    url(r'^delete/(?P<id>\d+)/$',post_delete,name="delete"),
]
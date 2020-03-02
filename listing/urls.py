from django.conf.urls import url
from .views import add_property, view_property

urlpatterns = [
    url(r'^$', view_property, name='view_property'),
   # url(r'^(?P<pk>\d+)/$', full_listing, name='view_Listing'),
    url(r'^add_property/$', add_property, name='add_property'),
   # url(r'^(?P<pk>\d+)/edit/$', add_edit_listing, name='edit_property')
]
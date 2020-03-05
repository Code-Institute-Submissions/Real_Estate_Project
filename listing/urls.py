from django.conf.urls import url
from .views import add_property, view_property, property_detail, edit_property, delete


urlpatterns = [
    url(r'^$', view_property, name='view_property'),
    url(r'^(?P<pk>\d+)/$', property_detail, name='property_detail'),
    url(r'^add_property/$', add_property, name='add_property'),
    url(r'^(?P<pk>\d+)/edit_property/$', edit_property, name='edit_property'),
    url(r'^delete/(?P<pk>\d+)/$', delete, name="delete")
]
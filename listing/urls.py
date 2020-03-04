from django.conf.urls import url
from .views import add_property, view_property, property_detail


urlpatterns = [
    url(r'^$', view_property, name='view_property'),
    url(r'^(?P<pk>\d+)/$', property_detail, name='property_detail'),
    url(r'^add_property/$', add_property, name='add_property'),
    # url(r'^(?P<pk>\d+)/edit/$', add_edit_listing, name='edit_property')
]
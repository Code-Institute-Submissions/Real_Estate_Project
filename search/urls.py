from django.conf.urls import url
from .views import buy_search, rent_search, agency_search

urlpatterns = [
    url(r'^buy_search/$', buy_search, name='buy_search'),
    url(r'^rent_search/$', rent_search, name='rent_search'),
    url(r'^agency_search/$', agency_search, name='agency_search')
]

# (?P<pk>\d+)/
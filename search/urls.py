from django.conf.urls import url
from .views import buy_search, rent_search, search_all

urlpatterns = [
    url(r'^$', search_all, name='search'),
    url(r'^buy_search/$', buy_search, name='buy_search'),
    url(r'^rent_search/$', rent_search, name='rent_search'),
]

# (?P<pk>\d+)/
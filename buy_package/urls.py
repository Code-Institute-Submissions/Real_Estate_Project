from django.conf.urls import url
from .views import buy_package, add_to_buy_package, adjust_buy_package

urlpatterns = [
    url(r'^$', buy_package, name='buy_package'),
    url(r'^add/(?P<id>\d+)', add_to_buy_package, name='add_to_buy_package'),
    url(r'^adjust/(?P<id>\d+)', adjust_buy_package, name='adjust_buy_package'),
]
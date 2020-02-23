from django.conf.urls import url
from .views import payout

urlpatterns = [
    url(r'^$', payout, name='payment'),
]
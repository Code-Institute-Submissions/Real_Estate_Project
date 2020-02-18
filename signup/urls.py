from django.conf.urls import url
from signup.views import signup

urlspattern = [

    url(r'^signup/$', signup, name=signup),

]
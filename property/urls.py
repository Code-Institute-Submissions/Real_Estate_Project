"""property URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import index
from accounts import urls as urls_accounts
from signup.views import signup
from buy_package import urls as urls_buy_package
from payment.views import payout
from listing import urls as urls_listing
from search import urls as urls_search


from django.views import static
from .settings import MEDIA_ROOT


urlpatterns = [    
    
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^signup/', signup, name="signup"),
    url(r'^buy_package/', include(urls_buy_package)),
    url(r'^payout/', payout, name="payment"),
    url(r"^listing/", include(urls_listing)),
    url(r"^search/", include(urls_search)),

    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),

]

from django.conf.urls import patterns, include, url
from django.contrib import admin

from core.views import HomePageView


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^api/', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

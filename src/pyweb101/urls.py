from django.conf.urls import patterns, include, url
from django.contrib import admin

from profiles.views import LandingPageHypothesisView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', LandingPageHypothesisView.as_view(), name='landing-page'),
    url(r'^admin/', include(admin.site.urls)),
)

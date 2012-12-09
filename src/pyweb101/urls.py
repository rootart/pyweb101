from django.conf.urls import patterns, include, url
from django.contrib import admin

from profiles.views import LandingPageHypothesisView
from profiles.api import LHResource

admin.autodiscover()

landinghypothesis_resource = LHResource()

urlpatterns = patterns('',
    url(r'^$', LandingPageHypothesisView.as_view(), name='landing-page'),
    url(r'^section/*', LandingPageHypothesisView.as_view(), name='landing-page-section'),
    url(r'^api/', include(landinghypothesis_resource.urls)),
    url(r'^admin/', include(admin.site.urls)),
)

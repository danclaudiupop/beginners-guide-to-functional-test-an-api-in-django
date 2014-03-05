from django.conf.urls import patterns, url

from rest_framework.urlpatterns import format_suffix_patterns

from albumreview import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index_view, name='index_view'),
    url(r'^musicians/$', views.MusicianView.as_view(), name='musician-list'),
    url(r'^musician/(?P<pk>[\d]+)/$', views.MusicianInstanceView.as_view(), name='musician-instance'),
)

urlpatterns = format_suffix_patterns(urlpatterns)

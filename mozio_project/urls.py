from django.conf.urls import patterns, include, url
from django.contrib import admin
from mozio_app import views

admin.autodiscover()

urlpatterns = patterns('',
                       # Areas
                       url(r'^map/list$',
                           views.areas.list, name='map-list'),
                       url(r'^map/add$',
                           views.areas.save, name='map-create'),
                       url(r'^map/update/(?P<pk>[-\w]+)/$',
                           views.areas.save, name='map-update'),
                       url(r'^map/delete/(?P<pk>[-\w]+)/$',
                           views.areas.delete, name='map-delete'),

                       # Providers
                       url(r'^provider/list$',
                           views.provider.list, name='provider-list'),
                       url(r'^provider/add$',
                           views.provider.save, name='provider-create'),
                       url(r'^provider/update/(?P<pk>[-\w]+)/$',
                           views.provider.save, name='provider-update'),
                       url(r'^provider/delete/(?P<pk>[-\w]+)/$',
                           views.provider.delete, name='provider-delete'),

                       # Examples:
                       # url(r'^$', 'mozio_project.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       )


urlpatterns += patterns(
    'django.contrib.staticfiles.views',
    url(r'assets/(?P<path>.*)$', 'serve'),
)

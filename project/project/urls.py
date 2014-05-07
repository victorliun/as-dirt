from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('apps.home.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
#urlpatterns += patterns('',
#    (r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),)

urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
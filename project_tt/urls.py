from django.conf.urls import patterns, include, url
from catalog.views import CatalogList

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', CatalogList.as_view(), name='home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

import project_tt.settings
if project_tt.settings.DEBUG:
    from django.conf import settings
    from django.conf.urls.static import static
    urlpatterns = urlpatterns + static(project_tt.settings.STATIC_URL, document_root=project_tt.settings.STATIC_ROOT)

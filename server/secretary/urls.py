from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'secretary.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^user/', include('useraccounts.urls')),
    url(r'^diary/', include('diary.urls')),
    url(r'^notes/', include('notes.urls')),
    url(r'^pages/', include('pages.urls')),
    url(r'^tags/', include('tags.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

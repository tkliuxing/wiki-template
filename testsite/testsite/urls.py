from __future__ import absolute_import
from __future__ import unicode_literals
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.http.response import HttpResponse
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^robots.txt', lambda _: HttpResponse('User-agent: *\nDisallow: /')),
    url(r'^notifications/', include('django_nyt.urls')),
    url(r'', include('wiki.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

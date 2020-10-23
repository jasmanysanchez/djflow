from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from djflow.apps.chat import views
from djflow.core.json_settings import get_settings
from django.views.static import serve

settings_json = get_settings()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('djflow.apps.website.urls')),
    url(r'^chat/', include('djflow.apps.chat.urls'), name='room'),
    url(r'^flow/', include('djflow.apps.flow.urls')),
    url(r'^security/', include('djflow.apps.security.urls')),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

if settings_json["DEBUG"]:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

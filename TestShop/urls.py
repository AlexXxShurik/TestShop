from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from django.views.static import serve


from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('minishop.urls'), name='index')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        re_path(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        re_path(f'^{settings.STATIC_URL.lstrip("/")}(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
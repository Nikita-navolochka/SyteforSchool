from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Main.urls', namespace='Main')),
    
    # Этот префикс + пустой путь из файла выше дадут адрес /lisiskus/
    path('lisiskus/', include('lisiskus.urls', namespace='lisiskus')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
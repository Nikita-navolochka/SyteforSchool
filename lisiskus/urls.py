from django.urls import path
from django.http import HttpResponse
from pathlib import Path


app_name = 'lisiskus'
# Определяем папку текущего приложения
APP_DIR = Path(__file__).resolve().parent
# Формируем путь: /имя_приложения/custom_pages/about.html
HTML_FILE_PATH = APP_DIR / 'custom_pages' / 'index.html'

urlpatterns = [
    path('about/', lambda request: HttpResponse(
        open(HTML_FILE_PATH, 'r', encoding='utf-8').read(), 
        content_type='text/html'
    )),
]
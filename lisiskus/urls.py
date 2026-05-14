from django.urls import path
from django.http import HttpResponse, FileResponse
from pathlib import Path

app_name = 'lisiskus'

# Путь к папке lisiskus/custom_pages/
APP_DIR = Path(__file__).resolve().parent
PAGES_DIR = APP_DIR / 'custom_pages'

# Функция для отдачи картинок (бинарный режим)
def serve_image(request, img_name):
    img_path = PAGES_DIR / 'img' / img_name
    if img_path.exists():
        return FileResponse(open(img_path, 'rb'))
    return HttpResponse("Картинка не найдена", status=404)

urlpatterns = [
    # Пустая строка '' означает, что путь совпадает с главным префиксом /lisiskus/
    path('', lambda request: HttpResponse(
        open(PAGES_DIR / 'index.html', 'r', encoding='utf-8').read(), 
        content_type='text/html'
    ), name='index'),

    # Маршруты для ресурсов, чтобы работали стили, скрипты и ссылки
    path('2.html', lambda request: HttpResponse(open(PAGES_DIR / '2.html', 'r', encoding='utf-8').read(), content_type='text/html')),
    path('main.css', lambda request: HttpResponse(open(PAGES_DIR / 'main.css', 'r', encoding='utf-8').read(), content_type='text/css')),
    path('main.js', lambda request: HttpResponse(open(PAGES_DIR / 'main.js', 'r', encoding='utf-8').read(), content_type='application/javascript')),
    path('img/<str:img_name>', serve_image),
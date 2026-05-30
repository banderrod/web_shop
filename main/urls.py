from django.urls import path
from .views import home, product_list

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home),
    path('products/', product_list, name='product_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
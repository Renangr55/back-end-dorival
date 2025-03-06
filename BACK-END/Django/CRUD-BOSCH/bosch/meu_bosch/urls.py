from django.urls import path
from . import views
from .views import livro_list
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.livro_read, name='livro_read'),
    path('novo/', views.livro_create, name='livro_create'),
    path('edit/<int:pk>', views.livro_update, name='livro_update'),
    path("delete/<int:pk>", views.livro_delete, name='livro_delete'),
    path("livros/", views.livro_list, name='livro_list'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

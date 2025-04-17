from .views import PatoListCreateAPIView , PatoRetrieveUpdateDestroyAPIView , loginView2
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('patos/',PatoListCreateAPIView.as_view(), name='pato-list_create'),
    path('patos/<int:pk>/', PatoRetrieveUpdateDestroyAPIView.as_view(), name='pato específico'),
    #path('logar/', LoginView.as_view(), name='logar'),
    path('logar2/', loginView2.as_view(), name='login2')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
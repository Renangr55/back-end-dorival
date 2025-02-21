
from django.urls import path
from . import views

urlpatterns = [
    path("",views.Lista_produtos, name='Lista_produtos'),
    path("info/<int:produto_id>/", views.info_produto, name='info_produto'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('user/', view=views.createListUser),
    path('user/<int:pk>/', view=views.updateDelete)
    
]
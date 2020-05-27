from django.urls import path
from . import views

urlpatterns = [
    path('', views.read, name="home"),
    path('newblog/', views.create, name="create"),
    path('update/<int:pk>', views.update, name="update"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('detali/<int:pk>', views.detail, name="detail"),
    
]
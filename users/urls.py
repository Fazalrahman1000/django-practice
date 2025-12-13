from django.urls import path
from users import views

urlpatterns = [
    path('create-user/', views.create_user, name='create_user'),
]
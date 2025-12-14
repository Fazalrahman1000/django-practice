from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('foods.urls')),
    path('', include('users.urls')),
    path('login/', LoginView.as_view(template_name = 'users/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html'), name="logout"),
]

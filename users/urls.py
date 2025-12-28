from django.urls import path
from users import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'user'

urlpatterns = [
    path('create-user/', views.create_user, name='create_user'),
    path('login/', LoginView.as_view(template_name = 'users/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html'), name="logout"),
    path('profile/', views.profilepage, name = 'profile'),
]
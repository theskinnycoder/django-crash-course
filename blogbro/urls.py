import users.views as users_views
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', users_views.register, name='register'),
    path('login/', LoginView.as_view(
        template_name='users/login.html',
        redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include('articles.urls')),
]

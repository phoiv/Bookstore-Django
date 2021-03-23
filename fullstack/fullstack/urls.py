from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('', include('bookstore.urls')),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html',
                                                  next_page='book-home'), name='logout'),
    #path('app/', include('app.urls')),
]

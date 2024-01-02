from django.urls import path
from . import views
from .views import postar_comentario
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView, login_required, logout_then_login
from django.urls import path, re_path
from .views import profile
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', views.home, name="admin"),
    path('postar_comentario/', views.home, name="postar_comentario"),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('login/', LoginView.as_view(template_name='twitter/login.html'), name='login'),
    path('logout', views.logout_user, name='logout'),
    path('profile_list/', views.profile_list, name='profile_list'),

    path('register/', views.register_user, name='register'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
    path('editar/', views.editar, name='editar'),
    path('update_user/', views.update_user, name='update_user'),
    path('meep_like/<int:pk>', views.meep_like, name="meep_like"),
    path('postar_comentario/', postar_comentario, name='postar_comentario'),
]

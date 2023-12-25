from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static 
from django.contrib.auth import views as auth_views

app_name = "clientes_app"

urlpatterns = [
    path('', views.Inicio.as_view(), name='inicio'),
    path('login/', auth_views.LoginView.as_view(template_name = "crud/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = "crud/login.html"), name='logout'),
    path('compras/', views.Compras.as_view(), name='compras'),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
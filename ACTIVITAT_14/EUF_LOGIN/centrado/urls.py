from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('crear-usuario/', views.create_user, name='crear-usuario'),
    path('pagina-principal/', views.page_home, name='pagina-principal'),
    path('iniciar-sesion/', views.login_page, name='iniciar-sesion'),
    path('cerrar-sesion/', views.log_out, name='cerrar_sesion'),

]
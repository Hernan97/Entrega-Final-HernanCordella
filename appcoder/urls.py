from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from appcoder.views import *
from . import views
from .views import profile_view, register_view


urlpatterns = [
    path('', inicio, name="inicio"),
    path('cursos/', cursos, name="cursos"),
    path('precios/', precios, name="precios"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('profesores/', profesores, name="profesores"),
    path('entregables/', entregables, name="entregables"),
    path('blog/', blog, name='blog'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('login_register/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('newpost/', newpost, name='newpost'),
    path('register/', register_view, name="user_register"),  
    path('crearcurso/', crearcurso, name="crearcurso"),
    path('crearestudiante/', crearestudiante, name="crearestudiante"),
    path('workingpage/', workingpage, name="workingpage"),
    path('workingpage2/', workingpage2, name="workingpage2"),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/edit/', edit_post, name='edit_post'),
    path('post/<int:post_id>/delete/', delete_post, name='delete_post'),
    path('chat/', views.chat, name='chat'),
    path('chat/<int:receiver_id>/', views.chat_with_user, name='chat_with_user'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





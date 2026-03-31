from django.urls import path
from .views import detalhar_post, filtrar_posts

urlpatterns = [
    path('posts/<int:id>/', detalhar_post),
    path('posts/filtrar/', filtrar_posts), 
]
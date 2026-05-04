from django.urls import path
from .views import detalhar_post, filtrar_posts, criar_comentario

urlpatterns = [
    path('posts/<int:id>/', detalhar_post),
    path('posts/filtrar/', filtrar_posts),
    path('posts/criar/', criar_comentario),
]
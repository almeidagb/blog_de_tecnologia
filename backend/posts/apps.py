# posts/apps.py
from django.apps import AppConfig


class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'

    def ready(self):
        # IMPORTAÇÃO DENTRO DO MÉTODO READY
        from .models import Post, Comentario

        # Evita criar posts duplicados
        if not Post.objects.exists():
            # Cria o post e salva numa variável
            post = Post.objects.create(
                titulo="Meu primeiro post",
                conteudo="Conteúdo de teste"
            )

            # Cria comentário inicial para esse post
            Comentario.objects.create(
                post=post,  # <-- usa a variável correta
                autor="Admin",
                texto="Este é um comentário inicial."
            )
from django.db import models

# Create your models here.
from django.db import models

class Post(models.Model):
    
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.CharField(max_length=100)
    texto = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'comentário de {self.autor}'
    
    

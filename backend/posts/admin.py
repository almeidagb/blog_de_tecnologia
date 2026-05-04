from django.contrib import admin

from .models import Post, Comentario

admin .site.register(Post)
admin .site.register(Comentario) #para registrar no painel admin django
# Register your models here.

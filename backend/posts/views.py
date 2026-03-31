from django.http import JsonResponse
from .models import Post, Comentario
import json

def detalhar_post(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return JsonResponse({'erro': 'Post não encontrado'}, status=404)

    # GET → ver post + comentários
    if request.method == 'GET':
        comentarios = list(post.comentarios.values())

        return JsonResponse({
            'id': post.id,
            'titulo': post.titulo,
            'conteudo': post.conteudo,
            'comentarios': comentarios
        })

    # POST → criar comentário
    elif request.method == 'POST':
        try:
            dados = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'erro': 'JSON inválido'}, status=400)

        if not dados.get('autor') or not dados.get('texto'):
            return JsonResponse({'erro': 'autor e texto são obrigatórios'}, status=400)

        Comentario.objects.create(
            post=post,
            autor=dados.get('autor'),
            texto=dados.get('texto')
        )

        return JsonResponse({'mensagem': 'Comentário criado com sucesso'}, status=201)

    # Método não permitido
    return JsonResponse({'erro': 'Método não permitido'}, status=405)

def filtrar_posts(request):
    """
    Filtra posts pelo título usando query param ?q=palavra
    Exemplo: /api/posts/filtrar/?q=teste
    """
    if request.method != 'GET':
        return JsonResponse({'erro': 'Método não permitido'}, status=405)

    query = request.GET.get('q', '')  # pega o parâmetro 'q' da URL
    if query:
        posts = Post.objects.filter(titulo__icontains=query)
    else:
        posts = Post.objects.all()

    resultado = []
    for post in posts:
        # inclui comentários de cada post
        comentarios = list(post.comentarios.values())
        resultado.append({
            'id': post.id,
            'titulo': post.titulo,
            'conteudo': post.conteudo,
            'comentarios': comentarios
        })

    return JsonResponse(resultado, safe=False)
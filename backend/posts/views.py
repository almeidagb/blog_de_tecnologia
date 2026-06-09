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
    #deletar o post
    elif request.method == 'DELETE':
        post.delete()
        return JsonResponse({'mensagem': 'Post deletado com sucesso'}, status=200)
    
    return JsonResponse({'erro': 'Método não permitido'}, status=405)
    
    
    
def criar_comentario(request, id):
    # POST → criar comentário
    if request.method == 'POST':
        try:
            # Correção: alterado de request.id para request.body
            dados = json.loads(request.body) 
        except json.JSONDecodeError:
            return JsonResponse({'erro': 'JSON inválido'}, status=400)

        if not dados.get('autor') or not dados.get('texto'):
            return JsonResponse({'erro': 'autor e texto são obrigatórios'}, status=400)
        
        try:
            post = Post.objects.get(id=id)
        except Post.DoesNotExist:
            return JsonResponse({'erro': 'Post não encontrado'}, status=404)

        return JsonResponse({'mensagem': 'Comentário criado com sucesso'}, status=201)
    
    return JsonResponse({'erro': 'Método não permitido'}, status=405)


    
def deletar_comentario(request, id):
    """
    DELETE → Deleta um comentário específico pelo ID dele
    """
    if request.method == 'DELETE':
        try:
            comentario = Comentario.objects.get(id=id)
            comentario.delete()
            return JsonResponse({'mensagem': 'Comentário deletado com sucesso'}, status=200)
        except Comentario.DoesNotExist:
            return JsonResponse({'erro': 'Comentário não encontrado'}, status=404)
            
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
        comentarios = list(post.comentarios.values())
        resultado.append({
            'id': post.id,
            'titulo': post.titulo,
            'conteudo': post.conteudo,
            'comentarios': comentarios
        })

    return JsonResponse(resultado, safe=False)

def ediar(request, id):
    """
    PUT → Edita um post específico pelo ID recebido
    """
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return JsonResponse({'erro': 'Post não encontrado'}, status=404)

    if request.method == 'PUT':
        try:
            dados = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'erro': 'JSON inválido'}, status=400)

    
        post.titulo = dados.get('titulo', post.titulo)
        post.conteudo = dados.get('conteudo', post.conteudo)

       
        if not post.titulo or not post.conteudo:
            return JsonResponse({'erro': 'titulo e conteudo não podem ser vazios'}, status=400)

        post.save()

        return JsonResponse({
            'mensagem': 'Post atualizado com sucesso',
            'id': post.id,
            'titulo': post.titulo,
            'conteudo': post.conteudo
        }, status=200)

    return JsonResponse({'erro': 'Método não permitido'}, status=405)

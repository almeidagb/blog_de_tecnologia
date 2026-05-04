# Blog de Tecnologia

> [!NOTE]
> ### Qual é o tema do seu sistema?
O tema do sistema é um blog de tecnologia, onde usuários podem:

- Visualizar posts sobre tecnologia  
- Ler comentários relacionados aos posts  
- Criar comentários nos posts  

Ou seja, é um sistema de publicação de conteúdo e interação via comentários.

---

> [!IMPORTANT]
> ### Quais são as funcionalidades esperadas?

Com base no seu código e rotas:

- **Listar e detalhar posts** – cada post mostra título, conteúdo e comentários associados  
  - Rota: `/api/posts/<id>/` (GET)

- **Criar comentários** – usuários podem enviar comentários em posts existentes  
  - Rota: `/api/posts/<id>/` (POST)

- **Filtrar posts por título** – permite buscar posts por palavra-chave  
  - Rota: `/api/posts/filtrar/?q=palavra` (GET)

- **Administração via Django Admin** – adicionar, editar ou deletar posts e comentários  
  - Rota: `/admin/`

💡 Funcionalidades extras que você pode adicionar depois:
- Autenticação de usuários para comentar  
- Curtidas ou reações nos posts  
- Categorias ou tags de posts  

---

> [!TIP]
> ### Quais serão os dados armazenados?

Baseado no `models.py` do seu projeto:

#### 📌 Post
- `titulo` (CharField) → título do post  
- `conteudo` (TextField) → conteúdo do post  
- `data_criacao` (DateTimeField) → data/hora de criação  

#### 💬 Comentario
- `post` (ForeignKey para Post) → post relacionado  
- `autor` (CharField) → nome de quem comentou  
- `texto` (TextField) → conteúdo do comentário  
- `data` (DateTimeField) → data/hora do comentário  
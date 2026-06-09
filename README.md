# Blog de Tecnologia

Sistema de blog com Django REST Framework e PostgreSQL.

## 🚀 Quick Start

### Pré-requisitos
- Docker e Docker Compose instalados

### Executar com Docker Compose

```bash
docker compose up -d
```

Acesse em: **http://localhost:8000**

### Usar a imagem do Docker Hub

```bash
docker pull gabitcha/blog-de-tecnologia:latest
docker run -d -p 8000:8000 gabitcha/blog-de-tecnologia:latest
```

## ⚙️ Configuração

Crie um arquivo `.env` na raiz:

```
DB_NAME=blogtech
DB_USER=blog_user
DB_PASSWORD=blog_password
DEBUG=True
SECRET_KEY=chave-segura
```

## 📚 Endpoints

- **Listar posts**: `GET /api/posts/`
- **Detalhar post**: `GET /api/posts/<id>/`
- **Criar comentário**: `POST /api/posts/<id>/`
- **Filtrar posts**: `GET /api/posts/filtrar/?q=palavra`
- **Admin Django**: `GET /admin/`

## 🛑 Parar os containers

```bash
docker compose down
```

## 📦 Tecnologias

- Django 5.2 + Django REST Framework
- PostgreSQL 16
- Python 3.12
- Docker

---

> [!NOTE]
> ### Funcionalidades do sistema

O sistema permite:
- Visualizar posts sobre tecnologia
- Ler comentários nos posts
- Criar comentários nos posts
- Administração via Django Admin

---

> [!TIP]
> ### Dados armazenados

**Post**: título, conteúdo, data de criação

**Comentário**: post relacionado, autor, texto, data

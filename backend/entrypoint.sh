echo "Verificando o banco de dados..."

echo "Aplicando as migrações no banco de dados..."
python manage.py migrate

echo "Criando superuser..."
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("Superuser 'admin' criado com sucesso!")
else:
    print("Superuser 'admin' já existe!")
END

echo "Iniciando o servidor Python..."

exec "$@"

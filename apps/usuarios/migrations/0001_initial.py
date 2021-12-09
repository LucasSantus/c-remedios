
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=30, unique=True, verbose_name='Nome')),
                ('sigla', models.CharField(max_length=2, unique=True, verbose_name='Sigla')),
                ('dataHorarioCriacao', models.DateTimeField(auto_now_add=True, verbose_name='Data e hora de criação')),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
                'ordering': ['descricao'],
            },
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, verbose_name='Nome')),
                ('codigo_IBGE', models.IntegerField(verbose_name='Código do IBGE')),
                ('dataHorarioCriacao', models.DateTimeField(auto_now_add=True, verbose_name='Data e hora de criação')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estado_CidadeFK', to='usuarios.estado')),
            ],
            options={
                'verbose_name': 'Cidade',
                'verbose_name_plural': 'Cidades',
                'ordering': ['descricao'],
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nome', models.CharField(max_length=60, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=150, verbose_name='Sobrenome')),
                ('email', models.EmailField(max_length=194, unique=True, verbose_name='E-mail')),
                ('cpf', models.CharField(max_length=14, unique=True, verbose_name='CPF')),
                ('dataNascimento', models.DateField(blank=True, null=True, verbose_name='Data de nascimento')),
                ('genero', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro'), ('P', 'Prefiro não dizer')], max_length=1, null=True, verbose_name='Genero')),
                ('telefone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefone')),
                ('cep', models.CharField(blank=True, max_length=9, null=True, verbose_name='CEP')),
                ('bairro', models.CharField(blank=True, max_length=50, null=True, verbose_name='Bairro')),
                ('logradouro', models.CharField(blank=True, max_length=100, null=True, verbose_name='Logradouro')),
                ('complemento', models.CharField(blank=True, max_length=50, null=True, verbose_name='Complemento')),
                ('numeroResidencial', models.CharField(blank=True, max_length=10, null=True, verbose_name='Número da residência')),
                ('idGroup', models.IntegerField(blank=True, default=1, null=True, verbose_name='Id do grupo')),
                ('is_active', models.BooleanField(default=True, verbose_name='Usuário ativo')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Usuário desenvolvedor')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Super usuário')),
                ('cidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cidade_UsuarioFK', to='usuarios.cidade')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
        ),
    ]

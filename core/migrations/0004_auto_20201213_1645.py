# Generated by Django 3.1.4 on 2020-12-13 19:45

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201213_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=100, verbose_name='NOME')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='PREÇO')),
                ('vagas', models.IntegerField(verbose_name='VAGAS')),
                ('imagem', stdimage.models.StdImageField(upload_to='curso', verbose_name='Imagem')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=100, verbose_name='Slug')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Cursos',
        ),
    ]
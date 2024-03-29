# Generated by Django 4.0.5 on 2022-06-06 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('categoria', models.CharField(max_length=30)),
                ('capa', models.ImageField(upload_to='capa_livro')),
                ('autor', models.CharField(max_length=30, null=True)),
                ('data_publicacao', models.DateField()),
                ('pag', models.IntegerField(default=0)),
            ],
        ),
    ]

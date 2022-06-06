from django.db import models



class Livro(models.Model):

    nome = models.CharField(max_length=50, unique=True)

    categoria = models.CharField(max_length=30)

    capa = models.ImageField(upload_to='capa_livro')

    autor = models.CharField(max_length=30, null=True)

    data_publicacao = models.DateField()

    pag = models.IntegerField(default=0)


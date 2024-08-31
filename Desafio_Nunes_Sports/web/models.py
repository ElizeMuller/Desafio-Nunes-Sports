from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.CharField(max_length=200)
    imagem=models.ImageField(upload_to="web/static/images/",null=True,blank=True,)

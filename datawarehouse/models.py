from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Fornecedor(models.Model):
	nome = models.CharField(max_length = 100)
	cnpj = models.CharField(max_length = 20)
	telefone = models.CharField(max_length = 20)	

class Produto (models.Model):
	nome = models.CharField(max_length = 100)
	descricao = models.CharField(max_length = 250)
	foto = models.ImageField(upload_to= 'produto/')
	preco = models.FloatField()
	fornecedor = models.ForeignKey(Fornecedor, on_delete = models.CASCADE)

	def __str__(self):
		return self.nome


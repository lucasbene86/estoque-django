from django.db import models


class DadoProduto(models.Model):
    produto = models.CharField('Descrição', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    codigo_produto = models.IntegerField('Código')

    def __str__(self):
        return self.produto
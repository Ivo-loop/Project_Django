from djongo import models


class Produto(models.Model):
    _id = models.ObjectIdField()
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.CharField(max_length=20)
    object = models.DjongoManager()

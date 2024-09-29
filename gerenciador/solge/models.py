from django.db import models # type: ignore

# Create your models here.
class Produto(models.Model):
    nome = models.TextField()
    preco = models.FloatField()
    codigo_de_barras = models.TextField()
    
    def __str__(self):   # Model string representation
        return self.nome
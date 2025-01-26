from django.db import models
from django.contrib.auth.models import User  # Importa o modelo de usuário padrão do Django

class Autores(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=10)
    sobre_nome = models.CharField(max_length=20, null=True)
    nacionalidade = models.CharField(max_length=15, null=True)
    
    def __str__(self):
         return f"{self.nome} {self.sobre_nome}" if self.sobre_nome else self.nome
    
class Livros(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=40)
    sub_titulo = models.CharField(max_length=50, blank=True, null=True)
    genero = models.CharField(max_length=20)
    sinopse = models.TextField(blank=True, null=True)
    autor = models.ForeignKey(Autores, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Pedidos(models.Model):
    livro = models.ForeignKey(Livros, on_delete=models.CASCADE)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)  
    data_pedido = models.DateTimeField(auto_now_add=True)

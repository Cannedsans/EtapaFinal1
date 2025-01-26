# test_models.py
from django.test import TestCase
from biblioteca.models import Autores, Livros
from django.contrib.auth.models import User

class TestAutor(TestCase):
    def setUp(self):
        self.autor1 = Autores.objects.create(
            nome="João",
            sobre_nome="Silva",
            nacionalidade="Brasil"
        )
        self.autor2 = Autores.objects.create(
            nome="Maria",
            sobre_nome=None,
            nacionalidade="Portugal"
        )

    def test_autor_str(self):
        # Testando o método __str__ do modelo Autor
        self.assertEqual(str(self.autor1), "João Silva")
        self.assertEqual(str(self.autor2), "Maria")

class TestLivro(TestCase):
    def setUp(self):
        self.autor = Autores.objects.create(
            nome="Carlos",
            sobre_nome="Santos",
            nacionalidade="Brasil"
        )
        self.livro = Livros.objects.create(
            titulo="Python para Iniciantes",
            sub_titulo="Aprendendo programação",
            genero="Tecnologia",
            sinopse="Este livro ensina o básico de Python.",
            autor=self.autor
        )

    def test_livro_str(self):
        # Testando o método __str__ do modelo Livro
        self.assertEqual(str(self.livro), "Python para Iniciantes")


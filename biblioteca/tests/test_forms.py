# test_forms.py
from django.test import TestCase
from biblioteca.forms import AutorForm, LivroForm
from biblioteca.models import Autores, Livros

class TestAutorForm(TestCase):
    def test_form_valid(self):
        form_data = {'nome': 'João', 'sobre_nome': 'Silva', 'nacionalidade': 'Brasil'}
        form = AutorForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form_data = {'nome': '', 'sobre_nome': 'Silva', 'nacionalidade': 'Brasil'}
        form = AutorForm(data=form_data)
        self.assertFalse(form.is_valid())
    
    def test_sobrenome_opcional(self):
        form_data = {'nome': 'Maria', 'sobre_nome': '', 'nacionalidade': 'Portugal'}
        form = AutorForm(data=form_data)
        self.assertTrue(form.is_valid())

class TestLivroForm(TestCase):
    def setUp(self):
        self.autor = Autores.objects.create(
            nome="Carlos",
            sobre_nome="Santos",
            nacionalidade="Brasil"
        )

    def test_form_valid(self):
        form_data = {
            'titulo': 'Python Avançado',
            'sub_titulo': 'Desenvolvendo Aplicações',
            'genero': 'Tecnologia',
            'sinopse': 'Este livro é para quem já conhece o básico de Python.',
            'autor': self.autor.id
        }
        form = LivroForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form_data = {'titulo': '', 'genero': 'Tecnologia', 'autor': self.autor.id}
        form = LivroForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_subtitulo_opcional(self):
        form_data = {
            'titulo': 'Python Avançado',
            'genero': 'Tecnologia',
            'sinopse': 'Este livro é para quem já conhece o básico de Python.',
            'autor': self.autor.id
        }
        form = LivroForm(data=form_data)
        self.assertTrue(form.is_valid())

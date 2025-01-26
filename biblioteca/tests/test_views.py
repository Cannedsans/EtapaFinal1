from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from biblioteca.models import Livros, Autores, Pedidos
from django.contrib.messages import get_messages

class TestViews(TestCase):

    def setUp(self):
        # Criando um usuário para testar login
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.autor = Autores.objects.create(nome='Autor Teste', sobre_nome='Sobrenome Teste', nacionalidade='Brasileiro')
        self.livro = Livros.objects.create(titulo='Livro Teste', genero='Ficção', autor=self.autor)

    def test_index_view(self):
    # Loga o usuário antes de acessar a página
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


    def test_login_view(self):
        # Testa a view de login
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

        # Envia POST para fazer login
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertRedirects(response, reverse('home'))


    def test_adicionar_ao_carrinho(self):
        # Testa a adição de livros ao carrinho
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('adicionar_ao_carrinho', args=[self.livro.id]))
        self.assertRedirects(response, reverse('home'))

        # Verifica se o pedido foi criado
        pedido = Pedidos.objects.filter(cliente=self.user, livro=self.livro).exists()
        self.assertTrue(pedido)

    def test_finalizar_compra(self):
        # Testa a finalização da compra
        self.client.login(username='testuser', password='testpassword')
        Pedidos.objects.create(cliente=self.user, livro=self.livro)

        response = self.client.get(reverse('comprar'))
        self.assertRedirects(response, reverse('home'))

        # Verifica se os pedidos foram removidos após a compra
        pedidos = Pedidos.objects.filter(cliente=self.user)
        self.assertEqual(pedidos.count(), 0)

    def test_editar_livro(self):
        # Testa a edição de livro
        self.client.login(username='testuser', password='testpassword')
        url = reverse('editar_livro', args=[self.livro.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'editar_livro.html')

        # Envia o POST para editar
        response = self.client.post(url, {'titulo': 'Livro Editado', 'genero': 'Ficção', 'autor': self.autor.id})
        self.assertRedirects(response, reverse('home'))

        # Verifica se o livro foi atualizado
        self.livro.refresh_from_db()
        self.assertEqual(self.livro.titulo, 'Livro Editado')

    def test_adicionar_autor(self):
        # Testa a adição de um autor no admin
        self.client.login(username='testuser', password='testpassword')
        self.user.is_superuser = True
        self.user.save()
        response = self.client.get(reverse('gerir'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'adm.html')

        # Envia o POST para adicionar autor
        response = self.client.post(reverse('gerir'), {'submit_autor': 'submit_autor', 'nome': 'Novo Autor', 'sobre_nome': 'Novo Sobrenome', 'nacionalidade': 'Brasileiro'})
        self.assertRedirects(response, reverse('home'))

        # Verifica se o autor foi adicionado
        novo_autor = Autores.objects.filter(nome='Novo Autor').exists()
        self.assertTrue(novo_autor)

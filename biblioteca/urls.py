from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('login/', mlogin, name='login'),
    path('singup/', signup, name='cadastro'),
    path('carrinho/', listar_pedidos_usuario, name='carrinho'),
    path('remover/<int:pedido_id>/', tiralivro, name='remover_pedido'),
    path('sair', mlogout, name='sair'),
    path('gerir/', admin_page, name='gerir'),
    path('adicionar_ao_carrinho/<int:livro_id>/', adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('finalizar/', finalizar_compra, name='comprar'),
    path('editar_livro/<int:livro_id>/', editar_livro, name='editar_livro'),
    path('editar_autor/<int:autor_id>/', editar_autor, name='editar_autor'),
]

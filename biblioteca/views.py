from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.
@login_required
def index(request):
    autor_id = request.GET.get('autor')  # Pega o autor da URL
    if autor_id:
        livros = Livros.objects.filter(autor_id=autor_id)  # Filtra os livros do autor
        autor = Autores.objects.get(id=autor_id)  # Pega o autor
    else:
        livros = Livros.objects.all()  # Mostra todos os livros
        autor = None  # Nenhum autor selecionado
    autores = Autores.objects.all()  # Pega todos os autores
    
    return render(request, 'home.html', {'livros': livros, 'autores': autores, 'autor': autor})

def mlogin(request):
    if request.method == 'POST':
        form = CustomAutForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha incorretos")
    else:
        form = CustomAutForm()
    return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect('login')  
        else:
            messages.error(request, "Erro no cadastro. Verifique os dados.")
    else:
        form = UserCreationForm()

    return render(request, 'singup.html', {'form': form})

@login_required
def listar_pedidos_usuario(request):
    usuario_logado = request.user
    pedidos_usuario = Pedidos.objects.filter(cliente=usuario_logado)
    
    return render(request, 'carrinho.html', {'pedidos': pedidos_usuario})


def tiralivro(request, pedido_id):
    pedido = Pedidos.objects.get(id = pedido_id)
    pedido.delete()
    return redirect('carrinho')    

def mlogout(request):
    logout(request)
    return redirect('/')

def admin_page(request):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect('home')

    if request.method == 'POST':
        if 'submit_autor' in request.POST:
            autor_form = AutorForm(request.POST)
            if autor_form.is_valid():
                autor_form.save()
                return redirect('/')
        elif 'submit_livro' in request.POST:
            livro_form = LivroForm(request.POST)
            if livro_form.is_valid():
                livro_form.save()
                return redirect('/')
    else:
        autor_form = AutorForm()
        livro_form = LivroForm()

    context = {
        'autor_form': autor_form,
        'livro_form': livro_form,
    }
    return render(request, 'adm.html', context)

@login_required
def adicionar_ao_carrinho(request, livro_id):
    livro = Livros.objects.get(id=livro_id)
    cliente = request.user
    
    # Verifica se o livro já foi adicionado ao carrinho do cliente
    if not Pedidos.objects.filter(livro=livro, cliente=cliente).exists():
        Pedidos.objects.create(livro=livro, cliente=cliente)
        messages.success(request, "Livro adicionado ao carrinho!")
    else:
        messages.info(request, "Este livro já está no seu carrinho.")
    
    return redirect('home')

@login_required
def finalizar_compra(request):
    usuario_logado = request.user
    # Excluir todos os pedidos do usuário
    Pedidos.objects.filter(cliente=usuario_logado).delete()
    
    # Exibir uma mensagem de sucesso
    messages.success(request, "Compra finalizada e carrinho esvaziado!")
    
    return redirect('home')  # Redireciona para a página inicial após finalizar a compra

@login_required
def editar_livro(request, livro_id):
    livro = get_object_or_404(Livros, id=livro_id)
    
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            messages.success(request, "Livro editado com sucesso!")
            return redirect('home')
    else:
        form = LivroForm(instance=livro)
    
    return render(request, 'editar_livro.html', {'form': form, 'livro': livro})

@login_required
def editar_autor(request, autor_id):
    autor = get_object_or_404(Autores, id=autor_id)
    
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            messages.success(request, "Autor editado com sucesso!")
            return redirect('home')
    else:
        form = AutorForm(instance=autor)
    
    return render(request, 'editar_autor.html', {'form': form, 'autor': autor})
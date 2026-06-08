from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def cadastro(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            return redirect("login")

    return render(request, "cadastro.html")

def login_view(request):

    erro = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            erro = 'Usuário ou senha inválidos.'

    return render(request, 'login.html', {'erro': erro})

def index(request):
    return render(request, 'index.html')

def receitas(request):
    return render(request, 'receitas.html')

def despesas(request):
    return render(request, 'despesas.html')

def categorias(request):
    return render(request, 'categorias.html')

def cartoes(request):
    return render(request, 'cartoes.html')

def contas(request):
    return render(request, 'contas.html')

def metas(request):
    return render(request, 'metas.html')

def relatorios(request):
    return render(request, 'relatorios.html')

def saldos(request):
    return render(request, 'saldos.html')

def notificacoes(request):
    return render(request, 'notificacoes.html')

def limite_gastos(request):
    return render(request, 'limite_gastos.html')

def perfil(request):
    return render(request, 'perfil.html')


# ⚓ ADICIONADOS (faltavam no seu sistema)

def gastos_cartoes(request):
    return render(request, 'gastos_cartoes.html')

def graficos(request):
    return render(request, 'graficos.html')

def historico(request):
    return render(request, 'historico.html')

def recorrentes(request):
    return render(request, 'recorrentes.html')

def usuarios(request):
    return render(request, 'usuarios.html')
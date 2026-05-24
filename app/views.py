from django.shortcuts import render

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
from django.urls import path
from . import views

urlpatterns = [
   path('', views.login_view, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('index/', views.index, name='index'),

    path('receitas/', views.receitas, name='receitas'),
    path('despesas/', views.despesas, name='despesas'),
    path('categorias/', views.categorias, name='categorias'),
    path('cartoes/', views.cartoes, name='cartoes'),
    path('contas/', views.contas, name='contas'),

    path('metas/', views.metas, name='metas'),
    path('relatorios/', views.relatorios, name='relatorios'),
    path('saldos/', views.saldos, name='saldos'),

    path('notificacoes/', views.notificacoes, name='notificacoes'),
    path('limites/', views.limite_gastos, name='limites'),
    path('perfil/', views.perfil, name='perfil'),

    path('gastos-cartoes/', views.gastos_cartoes, name='gastos_cartoes'),
    path('graficos/', views.graficos, name='graficos'),
    path('historico/', views.historico, name='historico'),
    path('recorrentes/', views.recorrentes, name='recorrentes'),
    path('usuarios/', views.usuarios, name='usuarios'),
]
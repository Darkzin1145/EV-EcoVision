from django.contrib import admin
from .models import *

admin.site.register(Usuario)
admin.site.register(Perfil)
admin.site.register(Categoria)
admin.site.register(Receita)
admin.site.register(Despesa)
admin.site.register(Saldo)
admin.site.register(MetaFinanceira)
admin.site.register(GraficoFinanceiro)
admin.site.register(RelatorioFinanceiro)
admin.site.register(Cartao)
admin.site.register(GastoCartao)
admin.site.register(ContaBancaria)
admin.site.register(PagamentoRecorrente)
admin.site.register(Notificacao)
admin.site.register(HistoricoFinanceiro)
admin.site.register(LimiteGastos)
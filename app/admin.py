from django.contrib import admin
from .models import (
    Usuario, Perfil, Login, MetaFinanceira, Categoria, 
    Receita, Despesa, Cartao, GastoCartao, ContaBancaria, 
    Notificacao, RelatorioFinanceiro, GraficoFinanceiro, 
    Saldo, HistoricoFinanceiro, PagamentoRecorrente, LimiteGastos
)

# ==========================================
# ⚓ CLASSES INLINE (Para tabelas que têm ForeignKey)
# ==========================================

class PerfilInline(admin.StackedInline):
    model = Perfil
    extra = 1

class LoginInline(admin.TabularInline):
    model = Login
    extra = 1

class MetaFinanceiraInline(admin.TabularInline):
    model = MetaFinanceira
    extra = 1

class ReceitaInline(admin.TabularInline):
    model = Receita
    extra = 1

class DespesaInline(admin.TabularInline):
    model = Despesa
    extra = 1

class ContaBancariaInline(admin.TabularInline):
    model = ContaBancaria
    extra = 1

class NotificacaoInline(admin.TabularInline):
    model = Notificacao
    extra = 1

class GastoCartaoInline(admin.TabularInline):
    model = GastoCartao
    extra = 1

class LimiteGastosInline(admin.TabularInline):
    model = LimiteGastos
    extra = 1


# ==========================================
# ⚙️ REGISTRO DOS MODELOS COM SEUS INLINES
# ==========================================

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_cadastro')
    inlines = [
        PerfilInline, 
        LoginInline, 
        MetaFinanceiraInline, 
        ReceitaInline, 
        DespesaInline, 
        ContaBancariaInline, 
        NotificacaoInline
    ]

@admin.register(Cartao)
class CartaoAdmin(admin.ModelAdmin):
    list_display = ('nome_cartao', 'limite', 'vencimento')
    inlines = [GastoCartaoInline]

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo')
    inlines = [LimiteGastosInline]


# ==========================================
# 📋 REGISTRO DOS OUTROS MODELOS DO SEU SISTEMA
# ==========================================
# Estes aparecem na página principal do admin para o gerenciamento padrão.

admin.site.register(RelatorioFinanceiro)
admin.site.register(GraficoFinanceiro)
admin.site.register(Saldo)
admin.site.register(HistoricoFinanceiro)
admin.site.register(PagamentoRecorrente)

# Registrando os modelos filhos separadamente também, caso o admin queira vê-los fora do Usuário
admin.site.register(Perfil)
admin.site.register(Login)
admin.site.register(MetaFinanceira)
admin.site.register(Receita)
admin.site.register(Despesa)
admin.site.register(GastoCartao)
admin.site.register(ContaBancaria)
admin.site.register(Notificacao)
admin.site.register(LimiteGastos)
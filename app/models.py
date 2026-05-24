from django.db import models


# =========================
# USUÁRIO
# =========================
class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)
    data_cadastro = models.DateField()

    def __str__(self):
        return self.nome


# =========================
# PERFIL
# =========================
class Perfil(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

    foto = models.ImageField(upload_to='perfil/')
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario.nome


# =========================
# LOGIN
# =========================
class Login(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

    email = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)
    ultimo_acesso = models.DateField()

    def __str__(self):
        return self.email


# =========================
# META FINANCEIRA
# =========================
class MetaFinanceira(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    nome = models.CharField(max_length=50)
    valor_objetivo = models.DecimalField(max_digits=10, decimal_places=2)
    valor_atual = models.DecimalField(max_digits=10, decimal_places=2)

    data_inicio = models.DateField()
    data_fim = models.DateField()

    status = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


# =========================
# CATEGORIA
# =========================
class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


# =========================
# RECEITA
# =========================
class Receita(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    descricao = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

    def __str__(self):
        return self.descricao


# =========================
# DESPESA
# =========================
class Despesa(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    descricao = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

    def __str__(self):
        return self.descricao


# =========================
# CARTÃO
# =========================
class Cartao(models.Model):

    nome_cartao = models.CharField(max_length=50)

    limite = models.DecimalField(max_digits=10, decimal_places=2)

    vencimento = models.DateField()

    def __str__(self):
        return self.nome_cartao


# =========================
# GASTO CARTÃO
# =========================
class GastoCartao(models.Model):
    cartao = models.ForeignKey(Cartao, on_delete=models.CASCADE)

    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


# =========================
# CONTA BANCÁRIA
# =========================
class ContaBancaria(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    banco = models.CharField(max_length=50)
    agencia = models.CharField(max_length=20)
    conta = models.CharField(max_length=20)

    saldo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.banco


# =========================
# NOTIFICAÇÃO
# =========================
class Notificacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    mensagem = models.TextField()
    data_envio = models.DateField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.mensagem


# =========================
# RELATÓRIO FINANCEIRO
# =========================
class RelatorioFinanceiro(models.Model):
    tipo = models.CharField(max_length=50)

    periodo_inicio = models.DateField()
    periodo_fim = models.DateField()

    data_geracao = models.DateField()
    formato = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo


# =========================
# GRÁFICO FINANCEIRO
# =========================
class GraficoFinanceiro(models.Model):
    tipo = models.CharField(max_length=50)

    periodo_inicio = models.DateField()
    periodo_fim = models.DateField()

    dados = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.tipo


# =========================
# SALDO
# =========================
class Saldo(models.Model):
    valor_atual = models.DecimalField(max_digits=10, decimal_places=2)
    data_ultima_atualizacao = models.DateField()

    def __str__(self):
        return str(self.valor_atual)


# =========================
# HISTÓRICO FINANCEIRO
# =========================
class HistoricoFinanceiro(models.Model):
    registro = models.TextField()
    tipo = models.CharField(max_length=20)
    data = models.DateField()

    def __str__(self):
        return self.tipo


# =========================
# PAGAMENTO RECORRENTE
# =========================
class PagamentoRecorrente(models.Model):
    descricao = models.CharField(max_length=100)

    valor = models.DecimalField(max_digits=10, decimal_places=2)

    periodicidade = models.CharField(max_length=20)

    def __str__(self):
        return self.descricao


# =========================
# LIMITE DE GASTOS
# =========================
class LimiteGastos(models.Model):
    valor_limite = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.categoria.nome} - R$ {self.valor_limite}"
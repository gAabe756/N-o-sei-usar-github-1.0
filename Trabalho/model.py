from datetime import datetime, timedelta

# Superclasse (Generalização)
class Midia:
    def __init__(self, titulo, genero, avaliacao, ano, idioma):
        self.titulo = titulo
        self.genero = genero
        self.avaliacao = avaliacao
        self.ano = ano
        self.idioma = idioma
        self.data_lancamento = None  # None = disponível, em caso de destaque, guarda a data de lançamento

    def destacar(self, dias=10):
        self.data_lancamento = datetime.now() + timedelta(days=dias)

    def excluir(self):
        self.data_lancamento = None

    def esta_destaque(self):
        return self.data_lancamento is not None

    def descricao(self):
        return f"{self.titulo}, Gênero: {self.genero}, Nota: {self.avaliacao}, Lançamento: {self.ano}, Idioma: {self.idioma}"

# Subclasses (Especificação)
class Filme(Midia):
    def __init__(self, titulo, avaliacao, ano, idioma):
        super().__init__(titulo, "Filme", avaliacao, ano, idioma)

    def descricao(self):
        return f"🎬 Filme: {self.titulo}, Nota: {self.avaliacao}, Lançamento: {self.ano}, Idioma: {self.idioma}"

class Serie(Midia):
    def __init__(self, titulo, avaliacao, ano, idioma):
        super().__init__(titulo, "Série", avaliacao, ano, idioma)

    def descricao(self):
        return f"📺 Série: {self.titulo}, Nota: {self.avaliacao}, Lançamento: {self.ano}, Idioma: {self.idioma}"

class Anime(Midia):
    def __init__(self, titulo, avaliacao, ano, idioma):
        super().__init__(titulo, "Anime", avaliacao, ano, idioma)

    def descricao(self):
        return f"🍥 Anime: {self.titulo}, Nota: {self.avaliacao}, Lançamento: {self.ano}, Idioma: {self.idioma}"

# Modelo principal de armazenamento das mídias
class StreamingModel:
    def __init__(self):
        self.midia_disponiveis = []
        self.midia_destaque = []

    def adicionar_midia(self, titulo, genero, avaliacao, ano, idioma):
        if genero == "Filme":
            nova_midia = Filme(titulo, avaliacao, ano, idioma)
        elif genero == "Série":
            nova_midia = Serie(titulo, avaliacao, ano, idioma)
        elif genero == "Anime":
            nova_midia = Anime(titulo, avaliacao, ano, idioma)
        else:
            raise ValueError("Gênero inválido")
        self.midia_disponiveis.append(nova_midia)

    def listar_disponiveis(self):
        return self.midia_disponiveis

    def listar_destaque(self):
        return self.midia_destaque

    def remover_midia(self, indice):
        if 0 <= indice < len(self.midia_disponiveis):
            self.midia_disponiveis.pop(indice)

    def destacar_midia(self, indice, dias=10):
        if 0 <= indice < len(self.midia_disponiveis):
            midia = self.midia_disponiveis.pop(indice)
            midia.destacar(dias)
            self.midia_destaque.append(midia)

    def excluir_midia(self, indice):
        if 0 <= indice < len(self.midia_destaque):
            midia = self.midia_destaque.pop(indice)
            midia.excluir()
            self.midia_disponiveis.append(midia)

# Modelo de Usuário
class UsuarioModel:
    def __init__(self):
        self.usuario = 'hiro'
        self.senha = 'vendetta'

    def autenticar(self, usuario, senha):
        return usuario == self.usuario and senha == self.senha

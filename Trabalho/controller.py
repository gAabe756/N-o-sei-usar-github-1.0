from model import StreamingModel, UsuarioModel

class StreamingController:
    def __init__(self):
        self.model = StreamingModel()
        self.usuario_model = UsuarioModel()

    # Usuário
    def login(self, usuario, senha):
        return self.usuario_model.autenticar(usuario, senha)

    # Mídia
    def adicionar_midia(self, titulo, genero, avaliacao, ano, idioma):
        self.model.adicionar_midia(titulo, genero, avaliacao, ano, idioma)

    def listar_disponiveis(self):
        return self.model.listar_disponiveis()

    def listar_destaque(self):
        return self.model.listar_destaque()

    def destacar_midia(self, indice, dias=10):
        self.model.destacar_midia(indice, dias)

    def excluir_midia(self, indice):
        self.model.excluir_midia(indice)

    def remover_midia(self, indice):
        self.model.remover_midia(indice)

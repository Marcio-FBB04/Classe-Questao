# classe.py
#olá

class Questao:
    def __init__(self, id, titulo, nivel_dificuldade, tipo_programacao, tema, tamanho_codigo, qualidade_codigo, imagem=None):
        self._id = id
        self._titulo = titulo
        self._nivel_dificuldade = nivel_dificuldade
        self._tipo_programacao = tipo_programacao
        self._tema = tema
        self._tamanho_codigo = tamanho_codigo
        self._qualidade_codigo = qualidade_codigo
        self._imagem = imagem  # Adicionando a nova variável de imagem

        # Adicione um breakpoint aqui para depurar a inicialização
        breakpoint()

    def __str__(self):
        imagem_str = f"\nImagem: {self._imagem}" if self._imagem else "\nNenhuma imagem disponível"
        return (f"Questao ID: {self._id}\n"
                f"Título: {self._titulo}\n"
                f"Nível de Dificuldade: {self._nivel_dificuldade}\n"
                f"Tipo de Programação: {self._tipo_programacao}\n"
                f"Tema: {self._tema}\n"
                f"Tamanho do Código: {self._tamanho_codigo}\n"
                f"Qualidade do Código: {self._qualidade_codigo} estrelas"
                f"{imagem_str}\n")

    # Getters e Setters
    @property
    def id(self):
        return self._id

    @property
    def titulo(self):
        return self._titulo

    @property
    def nivel_dificuldade(self):
        return self._nivel_dificuldade

    @property
    def tipo_programacao(self):
        return self._tipo_programacao

    @property
    def tema(self):
        return self._tema

    @property
    def tamanho_codigo(self):
        return self._tamanho_codigo

    @property
    def qualidade_codigo(self):
        return self._qualidade_codigo

    @property
    def imagem(self):
        return self._imagem

    @id.setter
    def id(self, valor):
        self._id = valor

    @titulo.setter
    def titulo(self, valor):
        self._titulo = valor

    @nivel_dificuldade.setter
    def nivel_dificuldade(self, valor):
        self._nivel_dificuldade = valor

    @tipo_programacao.setter
    def tipo_programacao(self, valor):
        self._tipo_programacao = valor

    @tema.setter
    def tema(self, valor):
        self._tema = valor

    @tamanho_codigo.setter
    def tamanho_codigo(self, valor):
        self._tamanho_codigo = valor

    @qualidade_codigo.setter
    def qualidade_codigo(self, valor):
        self._qualidade_codigo = valor

    @imagem.setter
    def imagem(self, valor):
        self._imagem = valor

    # Método para configurar a questão usando o menu
    def configurar_questao(self):
        # Adicione um breakpoint aqui para depurar antes de chamar o menu
        breakpoint()
        from menu import menu_interativo  # Importa a função menu_interativo aqui
        # Chama o menu interativo para configurar a questão
        menu_interativo(self)


# Exemplo de uso
if __name__ == "__main__":
    # Adicione um breakpoint aqui para depurar antes de criar a instância de Questao
    breakpoint()
    questao = Questao(
        id=1,
        titulo="Questão de Exemplo",
        nivel_dificuldade=0,
        tipo_programacao="",
        tema="",
        tamanho_codigo="",
        qualidade_codigo=0,
        imagem="caminho/para/imagem.jpg"  # Exemplo de caminho de imagem
    )
    questao.configurar_questao()
    print(questao)
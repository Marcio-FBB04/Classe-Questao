import inquirer


class Questao:
    def __init__(self, id, titulo, nivel_dificuldade, tipo_programacao, tema, tamanho_codigo, qualidade_codigo):
        self.id = id
        self.titulo = titulo
        self.nivel_dificuldade = nivel_dificuldade
        self.tipo_programacao = tipo_programacao
        self.tema = tema
        self.tamanho_codigo = tamanho_codigo
        self.qualidade_codigo = qualidade_codigo

    def __str__(self):
        return (f"Questao ID: {self.id}\n"
                f"Título: {self.titulo}\n"
                f"Nível de Dificuldade: {self.nivel_dificuldade}\n"
                f"Tipo de Programação: {self.tipo_programacao}\n"
                f"Tema: {self.tema}\n"
                f"Tamanho do Código: {self.tamanho_codigo}\n"
                f"Qualidade do Código: {self.qualidade_codigo} estrelas\n")

    def avaliar_questao(self, nova_qualidade):
        if 1 <= nova_qualidade <= 5:
            self.qualidade_codigo = nova_qualidade
        else:
            raise ValueError("A qualidade deve estar entre 1 e 5 estrelas")

    def atualizar_dificuldade(self, nova_dificuldade):
        if 1 <= nova_dificuldade <= 5:
            self.nivel_dificuldade = nova_dificuldade
        else:
            raise ValueError("O nível de dificuldade deve estar entre 1 e 5")


# Função que cria o menu interativo para configurar a questão
def menu_interativo():
    # Configurando a questão
    questao = Questao(
        id=1,
        titulo="Questão de Exemplo",
        nivel_dificuldade=0,
        tipo_programacao="",
        tema="",
        tamanho_codigo="",
        qualidade_codigo=0
    )

    # Perguntar o nível de dificuldade
    nivel_pergunta = [
        inquirer.List(
            'nivel_dificuldade',
            message="Selecione o Nível de Dificuldade",
            choices=['1 - Muito Fácil', '2 - Fácil',
                     '3 - Médio', '4 - Difícil', '5 - Muito Difícil'],
        ),
    ]
    nivel_resposta = inquirer.prompt(nivel_pergunta)
    questao.nivel_dificuldade = int(
        nivel_resposta['nivel_dificuldade'].split(' ')[0])

    # Perguntar o tipo de programação
    tipo_pergunta = [
        inquirer.List(
            'tipo_programacao',
            message="Selecione o Tipo de Programação",
            choices=['Python', 'Java', 'C++',
                     'JavaScript', 'C#', 'Ruby', 'PHP'],
        ),
    ]
    tipo_resposta = inquirer.prompt(tipo_pergunta)
    questao.tipo_programacao = tipo_resposta['tipo_programacao']

    # Perguntar o tema
    tema_pergunta = [
        inquirer.List(
            'tema',
            message="Selecione o Tema",
            choices=['Estruturas de Controle', 'Estruturas de Dados',
                     'Funções e Procedimentos', 'POO'],
        ),
    ]
    tema_resposta = inquirer.prompt(tema_pergunta)
    questao.tema = tema_resposta['tema']

    # Perguntar o tamanho do código
    tamanho_pergunta = [
        inquirer.List(
            'tamanho_codigo',
            message="Selecione o Tamanho do Código",
            choices=['pequeno', 'médio', 'grande'],
        ),
    ]
    tamanho_resposta = inquirer.prompt(tamanho_pergunta)
    questao.tamanho_codigo = tamanho_resposta['tamanho_codigo']

    # Perguntar a qualidade do código
    qualidade_pergunta = [
        inquirer.List(
            'qualidade_codigo',
            message="Selecione a Qualidade do Código",
            choices=['1 - Muito Ruim', '2 - Ruim',
                     '3 - Médio', '4 - Bom', '5 - Excelente'],
        ),
    ]
    qualidade_resposta = inquirer.prompt(qualidade_pergunta)
    questao.qualidade_codigo = int(
        qualidade_resposta['qualidade_codigo'].split(' ')[0])

    # Exibir o resultado
    print("\nQuestão configurada:")
    print(questao)


if __name__ == "__main__":
    menu_interativo()

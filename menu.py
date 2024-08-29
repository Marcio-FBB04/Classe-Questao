# menu.py
import inquirer 
from typing import Any  # Para evitar importação circular, usamos Any


def menu_interativo(questao: Any):
    # Adicione um breakpoint aqui para depurar ao iniciar o menu interativo
    breakpoint()

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

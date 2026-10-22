"""
Desafio do Bondinho - Controle de Capacidade
Descrição: Programa para verificar se o total de passageiros (alunos, monitores e professores)
cabe na capacidade do bondinho em uma única viagem.
"""

def verificar_capacidade():
    # Definição das constantes do problema
    CAPACIDADE_MAXIMA = 30
    NUMERO_DE_PROFESSORES = 8

    # Mensagens de retorno
    RESPOSTA_POSITIVA = "pode ir"
    RESPOSTA_NEGATIVA = "não pode ir"

    print("=== CONTROLE DE CAPACIDADE DO BONDINHO ===")
    
    try:
        # Entradas do usuário
        numero_de_alunos = int(input("Digite a quantidade de alunos: "))
        numero_de_monitores = int(input("Digite a quantidade de monitores: "))

        # Validação para evitar números negativos
        if numero_de_alunos < 0 or numero_de_monitores < 0:
            print("Por favor, digite apenas valores inteiros positivos.")
            return

        # Cálculo do total de pessoas
        total_de_pessoas = numero_de_alunos + numero_de_monitores + NUMERO_DE_PROFESSORES

        # Exibição do resumo
        print(f"\nResumo da Viagem:")
        print(f"- Alunos: {numero_de_alunos}")
        print(f"- Monitores: {numero_de_monitores}")
        print(f"- Professores: {NUMERO_DE_PROFESSORES}")
        print(f"- Total de Pessoas: {total_de_pessoas}")
        print(f"- Capacidade Máxima: {CAPACIDADE_MAXIMA}")
        print("-----------------------------------")

        # Estrutura condicional para tomada de decisão
        if total_de_pessoas <= CAPACIDADE_MAXIMA:
            print(f"Resultado: {RESPOSTA_POSITIVA}")
        else:
            print(f"Resultado: {RESPOSTA_NEGATIVA}")

    except ValueError:
        print("Erro: Por favor, insira apenas números inteiros válidos.")

if __name__ == "__main__":
    verificar_capacidade()

# ==============================================================================
# CAMADA 1: REGRAS DE NEGÓCIO (Funções Puras)
# ==============================================================================

def calcular_media(notas: list[float]) -> float:
    """
    Calcula a média aritmética de uma lista de notas.
    Possui cláusula de guarda para evitar divisão por zero em listas vazias.
    """
    if not notas:
        return 0.0
    return round(sum(notas) / len(notas), 2)


def verificar_status(media: float, corte: float = 5.0) -> str:
    """
    Determina a situação do aluno com base na nota de corte configurável.
    """
    return "Aprovado" if media >= corte else "Reprovado"


def processar_aluno(nome: str, notas: list[float], corte: float = 5.0) -> dict:
    """
    Consolida as informações de um estudante gerando um registro estruturado.
    """
    media = calcular_media(notas)
    status = verificar_status(media, corte)
    return {
        "nome": nome,
        "notas": notas,
        "media": media,
        "status": status
    }


# ==============================================================================
# CAMADA 2: ENTRADA E VALIDAÇÃO (I/O - Entrada)
# ==============================================================================

def coletar_nota(ordem: int) -> float:
    """
    Valida a entrada de dados do utilizador via terminal.
    Impede que valores não numéricos ou fora da faixa de 0 a 10 quebrem a execução.
    """
    while True:
        try:
            entrada = input(f"Digite a {ordem}ª nota (0.0 a 10.0): ").strip()
            nota = float(entrada)
            if 0.0 <= nota <= 10.0:
                return nota
            print("Erro: A nota deve estar estritamente entre 0.0 e 10.0.")
        except ValueError:
            print("Erro: Entrada inválida. Digite um número decimal válido (ex: 7.5).")


def cadastrar_turma(quantidade_alunos: int) -> list[dict]:
    """
    Coleta dados de múltiplos alunos e armazena em memória para processamento posterior.
    """
    turma = []
    for i in range(quantidade_alunos):
        print(f"\n--- Cadastro do Aluno {i + 1} de {quantidade_alunos} ---")
        nome = input("Nome do estudante: ").strip() or f"Aluno {i + 1}"
        
        # Coleta 3 notas por estudante
        notas = [coletar_nota(j + 1) for j in range(3)]
        
        aluno_processado = processar_aluno(nome, notas)
        turma.append(aluno_processado)
    return turma


# ==============================================================================
# CAMADA 3: APRESENTAÇÃO (I/O - Saída)
# ==============================================================================

def exibir_relatorio(turma: list[dict]) -> None:
    """
    Procedimento responsável por formatar e exibir os dados na consola.
    """
    print("\n" + "=" * 46)
    print(f"{'NOME':<20} | {'MÉDIA':<8} | {'STATUS':<12}")
    print("=" * 46)
    for aluno in turma:
        print(f"{aluno['nome']:<20} | {aluno['media']:<8.2f} | {aluno['status']:<12}")
    print("=" * 46)


# ==============================================================================
# PONTO DE ENTRADA (Execução ao clicar em "Run")
# ==============================================================================

def main() -> None:
    print("=== SISTEMA DE GESTÃO DE NOTAS ESCOLARES ===")
    
    # Pergunta quantos alunos serão cadastrados com validação
    while True:
        try:
            qtd = int(input("Quantos alunos deseja cadastrar na turma? ").strip())
            if qtd > 0:
                break
            print("Erro: Informe um número inteiro maior que 0.")
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido.")

    turma = cadastrar_turma(qtd)
    exibir_relatorio(turma)


if __name__ == "__main__":
    main()
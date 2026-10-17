from colorama import Fore, Style, init

init()

situacoes = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]
def definir_cor(nivel):
    cores = [
        Fore.RED,
        Fore.YELLOW,
        Fore.GREEN,
        Fore.CYAN,
        Fore.BLUE
    ]
    return cores[nivel - 1]
def exibir_situacao(nivel):
    if 1 <= nivel <= 5:
        mensagem = situacoes[nivel - 1]
        cor = definir_cor(nivel)
        print(f"{cor}Nível {nivel}: {mensagem}{Style.RESET_ALL}")
    else:
        print("Nível inválido. Informe um número entre 1 e 5.")
def main():
    print("=== Monitoramento do reservatório ===")

    try:
        nivel_atual = int(input("Informe o nível da água (1 a 5): "))
        exibir_situacao(nivel_atual)
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")


if __name__ == "__main__":
    main()
        
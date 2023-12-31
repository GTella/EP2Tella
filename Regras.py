from funcoes import indica_posicao
def imprime_layout():
    print("=" * 30)
    print("|                           |")
    print("| Bem-vindo ao Insper Termo |")
    print("|                           |")
    print(" ==== Design de Software === ")
    print("Comandos: desisto")
    print("Regras:")
    print(" - Você tem 6 tentativas para acertar uma palavra aleatória com a quantidade de letras escolhida.")
    print(" - A cada tentativa, a palavra testada terá suas letras coloridas conforme:")
    print("   . \033[1;36;40m{}\033[m  : a letra está na posição correta;".format('Azul'))
    print("   . \033[1;33;40m{}\033[m  : a palavra tem a letra, mas está na posição errada;".format('Amarelo'))
    print("   . \033[1;37;40m{}\033[m  : a palavra não tem a letra.".format('Cinza'))
    print(" - Os acentos são ignorados;")
    print(" - As palavras podem possuir letras repetidas.")

def main(letras, sorteada):
    tentativas_restantes = letras + 1

    print(f"Você tem {tentativas_restantes} tentativa(s)")

    while tentativas_restantes > 0:
        palpite = input("Qual é o seu palpite? ").lower()
        
        return

def sorteando():
    print('\033[1;35;40m{}\033[m'.format("Sorteando uma palavra..."))
    print('\033[1;35;40m{}\033[m'.format("Já tenho uma palavra! Tente adivinhá-la!"))
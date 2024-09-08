# limpar o console
import os

def exibir_nome_do_programa():
    print(""" Ｓａｂｏｒ Ｅｘｐｒｅｓｓ
""")

def exibir_opcoes ():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

#function///////////////////////////////////////
def finalizar_app():
    os.system('cls')
    print('Finalizando app\n')

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    if opcao_escolhida == 1 :
        print('cadastrar restaurante')
    elif opcao_escolhida == 2 :
        print('Listar restaurante')
    elif opcao_escolhida == 3 :
        print('Ativar restaurante')
    else:
    # Criar um caso isolado
        finalizar_app()
        
"""opcao_escolhida = int(input('Escolha uma opção: '))
match opcao_escolhida:
    case 1:
        print('Adicionar restaurante')
    case 2:
        print('Listar restaurantes')
    case 3:
        print('Ativar restaurante')
    case 4:
        print('Finalizar app')
    case _:
        print('Opção inválida!')"""


def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    

if __name__ == '__main__':
    main()

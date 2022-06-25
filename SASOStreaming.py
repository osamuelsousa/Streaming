#Criando um passo a passo
#'''    -Coisas para fazer ainda: login (dar continuidade) / 
#       -Criar  uma tela de login igual o da disney (botão de entrar, e outro que mostra os planos e depois ja mostra pra pessoa se cadasrtear de acoro com o plano, e um outro de assine agora)
# '''

from re import S


def formatacao_de_titulos(a):
    print("-"*60)
    print(f'{a:^60}'.upper())
    print("-"*60)

#Tela inicial
iniciando = 0
while iniciando == 0:
    formatacao_de_titulos("Bem vindo as SASORO Plus")
    print("Digite:\n1 - Para entrar.\n2 - Para se cadastrar.\n3 - Para conhecer os planos.\n4 - Para encerrar o programa.")
    d = int(input("Digite: "))

    if d == 1:
        formatacao_de_titulos("Óla, use seu e-mail para entrar:")
        email = input("Email: ")
        senha = input("Senha: ")
        #terminar

    elif d == 2:
        continuar = 1
        while continuar == 1:
                formatacao_de_titulos("CADASTRE SUA CONTA ABAIXO.")
                input("\nInforme um E-mail: ")
                a = input("Crie uma senha: ")
                b = input("Digite novamente a senha: ")
                if a == b:
                    print("\nConta cadastrada com sucesso!")
                elif a != b:
                    b = "As senhas inseridas são diferentes..."
                    c = "Você deseja tentar novamente ou voltar ao inicio?"
                    d = "Voltar ao inicio = 1"
                    e = "Tentar novamente = 2"
                    print("\n\n")
                    print(f'{b:^60}')
                    print(f'{c:^60}')
                    print(f'{d:^60}')
                    print(f'{e:^60}')
                    a = int(input("Digite: "))
                    if a == 2:
                        continue
                    elif a == 1:
                        continuar = 0
                    else:
                        print("Erro desconhecido ;(")
        print("teste")
    elif d == 4:
        break
#teste para ver se ele volta ao inicio...             
num = 0
while num in range(0 , 100):
    print(num)
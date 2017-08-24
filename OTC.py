import time
import sqlite3
import os

connection = sqlite3.connect('otc.db')
cursor = connection.cursor()

def Create_Table():
    cursor.execute('CREATE TABLE IF NOT EXISTS dados (Nome text, Idade integer, CPF double, Email text)') 

def Menu():
    print ("--------------------------------------------------------------")
    print("1 - Cadastrar")
    print("2 - Entrar")
    print("3 - Sair")
    print ("--------------------------------------------------------------")
    opcao = int(input("Escolha uma opcao: "))
    print ("--------------------------------------------------------------")
    return opcao


def Menu2():
    print ("--------------------------------------------------------------")
    print("1 - Nova Viagem")
    print("2 - Consultar Viagens")
    print("3 - Sair")
    print ("--------------------------------------------------------------")
    opcaox = int(input("Escolha uma opcao: "))
    print ("--------------------------------------------------------------")
    return opcaox


def Cadastrar():
    os.system("cls")
    print ("Vamos iniciar o cadastro:")
    print ("--------------------------------------------------------------")
    nome = (input("Qual seu nome? ")) 
    idade = (input("Qual sua idade? "))
    cpf = (input("Qual seu CPF? "))
    email = (input("Qual seu email? "))
    cursor.execute ('INSERT INTO dados (Nome, Idade, CPF, Email) VALUES (?,?,?,?)', (nome, idade, cpf, email))
    connection.commit()
    print ("--------------------------------------------------------------")


def Entrar():
    os.system("cls")
    retorno = 0
    while(retorno != 1):
        comp = input("CPF: ")
        retorno = Autenticar(comp)
    while True:
        opcao_1 = Menu2()
        if opcao_1 == 3:
            break
        elif opcao_1 == 2:
            Consultar()
        elif opcao_1 == 1:
            Quest()
        

def Autenticar(comp):
    resultado = 'SELECT * FROM dados WHERE CPF = ?'
    x = 0
    for row in cursor.execute(resultado, (comp,)):
         x = row[2]
    if(x != 0):
        print ("--------------------------------------------------------------")
        print (">>>>>>>>>>>>>>>>>>>>>>> Autenticação OK! <<<<<<<<<<<<<<<<<<<<<")
        print ("--------------------------------------------------------------")
        return 1
    else:
        print ("--------------------------------------------------------------")
        print ("                          CPF invalido!                       ")
        print ("--------------------------------------------------------------")
        return 0


def Consultar():
    print("Extensão Ainda não disponivel")
    print("Pressione qualquer tecla para voltar")
    x = input()


def Quest():
    print ("--------------------------------------------------------------")
    print("1 - Você Gostaria de Ajuda para decidir o Local? ")
    print("a) Sim")
    print("b) Não")
    x = input()
    if(1 == "b"):
        print("Obrigado, até a proxima!")
    else:
        print ("--------------------------------------------------------------")
        print("Gostaria de uma Cidade: ")
        print("a) Internacioal")
        print("b) Nacional")
        y = input()
        print ("--------------------------------------------------------------")
        print("Gostaria de uma cidade onde predomina: ")
        print("a) Frio")
        print("b) Calor")
        z = input()
        print ("--------------------------------------------------------------")
        print("Qual a razão da viagem? ")
        print("a) Trabalho")
        print("b) Turismo")
        print("c) Excursão")
        w = input()
        print ("--------------------------------------------------------------")
        print (" >>>>>>>>>>>>>>>>>>>>>>>>> Buscando <<<<<<<<<<<<<<<<<<<<<<<<<<")
        print ("--------------------------------------------------------------")
        time.sleep(5)
        if((y == 'a') and (z == 'a') and (w == 'a')):
            print ("Indicamos para você a cidade de: Ottawa, Canada ")
            print("Pressione qualquer tecla para voltar")
            algo = input()
        if((y == 'a') and (z == 'a') and (w == 'b')):
            print ("Indicamos para você a cidade de: Barcelona, Espanha ")
            print("Pressione qualquer tecla para voltar")
            algo = input()
        if((y == 'a') and (z == 'a') and (w == 'c')):
            print ("Indicamos para você a cidade de: Madrid, Espanha ")
            print("Pressione qualquer tecla para voltar")
            algo = input()
        if((y == 'a') and (z == 'b') and (w == 'a')):
            print ("Indicamos para você a cidade de: Paris, França")
            print("Pressione qualquer tecla para voltar")
            algo = input()
        if((y == 'a') and (z == 'b') and (w == 'b')):
            print ("Indicamos para você a cidade de: Florida, Estados Unidos")
            print("Pressione qualquer tecla para voltar")
            algo = input()
        if((y == 'a') and (z == 'b') and (w == 'c')):
            print ("Indicamos para você a cidade de: Santiago, Chile")
            print("Pressione qualquer tecla para voltar")
            algo = input()
        if((y == 'b') and (z == 'a') and (w == 'a')):
            print ("Indicamos para você a cidade de: Porto Alegre (RS)")
            print("Pressione qualquer tecla para voltar")
            algo = input()
        if((y == 'b') and (z == 'a') and (w == 'b')):
            print ("Indicamos para você a cidade de: Fox do Iguaçu (SC)")
            print("Pressione qualquer tecla para voltar")
            algo = input()
        if((y == 'b') and (z == 'a') and (w == 'c')):
            print ("Indicamos para você a cidade de: Curitiba (SC)")
            print("Pressione qualquer tecla para voltar")
            algo = input()
        if((y == 'b') and (z == 'b') and (w == 'a')):
            print ("Indicamos para você a cidade de: Três Lagoas (MG)")
            print("Pressione qualquer tecla para voltar")
            algo = input()
        if((y == 'b') and (z == 'b') and (w == 'b')):
            print ("Indicamos para você a cidade de: Caldas Novas (GO)")
            print("Pressione qualquer tecla para voltar")
            algo = input()
        if((y == 'b') and (z == 'b') and (w == 'c')):
            print ("Indicamos para você a cidade de: Recife (PE)")
            print("Pressione qualquer tecla para voltar")
            algo = input()
   
        
while True:
    os.system("cls")
    Create_Table()
    opcao = Menu()
    if opcao == 3:
        print("Até Logo!")
        break
    elif opcao == 2:
        Entrar()
    elif opcao == 1:
        Cadastrar()
time.sleep(3)

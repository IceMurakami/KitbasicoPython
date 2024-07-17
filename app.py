import random
import string
def banner():
    print("""
         
    ██╗░░██╗██╗████████╗  ██████╗░░█████╗░░██████╗██╗░█████╗░░█████╗░
    ██║░██╔╝██║╚══██╔══╝  ██╔══██╗██╔══██╗██╔════╝██║██╔══██╗██╔══██╗
    █████═╝░██║░░░██║░░░  ██████╦╝███████║╚█████╗░██║██║░░╚═╝██║░░██║
    ██╔═██╗░██║░░░██║░░░  ██╔══██╗██╔══██║░╚═══██╗██║██║░░██╗██║░░██║
    ██║░╚██╗██║░░░██║░░░  ██████╦╝██║░░██║██████╔╝██║╚█████╔╝╚█████╔╝
    ╚═╝░░╚═╝╚═╝░░░╚═╝░░░  ╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░╚════╝░░╚════╝░ 
      """)
    

def menu():
    print('1 - Ping\n2 - DNS\n 3 - Gerador de senha')


banner()

def gerar_senha(senha, tamanho):
    senha = "".join(random.sample(senha, tamanho))
    return senha

def maiuscula():
    Maiuscula = string.ascii_lowercase
    return  Maiuscula

def minuscula():
    Miniscula = string.ascii_uppercase
    return Miniscula

def caracter_especial():
    especial = '{}[]/*&!@#$¨&*()'
    return especial

def comprimir_dados(dado_um, dado_dois,minuscula, maiuscula, especial):
    dados = (dado_um + dado_dois + minuscula + maiuscula + especial)
    return dados

def op_senha_texto():
    dado_texto = input("Informe quais caracters deseja ter em sua senha: ")
    dado_num = input("Informe quais numero deseja na sua senha: ")
    dado_size = int(input("Informe o tamano da senha: "))

    return dado_texto, dado_num, dado_size


texto,numero,tamanho = op_senha_texto()
miniscula = minuscula()
maiuscula = maiuscula()
especial =  caracter_especial()

senha = comprimir_dados(texto, numero, miniscula, maiuscula, especial)

print(gerar_senha(senha, tamanho))



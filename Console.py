def gerador_de_senha():
    import app

def rede():
    import rede

def banner():
    print("""
         
        ██╗░░██╗██╗████████╗██████╗░░█████╗░░██████╗██╗░█████╗░░█████╗░
        ██║░██╔╝██║╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║██╔══██╗██╔══██╗
        █████═╝░██║░░░██║░░░██████╦╝███████║╚█████╗░██║██║░░╚═╝██║░░██║
        ██╔═██╗░██║░░░██║░░░██╔══██╗██╔══██║░╚═══██╗██║██║░░██╗██║░░██║
        ██║░╚██╗██║░░░██║░░░██████╦╝██║░░██║██████╔╝██║╚█████╔╝╚█████╔╝
        ╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░╚════╝░░╚════╝░ 
      """)
    

def menu():
    print('1 - Gerador de senha\n2 - Ping\n3 - DNS\n4 - Retornar ao menu\n5 - Sair')

def opcao():
    op = int(input("Escolha um item: "))
    return op

banner()
menu()
opcao = opcao()


while(opcao < 5):
    if(opcao == 1):
       gerador_de_senha()
    elif(opcao == 2):
        rede()
    elif(opcao == 3):
        print('DNS')
    elif(opcao == 4):
        menu()
        opcao = opcao()
    else:
        break
    
import os

def host():
    host_da_maquina = input()
    return host_da_maquina


def pingar(ip):
    return os.system('ping -t ' + ip)

print('Informe o host que deseja chegar a conexão: ')
host_da_maquina = host()

pingar(host_da_maquina)



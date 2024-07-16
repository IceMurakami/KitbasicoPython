import os

host  = "172.31.130.144"

ping = os.system('ping -t ' + host)

print(ping)
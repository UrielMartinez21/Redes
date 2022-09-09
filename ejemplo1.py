import socket
hostname=socket.gethostname()
ip=socket.gethostbyname(hostname)
#print(f"\t-->El nombre del ordenador es: {hostname}")
#print(f"\t-->Tu direccion IP es: {ip}")

with open(r'C:\Users\Uriel Martinez\Desktop\Uriel Martinez\Personal\Programacion\Python\Redes\texto.txt', 'w') as f:
    f.write("Esto fue creado sin nada\n")
    f.write(f"\t-->El nombre del ordenador es: {hostname}\n")
    f.write(f"\t-->Tu direccion IP es: {ip}\n")

with open(r'C:\Users\Uriel Martinez\Desktop\Uriel Martinez\Personal\Programacion\Python\Redes\texto.txt', 'r') as f:
    print(f.read())
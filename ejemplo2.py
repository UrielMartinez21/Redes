import socket

def create_socket():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    with open(r'C:\Users\Uriel Martinez\Desktop\Uriel Martinez\Personal\Programacion\Python\Redes\texto.txt', 'w') as f:
        f.write("Esto fue creado con una funcion\n")
        f.write(f"\t-->El nombre del ordenador es: {hostname}\n")
        f.write(f"\t-->Tu direccion IP es: {ip}\n")
    
def mostrar_socket():
    with open(r'C:\Users\Uriel Martinez\Desktop\Uriel Martinez\Personal\Programacion\Python\Redes\texto.txt', 'r') as f:
        print(f.read())

create_socket()
mostrar_socket()
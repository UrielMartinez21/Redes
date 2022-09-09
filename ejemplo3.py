import socket
class sock:
    def __init__(self):
        self.hostname=socket.gethostname()
        self.ip=socket.gethostbyname(self.hostname)
        print("[+]El socket fue creado")
    def mostrar(self):
        print(f"[+]Nombre:\t{self.hostname}")
        print(f"[+]Su ip es:\t{self.ip}")
    def escribir_bloc(self):
        with open(r'C:\Users\Uriel Martinez\Desktop\Uriel Martinez\Personal\Programacion\Python\Redes\texto.txt', 'w') as f:
            f.write(f"[+]Nombre:\t{self.hostname}\n")
            f.write(f"[+]Su ip es:\t{self.ip}\n")
    def mostrar_bloc(self):
        with open(r'C:\Users\Uriel Martinez\Desktop\Uriel Martinez\Personal\Programacion\Python\Redes\texto.txt', 'r') as f:
            print(f.read())
c=sock()
c.mostrar()
c.escribir_bloc()
c.mostrar_bloc()
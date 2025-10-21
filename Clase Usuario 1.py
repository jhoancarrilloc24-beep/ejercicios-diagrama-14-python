# Clase Usuario

class Usuario:
    # constructor de usuario

    def __init__(self, nombre, apellido, n_cuenta, direccion, login, password):
        self.nombre = nombre
        self.apellido = apellido
        self.n_cuenta = n_cuenta
        self.direccion = direccion
        self.login = login
        self.password = password
        print(f"Usuario creado: {self.nombre} {self.apellido}, cuenta N° {self.n_cuenta}.")

# imprimir texto

    def enviar_sugerencia(self):
        print(f"{self.nombre} ha enviado una sugerencia al sistema ➡️.")

    def leer(self):
        print(f"{self.nombre} está leyendo un producto del catálogo 📦.")

    def comprar(self):
        print(f"{self.nombre} ha realizado una compra 💰.")

    def vender(self):
        print(f"{self.nombre} ha vendido un producto ✉️.")

    def realizar_reclamacion(self):
        print(f"{self.nombre} ha realizado una reclamación ➡️.")

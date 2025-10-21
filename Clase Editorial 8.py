# Clase Editorial

class Editorial:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
# texto

    def vender(self):
        print(f"La editorial '{self.nombre}' ha vendido un producto 📦.")

# Clase Producto

class Producto:
    # constructor de producto

    def __init__(self, precio, titulo, autor, editorial, anio_edicion, preferencias):
        self.precio = precio
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.anio_edicion = anio_edicion
        self.preferencias = preferencias

# texto a mostrar

    def vender(self):
        print(f"Producto '{self.titulo}' vendido con éxito ✅.")

    def comprar(self):
        print(f"Producto '{self.titulo}' comprado correctamente ✅.")

    def ver_catalogo(self):
        print(f"Mostrando información del producto: {self.titulo}")

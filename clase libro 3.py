# Subclases de Producto

class Libro(Producto):
    # constructor de libro


    def __init__(self, precio, titulo, autor, editorial, anio_edicion, preferencias, genero):
        super().__init__(precio, titulo, autor, editorial, anio_edicion, preferencias)
        self.genero = genero
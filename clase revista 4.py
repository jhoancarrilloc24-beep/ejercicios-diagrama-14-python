# subclass de revista

class Revista(Producto):
    #constructor de revista

    def __init__(self, precio, titulo, autor, editorial, anio_edicion, preferencias, categoria):
        super().__init__(precio, titulo, autor, editorial, anio_edicion, preferencias)
        self.categoria = categoria
# subclass de articulo segunda mano

class ArticuloSegundaMano(Producto):
    # constructor de articulo segunda mano

    def __init__(self, precio, titulo, autor, editorial, anio_edicion, preferencias, clasificacion, tema, vendedor):
        super().__init__(precio, titulo, autor, editorial, anio_edicion, preferencias)
        self.clasificacion = clasificacion
        self.tema = tema
        self.vendedor = vendedor

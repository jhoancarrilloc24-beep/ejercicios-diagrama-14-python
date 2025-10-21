# subclass articulo online

class ArticuloOnline(Producto):
    # constructor de articulo online

    def __init__(self, precio, titulo, autor, editorial, anio_edicion, preferencias, tema):
        super().__init__(precio, titulo, autor, editorial, anio_edicion, preferencias)
        self.tema = tema
# texto

    def publicar(self):
        print(f"Artículo online '{self.titulo}' publicado en la web.")

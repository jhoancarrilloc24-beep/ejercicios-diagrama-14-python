# subclass de novedades

class Novedades(Producto):
    # constructor de novedades

    def __init__(self, precio, titulo, autor, editorial, anio_edicion, preferencias, clasificacion, tema):
        super().__init__(precio, titulo, autor, editorial, anio_edicion, preferencias)
        self.clasificacion = clasificacion
        self.tema = tema

    def cambiar_clasificacion(self, nueva):
        # texto
        print(f"Novedad '{self.titulo}' cambió su clasificación de {self.clasificacion} a {nueva}.")
        self.clasificacion = nueva
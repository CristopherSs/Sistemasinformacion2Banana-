"""
    este archivo contiene la subclase de tipo usuario
    :Docente
"""
from backend.usuario.usuario import Usuario


class Docente(Usuario):
    """
        esta clase modela la interaccion a las funconalidades
        que tendra un usuario de tipo docente
    """

    def __init__(self, nombre: str, contrasenia: str) -> None:
        Usuario.__init__(self, nombre, contrasenia)


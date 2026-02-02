from typing import List
from modelos.proyecto import Proyecto

class Usuario:
    """Clase que representa un usuario del sistema"""
    
    def __init__(self, nombre: str, email: str, rol: str = "estudiante"):
        self._nombre = nombre
        self._email = email
        self._rol = rol
        self._proyectos = []
        self._id = id(self)
    
    @property
    def id(self):
        return self._id
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def email(self):
        return self._email
    
    @property
    def rol(self):
        return self._rol
    
    def agregar_proyecto(self, proyecto: Proyecto):
        """Agrega un proyecto al usuario"""
        self._proyectos.append(proyecto)
    
    def eliminar_proyecto(self, proyecto_id: int):
        """Elimina un proyecto por ID"""
        self._proyectos = [p for p in self._proyectos if p.id != proyecto_id]
    
    def obtener_proyecto_por_nombre(self, nombre: str) -> Proyecto:
        """Busca un proyecto por nombre"""
        for proyecto in self._proyectos:
            if proyecto.nombre.lower() == nombre.lower():
                return proyecto
        return None
    
    @property
    def proyectos(self):
        return self._proyectos.copy()
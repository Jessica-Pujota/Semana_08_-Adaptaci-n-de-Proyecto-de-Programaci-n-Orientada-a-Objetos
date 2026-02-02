from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum

class EstadoTarea(Enum):
    """Enumeración para estados de tarea (Principio de responsabilidad única)"""
    PENDIENTE = "Pendiente"
    EN_PROGRESO = "En progreso"
    COMPLETADA = "Completada"
    BLOQUEADA = "Bloqueada"

class Prioridad(Enum):
    """Enumeración para prioridades (Principio de abierto/cerrado)"""
    BAJA = 1
    MEDIA = 2
    ALTA = 3
    URGENTE = 4
    
class Tarea(ABC):
    """Clase abstracta base para tareas (Principio de sustitución de Liskov)"""
    
    def __init__(self, titulo: str, descripcion: str = "", prioridad: Prioridad = Prioridad.MEDIA):
        self._titulo = titulo
        self._descripcion = descripcion
        self._prioridad = prioridad
        self._estado = EstadoTarea.PENDIENTE
        self._fecha_creacion = datetime.now()
        self._fecha_completada = None
        self._id = id(self)  # ID único basado en dirección de memoria
    
    @property
    def id(self):
        return self._id
    
    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("El título no puede estar vacío")
        self._titulo = valor
    
    @property
    def estado(self):
        return self._estado
    
    @estado.setter
    def estado(self, nuevo_estado: EstadoTarea):
        self._estado = nuevo_estado
        if nuevo_estado == EstadoTarea.COMPLETADA:
            self._fecha_completada = datetime.now()
    
    @abstractmethod
    def calcular_duracion_estimada(self) -> int:
        """Método abstracto para calcular duración estimada"""
        pass
    
    def __str__(self):
        return f"{self._titulo} - {self._estado.value}"
    
    def __repr__(self):
        return f"Tarea(id={self._id}, titulo='{self._titulo}', estado={self._estado})"

class TareaSimple(Tarea):
    """Implementación concreta de Tarea para tareas simples"""
    
    def __init__(self, titulo: str, descripcion: str = "", 
                 prioridad: Prioridad = Prioridad.MEDIA, horas_estimadas: int = 1):
        super().__init__(titulo, descripcion, prioridad)
        self._horas_estimadas = max(1, horas_estimadas)
    
    def calcular_duracion_estimada(self) -> int:
        return self._horas_estimadas
    
    @property
    def horas_estimadas(self):
        return self._horas_estimadas
    
    @horas_estimadas.setter
    def horas_estimadas(self, valor: int):
        if valor < 1:
            raise ValueError("Las horas estimadas deben ser al menos 1")
        self._horas_estimadas = valor

class TareaCompuesta(Tarea):
    """Implementación para tareas compuestas (pueden contener subtareas)"""
    
    def __init__(self, titulo: str, descripcion: str = "", 
                 prioridad: Prioridad = Prioridad.MEDIA):
        super().__init__(titulo, descripcion, prioridad)
        self._subtareas = []
    
    def agregar_subtarea(self, subtarea: Tarea):
        """Agrega una subtarea a la tarea compuesta"""
        if subtarea is self:
            raise ValueError("Una tarea no puede ser subtarea de sí misma")
        self._subtareas.append(subtarea)
    
    def eliminar_subtarea(self, subtarea_id: int):
        """Elimina una subtarea por ID"""
        self._subtareas = [t for t in self._subtareas if t.id != subtarea_id]
    
    def calcular_duracion_estimada(self) -> int:
        """Calcula la duración total sumando todas las subtareas"""
        return sum(tarea.calcular_duracion_estimada() for tarea in self._subtareas)
    
    @property
    def subtareas(self):
        return self._subtareas.copy()
from datetime import datetime
from typing import List
from modelos.tarea import Tarea, EstadoTarea, Prioridad

class Proyecto:        
    """Clase que representa un proyecto con múltiples tareas"""
    def __init__(self, nombre: str, descripcion: str = ""):
        self._nombre = nombre
        self._descripcion = descripcion
        self._tareas = []
        self._fecha_inicio = datetime.now()
        self._fecha_fin_estimada = None
        self._id = id(self)
    
    @property
    def id(self):
        return self._id
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("El nombre del proyecto no puede estar vacío")
        self._nombre = valor
    
    def agregar_tarea(self, tarea: Tarea):
        """Agrega una tarea al proyecto"""
        self._tareas.append(tarea)
    
    def eliminar_tarea(self, tarea_id: int):
        """Elimina una tarea del proyecto por ID"""
        self._tareas = [t for t in self._tareas if t.id != tarea_id]
    
    def obtener_tareas_por_estado(self, estado: EstadoTarea) -> List[Tarea]:
        """Filtra tareas por estado"""
        return [t for t in self._tareas if t.estado == estado]
    
    def obtener_tareas_por_prioridad(self, prioridad: Prioridad) -> List[Tarea]:
        """Filtra tareas por prioridad"""
        return [t for t in self._tareas if t._prioridad == prioridad]
    
    def calcular_progreso(self) -> float:
        """Calcula el porcentaje de progreso del proyecto"""
        if not self._tareas:
            return 0.0
        
        completadas = len(self.obtener_tareas_por_estado(EstadoTarea.COMPLETADA))
        return (completadas / len(self._tareas)) * 100
    
    @property
    def tareas(self):
        return self._tareas.copy()
    
    def __str__(self):
        return f"Proyecto: {self._nombre} ({len(self._tareas)} tareas)"
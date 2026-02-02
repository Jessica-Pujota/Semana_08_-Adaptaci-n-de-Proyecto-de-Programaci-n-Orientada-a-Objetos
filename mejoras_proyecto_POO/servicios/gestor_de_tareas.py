from typing import List, Dict
from modelos.tarea import Tarea, TareaSimple, TareaCompuesta, EstadoTarea, Prioridad

class GestorTareas:
    """Servicio para gestionar operaciones relacionadas con tareas"""
    
    def __init__(self):
        self._tareas = {}
    
    def crear_tarea_simple(self, titulo: str, descripcion: str = "", 
                          prioridad: Prioridad = Prioridad.MEDIA, 
                          horas_estimadas: int = 1) -> TareaSimple:
        """Crea una nueva tarea simple"""
        tarea = TareaSimple(titulo, descripcion, prioridad, horas_estimadas)
        self._tareas[tarea.id] = tarea
        return tarea
    
    def crear_tarea_compuesta(self, titulo: str, descripcion: str = "", 
                             prioridad: Prioridad = Prioridad.MEDIA) -> TareaCompuesta:
        """Crea una nueva tarea compuesta"""
        tarea = TareaCompuesta(titulo, descripcion, prioridad)
        self._tareas[tarea.id] = tarea
        return tarea
    
    def obtener_tarea(self, tarea_id: int) -> Tarea:
        """Obtiene una tarea por ID"""
        return self._tareas.get(tarea_id)
    
    def actualizar_estado_tarea(self, tarea_id: int, estado: EstadoTarea) -> bool:
        """Actualiza el estado de una tarea"""
        tarea = self.obtener_tarea(tarea_id)
        if tarea:
            tarea.estado = estado
            return True
        return False
    
    def filtrar_tareas_por_prioridad(self, prioridad: Prioridad) -> List[Tarea]:
        """Filtra tareas por prioridad"""
        return [t for t in self._tareas.values() if t._prioridad == prioridad]
    
    def obtener_tareas_pendientes(self) -> List[Tarea]:
        """Obtiene todas las tareas pendientes"""
        return self._filtrar_tareas_por_estado(EstadoTarea.PENDIENTE)
    
    def obtener_tareas_completadas(self) -> List[Tarea]:
        """Obtiene todas las tareas completadas"""
        return self._filtrar_tareas_por_estado(EstadoTarea.COMPLETADA)
    
    def _filtrar_tareas_por_estado(self, estado: EstadoTarea) -> List[Tarea]:
        """Método privado para filtrar tareas por estado"""
        return [t for t in self._tareas.values() if t.estado == estado]
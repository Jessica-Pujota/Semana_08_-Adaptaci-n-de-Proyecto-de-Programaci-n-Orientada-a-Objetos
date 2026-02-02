from typing import List, Dict
from modelos.proyecto import Proyecto
from modelos.tarea import Tarea, EstadoTarea

class GestorProyectos:
    """Servicio para gestionar operaciones relacionadas con proyectos"""
    
    def __init__(self):
        self._proyectos = {}
    
    def crear_proyecto(self, nombre: str, descripcion: str = "") -> Proyecto:
        """Crea un nuevo proyecto"""
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del proyecto no puede estar vacío")
        
        proyecto = Proyecto(nombre, descripcion)
        self._proyectos[proyecto.id] = proyecto
        return proyecto
    
    def obtener_proyecto(self, proyecto_id: int) -> Proyecto:
        """Obtiene un proyecto por ID"""
        return self._proyectos.get(proyecto_id)
    
    def eliminar_proyecto(self, proyecto_id: int) -> bool:
        """Elimina un proyecto por ID"""
        if proyecto_id in self._proyectos:
            del self._proyectos[proyecto_id]
            return True
        return False
    
    def listar_proyectos(self) -> List[Proyecto]:
        """Lista todos los proyectos"""
        return list(self._proyectos.values())
    
    def agregar_tarea_a_proyecto(self, proyecto_id: int, tarea: Tarea) -> bool:
        """Agrega una tarea a un proyecto específico"""
        proyecto = self.obtener_proyecto(proyecto_id)
        if proyecto:
            proyecto.agregar_tarea(tarea)
            return True
        return False
    
    def obtener_estadisticas_proyecto(self, proyecto_id: int) -> Dict:
        """Obtiene estadísticas detalladas de un proyecto"""
        proyecto = self.obtener_proyecto(proyecto_id)
        if not proyecto:
            return {}
        
        tareas = proyecto.tareas
        total_tareas = len(tareas)
        
        return {
            'total_tareas': total_tareas,
            'tareas_pendientes': len(proyecto.obtener_tareas_por_estado(EstadoTarea.PENDIENTE)),
            'tareas_en_progreso': len(proyecto.obtener_tareas_por_estado(EstadoTarea.EN_PROGRESO)),
            'tareas_completadas': len(proyecto.obtener_tareas_por_estado(EstadoTarea.COMPLETADA)),
            'progreso': proyecto.calcular_progreso()
        }
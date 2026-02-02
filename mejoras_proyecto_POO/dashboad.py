""" Dashboard para gestión de proyectos y tareas de POO
Refactorizado aplicando principios SOLID y separación de responsabilidades
"""

import os
from typing import Optional
from datetime import datetime

from modelos.tarea import TareaSimple, TareaCompuesta, EstadoTarea, Prioridad
from modelos.proyecto import Proyecto
from modelos.usuario import Usuario
from servicios.gestor_de_proyectos import GestorProyectos
from servicios.gestor_de_tareas import GestorTareas
from servicios.gestor_de_usuarios import GestorUsuarios
from utilerias.validadores import validar_cadena_no_vacia, validar_numero_positivo
class Dashboard:
    """Clase principal del Dashboard que coordina la interfaz de usuario.
    Aplica principio de responsabilidad única: solo maneja la interacción con el usuario.
    """    
    def __init__(self):
        """Inicializa el dashboard con los gestores de servicios"""
        self.gestor_proyectos = GestorProyectos()
        self.gestor_tareas = GestorTareas()
        self.gestor_usuarios = GestorUsuarios()
        self.usuario_actual: Optional[Usuario] = None
        
        # Colores para la interfaz (ANSI escape codes)
        self.COLORES = {
            'titulo': '\033[1;36m',  # Cian brillante
            'subtitulo': '\033[1;33m',  # Amarillo brillante
            'exito': '\033[1;32m',  # Verde brillante
            'error': '\033[1;31m',  # Rojo brillante
            'advertencia': '\033[1;33m',  # Amarillo brillante
            'info': '\033[1;34m',  # Azul brillante
            'menu': '\033[1;35m',  # Magenta brillante
            'reset': '\033[0m'  # Resetear color
        }
    
    def limpiar_pantalla(self):
        """Limpia la pantalla de la consola"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_titulo(self, titulo: str):
        """Muestra un título con formato"""
        print(f"\n{self.COLORES['titulo']}{'='*60}")
        print(f"{titulo.center(60)}")
        print(f"{'='*60}{self.COLORES['reset']}\n")
    
    def mostrar_mensaje(self, mensaje: str, tipo: str = 'info'):
        """Muestra un mensaje con color según el tipo"""
        color = self.COLORES.get(tipo, self.COLORES['info'])
        print(f"{color}{mensaje}{self.COLORES['reset']}")
    
    def pausar(self):
        """Pausa la ejecución hasta que el usuario presione Enter"""
        input(f"\n{self.COLORES['info']}Presiona Enter para continuar...{self.COLORES['reset']}")
    
    def mostrar_menu_principal(self):
        """Muestra el menú principal del dashboard"""
        self.limpiar_pantalla()
        self.mostrar_titulo("DASHBOARD DE GESTIÓN POO")
        
        if self.usuario_actual:
            print(f"Usuario: {self.COLORES['exito']}{self.usuario_actual.nombre}{self.COLORES['reset']}")
            print(f"Rol: {self.usuario_actual.rol}")
            print(f"Proyectos: {len(self.usuario_actual.proyectos)}")
        
        print(f"\n{self.COLORES['menu']}MENÚ PRINCIPAL{self.COLORES['reset']}")
        print("1. Gestionar Proyectos")
        print("2. Gestionar Tareas")
        print("3. Ver Estadísticas")
        print("4. Cambiar de Usuario")
        print("5. Salir")
        
        opcion = input(f"\n{self.COLORES['subtitulo']}Selecciona una opción: {self.COLORES['reset']}")
        return opcion
    
    def gestionar_proyectos(self):
        """Menú para gestionar proyectos"""
        while True:
            self.limpiar_pantalla()
            self.mostrar_titulo("GESTIÓN DE PROYECTOS")
            
            print("1. Crear nuevo proyecto")
            print("2. Listar proyectos")
            print("3. Ver detalles de proyecto")
            print("4. Agregar tarea a proyecto")
            print("5. Volver al menú principal")
            
            opcion = input(f"\n{self.COLORES['subtitulo']}Selecciona una opción: {self.COLORES['reset']}")
            
            if opcion == '1':
                self.crear_proyecto()
            elif opcion == '2':
                self.listar_proyectos()
            elif opcion == '3':
                self.ver_detalles_proyecto()
            elif opcion == '4':
                self.agregar_tarea_a_proyecto()
            elif opcion == '5':
                break
            else:
                self.mostrar_mensaje("Opción inválida. Intenta nuevamente.", 'error')
                self.pausar()
    
    def crear_proyecto(self):
        """Crea un nuevo proyecto"""
        self.limpiar_pantalla()
        self.mostrar_titulo("CREAR NUEVO PROYECTO")
        
        try:
            nombre = validar_cadena_no_vacia(
                input("Nombre del proyecto: "), 
                "Nombre del proyecto"
            )
            descripcion = input("Descripción (opcional): ")
            proyecto = self.gestor_proyectos.crear_proyecto(nombre, descripcion)
            if self.usuario_actual:
                self.usuario_actual.agregar_proyecto(proyecto)
            
            self.mostrar_mensaje(f"¡Proyecto '{nombre}' creado exitosamente!", 'exito')
            self.mostrar_mensaje(f"ID del proyecto: {proyecto.id}", 'info')
        
        except ValueError as e:
            self.mostrar_mensaje(f"Error: {e}", 'error')
        self.pausar()
    
    def listar_proyectos(self):
        """Lista todos los proyectos"""
        self.limpiar_pantalla()
        self.mostrar_titulo("LISTA DE PROYECTOS")
        proyectos = self.gestor_proyectos.listar_proyectos()
        
        if not proyectos:
            self.mostrar_mensaje("No hay proyectos registrados.", 'advertencia')
        else:
            for i, proyecto in enumerate(proyectos, 1):
                progreso = proyecto.calcular_progreso()
                tareas = proyecto.tareas
                
                # Determinar color según progreso
                if progreso == 100:
                    color_progreso = self.COLORES['exito']
                elif progreso > 50:
                    color_progreso = self.COLORES['info']
                else:
                    color_progreso = self.COLORES['advertencia']
                
                print(f"{self.COLORES['subtitulo']}{i}. {proyecto.nombre}{self.COLORES['reset']}")
                print(f"   ID: {proyecto.id}")
                print(f"   Tareas: {len(tareas)}")
                print(f"   Progreso: {color_progreso}{progreso:.1f}%{self.COLORES['reset']}")
                print()
        
        self.pausar()
    
    def ver_detalles_proyecto(self):
        """Muestra detalles de un proyecto específico"""
        self.limpiar_pantalla()
        self.mostrar_titulo("DETALLES DE PROYECTO")
        
        try:
            proyecto_id = int(input("ID del proyecto: "))
            proyecto = self.gestor_proyectos.obtener_proyecto(proyecto_id)
            
            if not proyecto:
                self.mostrar_mensaje("Proyecto no encontrado.", 'error')
                self.pausar()
                return
            
            estadisticas = self.gestor_proyectos.obtener_estadisticas_proyecto(proyecto_id)
            progreso = proyecto.calcular_progreso()
            
            # Mostrar información del proyecto
            print(f"{self.COLORES['subtitulo']}Nombre:{self.COLORES['reset']} {proyecto.nombre}")
            print(f"{self.COLORES['subtitulo']}Descripción:{self.COLORES['reset']} {proyecto._descripcion}")
            print(f"{self.COLORES['subtitulo']}ID:{self.COLORES['reset']} {proyecto.id}")
            print()
            
            # Barra de progreso
            barra_largo = 40
            completado = int((progreso / 100) * barra_largo)
            barra = f"[{'#' * completado}{'-' * (barra_largo - completado)}]"
            
            print(f"{self.COLORES['subtitulo']}Progreso:{self.COLORES['reset']}")
            print(f"  {barra} {progreso:.1f}%")
            print()
            
            # Estadísticas
            print(f"{self.COLORES['subtitulo']}Estadísticas:{self.COLORES['reset']}")
            print(f"  Total tareas: {estadisticas['total_tareas']}")
            print(f"  Pendientes: {estadisticas['tareas_pendientes']}")
            print(f"  En progreso: {estadisticas['tareas_en_progreso']}")
            print(f"  Completadas: {estadisticas['tareas_completadas']}")
            print()
            
            # Listar tareas
            if proyecto.tareas:
                print(f"{self.COLORES['subtitulo']}Tareas del proyecto:{self.COLORES['reset']}")
                for i, tarea in enumerate(proyecto.tareas, 1):
                    estado_color = self.COLORES['exito'] if tarea.estado == EstadoTarea.COMPLETADA else self.COLORES['info']
                    print(f"  {i}. {tarea.titulo} - {estado_color}{tarea.estado.value}{self.COLORES['reset']}")
        
        except ValueError:
            self.mostrar_mensaje("ID inválido. Debe ser un número.", 'error')
        
        self.pausar()
    
    def agregar_tarea_a_proyecto(self):
        """Agrega una tarea a un proyecto existente"""
        self.limpiar_pantalla()
        self.mostrar_titulo("AGREGAR TAREA A PROYECTO")
        
        try:
            proyecto_id = int(input("ID del proyecto: "))
            proyecto = self.gestor_proyectos.obtener_proyecto(proyecto_id)
            
            if not proyecto:
                self.mostrar_mensaje("Proyecto no encontrado.", 'error')
                self.pausar()
                return
            
            print(f"\nProyecto: {self.COLORES['info']}{proyecto.nombre}{self.COLORES['reset']}")
            print("\n1. Crear tarea simple")
            print("2. Crear tarea compuesta")
            
            tipo_tarea = input("\nTipo de tarea: ")
            
            titulo = validar_cadena_no_vacia(input("Título de la tarea: "), "Título de la tarea")
            descripcion = input("Descripción (opcional): ")
            
            # Seleccionar prioridad
            print("\nPrioridades disponibles:")
            for prioridad in Prioridad:
                print(f"  {prioridad.value}. {prioridad.name}")
            
            prioridad_valor = int(input("\nPrioridad (1-4): "))
            prioridad = Prioridad(prioridad_valor)
            
            if tipo_tarea == '1':
                horas = int(input("Horas estimadas: "))
                horas = validar_numero_positivo(horas, "Horas estimadas")
                tarea = self.gestor_tareas.crear_tarea_simple(titulo, descripcion, prioridad, horas)
            else:
                tarea = self.gestor_tareas.crear_tarea_compuesta(titulo, descripcion, prioridad)
            
            # Agregar tarea al proyecto
            self.gestor_proyectos.agregar_tarea_a_proyecto(proyecto_id, tarea)
            
            self.mostrar_mensaje(f"¡Tarea '{titulo}' agregada al proyecto exitosamente!", 'exito')
        
        except (ValueError, KeyError) as e:
            self.mostrar_mensaje(f"Error: {e}", 'error')
        
        self.pausar()
    
    def gestionar_tareas(self):
        """Menú para gestionar tareas"""
        while True:
            self.limpiar_pantalla()
            self.mostrar_titulo("GESTIÓN DE TAREAS")
            
            print("1. Ver todas las tareas")
            print("2. Ver tareas pendientes")
            print("3. Ver tareas completadas")
            print("4. Cambiar estado de tarea")
            print("5. Volver al menú principal")
            
            opcion = input(f"\n{self.COLORES['subtitulo']}Selecciona una opción: {self.COLORES['reset']}")
            
            if opcion == '1':
                self.listar_todas_tareas()
            elif opcion == '2':
                self.listar_tareas_pendientes()
            elif opcion == '3':
                self.listar_tareas_completadas()
            elif opcion == '4':
                self.cambiar_estado_tarea()
            elif opcion == '5':
                break
            else:
                self.mostrar_mensaje("Opción inválida. Intenta nuevamente.", 'error')
                self.pausar()
    
    def listar_todas_tareas(self):
        """Lista todas las tareas del sistema"""
        self.limpiar_pantalla()
        self.mostrar_titulo("TODAS LAS TAREAS")
        
        # Obtener tareas de todos los proyectos
        todas_tareas = []
        proyectos = self.gestor_proyectos.listar_proyectos()
        
        for proyecto in proyectos:
            for tarea in proyecto.tareas:
                todas_tareas.append((proyecto, tarea))
        
        if not todas_tareas:
            self.mostrar_mensaje("No hay tareas registradas.", 'advertencia')
        else:
            for i, (proyecto, tarea) in enumerate(todas_tareas, 1):
                estado_color = self.COLORES['exito'] if tarea.estado == EstadoTarea.COMPLETADA else self.COLORES['info']
                print(f"{self.COLORES['subtitulo']}{i}. {tarea.titulo}{self.COLORES['reset']}")
                print(f"   Proyecto: {proyecto.nombre}")
                print(f"   Estado: {estado_color}{tarea.estado.value}{self.COLORES['reset']}")
                print(f"   Duración estimada: {tarea.calcular_duracion_estimada()} horas")
                print()
        
        self.pausar()
    
    def listar_tareas_pendientes(self):
        """Lista todas las tareas pendientes"""
        self.limpiar_pantalla()
        self.mostrar_titulo("TAREAS PENDIENTES")
        
        tareas_pendientes = self.gestor_tareas.obtener_tareas_pendientes()
        
        if not tareas_pendientes:
            self.mostrar_mensaje("No hay tareas pendientes. ¡Buen trabajo!", 'exito')
        else:
            for i, tarea in enumerate(tareas_pendientes, 1):
                print(f"{self.COLORES['subtitulo']}{i}. {tarea.titulo}{self.COLORES['reset']}")
                print(f"   Prioridad: {tarea._prioridad.name}")
                print(f"   Duración estimada: {tarea.calcular_duracion_estimada()} horas")
                print()
        
        self.pausar()
    
    def listar_tareas_completadas(self):
        """Lista todas las tareas completadas"""
        self.limpiar_pantalla()
        self.mostrar_titulo("TAREAS COMPLETADAS")
        
        tareas_completadas = self.gestor_tareas.obtener_tareas_completadas()
        
        if not tareas_completadas:
            self.mostrar_mensaje("No hay tareas completadas.", 'advertencia')
        else:
            for i, tarea in enumerate(tareas_completadas, 1):
                print(f"{self.COLORES['exito']}{i}. {tarea.titulo}{self.COLORES['reset']}")
                print(f"   Completada el: {tarea._fecha_completada}")
                print()
        
        self.pausar()
    
    def cambiar_estado_tarea(self):
        """Cambia el estado de una tarea"""
        self.limpiar_pantalla()
        self.mostrar_titulo("CAMBIAR ESTADO DE TAREA")
        
        try:
            tarea_id = int(input("ID de la tarea: "))
            tarea = self.gestor_tareas.obtener_tarea(tarea_id)
            
            if not tarea:
                self.mostrar_mensaje("Tarea no encontrada.", 'error')
                self.pausar()
                return
            
            print(f"\nTarea: {self.COLORES['info']}{tarea.titulo}{self.COLORES['reset']}")
            print(f"Estado actual: {tarea.estado.value}")
            print("\nEstados disponibles:")
            for estado in EstadoTarea:
                print(f"{estado.value}. {estado.name}") 
            nuevo_estado_valor = int(input("\nNuevo estado: "))
            nuevo_estado = EstadoTarea(nuevo_estado_valor)    
            self.gestor_tareas.actualizar_estado_tarea(tarea_id, nuevo_estado)
            self.mostrar_mensaje(f"¡Estado de la tarea '{tarea.titulo}' actualizado a '{nuevo_estado.name}'!", 'exito')
        except (ValueError, KeyError) as e:
            self.mostrar_mensaje(f"Error al cambiar estado de la tarea: {e}", 'error')
        self.pausar()
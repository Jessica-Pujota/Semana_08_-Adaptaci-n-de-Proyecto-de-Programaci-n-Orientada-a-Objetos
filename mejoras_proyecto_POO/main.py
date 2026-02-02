#!/usr/bin/env python3
"""
Archivo principal del sistema de gestión POO
Punto de entrada de la aplicación
"""
import sys
import os

# Agregar el directorio actual al path para que Python encuentre los módulos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from servicios.gestor_de_proyectos import GestorProyectos
    from servicios.gestor_de_tareas import GestorTareas
    from servicios.gestor_de_usuarios import GestorUsuarios
    
    # Prueba básica del sistema
    def main():
        print("=== SISTEMA DE GESTIÓN POO ===")
        print("Inicializando gestores...")
        
        # Crear instancias de los gestores
        gestor_proyectos = GestorProyectos()
        gestor_usuarios = GestorUsuarios()
        
        print("Gestores inicializados correctamente!")
        print(f"Gestor de proyectos: {gestor_proyectos}")
        print(f"Gestor de usuarios: {gestor_usuarios}")
        
        # Crear un usuario de prueba
        usuario = gestor_usuarios.registrar_usuario("Jessica", "jessica@example.com", "estudiante")
        print(f"\nUsuario creado: {usuario.nombre}")
        
        # Crear un proyecto de prueba
        proyecto = gestor_proyectos.crear_proyecto("Mi primer proyecto POO", "Proyecto de ejemplo")
        print(f"Proyecto creado: {proyecto.nombre}")
        
        print("\n¡Sistema funcionando correctamente!")
    
    if __name__ == "__main__":
        main()

except ImportError as e:
    print(f"Error de importación: {e}")
    print("\nAsegúrate de que:")
    print("1. Estás ejecutando desde la carpeta raíz del proyecto")
    print("2. Tienes todas las carpetas creadas: modelos/, servicios/")
    print("3. Los archivos __init__.py existen en cada carpeta")
    print("\nEstructura esperada:")
    print("mejoras_proyecto_POO/")
    print("├── modelos/")
    print("│   ├── __init__.py")
    print("│   ├── proyecto.py")
    print("│   ├── tarea.py")
    print("│   └── usuario.py")
    print("├── servicios/")
    print("│   ├── __init__.py")
    print("│   └── gestor_de_proyectos.py")
    print("└── main.py")
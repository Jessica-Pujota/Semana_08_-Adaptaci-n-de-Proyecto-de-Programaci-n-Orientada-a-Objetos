# Semana_08_-Adaptacion de Proyecto de Programacion Orientada a Objetos

Sistema de Gestión de Tareas POO con Principios SOLID

### Descripción del Proyecto
Este es un sistema de gestión de tareas y proyectos desarrollado en Python aplicando los principios SOLID de Programación Orientada a Objetos. El sistema permite a los estudiantes de POO organizar sus tareas, proyectos y actividades académicas de manera eficiente.

### Objetivos del Proyecto
- Aplicar principios SOLID en un proyecto real
- Separar responsabilidades mediante arquitectura en capas
- Implementar buenas prácticas de programación orientada a objetos
- Crear un sistema modular y fácil de mantener
- Desarrollar una interfaz de usuario intuitiva

### 🛠️ Principios SOLID Aplicados
1. S - Single Responsibility Principle (SRP)
Cada clase tiene una única responsabilidad

- Tarea: Representa una tarea del sistema
- GestorProyectos: Gestiona operaciones de proyectos
- Dashboard: Maneja solo la interfaz de usuario

2. O - Open/Closed Principle (OCP): Las clases están abiertas para extensión pero cerradas para modificación

- Tarea es abstracta, permite crear nuevos tipos sin modificar el código existente
- Prioridad y EstadoTarea como enumeraciones para fácil extensión

3. L - Liskov Substitution Principle (LSP): Las subclases pueden sustituir a sus clases base

- TareaSimple y TareaCompuesta pueden usarse donde se espera Tarea
- Todas implementan calcular_duracion_estimada() correctamente

4. I - Interface Segregation Principle (ISP)
Interfaces específicas para cada cliente

- Separación clara entre modelos, servicios y UI
- Ninguna clase depende de métodos que no usa

5. D - Dependency Inversion Principle (DIP): Dependencias de abstracciones, no de implementaciones concretas

- Los servicios dependen de interfaces de modelos
- Inyección de dependencias en el dashboard

### ✨ Características Principales
📊 Gestión de Proyectos
- Crear, listar y eliminar proyectos
- Seguimiento de progreso con barras visuales
- Estadísticas detalladas por proyecto

✅ Gestión de Tareas
- Tareas simples y compuestas (con subtareas)
- Sistema de prioridades (Baja, Media, Alta, Urgente)
- Estados: Pendiente, En progreso, Completada, Bloqueada
- Cálculo automático de duración estimada

👥 Gestión de Usuarios
- Registro y autenticación de usuarios
- Asignación de roles (estudiante, profesor, admin)
- Asociación de proyectos a usuarios

🎨 Interfaz de Usuario
- Dashboard con colores ANSI para mejor legibilidad
- Menús interactivos y fáciles de usar
- Formato consistente en toda la aplicación
- Limpieza automática de pantalla

🚀 Instalación y Uso
Requisitos Previos
Python 3.8 o superior

Git (para control de versiones)
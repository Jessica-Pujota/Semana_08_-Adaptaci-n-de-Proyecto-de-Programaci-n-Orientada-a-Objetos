from typing import List, Optional
from modelos.usuario import Usuario

class GestorUsuarios:
    """Servicio para gestionar operaciones relacionadas con usuarios"""
    
    def __init__(self):
        self._usuarios = {}
    
    def registrar_usuario(self, nombre: str, email: str, rol: str = "estudiante") -> Usuario:
        """Registra un nuevo usuario en el sistema"""
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        
        if not self._validar_email(email):
            raise ValueError("El email no tiene un formato válido")
        
        # Verificar si el email ya está registrado
        if self._buscar_usuario_por_email(email):
            raise ValueError("El email ya está registrado")
        
        usuario = Usuario(nombre, email, rol)
        self._usuarios[usuario.id] = usuario
        return usuario
    
    def obtener_usuario(self, usuario_id: int) -> Optional[Usuario]:
        """Obtiene un usuario por ID"""
        return self._usuarios.get(usuario_id)
    
    def _buscar_usuario_por_email(self, email: str) -> Optional[Usuario]:
        """Busca un usuario por email (método privado)"""
        for usuario in self._usuarios.values():
            if usuario.email == email:
                return usuario
        return None
    
    def _validar_email(self, email: str) -> bool:
        """Valida el formato del email (método privado)"""
        # Validación básica de email
        return '@' in email and '.' in email
    
    def listar_usuarios(self) -> List[Usuario]:
        """Lista todos los usuarios registrados"""
        return list(self._usuarios.values())
    
    def autenticar_usuario(self, nombre: str) -> Optional[Usuario]:
        """Autentica un usuario por nombre"""
        for usuario in self._usuarios.values():
            if usuario.nombre.lower() == nombre.lower():
                return usuario
        return None
    
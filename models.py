from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional

class Usuarios(BaseModel):
	id: str=Field(..., example='u1')
	nombre: str= Field(..., example='Enrique')
	email: EmailStr= Field(..., example='enrique.manrique@example.com')
	edad: int= Field(..., example=34)

class Proyectos(BaseModel):
	id: str=Field(..., example='p1')
	nombre: str= Field(..., example='Desarrollo de aplicación movil')
	descripcion: Optional[str]= Field(None, example='Desarrollar una app que permite a los usuarios interactuar desde su dispositivo móvil, con notificaciones sobre promociones y recordatorios')
	id_usuario: str = Field (..., example='u1')
	fecha_creacion: str = Field(..., example='2024-10-23T19:00:002')
	
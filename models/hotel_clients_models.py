from pydantic import BaseModel

class ingresarNuevoCliente(BaseModel):
    email:str
    nombre:str
    apellido:str
    telefono:str
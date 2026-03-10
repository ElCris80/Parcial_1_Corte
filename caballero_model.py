from pydantic import BaseModel

from enum_material import Material

class Caballero(BaseModel):
    id: int
    name: str
    material: Material
    attack: int
    constelation: str


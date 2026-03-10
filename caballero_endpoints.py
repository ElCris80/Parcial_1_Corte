from fastapi import APIRouter, HTTPException
from datetime import datetime

from caballero_model import Caballero
from db import lista_caballeros
from enum_material import Material

router = APIRouter(prefix="/caballero", tags=["caballero"])

@router.get("/lista_caballeros")
def listaCaballeros():
    return lista_caballeros

@router.get("/show_caballero/{id}")
def showCaballero(id: int):
    for caballero in lista_caballeros:
        if caballero.id == id:
            return caballero
    raise HTTPException(status_code=404, detail="Caballero no encontrado")

@router.get("/figth_caballero/{id1}/{id2}")
def figthCaballero(id1: int, id2: int):
    caballero1 = None
    caballero2 = None

    for caballero in lista_caballeros:
        if caballero.id == id1:
            caballero1 = caballero
        elif caballero.id == id2:
            caballero2 = caballero

    if not caballero1 or not caballero2:
        raise HTTPException(status_code=404, detail="Uno o ambos caballeros no encontrados")

    if caballero1.attack > caballero2.attack:
        return {"winner": caballero1.name}
    elif caballero2.attack > caballero1.attack:
        return {"winner": caballero2.name}
    else:
        return {"message": "Empate"}
    
@router.get("/show_Constelation/{id}")
def showConstelation(id: int):
    caballero = showCaballero(id)
    if caballero:
        return {"constelation": caballero.constelation}
    raise HTTPException(status_code=404, detail="Caballero no encontrado")

@router.get("/showYourCaballero")
def showYourCaballero(date: datetime):
    """
    date = datetime.strptime(date_str, "%Y-%m-%d")
    date = datetime(2024, 6, 15)  # Ejemplo de fecha
    """
    day_of_week = date.weekday()
    caballero = lista_caballeros[day_of_week % len(lista_caballeros)]
    return {"caballero": caballero.name, "constelation": caballero.constelation}

@router.get("/filter_by_material/{material}")
def filterByMaterial(material: str):
    try:
        mat = Material[material.upper()]
    except KeyError:
        raise HTTPException(status_code=400, detail="Material inválido")
    filtered = [c for c in lista_caballeros if c.material == mat]
    return filtered

@router.get("/filter_by_constelation/{constelation}")
def filterByConstelation(constelation: str):
    filtered = [c for c in lista_caballeros if c.constelation.lower() == constelation.lower()]
    return filtered


@router.get("/top_attack/{n}")
def topAttack(n: int):
    if n <= 0:
        raise HTTPException(status_code=400, detail="n debe ser positivo")
    sorted_list = sorted(lista_caballeros, key=lambda c: c.attack, reverse=True)
    return sorted_list[:n]


@router.get("/stats")
def stats():
    if not lista_caballeros:
        return {"message": "No hay caballeros"}
    attacks = [c.attack for c in lista_caballeros]
    return {
        "total_caballeros": len(lista_caballeros),
        "average_attack": sum(attacks) / len(attacks),
        "max_attack": max(attacks),
        "min_attack": min(attacks)
    }
    

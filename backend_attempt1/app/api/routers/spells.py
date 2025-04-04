from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(
    prefix='/api/spells'
)


class Spell(BaseModel):
    name: str
    level: str
    # TODO: add below. For tutorial purpose, stick w name and level
    # cast_class: str
    # cast_time: str
    # range: str
    # components: str # should prob be an array of strings/chars?
    # duration: str
    # description: str
    # spell_list: str # should def be an array of string


all_spells = [
    Spell(name='Fireball', level='3'),
    Spell(name='Chill Touch', level='0')
]


@router.get('/', response_model=List[Spell])
async def get_spells():
    # Retrieve all spells
    return all_spells


@router.get('/list/', response_model=List[str])
async def get_spell_names():
    # Retrieve list of spell names
    return [spell.name for spell in all_spells]

from typing import Any, Annotated

from fastapi import FastAPI, Body

from database import Database
from entites.person import Person

app = FastAPI()

db = Database()


@app.post("/api/person")
async def add_person(firstname: Annotated[str, Body()], lastname: Annotated[str, Body()]) -> int | bool:
    person = db.add_person(Person(firstname=firstname, lastname=lastname))
    return person.id or False


@app.get("/api/person/list")
async def get_person_list() -> list[dict[str, Any]]:
    return db.get_persons_list()


@app.get("/api/person/{person_id}")
async def get_person(person_id: int) -> Person | bool:
    return db.get_person(person_id) or False


@app.post("/api/person/{person_id}/field")
async def add_field(person_id: int, name: Annotated[str, Body()], content: Annotated[str, Body()] = "") -> bool:
    return db.add_field_to_person(person_id, name, content)


@app.put("/api/person/{person_id}/field/{field_name}/content")
async def edit_field(person_id: int, field_name: str, content: Annotated[str, Body()]) -> bool:
    return db.edit_field_to_person(person_id, field_name, content)


@app.put("/api/person/{person_id}/field/{field_name}/rename")
async def edit_field(person_id: int, field_name: str, new_name: Annotated[str, Body()]) -> bool:
    return db.edit_field_to_person(person_id, field_name, new_name)


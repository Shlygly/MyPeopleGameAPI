from typing import Any

from pydantic import BaseModel

from entites.field import Field


class Person(BaseModel):
    id: int | None = None
    firstname: str
    lastname: str
    fields: list[Field] = [
        Field(name="divers")
    ]

    def get_fullname(self) -> str:
        return f"{self.firstname.title()} {self.lastname.title()}"

    def add_field(self, name: str, content: str = "") -> bool:
        if not self.has_field(name):
            self.fields.append(Field(name=name.lower(), content=content))
            return True
        return False

    def has_field(self, name: str) -> bool:
        return any(name.lower() == field.name for field in self.fields)

    def edit_field(self, name: str, content: str) -> bool:
        if self.has_field(name):
            for field in self.fields:
                if field.name == name:
                    field.content = content
                    return True
        return False

    def rename_field(self, old_name: str, new_name: str) -> bool:
        if self.has_field(old_name):
            for field in self.fields:
                if field.name == old_name:
                    field.name = new_name
                    return True
        return False

    def short_dump(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "fullname": self.get_fullname(),
            "description": next(
                (
                    field.content
                    for field in self.fields
                    if field.name == "description"
                ),
                False
            )
        }

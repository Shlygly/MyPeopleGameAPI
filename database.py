from typing import Any

from entites.person import Person


class Database:
    def __init__(self):
        self.persons: list[Person] = [
            Person(id=1, firstname="Mickey", lastname="Brenon"),
            Person(id=2, firstname="David", lastname="Brenon"),
            Person(id=3, firstname="Maëva", lastname="Berthier")
        ]

    def add_person(self, person: Person) -> Person:
        new_id = max(*(person.id for person in self.persons)) + 1
        person.id = new_id
        self.persons.append(person)
        return person

    def get_persons_list(self) -> list[dict[str, Any]]:
        return [
            person.short_dump()
            for person in self.persons
        ]

    def get_person(self, person_id: int) -> Person | None:
        return next(
            (
                person
                for person in self.persons
                if person.id == person_id
            ),
            None
        )

    def add_field_to_person(self, person_id: int, name: str, content: str = "") -> bool:
        person = self.get_person(person_id)
        if person:
            return person.add_field(name, content)
        return False

    def edit_field_to_person(self, person_id: int, name: str, content: str) -> bool:
        person = self.get_person(person_id)
        if person:
            return person.edit_field(name, content)
        return False

    def rename_field_to_person(self, person_id: int, old_name: str, new_name: str) -> bool:
        person = self.get_person(person_id)
        if person:
            return person.rename_field(old_name, new_name)
        return False

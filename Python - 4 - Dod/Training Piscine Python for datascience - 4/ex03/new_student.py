import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Dataclass for a student with auto login and random id."""
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):

        # login = first letter of name + surname,
        # capitalized (e.g., "E" + "agle" -> "Eagle")
        if not isinstance(self.name, str) or not isinstance(self.surname, str):
            raise TypeError("name and surname must be strings")
        if not self.name:
            raise ValueError("name must be non-empty")
        self.login = (self.name[0] + self.surname).capitalize()

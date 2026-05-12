from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Your docstring for Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Your docstring for Method"""
        self.is_alive = False

    @abstractmethod
    def __str__(self):
        pass


class Stark(Character):
    """Your docstring for Class"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)

    def __str__(self):
        """Your docstring for Method"""
        return f"A Stark named {self.first_name}"

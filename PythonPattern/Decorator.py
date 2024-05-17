"""
dynamically attach new behaviour to objects without changing its implementation by wrapping the object into
new wrapper object
"""

# create abstract Coffee/ interface and create a concreate class first like plain coffee
from abc import ABC, abstractmethod
class Character(ABC):
    @abstractmethod
    def get_damage(self):
        pass
    @abstractmethod
    def get_description(self):
        pass

class BasicCharacter(Character):
    def get_damage(self):
        return 1
    def get_description(self):
        return "Basic Character"


# create a decorator interface or abstract class that take obj of Character
class CharacterDecorator(Character,ABC):
    def __init__(self, character) -> None:
        self._character = character
        
    @abstractmethod
    def get_description(self):
        pass
    @abstractmethod
    def get_damage(self):
        pass

class DoubleDamageDecorator(CharacterDecorator):
    def get_description(self):
        return self._character.get_description() + " with Double Damage"
    def get_damage(self):
        return self._character.get_damage()*2

class FireballDecorator(CharacterDecorator):
    def get_description(self):
        return self._character.get_description() + " with Fireball"
    def get_damage(self):
        return self._character.get_damage() + 20

# if __name__=="__main__":
#     character = BasicCharacter()
#     print(character.get_description())
#     print(character.get_damage())

#     double_damage_decorator = DoubleDamageDecorator(character)
#     print(double_damage_decorator.get_description())  
#     print(double_damage_decorator.get_damage())

#     double_fireball_character = DoubleDamageDecorator(FireballDecorator(character))
#     print(double_fireball_character.get_description())  
#     print(double_fireball_character.get_damage())


class BasePizza(ABC):
    @abstractmethod
    def get_cost(self):
        pass

class PlainDough(BasePizza):
    def get_cost(self):
        return 10
    
class MaidaDough(BasePizza):
    def get_cost(self):
        return 5

class PizzaDecorator(BasePizza, ABC):
    def __init__(self, basePizza) -> None:
        self._basePizza = basePizza
    def get_cost(self):
        pass

class CheeseTopping(PizzaDecorator):
    def get_cost(self):
        return self._basePizza.get_cost() + 33

if __name__=="__main__":
    plaindough = MaidaDough()
    cheeseTopping = CheeseTopping(plaindough)
    print(cheeseTopping.get_cost())
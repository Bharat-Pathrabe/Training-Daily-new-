from abc import ABC, abstractmethod
class Character(ABC):
   def __init__(self, name, health, attack, defense, gold):
       self._name = name
       self._health = health
       self._attack = attack
       self._defense = defense
       self._gold = gold
   def get_name(self):
       return self._name
   def get_health(self):
       return self._health
   def set_health(self, health):
       self._health = health
   def get_attack(self):
       return self._attack
   def get_defense(self):
       return self._defense
   def get_gold(self):
       return self._gold
   def increase_gold(self, amount):
       self._gold += amount
   def decrease_gold(self, amount):
       self._gold -= amount
   @abstractmethod
   def attack_enemy(self, enemy):
       pass
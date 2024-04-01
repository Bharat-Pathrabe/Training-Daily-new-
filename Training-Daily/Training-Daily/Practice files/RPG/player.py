from character import Character
class Player(Character):
   def __init__(self, name, health, attack, defense, gold):
       super().__init__(name, health, attack, defense, gold)
   def attack_enemy(self, enemy):
       damage = max(0, self.get_attack() - enemy.get_defense())
       enemy.set_health(enemy.get_health() - damage)
       print(f"{self.get_name()} attacks {enemy.get_name()} for {damage} damage!")
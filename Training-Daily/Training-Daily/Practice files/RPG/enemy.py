from character import Character
class Enemy(Character):
   def __init__(self, name, health, attack, defense, gold):
       super().__init__(name, health, attack, defense, gold)
   def attack_enemy(self, player):
       damage = max(0, self.get_attack() - player.get_defense())
       player.set_health(player.get_health() - damage)
       print(f"{self.get_name()} attacks {player.get_name()} for {damage} damage!")
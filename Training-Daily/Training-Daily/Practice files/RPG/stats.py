class Stats:
   @staticmethod
   def display_stats(player):
       print(f"Name: {player.get_name()}")
       print(f"Health: {player.get_health()}")
       print(f"Attack: {player.get_attack()}")
       print(f"Defense: {player.get_defense()}")
       print(f"Gold: {player.get_gold()}")
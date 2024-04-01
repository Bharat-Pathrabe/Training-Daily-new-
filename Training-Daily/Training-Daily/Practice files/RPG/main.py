import random
from player import Player
from enemy import Enemy
from merchant import Merchant
from stats import Stats
def battle(player, enemy):
   print(f"A wild {enemy.get_name()} appears!")
   while player.get_health() > 0 and enemy.get_health() > 0:
       print(f"Your health: {player.get_health()}")
       print(f"{enemy.get_name()}'s health: {enemy.get_health()}")
       print("1. Attack")
       print("2. Run")
       choice = input("Choose your action: ")
       if choice == "1":
           player.attack_enemy(enemy)
           if enemy.get_health() <= 0:
               print(f"You defeated the {enemy.get_name()}!")
               player.increase_gold(enemy.get_gold())
               break
           enemy.attack_enemy(player)
           if player.get_health() <= 0:
               print("You were defeated!")
               break
       elif choice == "2":
           print("You run away from the battle!")
           break
def main():
   print("Welcome to the Text-based RPG!")
   name = input("Enter your name: ")
   player = Player(name, 100, 10, 5, 50)
   merchant = Merchant()
   while True:
       print("\n1. Explore")
       print("2. Check Stats")
       print("3. Visit Merchant")
       print("4. Quit")
       choice = input("Choose your action: ")
       if choice == "1":
           enemy = random.choice(enemies)
           battle(player, Enemy(**enemy))
       elif choice == "2":
           Stats.display_stats(player)
       elif choice == "3":
           print("Welcome to the Merchant's Shop!")
           print("Available items:")
           for item, cost in merchant.get_stock().items():
               print(f"{item}: {cost} gold")
           action = input("Do you want to buy or sell? (buy/sell): ")
           if action.lower() == "buy":
               item_to_buy = input("Enter the item name you want to buy: ")
               merchant.sell_item(player, item_to_buy)
           elif action.lower() == "sell":
               item_to_sell = input("Enter the item name you want to sell: ")
               merchant.buy_item(player, item_to_sell)
           else:
               print("Invalid choice.")
       elif choice == "4":
           print("Goodbye!")
           break
       else:
           print("Invalid choice. Please try again.")
if __name__ == "__main__":
   enemies = [
       {"name": "Goblin", "health": 30, "attack": 8, "defense": 2, "gold": 20},
       {"name": "Skeleton", "health": 40, "attack": 10, "defense": 3, "gold": 30},
       {"name": "Orc", "health": 50, "attack": 12, "defense": 5, "gold": 50}
   ]
   main()
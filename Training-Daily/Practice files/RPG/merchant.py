class Merchant:
   def __init__(self):
       self._stock = {"Health Potion": 50, "Magic Sword": 100}
   def get_stock(self):
       return self._stock
   def sell_item(self, player, item_name):
       if item_name in self._stock:
           cost = self._stock[item_name]
           player.decrease_gold(cost)
           print(f"{player.get_name()} bought {item_name} for {cost} gold.")
       else:
           print("Item not available in stock.")
   def buy_item(self, player, item_name):
       if item_name in player.get_inventory():
           price = player.get_inventory()[item_name]
           player.increase_gold(price)
           print(f"{player.get_name()} sold {item_name} for {price} gold.")
           del player.get_inventory()[item_name]
       else:
           print("Item not available.")
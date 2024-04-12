"""    1) Write a Python program to create a class representing a shopping cart which Includes the following methods.
        ◦ Adding a non-existing product with quantity and price. Quantity defaults to 1 if not provided.
        ◦ Removing an existing product.
        ◦ Updating the quantity/price of an existing product.
        ◦ Calculating the total unique products.
        ◦ Calculating the total price of all the products.
Example:

"Apple": {
“price“:78.25, “quantity“:1

"Orange”: {
“price“:63.75, ”quantity“:2 """

class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_product(self, name, price, quantity=1):
        if name in self.cart:
            print("Product already exists in the cart.")
            return
        self.cart[name] = {"price": price, "quantity": quantity}
        print(f"{name} added to the cart.")

    def remove_product(self, name):
        if name in self.cart:
            del self.cart[name]
            print(f"{name} removed from the cart.")
        else:
            print("Product not found in the cart.")

    def update_product(self, name, price=None, quantity=None):
        if name in self.cart:
            if price is not None:
                self.cart[name]["price"] = price
            if quantity is not None:
                self.cart[name]["quantity"] = quantity
            print(f"{name} updated successfully.")
        else:
            print("Product not found in the cart.")

    def total_unique_products(self):
        return len(self.cart)

    def total_price(self):
        total = sum(item["price"] * item["quantity"] for item in self.cart.values())
        return total


ob_sc = ShoppingCart()
while True:
    print("""
    1. Add Product
    2. Remove Product
    3. Update Product
    4. Total Unique Products
    5. Total Price
    6. Exit
    """)
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: ") or 1)
        ob_sc.add_product(name, price, quantity)
    elif choice == '2':
        name = input("Enter product name to remove: ")
        ob_sc.remove_product(name)
    elif choice == '3':
        name = input("Enter product name to update: ")
        price = int(input("Enter new price: "))  
        quantity = int(input("Enter new quantity: ")) 
        ob_sc.update_product(name, price, quantity)
    elif choice == '4':
        print("Total unique products:", ob_sc.total_unique_products())
    elif choice == '5':
        print("Total price of all products: $", ob_sc.total_price())
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
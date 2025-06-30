class Cart:
    def __init__(self):
        self._items = []
        """The _ prefix indicates it's a protected attribute
            meaning it shouldn't be accessed outside the class or sublcass (encapsulation).
            Discourage manipulation of the items list and encourage using
            the class methods.

            You can access docstrings of an object by using the .__doc__ attribute
            or the help() function
        """

    def add_item(self, item_name, price):
        """Add new items to the cart with name and price"""
        self._items.append({"name":item_name, "price":price})
        
    def remove_item(self, item_name):
        """Remove items matching given name from the cart"""
        new_items = []
        for item in self._items:
            if item_name != item["name"]:
                new_items.append(item)
        self._items = new_items

    def total_value(self):
        """Calculate the total price of all the items in the cart"""
        return sum(item["price"] for item in self._items)

#initialize cart object
cart = Cart()

#add items
cart.add_item("apple", 13)
print(cart._items)
cart.add_item("tomato", 11)
print(cart._items)

#remove item
cart.remove_item("tomato")
print(cart._items)

#calculate total item value
print(cart.total_value())

print(cart._items)


from random import randint
from .grid import Grid

class Item:
    """Representerar saker man kan plocka upp."""
    def __init__(self, name, value=10, symbol="?"):
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol


pickups = [Item("carrot"), Item("apple", value=20), Item("strawberry", value=20), Item("cherry", value=20), Item("watermelon", value=20), Item("radish"), Item("cucumber"), Item("meatball")]
traps = [Item("Foothold trap",value=-10, symbol="."), Item("Body gripping trap",value=-10, symbol="."), Item("Deadfall trap",value=-10, symbol="."), Item("Glue trap",value=-10, symbol=".")]

shovels = [Item("shovel",value=0, symbol="♠")]

chest_item = Item("chest", value=100, symbol="□")
key_item = Item("key", value=0, symbol="¬")
number_of_chests = randint(1,3)
chests = [chest_item] * number_of_chests
keys = [key_item] * number_of_chests


def add_items_to_grid(items:list, grid:Grid):
    for item in items:
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break


def randomize(grid):
    add_items_to_grid(pickups, grid)
    add_items_to_grid(traps, grid)
    add_items_to_grid(shovels, grid)
    add_items_to_grid(chests, grid)
    add_items_to_grid(keys, grid)

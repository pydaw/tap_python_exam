
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


def randomize(grid):
    for item in pickups:
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen
    
    for item in traps:
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen


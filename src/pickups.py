
class Item:
    """Representerar saker man kan plocka upp."""
    def __init__(self, name, value=10, symbol="?"):
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol


pickups = [Item("carrot"), Item("apple"), Item("strawberry"), Item("cherry"), Item("watermelon"), Item("radish"), Item("cucumber"), Item("meatball")]


def randomize(grid):
    for item in pickups:
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen


import src.pickups 
from src.pickups import Item
from src.grid import Grid

def test_item_init():
    item1 = Item("test1")
    item2 = Item("test2", 20, "X")

    actual = item1.name
    expected = "test1"
    assert actual == expected

    actual = item1.value
    expected = 10
    assert actual == expected

    actual = item1.symbol
    expected = "?"
    assert actual == expected


    actual = item2.name
    expected = "test2"
    assert actual == expected

    actual = item2.value
    expected = 20
    assert actual == expected

    actual = item2.symbol
    expected = "X"
    assert actual == expected

def test_str():
    item1 = Item("test1")
    actual = str(item1)
    expected = "?"
    assert actual == expected
    
    item2 = Item("test2", 20, "X")
    actual = str(item2)
    expected = "X"
    assert actual == expected
    
def test_items_to_grid():
    grid = Grid()
    item_list = [Item("test")] * 10
    
    src.pickups.add_items_to_grid(item_list, grid)

    # Kontrollera att antal pickups det finns i data
    number_of_pickup_element = 0
    for y in range(grid.width):
        for x in range(grid.height):
            number_of_pickup_element += 1 if isinstance(grid.data[x][y], src.pickups.Item) else 0
    
    actual = number_of_pickup_element
    expected = 10
    assert actual == expected
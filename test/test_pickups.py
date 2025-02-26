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


# TODO: Gör klar random funktionerna
def test_add_random_pickup():
    grid = Grid()
    assert True

def test_randomize():
    pass
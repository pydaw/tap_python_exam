from src.bomb import Bomb
from src.grid import Grid

def test_init_and_properties():
    bomb = Bomb(1,2,3)

    assert bomb.pos_x == 1
    assert bomb.pos_y == 2
    assert bomb.detonation_time == 3

def test_str():
    bomb = Bomb(1,1,10)
    actual = str(bomb)
    expected = bomb.symbol
    assert actual == expected

def test_detonation():
    grid = Grid()
    bomb = Bomb(1,1,10)

    # Fyll med vägg element
    grid.data = [[grid.wall for y in range(grid.width)] for x in range(grid.height)]

    # Kontrollera att det inte finns några positioner som är tomma
    number_of_empty_element = 0
    for element in grid.data:
        number_of_empty_element += element.count(grid.empty)
    assert number_of_empty_element == 0

    # Kontrollera att det finns positioner som är tomma
    bomb.detonation(grid)
    number_of_empty_element = 0
    for element in grid.data:
        number_of_empty_element += element.count(grid.empty)
    
    assert number_of_empty_element == 9

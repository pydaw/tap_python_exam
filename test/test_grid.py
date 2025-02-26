from src.grid import Grid
from src.player import Player
from src.enemy import enemies

def test_init():
    grid = Grid()

    # Kontrollera att lista skapas
    actual = len(grid.data)
    expected = grid.height
    assert actual == expected

    actual = len(grid.data[0])
    expected = grid.width
    assert actual == expected

    # Kontrollerar att listan består av en tom spelplan
    for element in grid.data:
        actual = element.count(grid.empty)
        expected = grid.width
        assert actual == expected

def test_get():
    grid = Grid()

    actual = grid.get(0, 0)
    expected = grid.empty
    assert actual == expected

def test_set():
    grid = Grid()
    grid.set(0, 0, "X")
    actual = grid.data[0][0]
    expected = "X"
    assert actual == expected

def test_set_player():
    player = Player(1,1)
    grid = Grid()

    grid.set_player(player)

    actual = grid.player
    excepted = player
    assert actual == excepted

def test_set_enemies():
    grid = Grid()
    grid.set_enemies(enemies)
    actual = grid.enemies
    excepted = enemies
    assert actual == excepted

def test_clear():
    grid = Grid()
    grid.set(0,0,"X")
    assert grid.data[0][0] == "X"

    grid.clear(0,0)
    assert grid.data[0][0] == grid.empty

def test_walls():
    grid = Grid()

    # Kontrollerar att listan består av en tom spelplan
    for element in grid.data:
        actual = element.count(grid.empty)
        expected = grid.width
        assert actual == expected

    grid.make_walls()

    # Kontrollerar att det finns vägg element
    number_of_wall_elements = 0
    for element in grid.data:
        number_of_wall_elements += element.count(grid.wall)
    assert number_of_wall_elements > 0

def test_get_random_x():
    grid = Grid()
    assert 0 <= grid.get_random_x() <= grid.width

def test_get_random_y():
    grid = Grid()
    assert 0 <= grid.get_random_y() <= grid.height

def test_is_empty():
    grid = Grid()
    actual = grid.is_empty(0,0)
    expected = True
    assert actual == expected

def test_is_wall():
    grid = Grid()
    grid.make_walls()
    actual = grid.is_wall(0,0)
    expected = True
    assert actual == expected




    
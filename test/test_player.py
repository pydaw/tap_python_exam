from src.player import Player
from src.grid import Grid

def test_init():
    x = 100
    y = 200
    player = Player(x, y)
    
    actual = player.pos_x
    expected = 100
    assert actual == expected

    actual = player.pos_y
    expected = 200
    assert actual == expected

def test_move():
    player = Player(100, 200)
    dx = 10
    dy = 20
    player.move(dx, dy)

    actual = player.pos_x
    expected = 110
    assert actual == expected
    
    actual = player.pos_y
    expected = 220
    assert actual == expected

def test_can_move():
    grid = Grid()
    player = Player(1,1)

    grid.set(10,10, grid.wall)

    actual = player.can_move(10,10,grid)
    excepted = False
    assert actual == excepted

    actual = player.can_move(5,5,grid)
    excepted = True
    assert actual == excepted

    
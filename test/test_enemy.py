import src.enemy
from src.enemy import Enemy
from src.player import Player
from src.grid import Grid

def test_init():
    x = 100
    y = 200
    enemy = Enemy(x, y)
    
    actual = enemy.pos_x
    expected = 100
    assert actual == expected

    actual = enemy.pos_y
    expected = 200
    assert actual == expected    

def test_move():
    enemy = Enemy(100, 200)
    dx = 10
    dy = 20
    enemy.move(dx, dy)

    actual = enemy.pos_x
    expected = 110
    assert actual == expected
    
    actual = enemy.pos_y
    expected = 220
    assert actual == expected

def test_can_move():
    grid = Grid()
    enemy = Enemy(1,1)

    grid.set(10,10, grid.wall)

    actual = enemy.can_move(10,10,grid)
    excepted = False
    assert actual == excepted

    actual = enemy.can_move(5,5,grid)
    excepted = True
    assert actual == excepted

def test_move_toward_player():
    grid = Grid()
    player = Player(3,3)
    enemy = Enemy(1,1)

    diff_x = abs(player.pos_x - enemy.pos_x) 
    diff_y = abs(player.pos_y - enemy.pos_y)

    for i in range(10):
        enemy.move_toward_player(grid, player)

    diff_after_moves_x = abs(player.pos_x - enemy.pos_x) 
    diff_after_moves_y = abs(player.pos_y - enemy.pos_y)

    # Kontrollerar om fienden kommer närmare spelare i x o y led efter några drag
    assert  diff_x > diff_after_moves_x and diff_y > diff_after_moves_y
    
def test_caught_player():
    grid = Grid()
    player = Player(3,3)
    enemy = Enemy(1,1)

    actual = enemy.caught_player(player)
    expected = False
    assert actual == expected

    enemy = Enemy(3,3)
    actual = enemy.caught_player(player)
    expected = True
    assert actual == expected

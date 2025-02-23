import random

from src.grid import Grid
from src.player import Player

class Enemy(Player):
    marker = "▲"

    def move_toward_player(self, grid:Grid, player:Player):
        dx = 1 if (player.pos_x - self.pos_x) > 0 else -1
        dy = 1 if (player.pos_y - self.pos_y) > 0 else -1 

        move_granted = random.choice([True, False])
        if move_granted:
            direction = random.choice(["x", "y"])
            if direction == "x" and self.can_move(self.pos_x+dx, self.pos_y, grid):
                self.move(dx,0)
                
            elif direction == "y" and self.can_move(self.pos_x, self.pos_y+dy, grid):
                self.move(0,dy)
    
    def caught_player(self, player:Player):
        if self.pos_x == player.pos_x and self.pos_y == player.pos_y:
            return True
        return False
        

number_of_enemies = random.randint(1,3)
enemies = list()
for i in range(number_of_enemies):
    enemies.append(Enemy(0,0))

def add_enemies_to_grid(items:list, grid:Grid):
    for enemy in enemies:
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                enemy.pos_x = x
                enemy.pos_y = y
                break

def randomize(grid):
    add_enemies_to_grid(enemies, grid)

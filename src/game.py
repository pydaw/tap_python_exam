from .grid import Grid
from .player import Player
from . import pickups

player_middle_pos_x = int(Grid.width/2)
player_middle_pos_y = int(Grid.height/2)

player = Player(player_middle_pos_x, player_middle_pos_y)
score = 0
inventory = []

g = Grid()
g.set_player(player)
g.make_walls()
pickups.randomize(g)


# TODO: flytta denna till en annan fil
def print_status(game_grid):
    """Visa spelvärlden och antal poäng."""
    print("--------------------------------------")
    print(f"You have {score} points.")
    print(game_grid)


command = "a"
# Loopa tills användaren trycker Q eller X.
while command.casefold() not in ["q", "x"]:
    print_status(g)

    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:1]

    # Command = Move player
    if command.casefold() in "wasd" and len(command) == 1:
        command_to_movement = {
            "w": (0, -1),  # Move up
            "a": (-1, 0),  # Move left
            "s": (0, 1),   # Move down
            "d": (1, 0),   # Move right
        }
        move_x, move_y = command_to_movement[command]
    
        maybe_item = None
        if player.can_move(player.pos_x + move_x, player.pos_y + move_y, g):
            maybe_item = g.get(player.pos_x + move_x, player.pos_y + move_y)
            player.move(move_x, move_y)

        if isinstance(maybe_item, pickups.Item):
            # we found something
            score += maybe_item.value
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            inventory.append(maybe_item)
            #g.set(player.pos_x, player.pos_y, g.empty)
            g.clear(player.pos_x, player.pos_y)


# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")

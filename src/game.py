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


def check_inventory(item_name:str):
    for item in inventory:
        if item.name == item_name:
            return item
    return None


command = "a"
loop = 0
# Loopa tills användaren trycker Q eller X.
while command.casefold() not in ["q", "x"]:
    
    # Bördig jord - Lägger till en frukt/grönsak var 25:e drag
    loop += 1
    print(f"loop: {loop}")
    if loop%25 == 0:
        pickups.add_random_pickup(g)

    print_status(g)

    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:1]

    # Command = Move player
    if command in "wasd" and len(command) == 1:
        command_to_movement = {
            "w": (0, -1),  # Move up
            "a": (-1, 0),  # Move left
            "s": (0, 1),   # Move down
            "d": (1, 0),   # Move right
        }
        move_x, move_y = command_to_movement[command]
        
        # Kontrollera om spade finns i intentory listan
        shovel = check_inventory("shovel")
        
        # Kontrollera om spelaren kan flytta sig till punkten
        maybe_item = None
        if player.can_move(player.pos_x + move_x, player.pos_y + move_y, g):
            maybe_item = g.get(player.pos_x + move_x, player.pos_y + move_y)
            player.move(move_x, move_y)
        
        # Möjligt att gå genom en vägg om man har en spade i inventory
        elif shovel:
            print("You have digged a hole through the wall!")
            inventory.remove(shovel)
            player.move(move_x, move_y)
            g.clear(player.pos_x, player.pos_y)


        # Konrollera om spelarens positionen har ett item att plocka upp
        if isinstance(maybe_item, pickups.Item):
            score += maybe_item.value
            
            # Kista (går att öppna med nyckel)
            if maybe_item.name == "chest":
                key = check_inventory("key")
                if key:
                    print(f"You found a chest and could open it, +{maybe_item.value} points.")
                    inventory.append(maybe_item)
                    inventory.remove(key)
                    g.clear(player.pos_x, player.pos_y)
                else:
                    print(f"You found a {maybe_item.name}. But it is locked!")
                    
            # Pickup item, spade eller nyckel
            elif maybe_item.value >= 0:
                print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
                inventory.append(maybe_item)
                g.clear(player.pos_x, player.pos_y)
            
            # Gömd fälla
            else:
                print(f"You found a {maybe_item.name}, {maybe_item.value} points.")
        
        else:
            # The floor is lava - för varje steg man går ska man tappa 1 poäng.
            # Tyckte det var lite roligare att man skulle behålla alla poäng för den item som man plockat upp,
            # där av är den inuti denna else-satsen
            score -= 1
    
    # Command = Show inventory
    elif command=="i":
        if len(inventory) > 0:
            print("Items found:")
            for item in inventory:
                print(f" - {item.name}")
        else:
            print("No items found yet!") 


# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")

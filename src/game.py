from src import bomb
from src import enemy
from src import pickups

from src.bomb import Bomb
from src.grid import Grid
from src.player import Player

player_middle_pos_x = int(Grid.width/2)
player_middle_pos_y = int(Grid.height/2)

player = Player(player_middle_pos_x, player_middle_pos_y)

score = 0
inventory = []

g = Grid()
g.set_player(player)
g.make_walls()
pickups.randomize(g)

enemy.randomize(g)
g.set_enemies(enemy.enemies)


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
grace_time = 0
trap_activated = False

# Loopa tills användaren trycker Q eller X.
while command.casefold() not in ["q", "x"]:
    
    # Bördig jord - Lägger till en frukt/grönsak var 25:e drag
    loop += 1
    if loop%25 == 0:
        pickups.add_random_pickup(g)

    print_status(g)

    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:2]
    
    # Command = Flytta spelare
    if command in "w a s d jw ja js jd" and len(command) > 0 and command != "j":
        command_to_movement = {
            "w":  (0, -1), # Upp
            "a":  (-1, 0), # Vänster
            "s":  (0, 1),  # Ner
            "d":  (1, 0),  # Höger
        }

        command_to_jump_movement = {
            "jw": (0, -2), # Hoppa uppåt
            "ja": (-2, 0), # Hoppa vänster
            "js": (0, 2),  # Hoppa neråt
            "jd": (2, 0),  # Hoppa höger
        }
        
        # Kontroll att flytta kommandot är ett jump kommando 
        # sparar även om det går att gå ett steg om man hoppar in ex.vis en vägg 
        move_x, move_y = command_to_movement[command] if len(command) == 1 else command_to_movement[command[1]]
        jump_move_x, jump_move_y = command_to_jump_movement[command] if len(command) == 2 else (0, 0)
        
        # Kontrollera om spade finns i intentory listan
        shovel = check_inventory("shovel")
        
        maybe_item = None
        # Kontrollera om spelaren kan flytta sig till punkten genom att hoppa
        if (abs(jump_move_x) > 0 or abs(jump_move_y) > 0) and player.can_move(player.pos_x + jump_move_x, player.pos_y + jump_move_y, g):
            maybe_item = g.get(player.pos_x + jump_move_x, player.pos_y + jump_move_y)
            player.move(jump_move_x, jump_move_y)
            
        # Kontrollera om spelaren kan flytta sig till punkten
        elif player.can_move(player.pos_x + move_x, player.pos_y + move_y, g):
            maybe_item = g.get(player.pos_x + move_x, player.pos_y + move_y)
            player.move(move_x, move_y)
        
        # Möjligt att gå genom en vägg om man har en spade i inventory
        # Ej möjligt att hoppa, skall gå lite tungt att gräva
        elif shovel:
            print("You have digged a hole through the wall!")
            inventory.remove(shovel)
            player.move(move_x, move_y)
            g.clear(player.pos_x, player.pos_y)

        # Konrollera om spelarens positionen har ett item att plocka upp
        if isinstance(maybe_item, pickups.Item):
            score += maybe_item.value
            
            # Exit när alla ursprungliga saker är hämtade 
            if maybe_item.name == "exit":
                # Utgå från att alla items är hittade (kommer bli False om något item saknas)
                all_original_items_picked_up = len(inventory) >= len(pickups.pickups)

                # Kontrollera att saker är i inventory listan
                for item_original in pickups.pickups: 
                    
                    # Loopa inte om item inte finns i inventory-lisan
                    if all_original_items_picked_up: 
                        for item_inventory in inventory:
                            all_original_items_picked_up = item_inventory == item_original
                            # Hoppa ur sista loopen om man hittat alla item i listan 
                            if all_original_items_picked_up:
                                break
                
                if all_original_items_picked_up:
                    print("Exit granted!")
                    break
                else:
                    print("You need more inventories to exit.")

            # Kista (går att öppna med nyckel)
            elif maybe_item.name == "chest":
                key = check_inventory("key")
                if key:
                    print(f"You found a chest and could open it, +{maybe_item.value} points.")
                    inventory.append(maybe_item)
                    inventory.remove(key)
                    g.clear(player.pos_x, player.pos_y)
                    grace_time = loop + 5
                else:
                    print(f"You found a {maybe_item.name}. But it is locked!")
                    
            # Pickup item, spade eller nyckel
            elif maybe_item.value >= 0 and maybe_item not in pickups.traps:
                print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
                inventory.append(maybe_item)
                g.clear(player.pos_x, player.pos_y)
                grace_time = loop + 5

            # Desarmerad fälla
            elif maybe_item.value == 0 and maybe_item in pickups.traps:
                print(f"You found a disarmed {maybe_item.name}, {maybe_item.value} points.")
                inventory.append(maybe_item)
                
            # Gömd fälla
            else:
                print(f"You found a {maybe_item.name}, {maybe_item.value} points.")
                trap_pos_x = player.pos_x
                trap_pos_y = player.pos_y
        
        else:
            # The floor is lava - för varje steg man går ska man tappa 1 poäng.
            # Tyckte det var lite roligare att man skulle behålla alla poäng för den item som man plockat upp,
            # där av är den inuti denna else-satsen, grace time tills loop är över 5 steg från det att man plockade upp något
            score -= 1 if loop > grace_time else 0
    
    # Command = Visa inventory
    elif command=="i":
        if len(inventory) > 0:
            print("Items found:")
            for item in inventory:
                print(f" - {item.name}")
        else:
            print("No items found yet!") 
    
    # Command = Placera ut en bomb
    elif command=="b":
        print("Bomb have been placed, run!")
        this_bomb = Bomb(player.pos_x, player.pos_y, loop + 3)
        bomb.bombs.append(this_bomb)
        g.set(this_bomb.pos_x, this_bomb.pos_y, this_bomb)

    # Command = Desamera fälla 
    elif command == "t":
        # Kontrollera att spelaren står på fällan om man skall desarmera fällan
        if trap_pos_x == player.pos_x and trap_pos_y == player.pos_y:
            print("Trap disarmed")

            # Ge tillbaka poäng
            score += 10

            # Gör fällan obrukbar
            if isinstance(maybe_item, pickups.Item):    
                maybe_item.value = 0

            # Radera positionen för fällan
            trap_pos_x = None
            trap_pos_y = None
            
        else:
            print("Could't find any trap to disarm!")


    # Kontrollera om någon bomb brisserar, radera allt runt bomben    
    for this_bomb in bomb.bombs:
        if loop == this_bomb.detonation_time:
            this_bomb.detonation(g)
            print("BOOM!!!")

            # Spelaren fölorar 100poäng om man står i explosionsområdet
            if abs(this_bomb.pos_x - player.pos_x) <= 1 and abs(this_bomb.pos_y - player.pos_y) <= 1:
                print("You were in the blast, -100 points.")
                score -= 100
            
            # Radera fiende om de finns i explosionsområdet
            for _enemy in enemy.enemies:
                if abs(this_bomb.pos_x - _enemy.pos_x) <= 1 and abs(this_bomb.pos_y - _enemy.pos_y) <= 1:
                    enemy.enemies.remove(_enemy)
        
    # Flytta fienden
    for _enemy in enemy.enemies:
        _enemy.move_toward_player(g, player)
        
        # Om man fångar spelaren så blir man av med 20p
        if _enemy.caught_player(player):
            score -= 20
            print("Caught by an enemy, -20 points.")


# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")

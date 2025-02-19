import random
from .play_fields import play_fields
class Grid:
    """Representerar spelplanen. Du kan ändra standardstorleken och tecknen för olika rutor. """
    width = 36
    height = 12
    empty = "."  # Tecken för en tom ruta
    wall = "■"   # Tecken för en ogenomtränglig vägg

    def __init__(self):
        """Skapa ett objekt av klassen Grid"""
        # Spelplanen lagras i en lista av listor. Vi använder "list comprehension" för att sätta tecknet för "empty" på varje plats på spelplanen.
        self.data = [[self.empty for y in range(self.width)] for z in range(
            self.height)]


    def get(self, x, y):
        """Hämta det som finns på en viss position"""
        return self.data[y][x]

    def set(self, x, y, value):
        """Ändra vad som finns på en viss position"""
        self.data[y][x] = value

    def set_player(self, player):
        self.player = player

    def clear(self, x, y):
        """Ta bort item från position"""
        self.set(x, y, self.empty)

    def __str__(self):
        """Gör så att vi kan skriva ut spelplanen med print(grid)"""
        xs = ""
        for y in range(len(self.data)):
            row = self.data[y]
            for x in range(len(row)):
                if x == self.player.pos_x and y == self.player.pos_y:
                    xs += self.player.marker
                else:
                    xs += str(row[x])
            xs += "\n"
        return xs

    def __make_internal_wall(self, x:int, y:int, x_length=1, y_length=1):
        """Privat metod, skapar väggar i spelplanen
        :param: x - Start posiston av väggen i x-led
        :param: y - Start posiston av väggen i y-led
        :param: x_length - Längd på vägg i x-led
        :param: y_length - Längd på vägg i y-led
        """

        # x-led
        for i in range(x, x + x_length+1):
            self.set(i, y, self.wall)

        # y-led
        for j in range(y, y + y_length+1):
            self.set(x, j, self.wall)


    def make_walls(self):
        """Skapa väggar runt hela spelplanen samt på spelplanen"""
        
        # Skapar väggar runt om spelplanen
        for i in range(self.height):
            self.set(0, i, self.wall)
            self.set(self.width - 1, i, self.wall)

        for j in range(1, self.width - 1):
            self.set(j, 0, self.wall)
            self.set(j, self.height - 1, self.wall)

        # Hämta de interna väggarna genom att slumpa ut en spelplan
        internal_walls = random.choice(play_fields)

        # Skapa de interna väggarna
        for wall in internal_walls:
            self.__make_internal_wall(
                x = wall["start"]["x"], 
                y = wall["start"]["y"], 
                x_length = wall["end"]["x"] - wall["start"]["x"],
                y_length = wall["end"]["y"] - wall["start"]["y"]
            )


    # Används i filen pickups.py
    def get_random_x(self):
        """Slumpa en x-position på spelplanen"""
        return random.randint(0, self.width-1)

    def get_random_y(self):
        """Slumpa en y-position på spelplanen"""
        return random.randint(0, self.height-1)


    def is_empty(self, x, y):
        """Returnerar True om det inte finns något på aktuell ruta"""
        return self.get(x, y) == self.empty


    def is_wall(self, x, y):
        """Returnerar True om det finns vägg på aktuell ruta"""
        return self.get(x, y) == self.wall


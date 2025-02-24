from src.grid import Grid

class Bomb:
    """Representerar bomb som spelaren kan placera ut på spelplanen"""
    def __init__(self, x, y, detonation_time):
        self.symbol = "B"
        self.__detonation_time = detonation_time
        self.__pos_x = x
        self.__pos_y = y

    def __str__(self):
        return self.symbol
    
    @property
    def pos_x(self):
        return self.__pos_x
    
    @property
    def pos_y(self):
        return self.__pos_y
    
    @property 
    def detonation_time(self):
        return self.__detonation_time
        
    def detonation(self, grid:Grid):
        # Rensa allt omkring bomben
        for dx in range(-1, 1+1):
            for dy in range(-1, 1+1):
                grid.clear(self.pos_x+dx, self.pos_y+dy)


bombs = list()
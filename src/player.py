from src.grid import Grid
class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """
        Flyttar spelaren.  
        dx = horisontell förflyttning, från vänster till höger  
        dy = vertikal förflyttning, uppifrån och ned
        """
        self.pos_x += dx
        self.pos_y += dy

    def can_move(self, x, y, grid:Grid):
        """
        Kontrollera att det är möjligt att flytta spelaren 
        till angiven position i spelfält.

        Returnerar True om möjligt att flytta annars returneras
        False om det finns en vägg på angiven position.
        """
        dx = x - self.pos_x
        dy = y - self.pos_y
        
        # Kontrollera om väggen finns längs sträckan i x-led
        for i in range(abs(dx)):
            direction = 1 if dx >= 0 else -1
            if grid.is_wall(self.pos_x+direction*(i+1), y):
                return False
        
        # Kontrollera om väggen finns längs sträckan i y-led
        for i in range(abs(dy)):
            direction = 1 if dy >= 0 else -1
            if grid.is_wall(x, self.pos_y+direction*(i+1)):
                return False
        
        # Om man inte hittar väggen returnera true
        return True


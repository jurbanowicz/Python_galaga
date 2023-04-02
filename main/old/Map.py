from Vector2d import Vector2d
class Map:
    def __init__(self, width, height):
        self.dimensions = Vector2d(width, height) #obiekt typu Vector2d przechowujący rozmiary mapy
        self.player = None
        self.objects = dict #Hashmapa nagród i wrogów


    def can_move_to(self, new_position: Vector2d) -> bool:
        if new_position.precedes(self.dimensions) and new_position.follows(self.dimensions):
            return True
        return False
    

    def clean(self):
        pass

    


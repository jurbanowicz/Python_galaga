from Vector2d import Vector2d

class MapElement:
    def __init__(self):
        self.position = None
        self.life = None
        self.image = None
        self.map = None
        self.size = None

    def move(self, vector: Vector2d) -> None:
        
        new_position = self.position.add(vector)

        if self.field.can_move_to(new_position):
            self.position = new_position



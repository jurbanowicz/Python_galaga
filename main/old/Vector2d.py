class Vector2d:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __eq__(self, other: object) -> bool:
        return self.x == other.x and self.y == other.y
    
    def __hash__(self) -> int:
        pass

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def add(self, other: object) -> object:
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector2d(new_x, new_y)

    def substract(self, other: object) -> None:
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector2d(new_x, new_y)
    

    def follows(self, other: object) -> bool:
        if self.x >= other.x and self.y >= other.y:
            return True
        return False

    def precedes(self, other: object) -> bool:
        if self.x <= other.x and self.y <= other.y:
            return True
        return False



class Point:
    """Clase que representa un punto en un plano cartesiano"""
    
    def __init__(self, x, y):
        self.x = x  # Coordenada x
        self.y = y  # Coordenada y

    def another_point(self, new_x, new_y):
        """Método para crear un nuevo punto a partir de coordenadas dadas"""
        return Point(new_x, new_y)
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self):
        return self.__str__()

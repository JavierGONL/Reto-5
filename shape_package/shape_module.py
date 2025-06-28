# Módulo Shape - Clase base para todas las figuras geométricas

class Shape:
    """Clase base para todas las figuras geométricas"""
    
    def __init__(self, edges: list = None):
        self.edges = edges if edges is not None else []
        self.inner_angles = []

    def compute_area(self):
        """Método para calcular el área - debe ser implementado por las subclases"""
        pass

    def compute_perimeter(self):
        """Método para calcular el perímetro - debe ser implementado por las subclases"""
        pass

    def compute_inner_angles(self):
        """Método para calcular los ángulos internos - debe ser implementado por las subclases"""
        pass

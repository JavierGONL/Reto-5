# Módulo Triangle - Implementa las clases de triángulos que heredan de Shape

from math import acos, degrees
from .shape_module import Shape

class Triangle(Shape): 
    """Clase base para triángulos"""
    
    def __init__(self, edges: list = None):
        super().__init__(edges)
        self.edges = edges if edges is not None else []
        self.perimeter = 0
        self._area = 0
        self.angulos = []
    
    def compute_perimeter(self):
        """Calcula el perímetro del triángulo"""
        if self.perimeter == 0:
            for i in range(len(self.edges)):
                self.edges[i].compute_length()
                self.perimeter += self.edges[i].length
        return self.perimeter

    def compute_area(self):
        """Calcula el área del triángulo usando la fórmula de Herón"""
        if self.perimeter == 0:
            self.compute_perimeter()
        semiperimetro = self.perimeter/2
        self.area = round((semiperimetro*(semiperimetro-self.edges[0].length)
                    *(semiperimetro-self.edges[1].length)
                    *(semiperimetro-self.edges[2].length))**(1/2), 3)
        return self.area

    def compute_inner_angles(self):
        """Calcula los ángulos internos de un triángulo usando la ley de cosenos"""
        angulos = []
        for i in range(len(self.edges)):
            self.edges[i].compute_length() 
        
        # Para cada vértice, calculamos el ángulo opuesto usando la fórmula del coseno
        for i in range(len(self.edges)):
            a = self.edges[i].length  # Lado opuesto al ángulo que queremos calcular
            b = self.edges[i-1].length  # Lado adyacente 1
            c = self.edges[i-2].length  # Lado adyacente 2
            
            # Calculamos el coseno del ángulo usando la ley de cosenos
            cos_i = ((a**2 - b**2 - c**2) / (-2 * b * c))
            
            # Aseguramos que el valor esté en el rango válido para acos
            cos_i = max(-1, min(1, cos_i))
            
            # Convertimos el coseno a grados y redondeamos
            angulo = round(degrees(acos(cos_i)))
            angulos.append(angulo)
        
        self.angulos = angulos
        return angulos


class Isosceles(Triangle):
    """Triángulo isósceles - con 2 lados y ángulos iguales"""
    
    definition: str = "Triangulo con 2 lados y angulos iguales"
    
    def __init__(self, edges=None):
        super().__init__(edges)


class Equilateral(Triangle):
    """Triángulo equilátero - con 3 lados y ángulos iguales"""
    
    definition: str = "Triangulo con 3 lados y angulos iguales"
    
    def __init__(self, edges=None):
        super().__init__(edges)


class Scalene(Triangle):
    """Triángulo escaleno - con lados y ángulos diferentes"""
    
    definition: str = "Triangulo con lados y angulos diferentes"
    
    def __init__(self, edges=None):
        super().__init__(edges)


class TriRectangle(Triangle):
    """Triángulo rectángulo - con un ángulo recto"""
    
    definition: str = "Triangulo con un angulo recto"
    
    def __init__(self, edges=None):
        super().__init__(edges)

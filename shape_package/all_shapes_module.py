# Módulo único que contiene todas las clases Shape
# Este es el enfoque 1: Un módulo único dentro del paquete Shape

from math import acos, degrees

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


class Line:
    """Clase que representa una línea en un plano cartesiano"""
    
    def __init__(self, inicio: "Point" = Point(0, 0), final: "Point" = Point(0, 0)):
        self.inicio = inicio  
        self.final = final  
        self.length = "you have to compute this first"  
        self.slope = "you have to compute this first"  
        self.range = "you have to compute this first" 

    def compute_length(self):
        """Método para calcular la longitud de la línea"""
        self.length: float = ((self.final.x - self.inicio.x)**2 
                        + (self.final.y - self.inicio.y)**2)**(1/2)
        return self.length

    def compute_slope(self):
        """Método para calcular la pendiente de la línea"""
        if self.final.x - self.inicio.x == 0:
            self.slope = float('inf')  # Línea vertical
        else:
            self.slope = ((self.final.y - self.inicio.y)
                        /(self.final.x - self.inicio.x))
        return self.slope

    def range_of_the_line(self):
        """Método para calcular el rango de puntos de la línea"""
        self.range = []
        if type(self.slope) != str: # Verifica que la pendiente haya sido calculada
            for i in range(self.inicio.x, self.final.x):
                self.range.append(Point(i, (self.slope) * i)) 
            return self.range
        else:
            return print("you have to compute slope first")

    def horizontal_cross(self):
        """Método para verificar si la línea cruza el eje x"""
        for i in range(len(self.range) - 1):
            if self.range[i].x < 0 and self.range[i + 1].x > 0:
                return print(f"Cross the x-axis between {self.range[i]} and {self.range[i+1]}")
        return print(f"don't Cross the x-axis")

    def vertical_cross(self):
        """Método para verificar si la línea cruza el eje y"""
        for i in range(len(self.range) - 1):
            if self.range[i].y < 0 and self.range[i + 1].y > 0:
                return print(f"Cross the y-axis between {self.range[i]} and {self.range[i+1]}")
        return print(f"don't Cross the y-axis")


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


class Rectangle(Shape):
    """Clase que representa un rectángulo"""
    
    def __init__(self, edges=None):
        super().__init__(edges)
        self.edges = edges if edges is not None else []
        self.width = 0
        self.height = 0
        self.point_bottom_left = None
        
        # Procesar los bordes si se proporcionan
        if self.edges:
            self._process_edges()

        # Puntos de las esquinas
        self.point_bottom_right = None
        self.point_upper_left = None
        self.point_upper_right = None

    def _process_edges(self):
        """Procesa los bordes para determinar dimensiones y punto base"""
        point_bottom_left_index = 0
        for i in range(len(self.edges)):
            self.edges[i].compute_length()
            if i < len(self.edges) - 1:
                if (self.edges[i+1].inicio.x > self.edges[i].inicio.x 
                     and self.edges[i+1].inicio.y > self.edges[i].inicio.y):
                    point_bottom_left_index = i
            
            # Determinar si es horizontal o vertical
            if self.edges[i].inicio.y == self.edges[i].final.y:
                self.width = self.edges[i].length
            if self.edges[i].inicio.x == self.edges[i].final.x:
                self.height = self.edges[i].length
        
        self.point_bottom_left = self.edges[point_bottom_left_index].inicio

    def compute_area(self):
        """Método para calcular el área del rectángulo"""
        return self.width * self.height

    def compute_perimeter(self):
        """Método para calcular el perímetro del rectángulo"""
        return 2 * self.width + 2 * self.height

    def compute_inner_angles(self):
        """Método para calcular los ángulos internos del rectángulo"""
        self.inner_angles = [90, 90, 90, 90]


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

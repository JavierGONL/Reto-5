# Módulo Rectangle - Implementa la clase Rectangle que hereda de Shape

from .shape_module import Shape
from .point_module import Point
from .line_module import Line

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

    def init_bottom_left(self):
        """Método para inicializar las esquinas del rectángulo"""
        if self.point_bottom_left is None:
            return None
            
        self.point_bottom_right = self.point_bottom_left.another_point(
            self.point_bottom_left.x + self.width, self.point_bottom_left.y
        )
        self.point_upper_left = self.point_bottom_left.another_point(
            self.point_bottom_left.x, self.point_bottom_left.y + self.height
        )
        self.point_upper_right = self.point_bottom_left.another_point(
            self.point_bottom_left.x + self.width, self.point_bottom_left.y + self.height
        )
        return [self.point_bottom_left, 
                self.point_bottom_right, 
                self.point_upper_left, 
                self.point_upper_right]

    def compute_center(self):
        """Método para calcular el centro del rectángulo"""
        if self.point_bottom_left is None:
            return None
        return Point(
            self.point_bottom_left.x + self.width / 2,
            self.point_bottom_left.y + self.height / 2,
        )

    def compute_area(self):
        """Método para calcular el área del rectángulo"""
        return self.width * self.height

    def compute_perimeter(self):
        """Método para calcular el perímetro del rectángulo"""
        return 2 * self.width + 2 * self.height

    def compute_inner_angles(self):
        """Método para calcular los ángulos internos del rectángulo"""
        self.inner_angles = [90, 90, 90, 90]

    def compute_interference_between_2_rectangles(self, square_2: "Rectangle"):
        """Método para verificar si dos rectángulos interfieren"""
        centro_1 = self.compute_center()
        centro_2 = square_2.compute_center()
        if centro_1 is None or centro_2 is None:
            return False
            
        distancia = ((centro_2.x - centro_1.x)**2 
                    +(centro_2.y - centro_1.y)**2)**0.5
        cateto_opuesto = centro_2.y - centro_1.y
        
        if distancia == 0:
            return True
            
        coseno = cateto_opuesto / distancia
        hipotenusa_square_1 = abs(coseno * (self.width / 2))
        hipotenusa_square_2 = abs((coseno * (square_2.width / 2)))
        
        if distancia <= hipotenusa_square_1 + hipotenusa_square_2:
            print(f"interfieren")
            return True
        else:
            print(f"no interfieren")
            return False

    def compute_interferece_between_rectangle_and_point(self, point: "Point"):
        """Método para verificar si un rectángulo interfiere con un punto"""
        centro_1 = self.compute_center()
        if centro_1 is None:
            return False
            
        centro_2 = point
        distancia = ((centro_2.x - centro_1.x)**2
                    +(centro_2.y - centro_1.y)**2)**0.5
        
        if distancia == 0:
            return True
            
        cateto_opuesto = centro_2.y - centro_1.y
        coseno = cateto_opuesto / distancia
        hipotenusa_square_1 = abs(coseno * (self.width / 2))
        
        if distancia <= hipotenusa_square_1:
            print(f"interfieren")
            return True
        else:
            print(f"no interfieren")
            return False

    def compute_interference_between_rectangle_and_line(self, line: "Line"):
        """Método para verificar si un rectángulo interfiere con una línea"""
        centro_1 = self.compute_center()
        if centro_1 is None:
            return False
            
        line_range = line.range_of_the_line()
        if not line_range:
            return False
            
        interfieren = False
        for point in line_range:
            distancia = (((point.x - centro_1.x))**2 
                        +(point.y - centro_1.y)**2)**0.5
            
            if distancia == 0:
                return True
                
            cateto_opuesto = point.y - centro_1.y
            coseno = cateto_opuesto / distancia
            
            if coseno == 0:
                hipotenusa_square_1 = self.width / 2
            else:
                hipotenusa_square_1 = abs(cateto_opuesto / coseno)
                
            if distancia <= hipotenusa_square_1:
                interfieren = True
                break
        return interfieren

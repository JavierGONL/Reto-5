from .point import Point

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

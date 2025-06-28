# Paquete Shape - Reto 5
# Este paquete contiene todas las clases relacionadas con figuras geométricas

# ENFOQUE 1: Un módulo único dentro del paquete Shape
# Importa todas las clases desde un solo módulo
from .all_shapes_module import *

# ENFOQUE 2: Módulos individuales que importan Shape e inheritan de él
# Comentar las líneas de arriba y descomentar las de abajo para usar este enfoque
# from .shape_module import Shape
# from .point_module import Point
# from .line_module import Line
# from .rectangle_module import Rectangle
# from .triangle_module import Triangle, Isosceles, Equilateral, Scalene, TriRectangle

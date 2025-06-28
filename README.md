# Paquete Shape - Reto 5

## Descripción
Este paquete contiene todas las clases relacionadas con figuras geométricas, implementado según los requerimientos del Reto 5.

## Estructura del Paquete

```
shape_package/
├── __init__.py                 # Archivo de inicialización del paquete
├── all_shapes_module.py        # ENFOQUE 1: Módulo único con todas las clases
├── shape_module.py             # ENFOQUE 2: Clase base Shape
├── point_module.py             # ENFOQUE 2: Clase Point
├── line_module.py              # ENFOQUE 2: Clase Line
├── rectangle_module.py         # ENFOQUE 2: Clase Rectangle
└── triangle_module.py          # ENFOQUE 2: Clases de triángulos
```

## Dos Enfoques Implementados

### Enfoque 1: Módulo Único
Un solo módulo (`all_shapes_module.py`) que contiene todas las clases:
- Point
- Line
- Shape (clase base)
- Rectangle (hereda de Shape)
- Triangle (hereda de Shape)
- Isosceles, Equilateral, Scalene, TriRectangle (heredan de Triangle)

### Enfoque 2: Módulos Individuales
Cada clase en su propio módulo, todas heredando de la clase base Shape:
- `shape_module.py`: Clase base Shape
- `point_module.py`: Clase Point
- `line_module.py`: Clase Line
- `rectangle_module.py`: Clase Rectangle
- `triangle_module.py`: Clases de triángulos

## Cómo Usar

### Usando el Enfoque 1 (Predeterminado)
```python
from shape_package import Point, Line, Rectangle, Triangle, Scalene

# Crear objetos y usar las clases
p1 = Point(0, 0)
p2 = Point(4, 3)
line = Line(p1, p2)
```

### Cambiar al Enfoque 2
1. Edita `__init__.py`
2. Comenta las líneas del Enfoque 1
3. Descomenta las líneas del Enfoque 2

```python
# En __init__.py cambiar de:
from .all_shapes_module import *

# A:
from .shape_module import Shape
from .point_module import Point
# etc...
```

## Clases Incluidas

### Point
- Representa un punto en el plano cartesiano
- Métodos: `another_point()`

### Line
- Representa una línea entre dos puntos
- Métodos: `compute_length()`, `compute_slope()`, `range_of_the_line()`, etc.

### Shape (Clase Base)
- Clase base para todas las figuras geométricas
- Métodos abstractos: `compute_area()`, `compute_perimeter()`, `compute_inner_angles()`

### Rectangle
- Hereda de Shape
- Métodos: `compute_area()`, `compute_perimeter()`, `compute_center()`, etc.

### Triangle
- Clase base para triángulos, hereda de Shape
- Métodos: `compute_area()` (Fórmula de Herón), `compute_inner_angles()` (Ley de cosenos)

### Tipos de Triángulos
- **Isosceles**: 2 lados y ángulos iguales
- **Equilateral**: 3 lados y ángulos iguales
- **Scalene**: Lados y ángulos diferentes
- **TriRectangle**: Con un ángulo recto

## Ejemplo de Uso
Ver `ejemplo_uso_paquete.py` para ejemplos completos de uso.

## Autor
Estudiante POO - Universidad Nacional de Colombia
Versión: 1.0.0

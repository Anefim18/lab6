# Абстрактний клас графічних примітивів
class GraphicPrimitive:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Абстрактний метод відображення
    @abstractmethod
    def draw(self):
        pass

    # Метод переміщення
    def move(self, x, y):
        self.x += x
        self.y += y


# Клас кола
class Circle(GraphicPrimitive):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def draw(self):
        print("Малюємо коло з центром в точці", (self.x, self.y), "і радіусом", self.radius)


# Клас прямокутника
class Rectangle(GraphicPrimitive):

    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def draw(self):
        print("Малюємо прямокутник з верхнім лівим кутом в точці", (self.x, self.y), "шириною", self.width, "і висотою", self.height)


# Клас трикутника
class Triangle(GraphicPrimitive):

    def __init__(self, x1, y1, x2, y2, x3, y3):
        super().__init__((x1 + x2 + x3) / 3, (y1 + y2 + y3) / 3)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def draw(self):
        print("Малюємо трикутник з вершинами", (self.x1, self.y1), (self.x2, self.y2), (self.x3, self.y3))


# Клас редактора графічних примітивів
class GraphicsEditor:

    def __init__(self):
        self.primitives = []

    def add_primitive(self, primitive):
        self.primitives.append(primitive)

    def draw_all(self):
        for primitive in self.primitives:
            primitive.draw()


# Додавання можливості масштабування фігур

def scale_primitive(primitive, factor):
    if isinstance(primitive, Circle):
        primitive.radius *= factor
    elif isinstance(primitive, Rectangle):
        primitive.width *= factor
        primitive.height *= factor


# Додавання можливості групування фігур

class Group(GraphicPrimitive):

    def __init__(self, primitives):
        super().__init__(0, 0)
        self.primitives = primitives

    def draw(self):
        for primitive in self.primitives:
            primitive.draw()

    def move(self, x, y):
        for primitive in self.primitives:
            primitive.move(x, y)

    def scale(self, factor):
        for primitive in self.primitives:
            scale_primitive(primitive, factor)


# Приклад використання

editor = GraphicsEditor()

editor.add_primitive(Circle(0, 0, 100))
editor.add_primitive(Rectangle(100, 100, 200, 300))
editor.add_primitive(Triangle(0, 0, 100, 100, 50, 50))

editor.draw_all()

# Масштабування фігур

scale_primitive(editor.primitives[0], 2)
scale_primitive(editor.primitives[2], 0.5)

editor.draw_all()

# Групування фігур

group = Group([editor.primitives[0], editor.primitives[1]])

group.move(100, 100)

editor.add_primitive(group)

editor.draw_all()

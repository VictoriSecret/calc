# cook your dish here
import math

class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        if self.is_valid():
            print("Треугольник существует")
        else:
            while True:
                print("Треугольник не существует, введите другие значения")
                self.side_a = float(input("Первая сторона - "))
                self.side_b = float(input("Вторая сторона - "))
                self.side_c = float(input("Третья сторона - "))
                if self.is_valid():
                    break




    def is_valid(self):
        return (self.side_a + self.side_b > self.side_c and
                self.side_a + self.side_c > self.side_b and
                self.side_b + self.side_c > self.side_a)

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def area(self):
        if not self.is_valid():
            return 0
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))


triangle = Triangle(0, 4, 5)
if triangle.is_valid():
    print(f"Периметр: {triangle.perimeter()}")
    print(f"Площадь: {triangle.area()}")
else:
    print("Треугольник недопустим.")
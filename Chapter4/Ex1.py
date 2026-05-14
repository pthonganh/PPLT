class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def calculate_area(self):
        return self.length * self.width


rectangle1 = Rectangle(5, 3)
rectangle2 = Rectangle(10, 4)

print("Hình chữ nhật 1")
print("Chu vi:", rectangle1.calculate_perimeter())
print("Diện tích:", rectangle1.calculate_area())

print("Hình chữ nhật 2")
print("Chu vi:", rectangle2.calculate_perimeter())
print("Diện tích:", rectangle2.calculate_area())
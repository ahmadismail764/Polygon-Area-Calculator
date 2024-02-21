class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def set_height(self, h):
        self.height = h

    def set_width(self, w):
        self.width = w

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        else:
            picture_repr = ""
            for _ in range(self.height):
                picture_repr += "*" * self.width + "\n"
            return picture_repr

    def get_amount_inside(self, other_shape):
        return self.get_area() // other_shape.get_area()

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, new_side):
        self.height = new_side
        self.width = new_side

    def set_height(self, h):
        self.height = h
        self.width = h

    def set_width(self, w):
        self.width = w
        self.height = w

    def __str__(self):
        return f"Square(side={self.height})"

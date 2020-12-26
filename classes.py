class Polygon():
    def __init__(self, n, l):
        self.n = n
        self.l = l

    def __str__(self):
        return ("Polygon with " + str(self.n) + " sides of length "
                + str(self.l) + " each.")

    def perimeter(self):
        return self.n * self.l

    def __mul__(self, p2):
        """
        For demonstration purposes, we will consider
        the product of two polygons as the product of their permieters
        """
        return self.perimeter() * p2.perimeter()


p1 = Polygon(4, 12)
p2 = Polygon(3, 5)
print(p1, '\n', p2)
print(p1.perimeter(), '\n', p2.perimeter())
print(p1 * p2)
print(48 * 15)
# Notice how __mul__ got called when we used the multiplication '*' sign

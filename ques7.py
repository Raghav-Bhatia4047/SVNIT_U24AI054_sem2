import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def rotation(self):
        return math.degrees(math.atan2(self.y, self.x))

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y

    def cross_product(self, other):
        return self.x * other.y - self.y * other.x

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def rotation(self):
        angle_xy = math.degrees(math.atan2(self.y, self.x))
        angle_xz = math.degrees(math.atan2(self.z, self.x))
        return angle_xy, angle_xz

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross_product(self, other):
        return (self.y * other.z - self.z * other.y,
                self.z * other.x - self.x * other.z,
                self.x * other.y - self.y * other.x)

v2_1 = Vector2D(3, 4)
v2_2 = Vector2D(1, 2)

v3_1 = Vector3D(3, 4, 5)
v3_2 = Vector3D(1, 2, 3)

print(f"2D Vector1 Magnitude: {v2_1.magnitude()}")
print(f"2D Vector1 Rotation: {v2_1.rotation()}")
print(f"Distance between 2D Vectors: {v2_1.distance(v2_2)}")
print(f"Dot Product (2D): {v2_1.dot_product(v2_2)}")
print(f"Cross Product (2D): {v2_1.cross_product(v2_2)}")

print(f"3D Vector1 Magnitude: {v3_1.magnitude()}")
print(f"3D Vector1 Rotation: {v3_1.rotation()}")
print(f"Distance between 3D Vectors: {v3_1.distance(v3_2)}")
print(f"Dot Product (3D): {v3_1.dot_product(v3_2)}")
print(f"Cross Product (3D): {v3_1.cross_product(v3_2)}")

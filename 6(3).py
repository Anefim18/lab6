# Клас для представлення та роботи з кватерніонами
class Quaternion:

    def __init__(self, w, x, y, z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    # Перевантаження операторів додавання, віднімання, множення
    def __add__(self, other):
        return Quaternion(self.w + other.w, self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Quaternion(self.w - other.w, self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        a = self.w * other.w - self.x * other.x - self.y * other.y - self.z * other.z
        b = self.w * other.x + self.x * other.w + self.y * other.z - self.z * other.y
        c = self.w * other.y - self.x * other.z + self.y * other.w + self.z * other.x
        d = self.w * other.z + self.x * other.y - self.y * other.x + self.z * other.w
        return Quaternion(a, b, c, d)

    # Методи для обчислення норми, спряженого кватерніона та інверсного кватерніона
    def norm(self):
        return math.sqrt(self.w ** 2 + self.x ** 2 + self.y ** 2 + self.z ** 2)

    def conjugate(self):
        return Quaternion(self.w, -self.x, -self.y, -self.z)

    def inverse(self):
        return self.conjugate() / self.norm() ** 2

    # Перевантаження операцій порівняння == та !=
    def __eq__(self, other):
        return self.w == other.w and self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return not self == other

    # Додавання можливості конвертації кватерніона в матрицю обертання та навпаки
    def to_rotation_matrix(self):
        return np.array(
            [[self.w * self.w + self.x * self.x - self.y * self.y - self.z * self.z, 2 * self.x * self.y - 2 * self.w * self.z, 2 * self.x * self.z + 2 * self.w * self.y],
             [2 * self.x * self.y + 2 * self.w * self.z, self.w * self.w - self.x * self.x + self.y * self.y - self.z * self.z, 2 * self.y * self.z - 2 * self.w * self.x],
             [2 * self.x * self.z - 2 * self.w * self.y, 2 * self.y * self.z + 2 * self.w * self.x, self.w * self.w - self.x * self.x - self.y * self.y + self.z * self.z]])

    @staticmethod
    def from_rotation_matrix(matrix):
        return Quaternion(
            matrix[0][0] + matrix[1][1] - matrix[2][2],
            2 * (matrix[0][1] - matrix[2][0]),
            2 * (matrix[0][2] + matrix[1][0]),
            2 * (matrix[2][1] - matrix[0][2]))


# Приклад використання
q1 = Quaternion(1, 2, 3, 4)
q2 = Quaternion(5, 6, 7, 8)

print(q1 + q2)
print(q1 - q2)
print(q1 * q2)
print(q1.norm

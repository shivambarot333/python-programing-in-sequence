class Matrix:
    def _init_(self, data):
        self.data = data

    def _add_(self, other):
        return Matrix([[self.data[i][j] + other.data[i][j] for j in range(3)] for i in range(3)])

    def _mul_(self, other):
        result = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                result[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(3))
        return Matrix(result)

    def transpose(self):
        return Matrix([[self.data[j][i] for j in range(3)] for i in range(3)])

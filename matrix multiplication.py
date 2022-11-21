class Matrix:
    def __init__(self, a: list, b: list):
        self.a, self.b = a, b
        self.A_ORDER = len(self.a), len(self.a[0]) if len(self.a) else 0
        self.B_ORDER = len(self.b), len(self.b[0]) if len(self.b) else 0

    def add(self):
        if self.A_ORDER != self.B_ORDER:
            return
        return_list = [[]]
        for i in range(self.A_ORDER[1]):
            for j in range(self.B_ORDER[0]):
                return_list[-1].append(self.a[i][j] + self.b[i][j])
            return_list.append([])
        return [i for i in return_list if i]

    def subtract(self):
        if self.A_ORDER != self.B_ORDER:
            return
        return_list = []
        for i in range(self.A_ORDER[1]):
            return_list.append([])
            for j in range(self.B_ORDER[0]):
                return_list[-1].append(self.a[i][j] - self.b[i][j])
        return return_list

    def transpose(self):
        if self.A_ORDER[1] != self.B_ORDER[0]:
            return
        B_transpose = []
        for i in range(self.B_ORDER[0]):
            B_transpose.append([])
            for j in self.b:
                B_transpose[i].append(j[i])
        return B_transpose

    def multiply(self):
        if self.A_ORDER[1] != self.B_ORDER[0]:
            return
        return_list = []
        B_transpose = self.transpose()
        for i in range(self.A_ORDER[0]):
            return_list.append([])
            for j in range(self.B_ORDER[1]):
                return_list[-1].append(
                    sum(
                        [
                            self.a[i][k] * B_transpose[j][k]
                            for k in range(self.A_ORDER[1])
                        ]
                    )
                )
        return return_list


matrix = Matrix([[1, 0], [0, 1]], [[2, 3], [4, 5]])
print(*matrix.multiply(), sep="\n")
print()
print(*matrix.add(), sep="\n")

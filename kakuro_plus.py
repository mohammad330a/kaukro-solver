from kakuro_simple import Kakuro

INF = float('inf')

class KakuroPlus(Kakuro):
    def __init__(self, n, m, hint_fields, block_fields):
        Kakuro.__init__(self, n, m, hint_fields, block_fields)
        self.constrained_values = dict()
        self.get_constrained_values()

    def get_constrained_values(self):
        for row in range(self.n):
            for col in range(self.m):
                if self.map[row][col] == '*':
                    col_hint = None
                    for i in range(row):
                        if isinstance(self.map[i][col], dict):
                            col_hint = self.map[i][col]
                    row_hint = None
                    for i in range(col):
                        if isinstance(self.map[row][i], dict):
                            row_hint = self.map[row][i]
                    self.constrained_values[(row, col)] = min(col_hint['down'], row_hint['right'])


    def solve(self):
        # self.show()
        cand_cell = self.get_most_constrained_empty_cell()
        if not cand_cell[0]:
            return self.has_solved()

        row, col, res = cand_cell[0][0], cand_cell[0][1], cand_cell[1]
        for num in range(min(res, 9), 0, -1):
            if self.check_column_constraint(row, col, num) and self.check_row_constraint(row, col, num):
                self.map[row][col] = num
                if self.solve():
                    return True
                self.map[row][col] = '*'
        return False

    def get_most_constrained_empty_cell(self):
        result = INF
        cand_cell = None
        for row, col in self.constrained_values:
            if self.map[row][col] == '*':
                if self.constrained_values[(row, col)] <= result:
                    result = self.constrained_values[(row, col)]
                    cand_cell = row, col

        for row in range(self.n):
            for col in range(self.m):
                if self.map[row][col] == '*':
                    col_hint = None
                    for i in range(row):
                        if isinstance(self.map[i][col], dict):
                            col_hint = self.map[i][col]
                    row_hint = None
                    for i in range(col):
                        if isinstance(self.map[row][i], dict):
                            row_hint = self.map[row][i]
                    if min(col_hint['down'], row_hint['right']) <= result:
                        result = min(col_hint['down'], row_hint['right'])
                        cand_cell = row, col
        return cand_cell, result

    def get_column_helper(self, row, col):
        cur_hint = None
        for i in range(row):
            if isinstance(self.map[i][col], dict):
                cur_hint = self.map[i][col]
        return cur_hint['down']
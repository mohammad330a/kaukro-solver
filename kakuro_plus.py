from kakuro_simple import Kakuro

class KakuroPlus(Kakuro):
    def solve(self):
        pass
        # empty_cell = self.get_empty_cell()
        # if not empty_cell:
        #     return self.has_solved()
        # row, col = empty_cell[0], empty_cell[1]
        # for num in range(1, 10):
        #     if self.check_column_constraint(row, col, num) and self.check_row_constraint(row, col, num):
        #         self.map[row][col] = num
        #         if self.solve():
        #             return True
        #         self.map[row][col] = '*'
        # return False

    def get_most_constrained_empty_cell(self):
        pass
        # for i in range(self.n):
        #     for j in range(self.m):
        #         if self.map[i][j] == '*':
        #             return i, j

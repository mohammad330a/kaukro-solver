INF = float('inf')

class Kakuro:
    def __init__(self, n, m, hint_fields, block_fields):
        self.n = n
        self.m = m
        self.map = list()
        self.hint_fields = hint_fields
        self.block_fields = block_fields
        for i in range(n):
            ls = list()
            for j in range(m):
                ls.append('*')
            self.map.append(ls)
        for field in hint_fields:
            self.map[field['i']][field['j']] = field['limit']
        for field in block_fields:
            self.map[field[0]][field[1]] = '#'

    def solve(self):
        # self.show()
        empty_cell = self.get_empty_cell()
        if not empty_cell:
            return self.has_solved()
        row, col = empty_cell[0], empty_cell[1]
        for num in range(1, 10):
            if self.check_column_constraint(row, col, num) and self.check_row_constraint(row, col, num):
                self.map[row][col] = num
                if self.solve():
                    return True
                self.map[row][col] = '*'
        return False

    def has_solved(self):
        # self.show()
        for helper in self.hint_fields:
            row, col, lim = helper['i'], helper['j'], helper['limit']
            if lim['right'] != INF:
                res = 0
                for j in range(col+1, self.m):
                    if self.map[row][j] == '#' or isinstance(self.map[row][j], dict):
                        break
                    res += self.map[row][j]
                if res != lim['right']:
                    return False
            if lim['down'] != INF:
                res = 0
                for i in range(row+1, self.n):
                    if self.map[i][col] == '#' or isinstance(self.map[i][col], dict):
                        break
                    res += self.map[i][col]
                if res != lim['down']:
                    return False
        return True

    def get_empty_cell(self):
        for i in range(self.n):
            for j in range(self.m):
                if self.map[i][j] == '*':
                    return i, j

    def check_column_constraint(self, row, col, num):
        num_cells = list()
        cur_hint = None
        for i in range(self.n):
            if i>=row and (isinstance(self.map[i][col], dict) or self.map[i][col] == '#'):
                break
            if isinstance(self.map[i][col], dict):
                cur_hint = self.map[i][col]
                num_cells = list()
            elif self.map[i][col] == '#':
                num_cells = list()
            else:
                num_cells.append(self.map[i][col])
        if not cur_hint:
            return True
        res = 0
        star_count = 0
        for val in num_cells:
            if val!='*':
                if val == num:
                    return False
                else:
                    res += val
            else:
                star_count += 1
        if res+num <= cur_hint['down'] <= res+num+(star_count - 1)*9:
            return True
        else:
            return False

    def check_row_constraint(self, row, col, num):
        num_cells = list()
        cur_hint = None
        for j in range(self.m):
            if j>=col and (isinstance(self.map[row][j], dict) or self.map[row][j] == '#'):
                break
            if isinstance(self.map[row][j], dict):
                cur_hint = self.map[row][j]
                num_cells = list()
            elif self.map[row][j] == '#':
                num_cells = list()
            else:
                num_cells.append(self.map[row][j])
        if not cur_hint:
            return True
        res = 0
        star_count = 0
        for val in num_cells:
            if val!='*':
                if val == num:
                    return False
                else:
                    res += val
            else:
                star_count+=1
        if res+num <= cur_hint['right'] <= res + num + (star_count - 1) * 9:
            return True
        else:
            return False

    def show(self):
        for row in range(self.n):
            res = ''
            for col in range(self.m):
                if isinstance(self.map[row][col], dict):
                    res += '@ '
                else:
                    res += f'{self.map[row][col]} '
            print(res)
        print()

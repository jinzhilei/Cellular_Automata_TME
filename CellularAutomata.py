import numpy as np
class cellular_automata:

    # Generate a two-dimensional cellular automaton.
    def cellular(self):
        # All the cells are in a state of having no cells, and there is only the microenvironment.
        self.cellular = np.full((self.M1, self.M2), 0, dtype=np.int8)  # Record the cellular automaton cell types, where 0 represents the absence of cells and 1 represents the presence of cells.
        self.cell_type = np.full((self.M1, self.M2), -1, dtype=np.int8)  # Record the cell types, where 0 represents normal cells, 1 represents tumor cells, and -1 represents empty positions.
        self.cell_state = np.full((self.M1, self.M2), -1, dtype=np.int8)  # Record the cell states, where 0 represents stem cells, 1 represents normal cells, and -1 represents empty positions.
        self.m = np.zeros(self.N)   # The value of the cellular microenvironment
        np.set_printoptions(precision=4,floatmode='fixed')    # Control the display precision of decimals.
        for i in range(self.N):
            self.m[i] = np.random.uniform(0, 1)  # The values of all microenvironments are randomly assigned within the range of 0 to 1.
    # Determine whether there are empty spaces around a hexagonal cellular automaton cell i, and return the surrounding empty spaces.
    # Currently, the cell number i is used. If it is inconvenient later, it can be replaced with [i, j].
    def empty_judge(self, i):
        # The six adjacent positions of [x, y] are: [x, y - 1], [x + 1, y - 1], [x - 1, y], [x + 1, y], [x, y + 1], [x + 1, y + 1]
        # x = int(i / self.M2) represents the row number where the cell is located.
        # y = int(i % self.M2) represents the column number where the cell is located.
        # For the cellular automaton cell i, its position is (x, y), where x * M2 + y = i. For example, for the critical element [x, y - 1]: its number j = x * M2 + y - 1 = i - 1.
        # The numbers corresponding to the six adjacent objects of the cellular automaton cell i are i - 1, i + self.M2 - 1, i - self.M2, i + self.M2, i + 1, and i + self.M2 + 1 respectively.
        num = []  # Surrounding empty spaces
        if i not in self.null_cell:
            if (i - 1) in range(self.N) and (i - 1) in self.null_cell:  # 多个if是并列情况会顺序执行,而if..elif是分枝情况,只执行其中一条
                num.append(i - 1)
            if (i + self.M2 - 1) in range(self.N) and (i + self.M2 - 1) in self.null_cell:
                num.append(i + self.M2 - 1)
            if (i - self.M2) in range(self.N) and (i - self.M2) in self.null_cell:
                num.append(i - self.M2)
            if (i + self.M2) in range(self.N) and (i + self.M2) in self.null_cell:
                num.append(i + self.M2)
            if (i + 1) in range(self.N) and (i + 1) in self.null_cell:
                num.append(i + 1)
            if (i + self.M2 + 1) in range(self.N) and (i + self.M2 + 1) in self.null_cell:
                num.append(i + self.M2 + 1)
        if len(num) == 0:
            return 0, 0
        else:
            return 1, num[np.random.randint(0, len(num))]
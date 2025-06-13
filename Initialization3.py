'''
initialization
'''
import numpy as np
from Read import read

class initialization3:
    # initialization
    def init(self):
        cell_number = read.opennumber('number1.xls')  # The quantity of cells for each type.
        data = read.openresult('cell_result1.xls')
        self.normal_stem_cell_total = list(map(int, data[0]))
        self.normal_cell_total = list(map(int, data[1]))
        self.normal_stem_cell = list(map(int, data[0]))
        self.normal_cell = list(map(int, data[1]))
        self.m = np.zeros(self.N)  # The value of the microenvironment of the cellular automaton cell.
        m = read.openm('m_real1.xls')
        self.m = list(map(float, m))  # The value of the cellular automaton's microenvironment

        self.cellular = np.full((self.M1, self.M2), 0, dtype=np.int8)  # Record the type of the cellular automaton cell. 0 represents the absence of a cell, and 1 represents the presence of a cell.
        self.cell_type = np.full((self.M1, self.M2), -1, dtype=np.int8)  # Record the cell type. 0 indicates a normal cell, 1 indicates a tumor cell, and -1 indicates an empty space.
        self.cell_state = np.full((self.M1, self.M2), -1, dtype=np.int8)  # Record the cell state. 0 represents a stem cell, 1 represents a normal cell, and -1 represents an empty position.

        for j in self.normal_stem_cell_total:
            self.cellular[int(j / self.M2), int(j % self.M2)] = 1
            self.cell_type[int(j / self.M2), int(j % self.M2)] = 0
            self.cell_state[int(j / self.M2), int(j % self.M2)] = 0
        for j in self.normal_cell_total:
            self.cellular[int(j / self.M2), int(j % self.M2)] = 1
            self.cell_type[int(j / self.M2), int(j % self.M2)] = 0
            self.cell_state[int(j / self.M2), int(j % self.M2)] = 1
        self.null_cell = list(set(list(range(self.N))) - set(self.normal_cell_total) - set(self.normal_stem_cell_total))
        for j in self.null_cell:
            self.cellular[int(j / self.M2), int(j % self.M2)] = 0
            self.cell_type[int(j / self.M2), int(j % self.M2)] = -1
            self.cell_state[int(j / self.M2), int(j % self.M2)] = -1

        z = 0
        while z < self.init_num:  # The initial number of tumor stem cells.
            this_one = np.random.choice(self.null_cell)
            # n % M2 = i     n / M2 + 1 = j
            if self.cellular[int(this_one / self.M2), int(this_one % self.M2)] == 0:  # Determine whether the cellular automaton cell is an empty cell.
                self.null_cell.remove(this_one)
                self.cellular[int(this_one / self.M2), int(this_one % self.M2)] = 1  # The attribute of the cellular automaton cell is that there is a cell.
                self.cell_type[int(this_one / self.M2), int(this_one % self.M2)] = 1  # The cell type is a tumor cell.
                self.cell_state[int(this_one / self.M2), int(this_one % self.M2)] = 0  # The cell state is that of a stem cell.
                self.cancer_stem_cell.append(this_one)
                self.cancer_stem_cell_total.extend(self.cancer_stem_cell)
                self.cancer_stem_cell_total = list(set(self.cancer_stem_cell_total))
                self.cell_total.append(this_one)
                self.cell_total = list(set(self.cell_total))
                z += 1
        self.cell_total = self.normal_cell_total + self.normal_stem_cell_total + self.cancer_stem_cell_total # All cell numbers are sorted in the order of the cells' generation sequence.
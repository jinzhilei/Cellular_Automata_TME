'''
initialization
'''
import numpy as np
from Read import read

class initialization1:
    # initialization
    def init(self):
        cell_number = read.opennumber('number1.xls')  # The number of cells of each type
        data = read.openresult('cell_result1.xls')
        self.normal_stem_cell_total = list(map(int, data[0]))
        self.normal_cell_total = list(map(int, data[1]))
        self.normal_stem_cell = list(map(int, data[0]))
        self.normal_cell = list(map(int, data[1]))
        self.m = np.zeros(self.N)  # The value of the cellular automaton microenvironment
        m = read.openm('m_real1.xls')
        self.m = list(map(float, m))  # The value of the microenvironment of the cellular automaton

        self.cellular = np.full((self.M1, self.M2), 0, dtype=np.int8)  # Record the types of cellular automaton cells, where 0 indicates the absence of cells and 1 indicates the presence of cells.
        self.cell_type = np.full((self.M1, self.M2), -1, dtype=np.int8)  # Record the cell types. 0 represents normal cells, 1 represents tumor cells, and -1 represents empty positions.
        self.cell_state = np.full((self.M1, self.M2), -1, dtype=np.int8)  # Record the cell states. 0 represents stem cells, 1 represents normal cells, and -1 represents an empty position.

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
        self.cell_total = self.normal_cell_total + self.normal_stem_cell_total  # All cell serial numbers are sorted in the order of the cells' generation sequence.


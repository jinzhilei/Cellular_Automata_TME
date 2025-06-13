'''
Cell proliferation rate, differentiation rate, and death rate calculation formulas
'''
import numpy as np
import math as ma

class calculation:
    # Random Generation of Normal Stem Cells
    def throw_in_latency(self):
        i = 0
        for j in range(self.N):
            if self.cellular[int(j / self.M2), int(j % self.M2)] == 0:
                self.null_cell.append(j)  # Append all empty cells to the list
        while i < self.init_num:  # Initial number of normal stem cells
            this_one = np.random.randint(0, self.N)
            # n % M2 = i     n / M2 + 1 = j
            if self.cellular[int(this_one / self.M2), int(this_one % self.M2)] == 0:  # Check whether the cell is empty
                self.null_cell.remove(this_one)
                self.cellular[int(this_one / self.M2), int(this_one % self.M2)] = 1  # The cell is occupied
                self.cell_type[int(this_one / self.M2), int(this_one % self.M2)] = 0  # The cell type is normal cell
                self.cell_state[int(this_one / self.M2), int(this_one % self.M2)] = 0  # Cell state is stem cell
                self.normal_stem_cell.append(this_one)
                self.normal_stem_cell_total.extend(self.normal_stem_cell)
                self.normal_stem_cell_total = list(set(self.normal_stem_cell_total))
                self.cell_total.append(this_one)
                self.cell_total = list(set(self.cell_total))
                i += 1

    #  Randomly generate normal stem cells and tumor stem cells
    def throw(self):
        i = 0
        z = 0
        for j in range(self.N):
            if self.cellular[int(j / self.M2), int(j % self.M2)] == 0:
                self.null_cell.append(j)  # Add all empty cells to the array
        while i < self.init_num:  # Initial number of normal stem cells
            this_one = np.random.randint(0, self.N)
            # n % M2 = i     n / M2 + 1 = j
            if self.cellular[int(this_one / self.M2), int(this_one % self.M2)] == 0:  # Check whether the cell is empty
                self.null_cell.remove(this_one)
                self.cellular[int(this_one / self.M2), int(this_one % self.M2)] = 1  # The cell is occupied
                self.cell_type[int(this_one / self.M2), int(this_one % self.M2)] = 0  # The cell type is normal cell
                self.cell_state[int(this_one / self.M2), int(this_one % self.M2)] = 0  # Cell state is stem cell
                self.normal_stem_cell.append(this_one)
                self.normal_stem_cell_total.extend(self.normal_stem_cell)
                self.normal_stem_cell_total = list(set(self.normal_stem_cell_total))
                self.cell_total.append(this_one)
                self.cell_total = list(set(self.cell_total))
                i += 1
        while z < self.init_num:  # Initial number of tumor stem cells
            this_one = np.random.randint(0, self.N)
            # n % M2 = i     n / M2 + 1 = j
            if self.cellular[int(this_one / self.M2), int(this_one % self.M2)] == 0:  # Check whether the cell is empty
                self.null_cell.remove(this_one)
                self.cellular[int(this_one / self.M2), int(this_one % self.M2)] = 1   # The cell is occupied
                self.cell_type[int(this_one / self.M2), int(this_one % self.M2)] = 1  # The cell type is normal cell
                self.cell_state[int(this_one / self.M2), int(this_one % self.M2)] = 0  # Cell state is stem cell
                self.cancer_stem_cell.append(this_one)
                self.cancer_stem_cell_total.extend(self.cancer_stem_cell)
                self.cancer_stem_cell_total = list(set(self.cancer_stem_cell_total))
                self.cell_total.append(this_one)
                self.cell_total = list(set(self.cell_total))
                z += 1

    # Calculate the average microenvironment value around cell i
    def microenvironment_value(self, i):
        num = []  # Surrounding positions
        m = 0  # Initial average microenvironment value around the cell
        if (i - 1) in range(self.N):
            num.append(i - 1)
            m += self.m[i - 1]
        if (i + self.M2 - 1) in range(self.N):
            num.append(i + self.M2 - 1)
            m += self.m[i + self.M2 - 1]
        if (i - self.M2) in range(self.N):
            num.append(i - self.M2)
            m += self.m[i - self.M2]
        if (i + self.M2) in range(self.N):
            num.append(i + self.M2)
            m += self.m[i + self.M2]
        if (i + 1) in range(self.N):
            num.append(i + 1)
            m += self.m[i + 1]
        if (i + self.M2 + 1) in range(self.N):
            num.append(i + self.M2 + 1)
            m += self.m[i + self.M2 + 1]
        m = m / len(num)
        return m

    #Calculation of normal stem cell proliferation rate
    def proliferation_normal_stem_cell(self, i):
        m = calculation.microenvironment_value(self, i)
        theta = self.theta0 + self.theta1 * (ma.pow(self.theta2,self.s1) / (ma.pow(self.theta2,self.s1) + ma.pow(m,self.s1)))
        normal_stem_cell_num = 0
        # Find the normal stem cells in the outer three layers of normal stem cells
        x = int(i / self.M2)
        y = int(i % self.M2)
        sub = [-3, -2, -1, 0, 1, 2, 3]
        for j in sub:
            for k in sub:
                if (x + k) * self.M2 + y + j in self.normal_stem_cell:
                    normal_stem_cell_num += 1
        beta = self.beta1 * (1 / (1 + ma.pow(normal_stem_cell_num / theta, self.s0)))
        return beta

    # Calculation of normal cell proliferation rate
    def proliferation_normal_cell(self, i):
        m = calculation.microenvironment_value(self, i)
        theta = self.theta0 + self.theta1 * (ma.pow(self.theta2, self.s1) / (ma.pow(self.theta2, self.s1) + ma.pow(m, self.s1)))
        normal_cell_num = 0
        # Find the normal cells in the outer three layers of normal cells
        x = int(i / self.M2)
        y = int(i % self.M2)
        sub = [-3, -2, -1, 0, 1, 2, 3]
        for j in sub:
            for k in sub:
                if (x + k) * self.M2 + y + j in self.normal_cell:
                   normal_cell_num += 1
        beta = self.beta2 * (1 / (1 + ma.pow(normal_cell_num / theta, self.s0)))
        return beta

    # Calculation of tumor stem cell proliferation rate
    def proliferation_cancer_stem_cell(self, i):
        m = calculation.microenvironment_value(self, i)
        theta = self.theta0 + self.theta1 * (ma.pow(m, self.s1) / (ma.pow(self.theta2, self.s1) + ma.pow(m, self.s1)))
        cancer_stem_cell_num = 0
        # Find the tumor stem cells in the outer three layers of tumor stem cells
        x = int(i / self.M2)
        y = int(i % self.M2)
        sub = [-3, -2, -1, 0, 1, 2, 3]
        for j in sub:
            for k in sub:
                if (x + k) * self.M2 + y + j in self.cancer_stem_cell:
                   cancer_stem_cell_num += 1
        beta = self.beta3 * (1 / (1 + ma.pow(cancer_stem_cell_num / theta, self.s0)))
        return beta

    # Calculation of tumor cell proliferation rate
    def proliferation_cancer_cell(self, i):
        m = calculation.microenvironment_value(self, i)
        theta = self.theta0 + self.theta1 * (ma.pow(m, self.s1) / (ma.pow(self.theta2, self.s1) + ma.pow(m, self.s1)))
        cancer_cell_num = 0
        # Find the tumor cells in the outer three layers of tumor cells
        x = int(i / self.M2)
        y = int(i % self.M2)
        sub = [-3, -2, -1, 0, 1, 2, 3]
        for j in sub:
            for k in sub:
                if (x + k) * self.M2 + y + j in self.cancer_cell:
                   cancer_cell_num += 1
        beta = self.beta4 * (1 / (1 + ma.pow(cancer_cell_num / theta, self.s0)))
        return beta

    #Calculation of normal cell death rate
    def dead_normal_cell(self, i):
        m = calculation.microenvironment_value(self, i)
        g = self.a * (1 - m)
        D = self.D1 / (1 + self.c * ma.exp(g))
        return D

    # Calculation of tumor cell death rate
    def dead_cancer_cell(self, i):
        m = calculation.microenvironment_value(self, i)
        g = self.a * m
        D = self.D2 / (1 + self.c * ma.exp(g))
        return D

    # The impact of local cell quantity on the microenvironment
    def microenvironment_effect(self):
        delta_t = 1
        self.cell_change = list(set(self.cell_change))
        for g in self.cell_change:
            x1 = int(g / self.M2)
            y1 = int(g % self.M2)
            sub = [-3, -2, -1, 0, 1, 2, 3]
            indlist1 = []
            # Find the microenvironment of the outer three layers through the cells
            for j1 in sub:
                for i1 in sub:
                    x2 = x1 + i1
                    y2 = y1 + j1
                    ind = (x1 + i1) * self.M2 + y1 + j1
                    if ind not in indlist1 and ind in range(self.N):
                        indlist1.append(ind)
                        effect_normal_cell = 0
                        effect_cancer_cell = 0
                        indlist2 = []
                        # Find the number of all normal cells and tumor cells in the outer layers through the microenvironment
                        for j2 in sub:
                            for i2 in sub:
                                ind2 = (x2 + i2) * self.M2 + y2 + j2
                                if ind2 not in indlist2:
                                    indlist2.append(ind2)
                                    if ind2 in self.normal_stem_cell + self.normal_cell:
                                        effect_normal_cell += 1
                                    elif ind2 in self.cancer_stem_cell + self.cancer_cell:
                                        effect_cancer_cell += 1
                        if effect_cancer_cell == 0:
                            Rc = 0
                        else:
                            Rc = effect_cancer_cell / (effect_cancer_cell + effect_normal_cell)  # Proportion of tumor (stem) cells
                        if effect_normal_cell == 0:
                            Rn = 0
                        else:
                            Rn = effect_normal_cell / (effect_cancer_cell + effect_normal_cell)  # Proportion of normal (stem) cells
                        k1 = self.k1_0 + self.k1_1 * (ma.pow(Rc, self.n1) / (ma.pow(self.k1_2, self.n1) + ma.pow(Rc, self.n1)))
                        k2 = self.k2_0 + self.k2_1 * (ma.pow(Rn, self.n2) / (ma.pow(self.k2_2, self.n2) + ma.pow(Rn, self.n2)))
                        self.m[ind] = self.m[ind] + delta_t * (k1 * (1 - self.m[ind]) - k2 * self.m[ind])

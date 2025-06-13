'''
Parameter and variable definitions involved in the code
'''
import numpy as np
from Read import read

class parameter_definition:
    def __init__(self):
        ''' Relevant Attributes '''
        self.M1 = 0  # Length
        self.M2 = 0  # Width
        self.init_num = 0  # Initial number of normal stem cells
        self.stemcell_mutation = 0  # Mutation rate of normal stem cells
        self.cell_mutation = 0  # Mutation rate of normal cells
        self.D1 = 0  # Apoptosis rate of normal cells
        self.D2 = 0  # Apoptosis rate of tumor cells
        self.beta1 = 0  # Maximum proliferation rate of normal stem cells
        self.beta2 = 0  # Maximum proliferation rate of normal cells
        self.beta3 = 0  # Maximum proliferation rate of tumor stem cells
        self.beta4 = 0  # Maximum proliferation rate of tumor cells
        self.Pmax1 = 0  # Maximum proliferation times of normal cells
        self.Pmax2 = 0  # Maximum proliferation times of tumor cells
        self.gamma1 = 0  # Differentiation rate during proliferation for normal stem cells
        self.gamma2 = 0  # Differentiation rate during proliferation for tumor stem cells
        self.delta1 = 0  # Differentiation rate during quiescence for normal stem cells
        self.delta2 = 0  # Differentiation rate during quiescence for tumor stem cells
        self.t = 0  # Simulation time in hours
        self.s0 = 0  # Coefficient of cell proliferation rate
        self.s1 = 0  # Coefficient of cell proliferation rate
        self.theta0 = 0  # Coefficient of cell proliferation rate
        self.theta1 = 0  # Coefficient of cell proliferation rate
        self.theta2 = 0  # Coefficient of cell proliferation rate
        self.a = 0  # Adaptive function coefficient for cell death rate
        self.c = 0  # Coefficient of cell death rate
        self.k1_0 = 0  # Coefficient of normal cell microenvironment change rate
        self.k1_1 = 0  # Coefficient of normal cell microenvironment change rate
        self.k1_2 = 0  # Coefficient of normal cell microenvironment change rate
        self.n1 = 0  # Coefficient of normal cell microenvironment change rate
        self.k2_0 = 0  # Coefficient of tumor cell microenvironment change rate
        self.k2_1 = 0  # Coefficient of tumor cell microenvironment change rate
        self.k2_2 = 0  # Coefficient of tumor cell microenvironment change rate
        self.n2 = 0  # Coefficient of tumor cell microenvironment change rate
        self.choose = 0  # Initial state selection:
        # 0 = only normal stem cells,
        # 1 = initial state includes normal stem cells and normal cells with zero mutation rate,
        # 2 = includes both normal and tumor stem cells,
        # 3 = includes normal stem cells, normal cells, and tumor stem cells
        read.read_file(self)
        self.N = self.M1 * self.M2  # Total number of cells
        self.cellular = []  # Record cell presence, 0 = no cell, 1 = has cell
        self.cell_type = []  # Record cell type, 0 = normal cell, 1 = tumor cell, -1 = empty
        self.cell_state = []  # Record cell state, 0 = stem cell, 1 = normal cell, -1 = empty
        self.m = []  # Microenvironment value of the cell
        self.null_cell = []  # IDs of empty cells
        self.normal_stem_cell = []  # IDs of normal stem cells
        self.normal_cell = []  # IDs of normal cells
        self.cancer_stem_cell = []  # IDs of tumor stem cells
        self.cancer_cell = []  # IDs of tumor cells
        self.normal_stem_cell_total = []  # All IDs of normal stem cells
        self.normal_cell_total = []  # All IDs of normal cells
        self.cancer_stem_cell_total = []  # All IDs of tumor stem cells
        self.cancer_cell_total = []  # All IDs of tumor cells
        self.cell_total = []  # All cell IDs, ordered by generation sequence
        self.frequency1 = np.zeros(self.N, dtype=np.int16)  # Proliferation count of normal cells initialized to 0
        self.frequency2 = np.zeros(self.N, dtype=np.int16)  # Proliferation count of tumor cells initialized to 0
        self.cell_change = []  # Cells that change every hour
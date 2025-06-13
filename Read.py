'''
Read parameter values from two files respectively. `input_public` stores public parameters and some relatively fixed parameters, while `input_individual` stores parameters for the cell evolution process.

'''
import pandas as pd


class read:
    def read_file(self):
        # input_public: stores public parameters and some fixed parameters
        with open('input_public', 'r', encoding='UTF-8') as f1:
            list1 = f1.readlines()
            for i in range(0, len(list1)):
                list1[i] = list1[i].rstrip('\n')
            self.M1 = int(list1[0].split(':')[1])  # Length
            self.M2 = int(list1[1].split(':')[1])  # Width
            self.init_num = int(list1[2].split(':')[1])  # Initial number of normal stem cells
            self.stemcell_mutation = float(list1[3].split(':')[1])  # Normal stem cell mutation rate
            self.cell_mutation = float(list1[4].split(':')[1])  # Normal cell mutation rate
            self.t = int(list1[5].split(':')[1])  # Simulation duration in hours
            self.choose = int(list1[6].split(':')[1])  # Initial cell state selection

        # input_individual: parameters for the cell evolution process
        parameter_individual = pd.read_table('input_individual', sep=":", header=None)
        self.D1 = float(parameter_individual[1][0])  # Apoptosis rate of normal cells
        self.D2 = float(parameter_individual[1][1])  # Apoptosis rate of tumor cells
        self.beta1 = float(parameter_individual[1][2])  # Max proliferation rate of normal stem cells
        self.beta2 = float(parameter_individual[1][3])  # Max proliferation rate of normal cells
        self.beta3 = float(parameter_individual[1][4])  # Max proliferation rate of tumor stem cells
        self.beta4 = float(parameter_individual[1][5])  # Max proliferation rate of tumor cells
        self.gamma1 = float(parameter_individual[1][6])  # Differentiation rate during division of normal stem cells
        self.gamma2 = float(parameter_individual[1][7])  # Differentiation rate during division of tumor stem cells
        self.delta1 = float(parameter_individual[1][8])  # Differentiation rate during quiescence of normal stem cells
        self.delta2 = float(parameter_individual[1][9])  # Differentiation rate during quiescence of tumor stem cells
        self.s0 = float(parameter_individual[1][10])  # Coefficient for cell proliferation rate
        self.s1 = float(parameter_individual[1][11])  # Coefficient for cell proliferation rate
        self.theta0 = int(parameter_individual[1][12])  # Coefficient for cell proliferation rate
        self.theta1 = int(parameter_individual[1][13])  # Coefficient for cell proliferation rate
        self.theta2 = float(parameter_individual[1][14])  # Coefficient for cell proliferation rate
        self.a = float(parameter_individual[1][15])  # Adaptation coefficient for cell death rate
        self.c = float(parameter_individual[1][16])  # Coefficient for cell death rate
        self.k1_0 = float(
            parameter_individual[1][17])  # Rate coefficient for change in microenvironment of normal cells
        self.k1_1 = float(
            parameter_individual[1][18])  # Rate coefficient for change in microenvironment of normal cells
        self.k1_2 = float(
            parameter_individual[1][19])  # Rate coefficient for change in microenvironment of normal cells
        self.n1 = float(parameter_individual[1][20])  # Rate coefficient for change in microenvironment of normal cells
        self.k2_0 = float(parameter_individual[1][21])  # Rate coefficient for change in microenvironment of tumor cells
        self.k2_1 = float(parameter_individual[1][22])  # Rate coefficient for change in microenvironment of tumor cells
        self.k2_2 = float(parameter_individual[1][23])  # Rate coefficient for change in microenvironment of tumor cells
        self.n2 = float(parameter_individual[1][24])  # Rate coefficient for change in microenvironment of tumor cells

    def opennumber(file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            last_line = lines[-1].strip()
            res = last_line.strip('[')
            res = res.strip(']')
            res = res.split('\t')
        return res

    def openresult(file_name):
        data = []
        file = open(file_name, 'r')  # Open file
        while True:
            oneline = file.readline().strip()
            if oneline:
                res = oneline.strip('[')
                res = res.strip(']')
                res = res.split('\t')
                data.append(res)
            else:
                break
        return data

    def openm(file_name):
        m = []
        file = open(file_name, 'r')  # Open file
        while True:
            oneline = file.readline().strip()
            if oneline:
                res = oneline.strip('[')
                res = res.strip(']')
                res = res.split('\t')
                m = m + res
            else:
                break
        return m
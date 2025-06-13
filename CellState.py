'''
Processing of various cell states, including proliferation, differentiation, migration, quiescence, and apoptosis'''
import numpy as np
from Update import update
from CellularAutomata import cellular_automata
from Calculation import calculation

class cell_state:
    # Normal stem cell processing
    def normal_stem_cell(self, i):
        beta = calculation.proliferation_normal_stem_cell(self, i)  # Obtain the proliferation rate
        A = np.random.uniform(0, 1)  # Generate a random number
        # Check if there is space in the neighborhood of normal stem cells
        space = cellular_automata.empty_judge(self, i)[0]
        if A <= beta and space == 1:  # 增殖
            # One of the cells retains its original number and position
            if A <= self.stemcell_mutation:
                update.change_cellstate(self, i, 0, 0)  # Remove from the normal stem cells
                self.cell_type[int(i / self.M2), int(i % self.M2)] = 1  # The type of i changes to tumor
                self.cell_state[int(i / self.M2), int(i % self.M2)] = 0  # The state of i changes to stem cell
                self.cell_change.append(i)
                self.cancer_stem_cell.append(i)  # Add the mutated normal stem cells to the tumor stem cell list
                self.cancer_stem_cell = list(set(self.cancer_stem_cell))
                self.cancer_stem_cell_total.extend(self.cancer_stem_cell)  # Add the cell to the list of tumor stem cells after all hours have passed
                self.cancer_stem_cell_total = list(set(self.cancer_stem_cell_total))
            elif self.stemcell_mutation < A <= self.stemcell_mutation + self.gamma1:
                update.change_cellstate(self, i, 0, 0)  # Remove from the normal stem cells
                self.cell_type[int(i / self.M2), int(i % self.M2)] = 0  # The type of i changes to normal
                self.cell_state[int(i / self.M2), int(i % self.M2)] = 1  # The state of i changes to normal cell
                self.cell_change.append(i)
                self.normal_cell.append(i)  # Add the differentiated normal stem cells to the normal cell list
                self.normal_cell = list(set(self.normal_cell))
                self.normal_cell_total.extend(self.normal_cell)
                self.normal_cell_total = list(set(self.normal_cell_total))
            else:
                pass  # Keep the original normal stem cell state, and the number remains unchanged
            number = cellular_automata.empty_judge(self, i)[1]
            B = np.random.uniform(0, 1)  # Generate a random number to make the probability of state transformation for the second cell different from that of the first cell
            # The other cell uses the newly assigned number and position
            if B <= self.stemcell_mutation:
                self.null_cell.remove(number)  # Remove the number from the empty cell
                self.cell_total.append(number)
                self.cellular[int(number / self.M2), int(number % self.M2)] = 1  # The cell attribute is "has cell"
                self.cell_type[int(number / self.M2), int(number % self.M2)] = 1  # The type of number changes to tumor
                self.cell_state[int(number / self.M2), int(number % self.M2)] = 0  # The state of number changes to stem cell
                self.cancer_stem_cell.append(number)  #Add the mutated normal stem cells to the tumor stem cell list
                self.cell_change.append(number)
                self.cancer_stem_cell = list(set(self.cancer_stem_cell))
                self.cancer_stem_cell_total.extend(self.cancer_stem_cell)  # Add the cell to the list of tumor stem cells after all hours have passed
                self.cancer_stem_cell_total = list(set(self.cancer_stem_cell_total))
            elif self.stemcell_mutation < B <= self.stemcell_mutation + self.gamma1:
                self.null_cell.remove(number)  # Remove number from the empty cell
                self.cell_total.append(number)
                self.cellular[int(number / self.M2), int(number % self.M2)] = 1  # The cell attribute is "has cell
                self.cell_type[int(number / self.M2), int(number % self.M2)] = 0  # The type of number changes to normal
                self.cell_state[int(number / self.M2), int(number % self.M2)] = 1  # The state of number changes to normal cell
                self.normal_cell.append(number)  # Add the differentiated normal stem cells to the normal cell list
                self.cell_change.append(number)
                self.normal_cell = list(set(self.normal_cell))
                self.normal_cell_total.extend(self.normal_cell)
                self.normal_cell_total = list(set(self.normal_cell_total))
            else:
                self.null_cell.remove(number)  # Remove number from the empty cell
                self.cell_total.append(number)
                self.cellular[int(number / self.M2), int(number % self.M2)] = 1  # The cell attribute is "has cell"
                self.cell_type[int(number / self.M2), int(number % self.M2)] = 0  # The type of number changes to normal cell
                self.cell_state[int(number / self.M2), int(number % self.M2)] = 0  # The state of number changes to stem cell
                self.normal_stem_cell.append(number)  # Add the proliferating normal stem cells to the normal stem cell list
                self.cell_change.append(number)
                self.normal_stem_cell = list(set(self.normal_stem_cell))
                self.normal_stem_cell_total.extend(self.normal_stem_cell)
                self.normal_stem_cell_total = list(set(self.normal_stem_cell_total))
        elif beta < A <= beta + self.delta1:  #
            update.change_cellstate(self, i, 0, 0)  # Remove from normal stem cells
            self.cell_type[int(i / self.M2), int(i % self.M2)] = 0  # Convert/Change the type of i to "normal cell
            self.cell_state[int(i / self.M2), int(i % self.M2)] = 1  # Change i's state to "normal cell"
            self.normal_cell.append(i)  # Add the quiescent differentiated normal stem cells to the normal cell list
            self.cell_change.append(i)
            self.normal_cell = list(set(self.normal_cell))
            self.normal_cell_total.extend(self.normal_cell)
            self.normal_cell_total = list(set(self.normal_cell_total))
        else:
            pass  # Maintain the original state of normal stem cells without changing their numbering

    # 正常细胞处理
    def normal_cell(self, i):
        beta = calculation.proliferation_normal_cell(self, i)  # Get the proliferation rate
        D = calculation.dead_normal_cell(self, i)  # Get the mortality rate
        A = np.random.uniform(0, 1)  # Generate a random number
        # Check if there is space in the neighborhood of normal cells
        space = cellular_automata.empty_judge(self, i)[0]
        if A <= beta and space == 1:  # Proliferation
            self.frequency1[i] += 1  # Increment the proliferation count
            # 其中一个细胞保持原来的编号和位置
            if A <= self.cell_mutation:
                update.change_cellstate(self, i, 0, 1)  # Remove from normal cells
                self.cell_type[int(i / self.M2), int(i % self.M2)] = 1  # Change the type of `i` to "tumor"
                self.cell_state[int(i / self.M2), int(i % self.M2)] = 1  # Change the state of `i` to "normal cell"
                self.cancer_cell.append(i)  # Add the mutated normal cells to the tumor cell list.
                self.cell_change.append(i)
                self.cancer_cell = list(set(self.cancer_cell))
                self.cancer_cell_total.extend(self.cancer_cell)  # Add the cells to the post-hour tumor cell list.
                self.cancer_cell_total = list(set(self.cancer_cell_total))
            else:
                pass  # Maintain the original state of normal cells without altering their numbering.
            number = cellular_automata.empty_judge(self, i)[1]
            B = np.random.uniform(0, 1)  # Generate a random number to make the state transition probability of the second cell differ from that of the first cell.
            # Another cell utilizes the newly added numbering and position.
            if B <= self.cell_mutation:
                self.null_cell.remove(number)  # Remove number from empty cells.
                self.cell_total.append(number)
                self.cellular[int(number / self.M2), int(number % self.M2)] = 1  # Set the cell attribute to "occupied
                self.cell_type[int(number / self.M2), int(number % self.M2)] = 1  # Change the type of number to "tumor
                self.cell_state[int(number / self.M2), int(number % self.M2)] = 1  # Change the state of number to "normal cell
                self.cancer_cell.append(number)  # Add the mutated normal cells to the tumor cell list.
                self.cell_change.append(number)
                self.cancer_cell = list(set(self.cancer_cell))
                self.cancer_cell_total.extend(self.cancer_cell)  # Add the cells to the post-hour tumor cell list
                self.cancer_cell_total = list(set(self.cancer_cell_total))
            else:
                self.null_cell.remove(number)  # Remove number from empty cells
                self.cell_total.append(number)
                self.cellular[int(number / self.M2), int(number % self.M2)] = 1  # Cell property set to "occupied
                self.cell_type[int(number / self.M2), int(number % self.M2)] = 0  # Change the type of number to "normal cell
                self.cell_state[int(number / self.M2), int(number % self.M2)] = 1  # Change the state of number to "normal cell
                self.normal_cell.append(number)  # Add the proliferated normal cells to the normal cell list.
                self.cell_change.append(number)
                self.normal_cell = list(set(self.normal_cell))
                self.normal_cell_total.extend(self.normal_cell)
                self.normal_cell_total = list(set(self.normal_cell_total))
        elif beta < A <= beta + D:  # death
            update.change_cellstate(self, i, 0, 1)  # Remove from normal cells.
            self.cellular[int(i / self.M2), int(i % self.M2)] = 0  # Set the cell attribute to "empty
            self.cell_type[int(i / self.M2), int(i % self.M2)] = -1  # Set i to empty.
            self.cell_state[int(i / self.M2), int(i % self.M2)] = -1  # Empty cell / Vacant position
            self.cell_total.remove(i)
            self.cell_change.append(i)
            self.null_cell.append(i)
            self.null_cell = list(set(self.null_cell))
        else:
            pass  # Maintain the original state of normal cells without changing their numbering

    # Tumor stem cell processing
    def cancer_stem_cell(self, i):
        beta = calculation.proliferation_cancer_stem_cell(self, i)
        A = np.random.uniform(0, 1)  # Generate a random number.
        # Check if there is space in the neighborhood of the tumor stem cell
        space = cellular_automata.empty_judge(self, i)[0]
        if A <= beta and space == 1:  # Proliferation.
            # One cell retains its original numbering and position
            if A <= self.gamma2:
                update.change_cellstate(self, i, 1, 0)  # Remove from tumor stem cells.
                self.cell_type[int(i / self.M2), int(i % self.M2)] = 1  # Change the type of i to "tumor"
                self.cell_state[int(i / self.M2), int(i % self.M2)] = 1  # Change the state of i to "normal cell
                self.cancer_cell.append(i)  # Add the differentiated tumor stem cells to the tumor cell list.
                self.cell_change.append(i)
                self.cancer_cell = list(set(self.cancer_cell))
                self.cancer_cell_total.extend(self.cancer_cell)  # Add the cells to the tumor cell list after all time intervals.
                self.cancer_cell_total = list(set(self.cancer_cell_total))
            else:
                pass  # Maintain the original state of normal cells without changing their numbering
            number = cellular_automata.empty_judge(self, i)[1]
            B = np.random.uniform(0, 1)  # Generate a random number to make the state transition probability of the second cell differ from that of the first cell
            # Another cell utilizes the newly assigned numbering and position
            if B <= self.gamma2:
                self.null_cell.remove(number)  # Remove number from empty cells.
                self.cell_total.append(number)
                self.cellular[int(number / self.M2), int(number % self.M2)] = 1  # The cellular attribute is that there are cells
                self.cell_type[int(number / self.M2), int(number % self.M2)] = 1  # The type of "number" is changed to "tumor"
                self.cell_state[int(number / self.M2), int(number % self.M2)] = 1  # The state of "number" changes to that of a normal cell.
                self.cancer_cell.append(number)  # Add the differentiated tumor stem cells to the list of tumor cells.
                self.cell_change.append(number)
                self.cancer_cell = list(set(self.cancer_cell))
                self.cancer_cell_total.extend(self.cancer_cell)  # Add the cells to the list of tumor cells at all hours later.
                self.cancer_cell_total = list(set(self.cancer_cell_total))
            else:
                self.null_cell.remove(number)  # Remove "number" from the empty cells
                self.cell_total.append(number)
                self.cell_change.append(number)
                self.cellular[int(number / self.M2), int(number % self.M2)] = 1  # The cell attribute indicates the presence of cells.
                self.cell_type[int(number / self.M2), int(number % self.M2)] = 1  # The type of "number" changes to tumor cells.
                self.cell_state[int(number / self.M2), int(number % self.M2)] = 0  # The state of "number" changes to stem cells.
                self.cancer_stem_cell.append(number)  # Add the proliferated tumor stem cells to the list of tumor stem cells.
                self.cancer_stem_cell = list(set(self.cancer_stem_cell))
                self.cancer_stem_cell_total.extend(self.cancer_stem_cell)
                self.cancer_stem_cell_total = list(set(self.cancer_stem_cell_total))
        elif beta < A <= beta + self.delta2:  # Quiescent - phase differentiation
            update.change_cellstate(self, i, 1, 0)  # Remove from the tumor stem cells
            self.cell_type[int(i / self.M2), int(i % self.M2)] = 1  # The type of "i" changes to tumor cells.
            self.cell_state[int(i / self.M2), int(i % self.M2)] = 1  # The state of "i" changes to that of a normal cell.
            self.cancer_cell.append(i)  # Add the tumor stem cells that have differentiated during the quiescent period to the list of tumor cells.
            self.cell_change.append(i)
            self.cancer_cell = list(set(self.cancer_cell))
            self.cancer_cell_total.extend(self.cancer_cell)
            self.cancer_cell_total = list(set(self.cancer_cell_total))
        else:
            pass  # Maintain the original state of the tumor stem cells, and the serial number will not be changed.

    # Tumor cell treatment
    def cancer_cell(self, i):
        beta = calculation.proliferation_cancer_cell(self, i)  # Obtain the proliferation rate
        D = calculation.dead_cancer_cell(self, i)  # Obtain the mortality rate
        A = np.random.uniform(0, 1)  # Generate a random number
        # Determine whether there is space in the neighborhood of the tumor cells.
        space = cellular_automata.empty_judge(self, i)[0]
        if A <= beta and space == 1:  # 增殖
            self.frequency2[i] += 1
            # One of the cells maintains its original serial number and position, and the other proliferating cell makes use of the newly added serial number and position.
            number = cellular_automata.empty_judge(self, i)[1]
            self.null_cell.remove(number)  # Remove "number" from the empty cells.
            self.cell_total.append(number)
            self.cell_change.append(number)
            self.cellular[int(number / self.M2), int(number % self.M2)] = 1  # The cellular attribute is that there are cells.
            self.cell_type[int(number / self.M2), int(number % self.M2)] = 1  # The type of "number" changes to that of a tumor.
            self.cell_state[int(number / self.M2), int(number % self.M2)] = 1  # The state of "number" changes to that of a normal cell.
            self.cancer_cell.append(number)  # Add the differentiated tumor stem cells to the list of tumor cells.
            self.cancer_cell = list(set(self.cancer_cell))
            self.cancer_cell_total.extend(self.cancer_cell)  # Add the cells to the list of tumor cells after all hours.
            self.cancer_cell_total = list(set(self.cancer_cell_total))
        elif beta < A <= beta + D:  # death
            update.change_cellstate(self, i, 1, 1)  # Remove from the tumor cells.
            self.cellular[int(i / self.M2), int(i % self.M2)] = 0  # The cell attribute is that there are no cells.
            self.cell_type[int(i / self.M2), int(i % self.M2)] = -1  # "i" changes into the microenvironment.
            self.cell_state[int(i / self.M2), int(i % self.M2)] = -1  # There are no cells.
            self.cell_total.remove(i)
            self.cell_change.append(i)
            self.null_cell.append(i)
            self.null_cell = list(set(self.null_cell))
        else:
            pass  # Maintain the original state of the tumor cells, and the serial number remains unchanged.


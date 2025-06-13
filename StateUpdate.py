'''
Update the state of the cells every hour.
'''
from CellState import cell_state
class state_update:
    # Update the hourly state of cells.
    def update_state(self):
        cell_loop = list(self.cell_total)   # Using the temporary variable `cell_loop` will update all the variables in `self.cell_total` (including both the old cells and the newly generated ones) once again.
        for j in cell_loop:
            # Normal stem cells
            if self.cell_type[int(j / self.M2), int(j % self.M2)] == 0 and self.cell_state[int(j / self.M2), int(j % self.M2)] == 0:
                cell_state.normal_stem_cell(self, j)
            # Normal cells
            elif self.cell_type[int(j / self.M2), int(j % self.M2)] == 0 and self.cell_state[int(j / self.M2), int(j % self.M2)] == 1:
                cell_state.normal_cell(self, j)
            # Tumor stem cells
            elif self.cell_type[int(j / self.M2), int(j % self.M2)] == 1 and self.cell_state[int(j / self.M2), int(j % self.M2)] == 0:
                cell_state.cancer_stem_cell(self, j)
            # Tumor cells
            elif self.cell_type[int(j / self.M2), int(j % self.M2)] == 1 and self.cell_state[int(j / self.M2), int(j % self.M2)] == 1:
                cell_state.cancer_cell(self, j)
        cell_loop = list(self.cell_total)  # Update cells.
        #print("cell_loop", cell_loop)

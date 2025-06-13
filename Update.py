'''
The hourly update of cell states.
'''
class update:

    # Change the original type and state of the cells.
    def change_cellstate(self, i, type, state):
        # The state of normal stem cells
        if type == 0 and state == 0:
            self.normal_stem_cell.remove(i)
            self.normal_stem_cell_total.remove(i)
        # The state of normal cells
        elif type == 0 and state == 1:
            self.normal_cell.remove(i)
            self.normal_cell_total.remove(i)
        # The state of tumor stem cells
        elif type == 1 and state == 0:
            self.cancer_stem_cell.remove(i)
            self.cancer_stem_cell_total.remove(i)
        # The state of tumor cells
        elif type == 1 and state == 1:
            self.cancer_cell.remove(i)
            self.cancer_cell_total.remove(i)

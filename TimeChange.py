'''
The time step is set to be once every 1 hour (which can be changed). Based on the time, corresponding work such as network update, individual state update, and data recording should be carried out.
'''
from Record import record
from StateUpdate import state_update
from Calculation import calculation

class time_change:
    def change(self, loop):
        # The simulation time of the program (in hours)
        for i in range(0, self.t):
            self.cell_change = []  # Record the cells whose states or types change every hour. Assign the record to be empty every hour and then record again.
            #if i>= 720:
            #    self.k1_1 = 0.2
            if i>= 720:
                #for j in range(len(self.m)):
                 #   self.m[j] = 0.2
                self.m = 0 * self.m + 0.2
            state_update.update_state(self)
            calculation.microenvironment_effect(self)
            record.record(self,loop)
            record.record_m(self, loop)
            if i % 24 == 0:  # Save the cell states and microenvironment values on a daily basis.
               record.record_result(self,loop)
               record.record_m_real(self, loop)
        record.record_frequency1(self, loop)
        record.record_frequency2(self, loop)
        # record.s_record(self, loop)
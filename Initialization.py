'''
初始化
'''
from CellularAutomata import cellular_automata
from Calculation import calculation

class initialization:
    # 初始化
    def init(self):
        cellular_automata.cellular(self)
        calculation.throw_in_latency(self)

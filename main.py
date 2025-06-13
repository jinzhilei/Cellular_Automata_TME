'''
Main function: Calculate the running time of the program, generate an instance of `agdate` to simulate the evolution of cells, and display the quantities of normal stem cells, normal cells, tumor stem cells, and tumor cells.
'''
import datetime
import os

from ParameterDefinition import parameter_definition
from Initialization import initialization
from TimeChange import time_change
from Initialization1 import initialization1
from Initialization2 import initialization2
from Initialization3 import initialization3
from Record import record
import math as ma

if __name__ == "__main__":
    start = datetime.datetime.now()
    # The number of simulation times of the program
    t = int(1)

    # Define the function.
    def zdcl(t):
        for i in range(0, t):
            #print("第",i + 1, "次")

            agdate = parameter_definition()
            if agdate.choose == 0:
               initialization.init(agdate)
            elif agdate.choose == 1:
               initialization1.init(agdate)
            elif agdate.choose == 2:
               initialization2.init(agdate)
            else:
               initialization3.init(agdate)
            time_change.change(agdate, i)
            del agdate
            '''
            #不同的K1和K2的值
            for k1_1 in [2]:
                for k1_2 in [2.5]:
                    agdate = parameter_definition()
                    agdate.k1_1 = k1_1
                    agdate.k1_2 = k1_2
                    if agdate.choose == 0:
                        initialization.init(agdate)
                    else:
                        initialization1.init(agdate)
                    time_change.change(agdate, i)
                    record.k_record(agdate, i)
                    del agdate
                '为了使输出数据的格式以矩阵的方式存入表格中，无实际意义'
                contents = os.getcwd() + '/output_result/'
                filename = contents + 'k_num.xls'
                with open(filename, 'a') as file_object:
                    file_object.write('\n')
            
            count = 1
            for stemcell_mutation in [ma.pow(10, -6), 5 * ma.pow(10, -6), ma.pow(10, -5), 5 * ma.pow(10, -5), ma.pow(10, -4),
                                      5 * ma.pow(10, -4),ma.pow(10, -3), 5 * ma.pow(10, -3), ma.pow(10, -2), 5 * ma.pow(10, -2), ma.pow(10, -1)]:
                agdate = parameter_definition()
                agdate.stemcell_mutation = stemcell_mutation
                if agdate.choose == 0:
                    initialization.init(agdate)
                else:
                    initialization1.init(agdate)
                time_change.change(agdate, count)
                record.s_record(agdate, count)
                count += 1
                del agdate
            '''
    # Call the function.
    zdcl(t)
    end = datetime.datetime.now()
    #print('运行时间：%s 秒' % (end - start))




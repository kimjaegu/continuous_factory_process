import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import process_data

class Scatter:
    """
    산점도를 표시한다
    """
    def __init__(self):
        self.data = process_data.Data()


    # PRIMARY OUTPUT TO CONTROL vs Combiner stage process parameters
    def scatter_combine_params(self):
        """
        RIMARY OUTPUT TO CONTROL vs Combiner stage process parameters
        의 산점도 표시
        """
        combine_params_actual = pd.concat([self.data.combine_params, self.data.primary_output_actual], axis = 1)
        for i in range(15):
            pd.plotting.scatter_matrix(
                combine_params_actual.iloc[:,[0, 1, 2, 3 + i]],
                alpha = 0.5,
                figsize= (10, 10),
                diagonal = 'hist'
                )
            plt.show()

    # machine1_process vs Combiner stage process parameters
    def scatter_machine1_process(self):
        """
        machine1_process vs Combiner stage process parameters
        의 산점도 표시
        """
        machine1_process_actual = pd.concat([self.data.machine1_process, self.data.primary_output_actual], axis = 1)
        for i in range(15):
            pd.plotting.scatter_matrix(
                machine1_process_actual.iloc[:,[0, 1, 2, 3, 4, 5, 6, 7, 8 + i]],
                alpha = 0.5,
                figsize= (10, 10),
                diagonal = 'hist'
                )
            plt.show()

    # machine2_process vs Combiner stage process parameters
    def scatter_machine2_process(self):
        """
        machine2_process vs Combiner stage process parameters
        의 산점도 표시
        """
        machine2_process_actual = pd.concat([self.data.machine2_process, self.data.primary_output_actual], axis = 1)
        for i in range(15):
            pd.plotting.scatter_matrix(
                machine2_process_actual.iloc[:,[0, 1, 2, 3, 4, 5, 6, 7, 8 + i]],
                alpha = 0.5,
                figsize= (10, 10),
                diagonal = 'hist'
                )
            plt.show()

    # machine3_process vs Combiner stage process parameters
    def scatter_machine3_process(self):
        """
        machine3_process vs Combiner stage process parameters
        의 산점도 표시
        """
        machine3_process_actual = pd.concat([self.data.machine3_process, self.data.primary_output_actual], axis = 1)
        for i in range(15):
            pd.plotting.scatter_matrix(
                machine3_process_actual.iloc[:,[0, 1, 2, 3, 4, 5, 6, 7, 8 + i]],
                alpha = 0.5,
                figsize = (10, 10),
                diagonal = 'hist'
                )
            plt.show()
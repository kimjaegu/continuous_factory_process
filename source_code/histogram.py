import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

train = pd.read_csv("./Data/continuous_factory_process.csv")
test = pd.read_csv("./Data/continuous_factory_process.csv")

factory_condition = train.iloc[:,1:3]
machine1_raw = train.iloc[:,3:7]
machine1_process = train.iloc[:,7:15]
machine2_raw = train.iloc[:,15:19]
machine2_process = train.iloc[:,19:27]
machine3_raw = train.iloc[:,27:31]
machine3_process = train.iloc[:,31:38]
combine_params = train.iloc[:,39:42]
primary_output = train.iloc[:,42:72]
machine4_process = train.iloc[:,72:79]
machine5_process = train.iloc[:,79:86]
secondary_output = train.iloc[:,86:]

var1 = [
    machine1_raw,
    machine1_process,
    machine2_raw,
    machine2_process,
    machine3_raw,
    machine3_process,
    combine_params,
    primary_output
    ]

actual_index = [i * 2 for i in range(15)]
setpoint_index = [i * 2 + 1 for i in range(15)]
primary_output_actual = primary_output.iloc[:,actual_index]
primary_output_setpoint = primary_output.iloc[:,setpoint_index]

# combine_params_actual.head()

# PRIMARY OUTPUT TO CONTROL vs Combiner stage process parameters
def scatter_combine_params():
    combine_params_actual = pd.concat([combine_params, primary_output_actual], axis = 1)
    for i in range(15):
        pd.plotting.scatter_matrix(
            combine_params_actual.iloc[:,[0, 1, 2, 3 + i]],
            alpha = 0.5,
            figsize= (10, 10),
            diagonal = 'hist'
            )
        plt.show()

# machine1_process vs Combiner stage process parameters
def scatter_machine1_process():
    machine1_process_actual = pd.concat([machine1_process, primary_output_actual], axis = 1)
    for i in range(15):
        pd.plotting.scatter_matrix(
            machine1_process_actual.iloc[:,[0, 1, 2, 3, 4, 5, 6, 7, 8 + i]],
            alpha = 0.5,
            figsize= (10, 10),
            diagonal = 'hist'
            )
        plt.show()

# machine2_process vs Combiner stage process parameters
def scatter_machine2_process():
    machine2_process_actual = pd.concat([machine2_process, primary_output_actual], axis = 1)
    for i in range(15):
        pd.plotting.scatter_matrix(
            machine2_process_actual.iloc[:,[0, 1, 2, 3, 4, 5, 6, 7, 8 + i]],
            alpha = 0.5,
            figsize= (10, 10),
            diagonal = 'hist'
            )
        plt.show()

# machine3_process vs Combiner stage process parameters
def scatter_machine3_process():
    machine3_process_actual = pd.concat([machine3_process, primary_output_actual], axis = 1)
    for i in range(15):
        pd.plotting.scatter_matrix(
            machine3_process_actual.iloc[:,[0, 1, 2, 3, 4, 5, 6, 7, 8 + i]],
            alpha = 0.5,
            figsize = (10, 10),
            diagonal = 'hist'
            )
        plt.show()


def scatter_machine1_raw():
    machine1_raw_actual = pd.concat([machine1_raw, primary_output_actual], axis = 1)
    for i in range(15):
        pd.plotting.scatter_matrix(
            machine1_raw_actual.iloc[:,[0, 1, 2, 3, 4 + i]],
            alpha = 0.5,
            figsize = (10, 10),
            diagonal = 'hist'
            )
        plt.show()

scatter_machine1_raw()
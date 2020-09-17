import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
cols = ['SPEED_A','TORQUE_A','P_OILOF']
test1 = pd.read_excel('VL.xlsx',usecols="SPEED_A",header=0)
print(test1)


# test1 = test1.drop([0])
# test1.plot(x='T_DB1',y='T_DB2')
# plt.show
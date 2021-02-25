import time

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import x
import PD

OX = np.arange(0, x.N/3600)
step_resp = [];

if x.reg == 1:
    step_resp.append(PD.T_wody2[0])
    for i in range(1, round((x.N)/3600)):
        step_resp.append(PD.T_wody2[i*3600])
elif x.reg == 2:
    #step_resp.append(rozm_PD.T_wody2[0])
    print("rozmyty");

plt.plot(OX, step_resp)
plt.show()


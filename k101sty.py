# -*- coding: UTF-8 -*-

import numpy as np
import scipy as sp
import pandas as pd
import pandas.lib
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import prettyplotlib
import ggplot

mpl.style.use("seaborn-whitegrid")

def sta001(k, nyear, xd):
    return round(np.fv(k, nyear, -xd, -xd))

def dr_xtpy(_dat):
    i = 0
    for xss in plt.style.available:
        plt.figure()
        plt.style.use(xss)
        _dat.plot()
        fss = "tmp\\k101_" + xss + ".png"
        plt.savefig(fss)
        i += 1
        print(i, xss, ", ", fss)
        plt.show() 

dx05 = [sta001(0.05, x, 1.4) for x in range(0, 40)]
dx10 = [sta001(0.10, x, 1.4) for x in range(0, 40)]
dx15 = [sta001(0.15, x, 1.4) for x in range(0, 40)]
dx20 = [sta001(0.20, x, 1.4) for x in range(0, 40)]

df = pd.DataFrame(columns=["dx05", "dx10", "dx15", "dx20"])
df["dx05"] = dx05
df["dx10"] = dx10
df["dx15"] = dx15
df["dx20"] = dx20

print df.tail()
dr_xtpy(df)
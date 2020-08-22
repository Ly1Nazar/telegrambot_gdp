import matplotlib.pyplot as plt
import numpy as np


def research_main(value):
    country_name = value[0]
    del value[0]
    for i in range(len(value)):
        if value[i] == 'no data':
            value[i] = 0
        else:
            continue
    # value represents y param
    x_value = np.arange(1980,2025,1)# represent x param
    y_values = np.asarray(value)#represent y param
    fig, ax = plt.subplots()
    plt.plot(x_value, y_values, 'c--')
    fig.savefig("test.png")

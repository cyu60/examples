import matplotlib.pyplot as plt
import numpy as np
import math

def plot_histogram(df1):
    values = df1['value']

    fig = plt.figure(figsize=(6, 4))
    fig.suptitle("Transactions of RFUEL", fontsize=14) #title
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.set_xlabel("Number of Tokens")
    ax1.set_ylabel("Number of Transactions")
    fig.subplots_adjust(top=0.85, wspace=0.3)

    # Get the min, and max
    max_value = values.max()
    min_value = values.min()

    # have the bin be in 500 ranges
    x_start = math.floor(min_value / 5000) * 5000
    x_end = math.ceil(max_value / 5000) * 5000

    bins = np.arange(x_start, x_end, 5000).tolist()
    
    # print(bins)
    plt.xticks(bins)
    plt.hist(values, density=False, bins=bins, rwidth=0.95)
    # plt.show()
    return fig

if __name__ == '__main__':
    pass
    

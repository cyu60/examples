import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.ticker import MaxNLocator
import random
from statistics import median


def plot_histogram(df1):
    values = get_values_from_df_thousands(df1)
    fig = generate_histogram(values)
    return fig

def get_values_from_df_thousands(df1):
    df2 = df1.copy(deep=True)
    df2['value_thousands'] = df1['value'].astype(float) / (10 ** 3)
    values = df2['value_thousands']
    return values.to_list()

def get_interval(diff):
    # div by 10 pattern??
    # while less than diff, keep mutiplying and checking?
    # alternate x5, x10
    if diff < 10:
        return 1
    elif diff < 50:
        return 5
    elif diff < 100:
        return 10
    else: # should look into adding more ranges
        return 50

def generate_histogram(values):
    fig = plt.figure(figsize=(6, 4))
    fig.suptitle("Transactions of RFUEL", fontsize=14) #title
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.set_xlabel("Number of Tokens (Thousands)")
    ax1.set_ylabel("Number of Transactions")
    fig.subplots_adjust(top=0.85, wspace=0.3)

    # Get the min, and max
    max_value = max(values)
    min_value = min(values)

    # find the right number of bins according to range
    # find the interval size
    diff = max_value - min_value

    # print(min_value)
    # print(max_value)

    interval = get_interval(diff)
    # have the bin be in interval ranges
    x_start = math.floor(min_value / interval) * interval
    x_end = math.ceil(max_value / interval) * interval
    
    # print(x_start, x_end)
    # Bins need to have at least 2 values -- create a range
    bins = np.arange(x_start, x_end + 1, interval).tolist()
    # print(bins)

    plt.xticks(bins)
    # set y axis to be ints > 0
    ax = fig.gca()
    # ax.set_ylim(ymin=0)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    plt.hist(values, density=False, bins=bins, rwidth=0.95)

    # add median ?
    # plt.axvline(median(values), color='r', linewidth=1, label='Transactions median')
    # plt.legend()
    
    # ONLY RUN WHEN TESTING!
    # plt.show()
    return fig

# For tests
def generate_data(min_value, max_value, num_values):
    # randint == size, # range == number of values
    return [random.randint(min_value, max_value) for _ in range(num_values)]

if __name__ == '__main__':
    data = generate_data(1, 500, 100)
    # data = [25215, 25214]

    print(data)
    print(max(data))
    print(min(data))
    generate_histogram(data)
    pass
    

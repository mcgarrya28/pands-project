# Fisher's Iris Data Analysis
#Anthony McGarry

"""Import the 2 libraries numpy and padas"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""Read in the Iris data set"""
iris = pd.read_csv("Iris.csv", names=["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species]"])


"""Create a summary of the data set using the describe method and output the statistical data into a .txt file"""
stat_summary = iris.describe()

with open('Iris Data Summary.txt', 'w') as f:
    f.write(str(stat_summary))

hist_params = {'bins': 20, 'edgecolor': 'black', 'alpha': 0.7}

# Generate a histogram of each variable and save it to a PNG file
for col in iris.columns[:-1]:  # Skip the last column (class)
    plt.hist(iris[col], **hist_params)
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.tight_layout()  # Add padding to the plot
    plt.savefig(f'{col}.png')
    plt.clf()  # Clear the figure for the next plot



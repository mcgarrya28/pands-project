# Fisher's Iris Data Analysis
#Anthony McGarry

"""Import the 2 libraries numpy and padas"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""Read in the Iris data set"""
iris = pd.read_csv("Iris.csv", names=["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"], header = 0)


"""Create a summary of the data set using the describe method and output the statistical data into a .txt file"""
iris_species = iris.groupby('Species')
stat_summary = iris_species.describe().T

with open('Iris Data Summary.txt', 'w') as f:
    f.write(str(stat_summary))

hist_params = {'bins': 15, 'edgecolor': 'black', 'alpha': 0.5}

"""Generate a histogram of each variable and save it to a PNG file"""
for col in iris.columns[:-1]:  # Skip the last column (Species)
    plt.hist(iris[col], **hist_params)
    plt.title('Iris Fisher Dataset')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.tight_layout()  
    plt.savefig(f'{col}.png')
    plt.clf()
    

sns.scatterplot(x='SepalLengthCm', y='SepalWidthCm', hue = 'Species' ,data=iris, x_bins = 15 , y_bins= 15)
plt.title('Sepal Length v Sepal Width')
plt.savefig(f'Sepal Length v Width Scatterplot.png')    

sns.pairplot(iris, hue = 'Species')
plt.savefig(f' Pairplot Sepal Length v Width.png')

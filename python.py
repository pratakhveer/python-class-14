import csv
from os import stat
import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

df = pd.read_csv("data.csv")
data = df["average"].tolist()

populationMean = statistics.mean(data)

# dataset = []

# for i in range(0, 100):
# randind = random.randint(0, len(data))
# value = data[randind]
# dataset.append(value)

# mean = statistics.mean(dataset)
# standardDev = statistics.stdev(dataset)

# print(standardDev, ":", mean)

populationStd = statistics.stdev(data)

print(populationMean, ":", populationStd)


def randomMean(counter):
    dataset = []

    for i in range(0, counter):
        randind = random.randint(0, len(data)-1)
        value = data[randind]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean


def showFig(meanList):

    df = meanList

    mean = statistics.mean(df)

    populationFig = ff.create_distplot(
        [data],
        ["temp"],
        show_hist=False
    )

    populationFig.add_trace(go.Scatter(
        x=[mean, mean],
        y=[0, 1],
        mode="lines",
        name="MEAN"
    ))

    populationFig.show()


def main():
    meanList = []
    for i in range(0, 1000):
        setOfMean = randomMean(100)
        meanList.append(setOfMean)
    showFig(meanList)


main()


def standardDev():
    meanList = []
    for i in range(0, 1000):
        setOfMean = randomMean(100)
        meanList.append(setOfMean)
    sd = statistics.stdev(meanList)
    print(sd)


standardDev()

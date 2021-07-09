import plotly.express as px
import csv
import numpy as np
import pandas as pd

def getDataSource(data_path, xName, yName):
    valueSet1 = []
    valueSet2 = []
    
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            valueSet1.append(float(row[xName]))
            valueSet2.append(float(row[yName]))
            
    return {"x": valueSet1, "y": valueSet2}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("correlation is ", correlation[0,1])
    
def generateScatterPlot(path, value1, value2):
    df = pd.read_csv(path)
    fig = px.scatter(df, value1, value2)
    
    fig.show()
    
def setUp(path, xName, yName):
    dataPath = path
    dataSource = getDataSource(dataPath, xName, yName)
    findCorrelation(dataSource)
    generateScatterPlot(dataPath, xName, yName)
    
setUp("coffeeData.csv", "Coffee in ml", "sleep in hours")
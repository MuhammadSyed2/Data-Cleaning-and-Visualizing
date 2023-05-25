import pandas as pd

dataframe1 = pd.read_csv("dataset.txt", sep=' ')

dataframe1.to_csv('dataset_csv1.csv',index = None)
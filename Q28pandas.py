#Q28.Write a program using pandas to read a CSV file and perform basic analysis.

import pandas as pd

#REad csv file 
df = pd.read_csv('data.csv')

#display data 
print ("full data: \n, df")

#basic  analysis 
print("\n Basic Analysis :")
print("First 5 rows:\n", df.haed())
print("\ncolumn  means :", df.columns)
print("\ncolumn names:", df.describe())
print("\nMean values:\n", df.mean(numeric_only=True))

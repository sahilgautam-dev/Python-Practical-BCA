#Q29. filter and group dat using pandaas 

import pandas as pd
#read csv file 
df = pd.read_csv("Q29pand.csv")
print("original Data:\n", df)

#filtering 
print("\n Filtered Data (marks > 80)")
filtered = df[df["maarks"]>80]
print(filtered)

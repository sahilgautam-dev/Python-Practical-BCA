#Q31. Write a program combining numpy, pandas, and matplotlib for simple data analysis.

# Q31: NumPy + Pandas + Matplotlib (Simple Data Analysis)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -------- NumPy: Create Data --------
data = np.array([10, 20, 30, 40, 50])

# -------- Pandas: Create DataFrame --------
df = pd.DataFrame({
    "Values": data
})

print("Data:\n", df)

# -------- Analysis --------
print("\nMean:", df["Values"].mean())
print("Max:", df["Values"].max())
print("Min:", df["Values"].min())

# -------- Matplotlib: Plot Graph --------
plt.plot(df["Values"])
plt.title("Line Graph of Data")
plt.xlabel("Index")
plt.ylabel("Values")

plt.show()
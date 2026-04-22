#Q30. Write a program using matplotlib to plot line and bar graphs
import matplotlib.pyplot as plt

#sample data 
x = [1,2,3,4,5]
y = [10,20,15,25,30]

#line graph 
plt.figure()

plt.pilot(x,y)
plt.title("Line Graphh")
plt.xlabel("x values")
plt.ylabel("y values")

plt.show()

#bar graph 
plt.figure()
plt.bar(x,y)
plt.title("Bar Graph")
plt.xlabel("x values ")
plt.ylabel("y values ")

plt.show()

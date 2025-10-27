#graph
import matplotlib.pyplot as plt
import numpy as np

x = np.array([2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018,2019, 2020])
y = np.array([21, 19, 24, 17, 16, 25, 24, 22, 21 ,21])

print(np.mean(y))
print(np.median(y))
print(np.std(y))

plt.xlabel("courses")
plt.ylabel("grades")

plt.plot(x, y)
plt.show()

#piechart
mylabels = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10"]
plt.pie(y, labels=mylabels)
plt.show()

#scatter plot

plt.scatter(x,y)
plt.show()
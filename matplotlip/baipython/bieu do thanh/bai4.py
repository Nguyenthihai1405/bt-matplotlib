import matplotlib.pyplot as plt
import numpy as np

divisions = ["Div -A","Div -B","Div -C","Div-D","Div -E"]
boys_average_marks = [68,67,77,61,70]
Girls_average_marks = [68,67,77,61,70]

index = np.arange(5)
width = 0.30

plt.bar(index,boys_average_marks , width, color='blue',label='boys marks')
plt.bar(index+width,Girls_average_marks ,width, color='red',label='Girl marks',bottom=boys_average_marks)

plt.title("Vertically Stacked bar Graphs")
plt.xlabel("divisions")
plt.ylabel("Marks")
plt.plt.xticks(index, divisions)

plt.legend(loc='best')
plt.show()
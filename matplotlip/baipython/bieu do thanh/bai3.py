import matplotlib.pyplot as plt
import numpy as np

divisions = ["Div -A","Div -B","Div -C","Div-D","Div -E"]
division_average_marks = [70, 82, 73, 65, 68]
boy_average_marks = [68,67,77,61,70]

index = np.arange(5)
width = 0.30

plt.bar(index,divisions, division_average_marks, width, color='green',label='Division Marks')
plt.bar(index+width, boy_average_marks,width, color='blue',label='boy marks')

plt.ylabel("Marks")
plt.xlabel("divisions")
plt.plt.xticks(index+ width/2, divisions)

plt.legend(loc='best')
plt.show()
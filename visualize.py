import csv
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

reader = csv.reader(open('./data.csv'))
data = np.array(list(reader))
stars = [a[0] for a in data]
countStars = Counter(stars)
print(countStars)

count = {}
for i in [1,2,3,4,5]:
    count[str(i)] = countStars[str(i)]
print(count)

chart = plt.bar(count.keys(), count.values())
for i,col in enumerate(chart):
    h = col.get_height()
    plt.text(col.get_x()+col.get_width()/2, h+0.05, list(count.values())[i], ha="center")
plt.show()


import codecademylib
from matplotlib import pyplot as plt
import numpy as np

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
As = [6, 3, 4, 3, 5]
Bs = [8, 12, 8, 9, 10]
Cs = [13, 12, 15, 13, 14]
Ds = [2, 3, 3, 2, 1]
Fs = [1, 0, 0, 3, 0]

x = range(5)

c_bottom = np.add(As, Bs)
d_bottom = np.add(c_bottom,Cs)
f_bottom = np.add(d_bottom,Ds)
#create d_bottom and f_bottom here

#create your plot here
plt.figure(figsize = (10,8))
ax = plt.subplot()
ax.bar(range(len(c_bottom)),As)
ax.bar(range(len(c_bottom)),Bs,bottom = As)
ax.bar(range(len(c_bottom)),Cs,bottom = Bs)
ax.bar(range(len(c_bottom)),Ds,bottom = Cs)
ax.bar(range(len(c_bottom)),Fs,bottom = Ds)
ax.set_xticks(range(len(unit_topics)))
ax.set_xticklabels(unit_topics)
ax.set_title("Grade distribution")
ax.set_ylabel("Number of students")
ax.set_xlabel("Unit")
plt.show()
plt.savefig("my_stacked_bar.png")
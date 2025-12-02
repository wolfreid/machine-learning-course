import codecademylib
from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]

t = 2 # There are two sets of data: A and B
w = 0.8 # We generally want bars to be 0.8
n = 1 # A is first set of data

def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]
# Make your chart here

school_a_x = create_x(t,w,1,len(middle_school_a))

school_b_x = create_x(t,1.6,1,len(middle_school_b))

plt.figure(figsize=(10,8))
ax = plt.subplot()

ax.bar(school_a_x,middle_school_a)
ax.bar(school_b_x,middle_school_b)
middle_x = [ (a + b) / 2.0 for a, b in zip(school_a_x, school_b_x)]
ax.set_xticks(middle_x)
ax.set_xticklabels(unit_topics)

ax.legend(("Middle School A", "Middle School B"))
ax.set_title("Test Averages on Different Units")
ax.set_xlabel("Unit")
ax.set_ylabel("Test Average")
plt.show()
plt.savefig("my_side_by_side.png")
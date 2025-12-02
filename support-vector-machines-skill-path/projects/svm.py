import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from svm_visualization import draw_boundary
from players import aaron_judge, jose_altuve, david_ortiz

print(aaron_judge.columns)
fig, ax = plt.subplots()
print(aaron_judge.description.unique())

print(aaron_judge.type.unique())

aaron_judge.type = aaron_judge.type.map({'S':1,'B':2,'X':3})
print(aaron_judge.type.unique())

print(aaron_judge.plate_x.head())
print(aaron_judge.plate_z.head())

print(aaron_judge.shape)
aaron_judge = aaron_judge.dropna(subset= ['plate_x','plate_z','type']) 
print(aaron_judge.shape)
# plt.cm.coolwarm(cmap = 'red')
fig = plt.figure(figsize =(8,10))
ax = fig.add_subplot(111)
ax.scatter(aaron_judge.plate_x,aaron_judge.plate_z,c = aaron_judge.type,cmap=plt.cm.coolwarm,alpha = 0.25)

x_train,x_valid = train_test_split(aaron_judge,random_state = 1)

classifier = SVC(kernel = 'rbf',gamma = 10, C=10)
classifier.fit(x_train[['plate_x','plate_z']],x_train['type'])
# a
draw_boundary(ax,classifier)
plt.show()

_score  = classifier.score(x_valid[['plate_x','plate_z']],x_valid['type'])
print(_score)


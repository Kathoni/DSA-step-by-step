import numpy as np

#generate random height and weight data for 1000 people
height = np.round(np.random.normal(1.75,0.20,1000),2)
weight = np.round(np.random.normal(60.04,15,1000),2)
np_gym = np.column_stack((height,weight))

print(np_gym[100:110])

print(np_gym[0][0])
print(np_gym[0][1])
print(np_gym[1][0])
print(np_gym[1][1])
print(np_gym[2][0])
print(np_gym[2][1])
print(np_gym[3][0])
print(np_gym[3][1])
print(np_gym[4][0])
print(np_gym[4][1])

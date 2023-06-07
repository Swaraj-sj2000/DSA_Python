import numpy as np
import matplotlib.pyplot as plt
h1=15
l1=10
l2=10
m1=5
x=np.arange(-5,5,0.01)
y=h1-m1*np.cos(np.pi/10*x)
plt.plot(x,y)


theta2=np.arccos((np.square(x)+np.square(y)-l1**2-l2**2)/(2*l1*l2))
theta1=np.arctan(x/y)-np.arctan(l2*np.sin(theta2)/(l1+l2*np.cos(theta2)))


x1=l1*np.sin(np.pi/2+theta1)+l2*np.sin(np.pi/2+theta1+theta2)
y1=l1*np.cos(np.pi/2+theta1)+l2*np.cos(np.pi/2+theta1+theta2)
plt.plot(x1,y1)
# plt.show()
# print(list(zip(np.degrees(theta1).astype('int32'),np.degrees(theta2).astype('int32'))))
print(np.unique(np.degrees(theta1).astype('int32')*-1))
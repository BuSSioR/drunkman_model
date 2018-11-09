import numpy as np
import matplotlib.pyplot as plt
import time
def variationv2 (steps,number_of_drunk_mans):
    location_array=np.random.randint(0,2,size=(steps,number_of_drunk_mans))
    steps=np.where(location_array>0,1,-1)
    return steps.sum(axis=0).std()
variations=[]
xaxis=[]
t=time.time()
for step in range(1000,10000,10):
    xaxis.append(step)
    variations.append(variationv2(step,100))
print(abs(t-time.time()))
plt.loglog(xaxis,variations)
plt.show()
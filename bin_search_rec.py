import random as rm
import numpy as np
import matplotlib.pyplot as plt
import time
from sklearn import linear_model as lr

def recBinSearch(arr, ele, high, low):
    if low > high:
        #print("Element not found")
        return

    mid = (high + low) // 2
    if arr[mid] == ele:
        #print("Element found at", mid)
        return
    elif arr[mid] > ele:
        high = mid - 1
    else:
        low = mid + 1

    recBinSearch(arr, ele, high, low)

ranges = 10
yplot = []
xplot = []
while(ranges <= 1000):
    arr = [rm.randint(0, ranges) for _ in range(0, ranges, 1)]
    ele = arr[len(arr)-1]
    st1 = time.process_time()
    recBinSearch(arr, ele, len(arr)-1, 0)
    tt = time.process_time() - st1
    yplot.append(tt)
    xplot.append(ranges)
    ranges = ranges + 10

#xp1 = np.array(xplot)
#yp1 = np.array(yplot)
#reg1 = lr.LinearRegression()
#reg1.fit(xp1.reshape(-1, 1), yplot)
#plt.plot(xp1, reg1.predict(xp1.reshape(-1, 1)), color="blue")
plt.scatter(xplot, yplot, color="red", marker="+")
plt.show()

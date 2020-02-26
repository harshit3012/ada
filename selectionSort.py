import random
import time as tm
import os
def selectionSort(arr):
	for i in range(len(arr)-1):
		pos = i
		for j in range(i+1, len(arr)):
			if arr[j] < arr[i]:
				pos = j
		arr[i], arr[pos] = arr[pos], arr[i]
    
current_n = 10
times = []
for _ in range(1500):
	arr = [random.randint(1, current_n) for i in range(current_n)]
	start_time = tm.time()
	selectionSort(arr)
	end_time = tm.time()	
	times.append((current_n, (end_time-start_time)))
	current_n += 70
print(times)

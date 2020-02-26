def modified_bubble_sort(a, n):
    for j in range(1, n):
        flag = False
        for i in range(0, n-j):
            if a[i] > a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
                flag = True
        if flag == False:
            break
          
test_arr = [1, 2, 3, 5, 7, 9, 10]
modified_bubble_sort(test_arr, len(test_arr))
print(test_arr)

test_arr = [11,2, 4, 7, 6 1, 9, 3, 10, 5, 0]
modified_bubble_sort(test_arr, len(test_arr))
print(test_arr)

def bubbleSort(arr):
        # code here
    for i in range(len(arr)):
        is_swap = 0
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                is_swap = 1
        if is_swap == 0:
            break
                
    print(arr)

bubbleSort([1,2,3,4,5])
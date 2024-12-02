def bubbleSort(arr):
        # code here
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                
    print(arr)

bubbleSort([1,64,34,25,12,22,11,90])
def calculate(arr):
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            pass
        else:
            return False
    return True

print(calculate([1,2,3,4]))
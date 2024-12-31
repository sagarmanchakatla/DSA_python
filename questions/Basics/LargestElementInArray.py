def calculate(arr):
    lar = 0
    for i in range(len(arr)):
        if arr[i] > lar:
            lar = arr[i] 
    print(lar)

calculate([1,2,3,4,5,55])
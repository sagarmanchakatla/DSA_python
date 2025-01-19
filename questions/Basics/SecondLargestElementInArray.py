def calculate(arr):
    if len(arr) < 2:
        return -1

    lar = 0
    sec = 0

    for i in range(len(arr)):
        if arr[i] > lar:
            sec = lar
            lar = arr[i]
        else:
            if arr[i] > sec and arr[i] < lar:
                sec = arr[i]
    print(sec)
    print(lar)

calculate([10, 10, 10])
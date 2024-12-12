def twoPointer(nums):
    L, C, H = 0, 0, len(nums)-1

    while C < H:
        if nums[C] == 0:
            nums[L], nums[C] = nums[C], nums[L]
            L += 1
            C += 1
        elif nums[C] == 2:
            nums[C], nums[H] = nums[H], nums[C]
        else:
            C += 1

    print(nums)

twoPointer([1,0,2])
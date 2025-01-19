def calculate(nums,k):
    n = len(nums)
    k %= n

    def rotate(start,end):
        while start < end:
            nums[start] , nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        
    rotate(0,n-1)
    rotate(0, k-1)
    rotate(k,n-1)
    print(nums)


def approch2(nums,k):
    k %= len(nums)

    nums[:] = nums[-k:] + nums[:-k]

    print(nums)



calculate([1,2,3,4,5,6,7],3)
approch2([1,2,3,4,5,6,7],3)

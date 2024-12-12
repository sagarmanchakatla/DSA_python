def calculate(nums):
    c = None

    if int(nums[len(nums)-1]) % 2 != 0:
        return nums


    for i in nums:
        if int(i)%2 != 0:
            c = max(c, int(i)) if c is not None else int(i)
    
    return str(c) if c is not None else ""

def calculate1(num):
    for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i + 1]
    return ''


print(10133890 % 2 == 0)
print(calculate1("10133890"))
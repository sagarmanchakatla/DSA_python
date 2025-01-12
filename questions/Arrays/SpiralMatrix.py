def solution(nums):
    n = len(nums)
    m = len(nums[0])
    top = 0
    bottom = n - 1
    left = 0
    right = m - 1
    ans = []

    while top <= bottom and left <= right:
        for i in range(left, right+1):
            ans.append(nums[top][i])
        top += 1

        for i in range(top, bottom+1):
            ans.append(nums[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left-1, -1):
                ans.append(nums[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top-1, -1):
                ans.append(nums[i][left])
            left += 1

    print(ans)

solution([[1,2,3],
          [4,5,6],
          [7,8,9]])
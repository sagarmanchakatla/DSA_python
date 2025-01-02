class Solution:
    def findFirst(self, nums, target):
        n = len(nums)
        first = -1
        low, high = 0, n-1

        while low <= high:
            mid = (low + high) //2
            if nums[mid] == target:
                first = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return first
    
    def findLast(self, nums, target):
        n = len(nums)
        last = -1
        low, high = 0, n-1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                last = mid
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return last
        
    def countFreq(self, arr, target):
        first = self.findFirst(arr, target)
        if first == -1:
            return 0
        second = self.findLast(arr, target)
        
        return second - first + 1

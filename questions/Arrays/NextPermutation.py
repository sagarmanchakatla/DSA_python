def permute(nums):
        result = []
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = permute(nums)
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        return result            

def nextPermutation(nums):
    # Generate all permutations
    permutations = permute(nums)

    # Sort permutations lexicographically
    permutations.sort()

    # Find the index of the current permutation
    for i in range(len(permutations)):
        if permutations[i] == nums:
            # Return the next permutation or the first if at the end
            next_index = (i + 1) % len(permutations)
            return permutations[next_index]
        
print('Next permutation is ',nextPermutation([2,1,5,4,3,0,0]))



def optimalSolution(nums):
    n = len(nums)
    index = -1

    for i in range(n-2, -1, -1):
        if nums[i] < nums[i+1]:
            index= i
            break
    
    if index == -1:
        nums.reverse()
        return nums

    for i in range(n-1, index-1, -1):
        if nums[i] > nums[index]:
            nums[i], nums[index] = nums[index], nums[i]
            break
    
    nums[index+1: ] = reversed(nums[index+1: ])
    return nums
    
print(optimalSolution([2,1,5,4,3,0,0]))
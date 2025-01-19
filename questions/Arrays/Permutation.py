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
        
result = permute([2,1,5,3,4,0,0])
result.sort()
print(result[result.index([2,1,5,4,3,0,0])+1])
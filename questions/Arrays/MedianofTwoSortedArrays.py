def findMedianSortedArrays( nums1, nums2):
    merged = []
    i, j = 0, 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    
    while i < len(nums1):
        merged.append(nums1[i])
        i += 1
    while j < len(nums2):
        merged.append(nums2[j])
        j += 1

    if len(merged) % 2 != 0:
        center = len(merged) // 2
        print(merged[center])
    else:
        center = len(merged) // 2
        pre = center -1
        print((merged[pre] + merged[center]) / 2)
    
    print(merged)

findMedianSortedArrays([1,2],[3,4])
def brute(nums1, nums2):
    len1, len2 = len(nums1), len(nums2)
    res = 0

    for n1 in nums1:
        for n2 in nums2:
            res ^= n1^n2

    return res



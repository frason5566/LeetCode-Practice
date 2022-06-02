def intersection(nums1, nums2):

    return list(set(nums1) & set(nums2))
def I(nums1,nums2):
    res = []
    for item in nums1:
        if item in nums2 and item not in res:
            res.append(item)
    return res

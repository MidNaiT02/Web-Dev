def array_count9(nums):
    counts = 0
    for i in nums:
        if i == 9:
            counts += 1
    return counts
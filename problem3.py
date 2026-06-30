def rearrange_by_frequency(nums: list[int]):
    chast = {}
    for x in nums:
        chast[x] = chast.get(x, 0) + 1

    return sorted(nums, key=lambda x: (-chast[x], x))

print(rearrange_by_frequency([4, 5, 6, 5, 4, 3, 4]))

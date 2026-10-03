def average_followers_via_median(nums: list[int]) -> float | None:
    if nums == []:
        return None
    nums.sort()
    count = len(nums)
    if count%2 == 1:
        median_calc = (len(nums)+1)//2
        median = nums[median_calc-1]
        return  median
    elif count%2 == 0:
        n1:int|float = len(nums)//2
        n2:int|float = (len(nums)+1)//2 + 1
        median = (nums[n1-1] + nums[n2-1])/2
        return median
value = average_followers_via_median([3, 1, 2, 4,5])
print(value)

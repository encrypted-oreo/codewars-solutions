# https://www.codewars.com/kata/5526fc09a1bbd946250002dc

def find_outlier(nums):
    nums.sort(key=lambda n: n & 1)
    if nums[0] % 2 != nums[1] % 2:
        return nums[0]
    return nums[-1]
    

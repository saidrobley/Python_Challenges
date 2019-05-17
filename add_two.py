'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
class AddTwo:
    def two_sum(self, nums, target):
        dic = {}
        for i, val in enumerate(nums):

            result = target - val  # 7

            if result in dic:
                return [dic[result], i]

            dic[val] = i

class TwoSum(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                return [nums_dict[nums[i]], i]
            else:
                nums_dict[target - nums[i]] = i



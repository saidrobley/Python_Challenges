class RemoveDuplicatesSortedArrays:
    def remove_duplicates(self, nums):
        if nums == []:
            return 0
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)


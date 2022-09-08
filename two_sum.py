class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums.sort()

        low = 0
        high = len(nums) - 1
        print(nums[low] + nums[high])
        print(low)
        print(high)

        while low < high:
            if nums[low] + nums[high] == target:

                return [low, high]
            elif nums[low] + nums[high] > target:
                high -= 1
            else:
                low += 1
        
        return []
    

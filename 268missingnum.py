class Solution(object):
	def missingNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""

		if 0 not in nums:
			return 0
		nums.sort()
		current = nums[0]
		for num in nums:
			if current + 1 in nums:
				current += 1
			else:
				return current + 1

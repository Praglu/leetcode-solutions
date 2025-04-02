'''
Runtime 3338 ms | Beats 5.51% :brother-ewww:
Memory 18.36 MB | Beats 87.30% :feels-good:
'''

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        results = []
        if len(nums) <= 1:
            return 0
        for index in range(len(nums)):
            counter = index + 1
            while counter < len(nums):
                if nums[index] + nums[counter] == target:
                    results.append(index)
                    results.append(counter)
                counter += 1
        return results

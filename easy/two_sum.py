class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, val in enumerate(nums):
            for index2, val2 in enumerate(nums):
                if index == index2:
                    continue
                elif val+val2 == target:
                    return [index, index2]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, number in enumerate(nums):
            rem = target - number

            if rem in seen:
                return [seen[rem], index]

            seen[number] = index
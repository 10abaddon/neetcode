class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}

        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in store:
                return [store[needed], i]

            store[nums[i]] = i
        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_dict = {}

        for i in set(nums):
            count = 0
            for j in range(len(nums)):
                if i == nums[j]:
                    count += 1
            sorted_dict[i] = count

        sorted_list = sorted(sorted_dict, key=lambda x: sorted_dict[x], reverse=True)[:k]
        return sorted_list
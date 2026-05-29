class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_n = Counter(nums)
        
        for _, count in count_n.items():
            if count > 1:
                return True
        return False

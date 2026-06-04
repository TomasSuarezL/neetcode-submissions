class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = -1

        if len(nums) == 0:
            return idx
        start_idx = 0
        if nums[start_idx] == target:
            return start_idx
        end_idx = len(nums)-1
        if nums[end_idx] == target:
            return end_idx
        search_idx = math.floor((end_idx - start_idx)/2)
        while end_idx - start_idx > 1:
            print(idx, search_idx, start_idx, end_idx)
            if nums[search_idx] == target:
                idx = search_idx
                break
            elif nums[search_idx] > target:
                end_idx = search_idx
                search_idx = math.floor((end_idx - start_idx)/2) + start_idx
            else:
                start_idx = search_idx
                search_idx = math.floor((end_idx - start_idx)/2) + start_idx
        return idx

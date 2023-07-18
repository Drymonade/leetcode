class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        p1 = 0
        p2 = 0

        while p2 < len(nums):
            if nums[p1] != nums[p2]:
                if p2 - p1 > 2:
                    nums[:] = nums[:p1] + nums[p2 - 2:]
                    p2 = p1
                else:
                    p1 = p2
            else:
                p2 += 1

        if p2 - p1 > 2:
            nums[:] = nums[:p1] + nums[p2 - 2:]
                    
        return len(nums)

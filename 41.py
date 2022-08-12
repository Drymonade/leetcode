class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        _min = min(nums)
        _max = max(nums)
        _len = len(nums)
        
        if _min > 1 or _max < 0:
            return 1

        bits = 0
        for i in nums:
            if i > 0 and i <= _len:
                bits |= 1 << (i - 1)

        return ((bin(bits))[:1:-1] + '0').index('0') + 1

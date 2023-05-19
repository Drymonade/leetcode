class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        _l = len(nums)

        _k = k % _l

        nums[:] = nums[(_l -_k):] + nums[:(_l - _k)]

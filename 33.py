class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def _search(nums, target):
            _l = len(nums)

            left = 0

            right = _l

            test = (left + right) // 2

            while nums[test] != target:
                if nums[test] > target:
                    right = test
                else:
                    left = test

                _test = (left + right) // 2

                if _test != test:
                    test = _test
                else:
                    if nums[test] == target:
                        return test
                    return -1
            return test

        if nums[-1] >= nums[0]:
            return _search(nums, target)
        else:

            _l = len(nums)

            left = 0

            right = _l - 1

            test = (left + right) // 2

            while nums[test] < nums[test + 1]:
                if nums[test] > nums[-1]:
                    left = test
                else:
                    right = test

                _test = (left + right) // 2

                if _test != test:
                    test = _test
                else:
                    break


            ll = _search(nums[:test + 1], target)
            rr = _search(nums[test:], target)

            if ll == -1 and rr == -1:
                return -1
            else:
                if ll == -1:
                    return test + rr
                else:
                    return ll

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def mergeTwo(a, b):
            if a[1] >= b[0]:
                if a[1] >= b[1]:
                    return [a[0], a[1]], True
                else:
                    return [a[0], b[1]], True
            else:
                return [a, b], False

        intervals = sorted(intervals, key=lambda x: x[0])
        result = [intervals[0]]
        pointer = 1
        while pointer < len(intervals):
            _result, merged = mergeTwo(result[-1], intervals[pointer])
            if merged:
                result[-1] = _result
            else:
                result[-1] = _result[0]
                result.append(_result[1])
            pointer += 1
        return result

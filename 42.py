class Solution:
    def trap(self, heights: List[int]) -> int:
        result = 0
        m = max(heights)
        max_index = 0
        for idx, value in enumerate(heights):
            if value == m:
                max_index = idx

        i = 0
        while i < max_index:
            for j in range(i + 1, max_index + 1):
                if heights[j] >= heights[i]:
                    for k in range(i + 1, j):
                        result += heights[i] - heights[k]
                    i = j
                    break

        i = len(heights) - 1

        while i > max_index:
            for j in range(i - 1, max_index - 1, -1):
                if heights[j] >= heights[i]:
                    for k in range(i - 1, j, -1):
                        result += heights[i] - heights[k]
                    i = j
                    break
        return result

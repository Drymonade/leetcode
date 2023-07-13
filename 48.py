class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = list(map(lambda x: x[::-1], map(lambda x: list(x), zip(*matrix))))

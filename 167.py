class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        le = len(numbers)

        for i in range(le):
            new_target = target - numbers[i]
            t1 = 0
            t2 = le

            while True:
                if t2 - t1 == 1:
                    break
                t = (t2 + t1) // 2
                if numbers[t] == new_target:
                    if t != i:
                        return sorted([t+1, i+1])
                    else:
                        break
                elif numbers[t] > new_target:
                    t2 = t
                else:
                    t1 = t

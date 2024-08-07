"""
# 167 two sum ii input array is sorted
"""
class Solution1:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1
        while(start < end):
            sum_two = numbers[start] + numbers[end]
            if sum_two > target:
                end -= 1
            elif sum_two < target:
                start += 1
            else:
                return [start+1, end+1]

class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)
        d = {}
        for i, x in enumerate(numbers):
            d[x] = i
        for i, x in enumerate(numbers):
            second = target - x
            if second in d:
                if i < d[second]:
                    return [i+1, d[second]+1]
                else:
                    return [d[second]+1, i+1]

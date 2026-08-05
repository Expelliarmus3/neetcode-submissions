class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            n=target-numbers[i]
            if n in numbers:
                return [i+1,numbers.index(n,i+1)+1]

        return []
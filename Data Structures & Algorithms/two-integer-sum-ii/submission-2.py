class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for num in numbers:
        #     if ((target-num) in numbers) and (target-num!=num):
        #         if (target-num)<num:
        #             return [(target-num),num]
        #         else:
        #             return [num,(target-num)]

        # return []

        for i in range(len(numbers)):
            n=target-numbers[i]
            if n in numbers:
                return [i+1,numbers.index(n,i+1)+1]

        return []
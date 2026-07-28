class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        for num in nums:
            if num in frequency_map:
                frequency_map[num] += 1
            else:
                frequency_map[num] = 1
        
        # 2. Sort the unique numbers based on their frequency count in descending order
        # dict.get retrieves the frequency for each unique number
        sorted_numbers = sorted(frequency_map.keys(), key=frequency_map.get, reverse=True)
        
        # 3. Return the first k elements
        return sorted_numbers[:k]
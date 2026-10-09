from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_counts = defaultdict(int)
        counts = []
        ans = []
        for num in nums:
            freq_counts[num] += 1
        
        for num, freq in freq_counts.items():
            pair = (freq, num)
            counts.append(pair)
        
        counts = sorted(counts, reverse=True)
        for i in range(k):
            ans.append(counts[i][1])
        
        return ans
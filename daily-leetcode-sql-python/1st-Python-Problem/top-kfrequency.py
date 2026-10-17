from typing import List
import heapq
 
 
class LogAnalyzer:
    def topKFrequent(self, ips: List[str], k: int) -> List[str]:
        """
        Finds the k most frequent IP addresses from the logs.
        """
        freq = {}
        for num in ips:
            freq[num] = freq.get(num, 0) + 1
                
        heap = []
        for num, count in freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, num))
            else:
                if count > heap[0][0]:
                    heapq.heapreplace(heap, (count, num))
                
        return [num for _, num in heap]         

class Solution:
    
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        pass
      

# --- Local Testing ---
if __name__ == "__main__":
    analyzer = LogAnalyzer()
    
    logs = [
        "192.168.1.1", "10.0.0.2", "192.168.1.1", 
        "10.0.0.2", "192.168.1.1", "172.16.0.1"
    ]
    k = 2
    
    result = analyzer.topKFrequent(logs, k)
    print(f"Top {k} IPs: {result}") 
    # Expected Output: ['192.168.1.1', '10.0.0.2'] (Order doesn't matter)
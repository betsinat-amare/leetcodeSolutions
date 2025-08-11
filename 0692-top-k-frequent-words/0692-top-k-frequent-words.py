class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        heap = [(-freq, word) for word, freq in counter.items()]
        heapq.heapify(heap)  

        result = []
        for _ in range(k):
            freq, word = heapq.heappop(heap)
            result.append(word)
        return result

            
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        counter = Counter(words)
        sorted_words = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
        result = [word for word, _ in sorted_words[:k]]
        return result

        
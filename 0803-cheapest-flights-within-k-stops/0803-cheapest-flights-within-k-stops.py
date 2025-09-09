class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        dist = [float("inf")] * n
        dist[src] = 0

        for _ in range(k + 1):
            tmp = dist[:]
            for u, v, w in flights:
                if dist[u] != float("inf"):
                    tmp[v] = min(tmp[v], dist[u] + w)
            dist = tmp

        return -1 if dist[dst] == float("inf") else dist[dst]

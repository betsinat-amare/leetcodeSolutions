import collections
import heapq

class Twitter:
    def __init__(self):
        self.time = 0 
        self.tweets = collections.defaultdict(list)  
        self.followees = collections.defaultdict(set) 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followees[followerId].discard(followeeId)

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []
        users = self.followees[userId] | {userId}
        for uid in users:
            tweets = self.tweets[uid]
            if tweets:
                idx = len(tweets) - 1
                time_stamp, tid = tweets[idx]
                heapq.heappush(heap, (-time_stamp, uid, idx, tid))

        feed = []
        while heap and len(feed) < 10:
            neg_time, uid, idx, tid = heapq.heappop(heap)
            feed.append(tid)
            if idx > 0:
                prev_time, prev_tid = self.tweets[uid][idx - 1]
                heapq.heappush(heap, (-prev_time, uid, idx - 1, prev_tid))
        return feed

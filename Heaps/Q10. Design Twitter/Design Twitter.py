import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)      # userId -> list of (time, tweetId)
        self.following = defaultdict(set)    # userId -> set of followees

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> list:
        heap = []
        
        # User follows themselves
        self.following[userId].add(userId)

        for followee in self.following[userId]:
            if followee in self.tweets:
                for time, tweetId in self.tweets[followee][-10:]:
                    heapq.heappush(heap, (-time, tweetId))

        res = []
        while heap and len(res) < 10:
            res.append(heapq.heappop(heap)[1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.following[followerId].discard(followeeId)

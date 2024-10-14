class Twitter:

    def __init__(self):
        self.user_net:Dict[int, Set[int]] = dict()
        # user_id against rank, tweetid
        self.user_tweets:Dict[int, Deque[Tuple[int, int]]] = dict()
        self.tweet = 0

    def create_user(self, user_id):
        if user_id not in self.user_net:
            self.user_net[user_id] = {user_id}
        if user_id not in self.user_tweets:
            self.user_tweets[user_id] = deque()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.create_user(userId)
        self.user_tweets[userId].appendleft((self.tweet, tweetId))
        self.tweet -= 1

        
    def getNewsFeed(self, userId: int) -> List[int]:
        sol = []
        tweet_heap = []
        self.create_user(userId)
        for following_id in self.user_net[userId]:
            for tweets in self.user_tweets[following_id]:
                heapq.heappush(tweet_heap, tweets)
        
        count = 10
        while(count > 0 and tweet_heap):
            sol.append(heapq.heappop(tweet_heap)[1])
            count -= 1

        return sol

    def follow(self, followerId: int, followeeId: int) -> None:
        self.create_user(followerId)
        self.create_user(followeeId)
        self.user_net[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.create_user(followerId)
        self.create_user(followeeId)
        if followeeId in self.user_net[followerId]:
            self.user_net[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
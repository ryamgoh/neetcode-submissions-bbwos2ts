class Twitter:

    def __init__(self):
        # tweets should contain the timestamp i.e. (tweet_id, time_stamp)
        # K: user_id V: [(tweet_id, time_stamp), (tweet_id_2, time_stamp_2)], where time_stamp < time_stamp_2
        self.tweets_by_user = defaultdict(list)
        self.following_by_user = defaultdict(list)
        self.time_stamp = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets_by_user[userId].append((tweetId, self.time_stamp))
        self.time_stamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # first we want to get all the following including user_id
        # so essentially, we want to merge all the user_ids' lists
        # which will we will order via time_stamp
        all_users = []
        all_users.append(userId)
        all_users += self.following_by_user[userId]
        # print(all_users)
        # we should have all users incl current
        # now we should grab all the tweets in that list
        all_tweets = []
        for user in all_users:
            all_tweets += self.tweets_by_user[user]

        # print(all_tweets)
        
        sorted_tweets = [x[0] for x in sorted(all_tweets, key=lambda x: x[1], reverse=True)]
        print(sorted_tweets)
        if len(sorted_tweets) > 10:
            return sorted_tweets[:10]
        return sorted_tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return
        elif followeeId in self.following_by_user[followerId]:
            return
        self.following_by_user[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.following_by_user[followerId]:
            return
        self.following_by_user[followerId].remove(followeeId)
        

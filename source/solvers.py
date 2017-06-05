class Solver:
    def __init__(self, tweetlist, tested_news):
        self.is_genuine = True
        self.tweet_list = tweetlist
        self.tested_news = tested_news
        self.news_count = 0

    def determine_genuity(self):
        tweets_in_one_string = ""
        for tweet in self.tweet_list:
            # print("TWEET:")
            # print(tweet)
            tweets_in_one_string += tweet

        self.news_count = \
            tweets_in_one_string.upper().count(self.tested_news.upper())
        # print(news_count)
        if self.news_count < 5:
            print("This is fake :(, presumably..")
        else:
            print("This is presumably true")

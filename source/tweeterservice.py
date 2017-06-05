import tweepy


class TwitterAPIService:
    def __init__(self, search_phrase):
        self.consumer_key =\
            'oneQRaDMOvE1Qq3AGVcXQV71d'
        self.consumer_secret =\
            'WF5LjoBZCwF7NJF7H6fxHwy6cy1Z6wBGKhbEMSrZEWxAvw0B2L'
        self.access_token =\
            '870650907528237058-Z9LYo2hAdTuIzAWU1DBjU7jET1LSuTn'
        self.access_token_secret =\
            'qHEuwWNzvMQKVtYKUckw1mfDZxD6nJwM7dFlwGs96CNst'

        self.search_phrase = search_phrase
        self.tweet_list = []

        # it will be initialized in initialize_api() method
        self.api = None

        self.initialize_api()

    def initialize_api(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)

        self.api = tweepy.API(auth)

    def search_tweets_and_save(self):
        max_tweets = 1000
        # print(self.search_phrase)
        search_results = tweepy.Cursor(self.api.search,
                                       q=self.search_phrase,
                                       since="2017-01-01",).items(max_tweets)
        for result in search_results:
            tweet_string = Tweet(result).get_text_of_tweet()
            self.tweet_list.append(tweet_string)

    def get_tweets_list(self):
        return self.tweet_list


class Tweet:
    def __init__(self, result):
        self.tweet = result

    def get_text_of_tweet(self):
        # print(self.tweet)
        return self.tweet.text

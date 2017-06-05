from parsers import StringArgumentParser
from tweeterservice import TwitterAPIService
from solvers import Solver
from articleservice import ArticleAPIService
from articleservice import TextProcessor


def main():
    url = StringArgumentParser().get_users_input()

    ## getting search text from some article...
    title = ArticleAPIService(url).get_title_of_html()
    search_text = TextProcessor(title).get_sentence()
    apiservice = TwitterAPIService(search_text)
    apiservice.search_tweets_and_save()
    Solver(apiservice.get_tweets_list(), search_text).determine_genuity()

if __name__ == '__main__':
    main()

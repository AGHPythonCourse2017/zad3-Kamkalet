from newspaper import Article
from textblob import TextBlob


class ArticleAPIService:
    def __init__(self, url):
        self.url = url
        self.html_title = ""

        self.initialize_article()

    def initialize_article(self):
        article = Article(self.url)
        article.download()
        article.parse()
        print("Checking genuity of the news below:")
        print(article.title)
        self.html_title = article.title

    def get_title_of_html(self):
        return self.html_title


class TextProcessor:
    def __init__(self, title):
        self.news = title

    def get_sentence(self):
        news_text_blob = TextBlob(self.news)
        first_sentence = str(news_text_blob.sentences[0])
        sentence_wo_dot = first_sentence.replace('.', '')
        return sentence_wo_dot

from tweet import Tweet

class Twitter():
    def __init__(self):
        self.tweets = [] # List of tweets

    def timeline(self):
        for t in self.tweets:
            print(t.web_version())

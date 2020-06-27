from tweet import Tweet

class Twitter():
    def __init__(self):
        self.tweets = [] # List of tweets

    def timeline(self):
        for t in self.tweets:
            print(t.web_version())


twitter = Twitter()
print('---Twitter timeline---')
print(f'{len(twitter.tweets)} at the moment.')

USERNAME = '@galileoguzman'

t1 = Tweet('Mi primer tweet!!!  ^_^', USERNAME)
t2 = Tweet('Aprendo @python', USERNAME)
t3 = Tweet('Hola ya vieron como tembló? -_-', USERNAME)

twitter.tweets.append(t1)
twitter.tweets.append(t2)
twitter.tweets.append(t3)

print(f'{len(twitter.tweets)} at the moment.')

texto = input('Qué estas pensando?')
nuevo_tweet = Tweet(texto, USERNAME)

twitter.tweets.append(nuevo_tweet)
print(f'{len(twitter.tweets)} at the moment.')
twitter.timeline()

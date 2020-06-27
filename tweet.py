from datetime import datetime

class Tweet():
    def __init__(self, text, author):
        # Instance variables / properties
        self.text = text
        self.author = author
        # Internal properties
        self.created_at = datetime.now()
        self.likes = 0

    @property
    def published_at(self):
        return self.created_at.strftime("%d %B, %Y")

    def add_like(self):
        self.likes = self.likes + 1

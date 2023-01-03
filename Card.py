from datetime import datetime
import sqlite3

class Card:
    def __init__(self,front, back):
        self.front = front
        self.back  = back
        self.created = datetime.now().strftime("%H:%M:%S") 
        self.last_reviewed = self.created   
        self.connection = sqlite3.connect("cards.db")

    def __repr__(self):
        return f"{self.front} | {self.back}"
    __str__ = __repr__

    def last_viewed(self):
        return self.last_reviewed


    

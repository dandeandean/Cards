import os
from datetime import datetime, timedelta
import sqlite3
class Card:
    def __init__(self,front = '', back = '', current_bin=0, last_viewed = datetime.timestamp(datetime.now())):
        self.front = front
        self.back  = back
        self.last_viewed = datetime.now()  
        self.current_bin = current_bin

    def __repr__(self):
        return f"{self.front} | {self.back}"
    __str__ = __repr__
    
    ## Getters
    def get_front(self): return self.front
    def get_back(self): return self.back
    def get_last_viewed(self): return self.last_viewed
    def get_current_bin(self): return self.current_bin
    
    ## Setters
    def set_current_bin(self,n):
        self.current_bin = n

    def set_last_viewed(self, flot=datetime.timestamp(datetime.now())):
        self.last_viewed = flot
    
    def time_delta(self):
        return datetime.timestamp(datetime.now()) - self.get_last_viewed()
    
    def view(self):
        self.set_last_viewed()
        inp = input(f"{self.front} | ")
        misses = 0
        miss_list = list()
        while (inp.strip().lower() != self.back) and (misses <=3):
            misses +=1 
            miss_list.append(inp.strip().lower())
            print("Try again!")
            inp = input(f"{self.front} | ")
        if misses == 4:
            print(f"The back of the card is {self.back} \nYou said {', '.join(miss_list)}")
    
class Database:
    def __init__(self, name:str="cards.db"):
        self.__name = name
        self.__connection = None
        self.__cursor = None
        self.connect()
        self.create()
        
    def get_curs(self):
        return self.__cursor
    
    def get_con(self):
        return self.__connection
    
    def get_name(self):
        return self.__name
    
    def get_name_stripped(self):
        return self.__name[:-3]
    
    def connect(self):
        self.__connection = sqlite3.connect(self.__name)
        self.__cursor = self.__connection.cursor()
        assert self.get_name() in os.listdir(), "Connection FAILED"
        
    def select(self, col:list , table:str):
        res = self.exe()(f"SELECT {','.join(col)} FROM {table}")
        return res
    
    def create(self, table="cards", cols=["front","back","current_bin","last_viewed"]):
        # This may cause an issue if it's the first time on the app
        try:
            self.exe()(f"CREATE TABLE {table}({', '.join(cols)})")
            print(f"CREATED: TABLE: {table} | {cols} in {self.get_name_stripped()}")
        except:
            print(f"Connected to database at {self.__name}")
            #print(f" TABLE: {table} | [{', '.join(cols)}] in {self.get_name_stripped()}")
        
    def exe(self):
        return self.get_curs().execute
    
    def get_all_cards(self):
        return self.select(["*"],"cards").fetchall()
    
    def push_card(self, card: Card):
        #FIXME
        payload = f"""
        INSERT INTO {self.get_name_stripped()} VALUES
                    ('{card.front}', '{card.back}', {card.get_current_bin()}, '{card.get_last_viewed()}')
                    """
        self.exe()(payload)
        self.get_con().commit()
        
    def delete_db(self):
        assert self.get_name() in os.listdir(), "No Database to delete"
        confirmation = input("Are you sure you want to delete the database? y/n")
        if confirmation == "y":
            os.remove(f"{self.get_name()}")
        
            
    def cards_from_db(self):
        out =list()
        for tup in self.get_all_cards():
            out.append(Card(tup[0],tup[1],tup[2]))
        return out

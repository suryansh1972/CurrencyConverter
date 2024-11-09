import requests
import json
import os

class Money:
    def __init__(self, user, money, rate):
        self._user = user 
        self.money = money
        self.rate = rate
        self.users = list()
        self.save_user_info()

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value

    def save_user_info(self):
        if os.path.exists('user.json') and os.path.getsize('user.json') > 0:
            with open('user.json', 'r') as f:
                self.users = json.load(f)
        
        #If entry already existing in the json file then the entry doesnt get added
        for x in self.users:
            if x["user"] == self.user:
                print(f"Duplicate entry found for {self.user}. Entry not added.")
                return
        #Adding user and saving user in the user.json file
        self.users.append({"user": self.user, "money": self.money, "rate": self.rate})
        with open('user.json', 'w') as f:
            json.dump(self.users, f, indent=4)
        print("User information saved to 'user.json'")

    def load_user_info(self):
        if os.path.exists('user.json') and os.path.getsize('user.json') > 0:
            with open('user.json', 'r') as f:
                self.users = json.load(f)
    @staticmethod        
    def display_all_users():
        with open ('user.json', 'r') as f:
            users = json.load(f)
        if users :
            for user in users:
                    print(f"User: {user['user']}, Money: {user['money']}, Rate: {user['rate']}")
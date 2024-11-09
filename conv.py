import requests
import json
import os
from money import Money

class ConvertCurrency(Money):
    base_url = "https://api.exchangerate-api.com/v4/latest"

    def __init__(self, user, money, rate, currency):
        super().__init__(user, money, rate)
        self.currency = currency

    def conv_curr(self):
        response = requests.get(f"{self.base_url}/{self.rate}")
        data = response.json()
        exchange_rate = data["rates"][self.currency]
        conv = self.money * exchange_rate
        print(f'{self.user} has {self.money} {self.rate}, which is approximately {conv} {self.currency}')
import datetime
import requests
from model import stock_graphs

"""
I want this code to focus on high cohesion and low coupling between components.
This will be done through a statement on each function that must NOT include the word 'and'
"""


class Controller:

    def obtain_values(self, start_at, end_at, symbol, base):
        response = requests.get(f'https://api.exchangeratesapi.io/history?start_at={start_at.strftime("%Y-%m-%d")}&end_at={end_at.strftime("%Y-%m-%d")}&symbols={symbol}&base={base}')
        values = response.json().get("rates", {})
        return(values)

    def generate_graph(self, dates, currencies):
        return(stock_graphs.render_graph(dates, currencies))

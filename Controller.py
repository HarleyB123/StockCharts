import datetime
from plotly.offline import plot
from plotly.graph_objs import Scatter
import requests

"""
I want this code to focus on high cohesion and low coupling between components.
This will be done through a statement on each function that must NOT include the word 'and'
"""


class Controller:

    def obtain_values(self, start_at, end_at, symbol, base):
        response = requests.get(f'https://api.exchangeratesapi.io/history?start_at={start_at.strftime("%Y-%m-%d")}&end_at={end_at.strftime("%Y-%m-%d")}&symbols={symbol}&base={base}')
        values = response.json().get("rates", {})
        return(values)

    # Should the below be in the model?
    def generate_graph(self, dates, currencies):
        return(plot([Scatter(x=dates, y=currencies)], output_type='div'))


# The below will no longer be needed (but shows how the process will work - some will be moved to View.py)
#    dates = [date for date, currencies in sorted(values.items())]
#    currencies = [currencies.get('GBP') for date, currencies in sorted(values.items())]
#    generate_graph(dates, currencies)

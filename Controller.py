import datetime
from plotly.offline import plot
from plotly.graph_objs import Scatter
import requests

"""
I want this code to focus on high cohesion and low coupling between components.
This will be done through a statement on each function that must NOT include the word 'and'
"""


class Controller():
    # Set values - Constants
    end = datetime.datetime.now()
    start = end - datetime.timedelta(days=365)

    # Variables - Want Symbols/Base

    def obtain_values(start_at, end_at):  # Will need to pass through: startdate, enddate, symbol and base
        response = requests.get(f'https://api.exchangeratesapi.io/history?start_at={start_at.strftime("%Y-%m-%d")}&end_at={end_at.strftime("%Y-%m-%d")}&symbols=GBP')
        values = response.json().get("rates", {})
        return(values)

    # Should the below be in the model?
    def generate_graph(dates, currencies):
        return(plot([Scatter(x=dates, y=currencies)], output_type='div'))


# The below will no longer be needed (but shows how the process will work - some will be moved to View.py)
if __name__ == '__main__':
    values = obtain_values(start, end)
    dates = [date for date, currencies in sorted(values.items())]
    currencies = [currencies.get('GBP') for date, currencies in sorted(values.items())]
    generate_graph(dates, currencies)

import datetime
import plotly.graph_objects as go
import requests

"""
I want this code to focus on high cohesion and low coupling between components.
This will be done through a statement on each function that must NOT include the word 'and'
"""

end = datetime.datetime.now()
start = end - datetime.timedelta(days=365)
response = requests.get(f'https://api.exchangeratesapi.io/history?start_at={start.strftime("%Y-%m-%d")}&end_at={end.strftime("%Y-%m-%d")}&symbols=GBP')
values = response.json().get("rates", {})
dates = [date for date, currencies in sorted(values.items())]
currencies = [currencies.get('GBP') for date, currencies in sorted(values.items())]
fig = go.Figure([go.Scatter(x=dates, y=currencies)])
fig.show()

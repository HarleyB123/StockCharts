from pandas.tseries.offsets import BDay
import pandas as pd
import datetime
import plotly.graph_objects as go
import aiohttp
import asyncio
import json

"""
I want this code to focus on high cohesion and low coupling between components - This will be done through a statement on each function that must NOT include the word 'and'
"""

dates = []
exchange_rates = []
urls = []

last = pd.datetime.today().replace(microsecond=0) - BDay(0)

# Clean up the code below further (if possible) :
for day in range(1, 366):
    date = str(last - BDay(day))
    format_date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    date = format_date.strftime('%Y-%m-%d')
    dates.append(date)

for date in dates:
    url = f'https://api.ratesapi.io/api/{date}?symbols=GBP'
    urls.append(url)


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


# Return htmls and do exchange rate in different function
async def main(urls, exchange_rates):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(fetch(session, url))
        htmls = await asyncio.gather(*tasks)
        for html in htmls:
            html = json.loads(html)
            exchange_rate = html['rates']['GBP']
            exchange_rates.append(exchange_rate)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(urls, exchange_rates))
date_objects = [datetime.datetime.strptime(date, '%Y-%m-%d').date() for date in dates]

fig = go.Figure([go.Scatter(x=date_objects, y=exchange_rates)])
fig.show()

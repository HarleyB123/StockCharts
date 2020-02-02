from plotly.offline import plot
from plotly.graph_objs import Scatter


class stock_graphs():
    def __init__(self, dates, currencies):
        self.dates = dates
        self.currencies = currencies

    @classmethod
    def render_graph(self, dates, currencies):
        return(plot([Scatter(x=dates, y=currencies)], output_type='div'))

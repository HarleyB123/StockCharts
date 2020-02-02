from flask import Flask, render_template, request
from flask_cors import CORS
from controller import Controller
import datetime

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/graphs', methods=['POST', 'GET'])
def graph_viewer():
    if request.method == 'POST':
        data = request.json
        symbol = data['symbol']
        base = data['base']
        end = datetime.datetime.now()
        start = end - datetime.timedelta(days=365)
        ApiController = Controller()
        # Will need to do Controller() actions here
        GraphHTML = render_template('reports.html', graph_placeholder=GraphDiv)
    return GraphHTML


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

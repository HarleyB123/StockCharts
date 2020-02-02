from flask import Flask, render_template, request
from flask_cors import CORS
from controller import Controller

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/graphs', methods=['POST', 'GET'])
def graph_viewer():
    if request.method == 'POST':
        data = request.json  # This will be Symbol & Base
        print(data)  # Will have to get Symbol & Base from JSON
        ApiController = Controller()
        # Will need to do Controller() actions here
        GraphHTML = render_template('reports.html', graph_placeholder=GraphDiv)
    return GraphHTML


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

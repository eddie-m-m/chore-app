# Create your flask import
from flask import Flask, request

app = Flask(__name__)


@app.route('/data')
def send_info():
    return {'some': 'info',
            'more': 'info again'}


if __name__ == "__main__":
    app.run(debug=False)

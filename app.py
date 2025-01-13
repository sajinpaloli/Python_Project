from flask import Flask, jsonify, send_file
from flask_cors import CORS
from database import get_data

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return send_file('./index.html')

@app.route('/api/data', methods=['GET'])
def fetch_data():
    data = get_data()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)

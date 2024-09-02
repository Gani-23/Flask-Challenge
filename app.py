import flask
from flask import request, jsonify, render_template

app = flask.Flask(__name__)

@app.route('/')
def home():
    # return render_template('index.html')
    return jsonify({'message': 'Hello, World!'})

# @app.route('/hello', methods=['GET'])
# def hello():
#     return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
    
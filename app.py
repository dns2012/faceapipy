from flask import Flask, request, jsonify
import os

# Init app 
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return jsonify({
        "message"   : "tested on server free tier"
    })

# Run server
if __name__ == '__main__':
    app.run(debug=True)

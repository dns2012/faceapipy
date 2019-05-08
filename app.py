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
    port = int(os.environ.get('PORT', 3000))
    app.run(debug=True, host='0.0.0.0', port=port)

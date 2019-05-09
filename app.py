from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import datetime

UPLOAD_FOLDER = './upload'

# Init app 
app = Flask(__name__, static_folder="upload")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=['GET'])
def hello():
    return jsonify({
        "message"   : "tested on server free tier"
    })


@app.route("/upload", methods=['POST'])
def upload():
    file = request.files['file']
    filename = secure_filename(datetime.datetime.now().replace(microsecond=0).isoformat() + file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return jsonify({
        "message"   : "image uploaded",
        "image"     : request.base_url + "/" + filename
    })


# Run server
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(debug=True, host='0.0.0.0', port=port)

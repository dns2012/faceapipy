from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import datetime
import face_recognition
import pymysql

# Database Connection
database = pymysql.connect(host='localhost',
                             user='root',
                             password='acception',
                             db='faceapps',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# Upload Directory
UPLOAD_FOLDER = './upload'

# Init App 
app = Flask(__name__, static_folder="upload")
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=['GET'])
def hello():
    return jsonify({
        "message"   : "tested on server free tier"
    })


@app.route("/present", methods=['POST'])
def present():
    file = request.files['image']
    filename = secure_filename(datetime.datetime.now().replace(microsecond=0).isoformat() + file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    with database.cursor() as cursor:
        sql = "SELECT * FROM user" 
        cursor.execute(sql)
        sql_results = cursor.fetchall()

    for data in sql_results:

        sample_picture = face_recognition.load_image_file("./sample_image/" + data["sample_image"])
        sample_picture_encoding = face_recognition.face_encodings(sample_picture)[0]
        
        unknown_picture = face_recognition.load_image_file("./upload/" + filename)
        unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

        results = face_recognition.compare_faces([sample_picture_encoding], unknown_face_encoding, 0.4)
        distance = face_recognition.face_distance([sample_picture_encoding], unknown_face_encoding)
        
        print(results)
        print(distance)

        if True in results:
            will_distanced = 1 - distance[0]
            distanced = int(will_distanced * 100)
            profile = data
            break
        else: 
            distanced = 0
            profile = ""

    return jsonify({
        "Distance"  : distanced,
        "Profile" : profile
    })



# Run Server
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(debug=True, host='0.0.0.0', port=port)

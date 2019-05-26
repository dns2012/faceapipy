from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import datetime
import face_recognition
import pymysql
import shutil
from PIL import Image

# Database Connection
database = pymysql.connect(host='localhost',
                             user='root',
                             password='Php7.0Native',
                             db='faceapps',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# Upload Directory
UPLOAD_FOLDER = './upload'
UPLOAD_FOLDER_SAMPLE = './sample_image'

# Init App 
app = Flask(__name__, static_folder="upload")
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_FOLDER_SAMPLE'] = UPLOAD_FOLDER_SAMPLE

@app.route("/", methods=['GET'])
def hello():
    return jsonify({
        "message"   : "tested on server free tier"
    })

# Image endpoint
@app.route("/image/resize", methods=['POST'])
def imageResize():
    file = request.files['image']
    filename = secure_filename(datetime.datetime.now().replace(microsecond=0).isoformat() + file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER_SAMPLE'], filename))

    image = Image.open("./sample_image/" + filename)
    # newImage = image.resize((300, 400))
    image.save(os.path.join(app.config['UPLOAD_FOLDER_SAMPLE'], filename), optimize=True, quality=50)

    return jsonify({
        "message" : "oke"
    })


@app.route("/image/verify", methods=['POST'])
def imageVerify():
    file = request.files['image']
    filename = secure_filename(datetime.datetime.now().replace(microsecond=0).isoformat() + file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER_SAMPLE'], filename))

    uploadedImage = Image.open("./sample_image/" + filename)
    # resizedImage = uploadedImage.resize((300,400))
    uploadedImage.save(os.path.join(app.config['UPLOAD_FOLDER_SAMPLE'], filename))

    shutil.copy("./sample_image/" + filename, "./upload/" + filename)

    unknown_picture = face_recognition.load_image_file("./sample_image/" + filename)
    unknown_face_encoding = face_recognition.face_encodings(unknown_picture)
    if(len(unknown_face_encoding) > 0):
        status = 1
        image = filename
    else:
        status = 0
        image = ""

    return jsonify({
        "status" : status,
        "image" : image
    })


# Present endpoint
@app.route("/present", methods=['POST'])
def present():
    file = request.files['image']
    filename = secure_filename(datetime.datetime.now().replace(microsecond=0).isoformat() + file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    uploadedImage = Image.open("./upload/" + filename)
    # resizedImage = uploadedImage.resize((300,400))
    uploadedImage.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    with database.cursor() as cursor:
        sql = "SELECT * FROM user" 
        cursor.execute(sql)
        sql_results = cursor.fetchall()

    for data in sql_results:

        sample_picture = face_recognition.load_image_file("./sample_image/" + data["sample_image"])
        sample_picture_encoding = face_recognition.face_encodings(sample_picture)[0]
        
        unknown_picture = face_recognition.load_image_file("./upload/" + filename)
        unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

        results = face_recognition.compare_faces([sample_picture_encoding], unknown_face_encoding, 0.45)
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
        "Image" : filename,
        "Profile" : profile
    })


@app.route("/present/<id>", methods=['POST'])
def presentId(id):
    file = request.files['image']
    filename = secure_filename(datetime.datetime.now().replace(microsecond=0).isoformat() + file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    uploadedImage = Image.open("./upload/" + filename)
    # resizedImage = uploadedImage.resize((300,400))
    uploadedImage.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    with database.cursor() as cursor:
        sql = "SELECT * FROM user WHERE id=%s" 
        cursor.execute(sql, (id))
        data = cursor.fetchone()

    sample_picture = face_recognition.load_image_file("./sample_image/" + data["sample_image"])
    sample_picture_encoding = face_recognition.face_encodings(sample_picture)[0]
    
    unknown_picture = face_recognition.load_image_file("./upload/" + filename)
    unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

    results = face_recognition.compare_faces([sample_picture_encoding], unknown_face_encoding, 0.45)
    distance = face_recognition.face_distance([sample_picture_encoding], unknown_face_encoding)
    
    print(results)
    print(distance)

    if True in results:
        will_distanced = 1 - distance[0]
        distanced = int(will_distanced * 100)
        profile = data
    else: 
        distanced = 0
        profile = ""

    return jsonify({
        "Distance"  : distanced,
        "Image" : filename,
        "Profile" : profile
    })


@app.route("/present/add", methods=['POST'])
def presentAdd():
    data = request.json
    userId = data['userId']
    image = data['image']
    similiar = data['similiar']
    latitude = data['latitude']
    longitude = data['longitude']
    created_at = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    updated_at = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')

    with database.cursor() as cursor:
        sql = "INSERT INTO present (user_id, image, similiar, latitude, longitude, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s)" 
        cursor.execute(sql, (userId, image, similiar, latitude, longitude, created_at, updated_at))
        database.commit()

    with database.cursor() as cursor:
        sql = "UPDATE user SET status='1', updated_at=%s WHERE id=%s"
        cursor.execute(sql, (updated_at, userId))
        database.commit()

    return jsonify({
        "message" : "completed"
    })


@app.route("/present/user/<id>", methods=['GET'])
def presentByUser(id):
    with database.cursor() as cursor:
        sql = "SELECT * FROM present WHERE user_id=%s ORDER BY created_at DESC" 
        cursor.execute(sql, (id))
        sql_results = cursor.fetchall()

    return jsonify({
        "Present" : sql_results
    })


@app.route("/present/<id>", methods=['GET'])
def presentById(id):
    with database.cursor() as cursor:
        sql = "SELECT user.name, user.image as userimage, present.* FROM present INNER JOIN user ON user.id = present.user_id WHERE present.id=%s" 
        cursor.execute(sql, (id))
        sql_results = cursor.fetchone()

    return jsonify({
        "Present" : sql_results
    })


@app.route("/present/friends/<id>", methods=['GET'])
def presentFriends(id):
    with database.cursor() as cursor:
        sql = "SELECT user.name, user.image as userimage, present.* FROM present INNER JOIN user ON user.id = present.user_id WHERE present.user_id!=%s ORDER BY present.created_at DESC" 
        cursor.execute(sql, (id))
        sql_results = cursor.fetchall()

    return jsonify({
        "Present" : sql_results
    })


# Profile endpoint
@app.route("/profile", methods=['POST'])
def profileAdd():
    data = request.json
    id = 0
    name = data['name']
    email = data['email']
    username = data['username']
    password = data['password']
    phone = data['phone']
    address = data['address']
    image = data['image']
    status = "0"
    created_at = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    updated_at = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')

    with database.cursor() as cursor:
        sql = "SELECT * FROM user WHERE username=%s OR email=%s" 
        cursor.execute(sql, (username, email))
        check_user = cursor.fetchone()
    
    if(check_user):
        message = "registered"
    else:
        with database.cursor() as cursor:
            sql = "INSERT INTO user VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" 
            cursor.execute(sql, (id, name, email, username, password, phone, address, image, image, status, created_at, updated_at))
            database.commit()
        message = "completed"

    return jsonify({
        "message" : message
    })


@app.route("/profile/username", methods=['POST'])
def profileUsername():
    data = request.json
    username = data['username']

    with database.cursor() as cursor:
        sql = "SELECT * FROM user WHERE username=%s" 
        cursor.execute(sql, (username))
        sql_results = cursor.fetchone()
    
    if(sql_results):
        message = "registered"
        profile = sql_results
    else:
        message = "unregistered"
        profile = ""

    return jsonify({
        "message" : message,
        "profile" : profile
    })


@app.route("/profile/<id>", methods=['GET'])
def profile(id):
    with database.cursor() as cursor:
        sql = "SELECT * FROM user WHERE id=%s" 
        cursor.execute(sql, (id))
        sql_results = cursor.fetchone()

    return jsonify({
        "Profile" : sql_results
    })


@app.route("/profile/<id>", methods=['PUT'])
def profileUpdate(id):
    data = request.json
    name = data['name']
    email = data['email']
    username = data['username']
    phone = data['phone']
    address = data['address']
    updated_at = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')

    with database.cursor() as cursor:
        sql = "UPDATE user SET name=%s, email=%s, username=%s, phone=%s, address=%s, updated_at=%s WHERE id=%s" 
        cursor.execute(sql, (name, email, username, phone, address, updated_at, id))
        database.commit()

    return jsonify({
        "message" : "completed"
    })

@app.route("/profile/photo/<id>", methods=['PUT'])
def profileUpdatePhoto(id):
    file = request.files['image']
    filename = secure_filename(datetime.datetime.now().replace(microsecond=0).isoformat() + file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    updated_at = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')

    with database.cursor() as cursor:
        sql = "UPDATE user SET image=%s, updated_at=%s WHERE id=%s" 
        cursor.execute(sql, (filename, updated_at, id))
        database.commit()

    return jsonify({
        "message" : "completed",
	    "image" : filename
    })


@app.route("/profile/status/<id>", methods=['PUT'])
def profileUpdateStatus(id):
    data = request.json
    status = data['status']
    updated_at = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')

    with database.cursor() as cursor:
        sql = "UPDATE user SET status=%s, updated_at=%s WHERE id=%s" 
        cursor.execute(sql, (status, updated_at, id))
        database.commit()

    return jsonify({
        "message" : "completed"
    })


# Run Server
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(debug=True, host='0.0.0.0', port=port)

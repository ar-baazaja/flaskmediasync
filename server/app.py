from flask import Flask, request, send_file
from flask_cors import CORS
import os
import cv2
import uuid

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload():
    name = request.form['name']
    email = request.form['email']
    image = request.files['image']
    audio = request.files['audio']

    image_path = os.path.join(UPLOAD_FOLDER, f"{uuid.uuid4().hex}_img.jpg")
    audio_path = os.path.join(UPLOAD_FOLDER, f"{uuid.uuid4().hex}_audio.mp3")

    image.save(image_path)

    img = cv2.imread(image_path)
    resized_img = cv2.resize(img, (300, 300))
    compressed_path = os.path.join(UPLOAD_FOLDER, f"{uuid.uuid4().hex}_compressed.jpg")
    cv2.imwrite(compressed_path, resized_img)

    audio.save(audio_path)

    return send_file(compressed_path, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)

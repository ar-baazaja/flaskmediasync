from flask import Flask
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import cv2
import numpy as np
import base64
import os

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

UPLOAD_FOLDER = 'uploads_socket'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@socketio.on('upload_media')
def handle_upload(data):
    name = data.get('name')
    email = data.get('email')
    image_data = data.get('image')
    audio_data = data.get('audio')

    if not image_data:
        emit('error', {'message': 'No image received'})
        return

    # Decode image
    header, base64_data = image_data.split(',', 1)
    img_bytes = base64.b64decode(base64_data)
    np_arr = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # Resize/compress image
    resized_img = cv2.resize(img, (300, 300))
    compressed_path = os.path.join(UPLOAD_FOLDER, f"compressed_{name or 'output'}.jpg")
    cv2.imwrite(compressed_path, resized_img)

    # Encode compressed image as base64 to emit back
    _, buffer = cv2.imencode('.jpg', resized_img)
    jpg_as_text = base64.b64encode(buffer).decode('utf-8')
    emit('processed_image', {'image': f'data:image/jpeg;base64,{jpg_as_text}'})

if __name__ == '__main__':
    socketio.run(app, debug=True)

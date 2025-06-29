from flask import Flask, send_file
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import os
import cv2
import numpy as np
import base64
from io import BytesIO
from PIL import Image

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def resize_image(image_bytes):
    nparr = np.frombuffer(image_bytes, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    resized = cv2.resize(img_np, (200, 200))
    _, buffer = cv2.imencode('.jpg', resized)
    return buffer.tobytes()

@socketio.on('upload_data')
def handle_upload(data):
    image_data = base64.b64decode(data['image'])
    audio_data = base64.b64decode(data['audio'])
    name = data['name']
    email = data['email']

    print(f"Received from {name} ({email})")

    # Save audio
    audio_path = os.path.join(UPLOAD_FOLDER, f"{name}_audio.wav")
    with open(audio_path, 'wb') as f:
        f.write(audio_data)

    # Process image
    resized_image = resize_image(image_data)

    # Encode resized image to base64 to send back
    image_base64 = base64.b64encode(resized_image).decode('utf-8')

    emit('image_response', {'image': image_base64})

if __name__ == '__main__':
    socketio.run(app, port=5000)

from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import os
import cv2
import numpy as np
import base64

# --- Flask Setup ---
app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

# --- Upload Directory ---
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# --- Helper Function to Resize Image ---
def resize_image(image_bytes):
    try:
        nparr = np.frombuffer(image_bytes, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        resized = cv2.resize(img_np, (200, 200))
        _, buffer = cv2.imencode('.jpg', resized)
        return buffer.tobytes()
    except Exception as e:
        print("Error resizing image:", e)
        return None

# --- SocketIO Event: Handle Upload ---
@socketio.on('upload_data')
def handle_upload(data):
    try:
        print("Received upload_data event")

        # Decode base64 data
        image_data = base64.b64decode(data['image'])
        audio_data = base64.b64decode(data['audio'])
        name = data['name']
        email = data['email']

        print(f"Data received from {name} ({email})")

        # Save audio file
        audio_path = os.path.join(UPLOAD_FOLDER, f"{name}_audio.wav")
        with open(audio_path, 'wb') as f:
            f.write(audio_data)
        print(f"Audio saved at {audio_path}")

        # Resize image
        resized_image = resize_image(image_data)
        if resized_image is None:
            emit('image_response', {'error': 'Image processing failed'})
            return

        # Encode resized image to base64 and send back
        image_base64 = base64.b64encode(resized_image).decode('utf-8')
        emit('image_response', {'image': image_base64})
        print("Resized image sent back to client")

    except Exception as e:
        print("Error handling upload_data:", e)
        emit('image_response', {'error': str(e)})

# --- Start Server ---
if __name__ == '__main__':
    print("Starting Flask SocketIO server...")
    port = int(os.environ.get("PORT", 5000))
    socketio.run(app, host='0.0.0.0', port=port)

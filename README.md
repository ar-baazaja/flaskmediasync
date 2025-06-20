# flaskmediasync

A full-stack media upload application built with React + Tailwind on the frontend and Flask + OpenCV on the backend.

## 📦 Structure

- `/client` — React frontend with Tailwind CSS
- `/server` — Flask backend API with OpenCV image compression

## 🚀 Getting Started

### Frontend
```bash
cd client
npm install
npm start
```

### Backend
```bash
cd server
pip install -r requirements.txt
python app.py
```

## 📸 Features

- Upload image & audio files
- Flask backend compresses image with OpenCV
- Audio stored, compressed image returned to client

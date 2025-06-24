# flaskmediasync

🔗 **Live Demo**: [https://685a8ec25b22bae7b0bfdb61--vocal-fox-af6b33.netlify.app](https://685a8ec25b22bae7b0bfdb61--vocal-fox-af6b33.netlify.app)

A full-stack media uploader built with **React + Tailwind CSS** (frontend) and **Flask + OpenCV** (backend).  
Users can upload an image and an audio file, and the app compresses and returns the processed image.

---
## 📸 Output Preview

The image below shows the **output UI** after a successful upload of an image and audio file.  
Once the user submits both files, the Flask backend compresses the image using OpenCV and returns it to the frontend, which then displays it in the browser.

<img src="./capture.png" alt="Compressed image preview after upload" width="600"/>
---
## 📁 Project Structure

```
flaskmediasync/
├── client/      # React + Tailwind frontend
└── server/      # Flask backend (REST API)
```

---

## 🚀 Frontend (React + Tailwind)

### ✅ Setup Locally

```bash
cd client
npm install
npm start
```

- Runs on: `http://localhost:3000`
- Communicates with Flask backend on port `5000`

---

### 🌐 Deploy Frontend on Netlify

1. Go to [https://netlify.com](https://netlify.com)
2. Click **"Add new site" → "Import from GitHub"**
3. Select the repo `ar-baazaja/flaskmediasync`
4. Set the following build options:

| Option            | Value         |
|------------------|---------------|
| Base directory   | `client` ✅    |
| Build command    | `npm run build` |
| Publish directory| `build` ✅     |

5. Click **Deploy Site**

---

## 🔧 Backend (Flask + OpenCV)

### ✅ Setup Locally

```bash
cd server
python -m venv venv
venv\Scripts\activate    # On Windows
# Or: source venv/bin/activate  # On Mac/Linux

pip install -r requirements.txt
python app.py
```

- Runs on: `http://localhost:5000`
- Accepts `POST` requests at `/upload`

---

### 🌍 Deploy Backend (Options)

Deploy Flask backend to:

- [Render.com](https://render.com)
- [Railway.app](https://railway.app)
- [Replit](https://replit.com)
- [PythonAnywhere](https://pythonanywhere.com)

Let me know if you want step-by-step backend deployment on any of these.

---

## 📸 Features

- Upload image and audio
- Compress image using OpenCV
- Return compressed image to frontend
- RESTful API design
- Fully responsive UI with Tailwind CSS

---

## 🧠 Future Improvements

- Add drag-and-drop upload
- Add Socket.IO for live updates
- Store metadata to a database
- Add user authentication

---

## 👤 Author

**Arbaz Ahmed Awan**  
GitHub: [@ar-baazaja](https://github.com/ar-baazaja)

---

## 📄 License

This project is open-sourced under the **MIT License**

import React, { useState } from 'react';
import { io } from 'socket.io-client';

const socket = io("http://localhost:5000");

function App() {
  const [image, setImage] = useState(null);
  const [audio, setAudio] = useState(null);
  const [resizedImage, setResizedImage] = useState(null);
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');

  const handleSubmit = async () => {
    const readFileAsBase64 = (file) => {
      return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = () => resolve(reader.result.split(',')[1]);
        reader.onerror = reject;
        reader.readAsDataURL(file);
      });
    };

    const imageBase64 = await readFileAsBase64(image);
    const audioBase64 = await readFileAsBase64(audio);

    socket.emit('upload_data', {
      image: imageBase64,
      audio: audioBase64,
      name,
      email
    });
  };

  socket.on('image_response', (data) => {
    setResizedImage(`data:image/jpeg;base64,${data.image}`);
  });

  return (
    <div>
      <h2>Upload Form</h2>
      <input type="text" placeholder="Name" onChange={(e) => setName(e.target.value)} />
      <input type="email" placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
      <input type="file" accept="image/*" onChange={(e) => setImage(e.target.files[0])} />
      <input type="file" accept="audio/*" onChange={(e) => setAudio(e.target.files[0])} />
      <button onClick={handleSubmit}>Send via Socket</button>
      {resizedImage && <img src={resizedImage} alt="Resized" />}
    </div>
  );
}

export default App;

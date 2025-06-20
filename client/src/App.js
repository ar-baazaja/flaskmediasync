import React, { useState } from "react";
import axios from "axios";

function App() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [image, setImage] = useState(null);
  const [audio, setAudio] = useState(null);
  const [resultImg, setResultImg] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    const formData = new FormData();
    formData.append("name", name);
    formData.append("email", email);
    formData.append("image", image);
    formData.append("audio", audio);

    try {
      const res = await axios.post("http://localhost:5000/upload", formData, {
        responseType: "blob",
      });
      setResultImg(URL.createObjectURL(res.data));
    } catch (err) {
      alert("Upload failed!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center p-6">
      <div className="bg-white shadow-lg rounded-xl p-8 max-w-md w-full">
        <h2 className="text-2xl font-bold mb-6 text-center text-gray-800">Media Uploader</h2>
        <form onSubmit={handleSubmit} className="space-y-4">
          <input type="text" placeholder="Name" className="w-full p-2 border rounded"
            onChange={(e) => setName(e.target.value)} required />
          <input type="email" placeholder="Email" className="w-full p-2 border rounded"
            onChange={(e) => setEmail(e.target.value)} required />
          <input type="file" accept="image/*" className="w-full p-2 border rounded"
            onChange={(e) => setImage(e.target.files[0])} required />
          <input type="file" accept="audio/*" className="w-full p-2 border rounded"
            onChange={(e) => setAudio(e.target.files[0])} required />
          <button type="submit" disabled={loading}
            className={`w-full py-2 px-4 rounded text-white ${loading ? "bg-gray-500" : "bg-blue-600 hover:bg-blue-700"}`}>
            {loading ? "Uploading..." : "Upload"}
          </button>
        </form>
        {resultImg && (
          <div className="mt-6 text-center">
            <h3 className="text-lg font-semibold mb-2">Compressed Image:</h3>
            <img src={resultImg} alt="Compressed" className="rounded-lg border shadow mx-auto" />
          </div>
        )}
      </div>
    </div>
  );
}

export default App;

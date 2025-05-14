import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './index.css';

const API_URL = process.env.REACT_APP_API_URL;
// console.log("API_URL",API_URL)

function App() {
  const [transcript, setTranscript] = useState('');
  const [transcripts, setTranscripts] = useState([]);

  const handleSubmit = async () => {
    if (transcript.trim() === '') return;
    await axios.post(`${API_URL}/transcripts`, {
      transcript_text: transcript,
    });
    setTranscript('');
    fetchTranscripts();
  };

  const fetchTranscripts = async () => {
    const res = await axios.get(`${API_URL}/transcripts`);
    setTranscripts(res.data);
  };

  useEffect(() => {
    fetchTranscripts();
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <div className="max-w-2xl mx-auto bg-white rounded-xl shadow-md p-6">
        <h1 className="text-2xl font-bold mb-4">Transcript Summarizer</h1>
        <textarea
          value={transcript}
          onChange={(e) => setTranscript(e.target.value)}
          className="w-full h-24 p-2 border rounded mb-4"
          placeholder="Enter your transcript..."
        />
        <button
          onClick={handleSubmit}
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
        >
          Submit
        </button>
        <h2 className="text-xl font-semibold mt-6">Saved Transcripts</h2>
        <ul className="mt-4 space-y-2">
          {transcripts.map((item) => (
            <li key={item.id} className="p-2 bg-gray-50 border rounded">
              <p><strong>Transcript:</strong> {item.transcript_text}</p>
              <p><strong>Summary:</strong> {item.summary}</p>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;

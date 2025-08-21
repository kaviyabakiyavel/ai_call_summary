import React, { useState, useEffect } from "react";
import axios from "axios";

const API_URL = process.env.REACT_APP_API_URL || "http://localhost:8000";

function TranscriptDashboard() {
  // Manual transcript states
  const [currentTranscript, setCurrentTranscript] = useState("");
  const [savedTranscripts, setSavedTranscripts] = useState([]);

  // Audio upload states
  const [audioFile, setAudioFile] = useState(null);
  const [audioResponse, setAudioResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  // Fetch saved transcripts
  const fetchTranscripts = async () => {
    try {
      const res = await axios.get(`${API_URL}/transcripts`);
      setSavedTranscripts(res.data);
    } catch (err) {
      console.error("Failed to fetch transcripts:", err);
    }
  };

  useEffect(() => {
    fetchTranscripts();
  }, []);

  // Manual transcript submit
  const handleManualSubmit = async () => {
    if (!currentTranscript.trim()) return;
    try {
      await axios.post(`${API_URL}/transcripts`, {
        transcript_text: currentTranscript,
      });
      setCurrentTranscript("");
      fetchTranscripts();
    } catch (err) {
      console.error("Failed to save transcript:", err);
    }
  };

  // Audio upload
  const handleAudioUpload = async (file) => {
    if (!file) return alert("Please select a file first!");
    setLoading(true);
    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await fetch(`${API_URL}/upload-audio/`, {
        method: "POST",
        body: formData,
      });
      const data = await res.json();
      setAudioResponse(data);
    } catch (err) {
      alert("Upload failed: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleUseSampleAudio = async () => {
    setLoading(true);
    try {
      const res = await fetch("/sample.mp3");
      const blob = await res.blob();
      const formData = new FormData();
      formData.append("file", blob, "sample.mp3");

      const response = await fetch(`${API_URL}/upload-audio/`, {
        method: "POST",
        body: formData,
      });
      const data = await response.json();
      setAudioResponse(data);
    } catch (err) {
      alert("Upload failed: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <div className="max-w-5xl mx-auto space-y-8">

        {/* Audio Upload Section */}
        <div className="bg-white rounded-2xl shadow-lg p-8">
          <h1 className="text-3xl font-bold mb-4 text-center">AI Call Summary Tool for Dental Offices</h1>
          <div className="flex flex-col items-center space-y-4">
            <input
              type="file"
              accept="audio/*"
              onChange={(e) => setAudioFile(e.target.files[0])}
              className="border border-gray-300 rounded px-3 py-2 w-full text-sm"
            />
            <button
              onClick={() => handleAudioUpload(audioFile)}
              disabled={loading}
              className="w-full bg-blue-500 hover:bg-blue-600 text-white font-semibold py-3 rounded-lg transition-colors"
            >
              {loading ? "Uploading..." : "Upload Audio"}
            </button>
            <button
              onClick={handleUseSampleAudio}
              disabled={loading}
              className="w-full bg-gray-500 hover:bg-gray-600 text-white font-semibold py-3 rounded-lg transition-colors"
            >
              {loading ? "Uploading..." : "Use Sample Audio"}
            </button>
          </div>

          {audioResponse && (
            <div className="mt-6 border-t border-gray-200 pt-4 space-y-4">
              <div>
                <h2 className="text-xl font-semibold mb-2">Transcript</h2>
                <p className="bg-gray-50 p-3 rounded border border-gray-200">{audioResponse.transcript}</p>
              </div>
              <div>
                <h2 className="text-xl font-semibold mb-2">Summary</h2>
                <p className="bg-gray-50 p-3 rounded border border-gray-200">{audioResponse.summary}</p>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default TranscriptDashboard;

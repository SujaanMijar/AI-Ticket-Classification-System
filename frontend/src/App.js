import { useState } from "react";
import { createTicket } from "./api";
import "./App.css";

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    setResult(null);

    try {
      const data = await createTicket(text);
      setResult(data);
      setText("");
    } catch (err) {
      setError("Something went wrong");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>🎫 AI Ticket System</h1>

      <form onSubmit={handleSubmit}>
        <textarea
          placeholder="Describe your issue..."
          value={text}
          onChange={(e) => setText(e.target.value)}
          required
        />

        <button type="submit" disabled={loading}>
          {loading ? "Analyzing..." : "Submit Ticket"}
        </button>
      </form>

      {error && <p className="error">{error}</p>}

      {result && (
        <div className="result-card">
          <h2>Prediction Result</h2>
          <p><strong>Text:</strong> {result.text}</p>
          <p><strong>Category:</strong> {result.category}</p>
          <p><strong>Sentiment:</strong> {result.sentiment}</p>
          <p><strong>Priority:</strong> {result.priority}</p>
          <p><strong>Created At:</strong> {result.created_at}</p>
        </div>
      )}
    </div>
  );
}

export default App;

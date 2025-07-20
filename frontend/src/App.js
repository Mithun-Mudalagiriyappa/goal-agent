import React, { useState } from 'react';
import GoalInput from './GoalInput';

function App() {
  const [typingText, setTypingText] = useState('');
  const [loading, setLoading] = useState(false);

  const handleGoalSubmit = async (goal) => {
    setTypingText('');
    setLoading(true);

    try {
      const response = await fetch('http://localhost:5000/generate-tasks-stream', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ goal }),
      });

      const reader = response.body.getReader();
      const decoder = new TextDecoder('utf-8');
      let buffer = '';

      while (true) {
        const { value, done } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value);

        const lines = buffer.split(/\n+/);
        for (let i = 0; i < lines.length - 1; i++) {
          await new Promise((resolve) => setTimeout(resolve, 50));
          setTypingText((prev) => prev + lines[i] + '\n');
        }

        buffer = lines[lines.length - 1];
      }

      setTypingText((prev) => prev + buffer);
    } catch (err) {
      console.error('Streaming error:', err);
      setTypingText('Failed to generate response.');
    }

    setLoading(false);
  };

  const spinnerStyle = {
    border: '4px solid #eee',
    borderTop: '4px solid #3498db',
    borderRadius: '50%',
    width: '30px',
    height: '30px',
    animation: 'spin 1s linear infinite',
    margin: '10px auto',
  };

  return (
    <div style={{ padding: '20px', maxWidth: '700px', margin: '0 auto', fontFamily: 'sans-serif' }}>
      <h2>🎯 Goal-Oriented Task Agent</h2>
      <GoalInput onSubmit={handleGoalSubmit} />

      {loading && (
        <div style={{ marginTop: '20px', textAlign: 'center', color: '#555' }}>
          <div style={spinnerStyle}></div>
          <p>Agent is thinking...</p>
        </div>
      )}

      <pre style={{ whiteSpace: 'pre-wrap', fontSize: '1rem', marginTop: '20px', lineHeight: '1.6' }}>
        {typingText}
      </pre>
    </div>
  );
}

export default App;
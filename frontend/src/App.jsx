import { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';
import { v4 as uuidv4 } from 'uuid';

function App() {
  const [sessionId, setSessionId] = useState('');
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  useEffect(() => {
    const id = uuidv4();
    setSessionId(id);
  }, []);

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMessage = { sender: 'user', text: input };
    setMessages((prev) => [...prev, userMessage]);

    console.log("Sending to backend:", {
      session_id: sessionId,
      message: input
    });

    try {
      const res = await axios.post('http://localhost:8000/chat', {
        session_id: sessionId,
        message: input
      });

      const botMessage = { sender: 'bot', text: res.data.response };
      setMessages((prev) => [...prev, botMessage]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { sender: 'bot', text: 'Error: ' + err.message }
      ]);
    }

    setInput('');
  };


  return (
    <div className="chat-container">
      <h2>Chatbot</h2>
       <div className="chat-box">
        {messages.map((msg, i) => (
          <div key={i} className={msg.sender === 'user' ? 'chat-msg user' : 'chat-msg bot'}>
            <strong>{msg.sender}:</strong> {msg.text}
          </div>
        ))}
      </div>
      <div className="chat-input">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && handleSend()}
          placeholder="Type a message..."
        />
        <button onClick={handleSend}>Send</button>
      </div>
    </div>
  );
}

export default App;

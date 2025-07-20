# goal-agent
# 🎯 Goal-Oriented Task Agent

An intelligent agent that breaks down high-level goals into actionable subtasks using LangChain, Mistral (via Ollama), and a React + Flask full-stack interface. Designed for real-time streaming and a ChatGPT-style typing experience.

---

## 🚀 Features

- 🔄 Real-time token streaming from backend to frontend
- 🧠 Uses LangChain + ChatOllama with Mistral for task generation
- 💬 Typing effect in React for conversational UX
- 🧩 Modular architecture with Flask backend and React frontend
- 🔐 CORS-enabled API for seamless local development

---

## 🛠️ Tech Stack

- **Frontend**: React (with hooks), custom loader, typing animation
- **Backend**: Flask, LangChain, ChatOllama
- **LLM**: Mistral via Ollama (local inference)
- **Streaming**: `ReadableStream` in React + Flask `Response` generator

---

## 📦 Folder Structure
goal-agent/ 
├── backend/ 
  │
  ├── app.py │   
  ├── agent_logic.py 
  │   └── streaming_callback.py 
├── frontend/ 
  │   
  ├── src/ 
  │   
  │   
  ├── App.js 
  │   
  │   
  ├── GoalInput.js 
  │   
  │   └── index.js 
  │   └── public/ 
├── .gitignore 
├── README.md

## 🧪 Running Locally

### 1. Start Flask backend
```bash
cd backend
python app.py

### 2. Start React frontend

```bash
cd frontend
npm install
npm start

### Ensure Ollama is running locally with the Mistral model loaded

### API Endpoint
- POST /generate-tasks-stream
- Request: { "goal": "Build SOS app for family safety" }
- Response: streamed plain text tokens

### Inspiration
Built to explore agentic AI and autonomous systems that break down goals intelligently — with a focus on privacy, accessibility, and real-world impact.

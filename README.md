# Local Chatbot Setup Guide

A simple chatbot you can run **entirely on your own computer** using a local AI model. No API keys or internet needed after setup.

This project uses:
- 🐍 Python backend (FastAPI)
- 💬 Llama 3.2B from [Ollama](https://ollama.com)
- ⚛️ React frontend (via Vite)
- 📦 Conda + NVM to manage dependencies

---

## 🚀 Getting Started

These steps will guide you from zero to chatbot.

---

### 1. Clone this repository
[Set up SSH keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) if you don't have any, and add it to your github account.

Clone the repository using ssh method:
```bash
git clone git@github.com:joshzhang28/chatbot-rag.git
cd local-chatbot
```

### 2. Install Miniconda (Python environment manager)
If you don't have it already:

👉 [Download Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main)

Then run in terminal:

```bash
conda env create -f backend/conda.yaml
conda activate chatbot-env

```

### 3. Install Ollama + Pull the AI Model

a. Download Ollama

👉 [https://ollama.com/download](https://ollama.com/download)

Install it like a regular app.

b. Pull the Llama3.2B model

```bash
ollama pull llama3.2
```


### 4. Set up the Frontend
We'll use `Node.js` and `Vite` to run the frontend.

a. Install NVM (Node Version Manager)

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
source ~/.bashrc  # or ~/.zshrc if using zsh
nvm install --lts
nvm use --lts
```

b. Install frontend dependencies
```
cd frontend
npm install
```

## Run the Local App

### 5. Run the Backend
In a new terminal tab:
```
cd backend
uvicorn main:app --reload --port 8000
```

This starts the chatbot API at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 6. Run the Frontend
```bash
cd frontend
npm run dev
```
This starts the UI at: [http://localhost:5173](http://localhost:5173)

### 7. Test It Out!
Visit [http://localhost:5173](http://localhost:5173)
Type a message like: Hello, what can you do?
The chatbot will respond using the local AI model (no internet needed)

## Future Development

### Backend
- [ ] Enable in-memory chat history
  - Maintain context during the session by storing the full conversation.
- [ ] Build persistent memory with PostgreSQL
  - Store and retrieve chat history locally for long-term memory support.
- [ ] Implement RAG (Retrieval-Augmented Generation)
  - Fetch relevant information from documents or knowledge base to enhance responses.
- [ ] Enable PDF input for RAG
  - Allow user-uploaded PDF files to be parsed and indexed for retrieval.

### Frontend
- [ ] Set a maximum width for the chat UI
  - Prevent the chat interface from stretching too wide on large screens for better readability.


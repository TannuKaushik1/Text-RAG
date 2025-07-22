🤖 RAG-based Q&A System with Gemini API
This project implements a Retrieval-Augmented Generation (RAG) pipeline that:
✅ Splits input text into chunks,
✅ Stores & indexes them in a ChromaDB vector database,
✅ Retrieves relevant chunks based on a user query using Sentence Transformers,
✅ Feeds the context into Google Gemini API to generate an intelligent answer.

✨ Features
✅ Chunking: Splits long input text into smaller pieces.

✅ Vector Search: Stores chunks in ChromaDB with embeddings (all-MiniLM-L6-v2).

✅ Semantic Retrieval: Retrieves top‑K relevant chunks for each query.

✅ Generative AI: Uses Google Gemini to produce context‑aware answers.

✅ Interactive CLI: Ask questions in a loop until you type exit.

🏗️ Tech Stack
Python 3.9+

Sentence Transformers (all-MiniLM-L6-v2 model)

ChromaDB

Google Generative AI (Gemini)

📂 Project Structure
bash
Copy
Edit
📦 rag-gemini-chroma
 ┣ 📜 main.py            # Main RAG implementation
 ┣ 📜 requirements.txt   # Python dependencies
 ┣ 📂 .chromadb/         # Local ChromaDB storage
 ┗ 📜 README.md
⚙️ Installation
1️⃣ Clone the repo:

bash
Copy
Edit
git clone https://github.com/yourusername/rag-gemini-chroma.git
cd rag-gemini-chroma
2️⃣ Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Set up Gemini API Key:
Replace the placeholder in main.py with your API key:

python
Copy
Edit
genai.configure(api_key="YOUR_GEMINI_API_KEY")
▶️ Usage
Run the script:

bash
Copy
Edit
python main.py
You will see:

pgsql
Copy
Edit
✅ Loaded X chunks from input text
Ask a question (or type 'exit'):
👉 Type a question and press Enter.
👉 The system retrieves relevant context and Gemini generates an answer.
👉 Type exit to quit.

📌 Example
Question:
What is PARA on Nasdaq?

Answer:
(Gemini will generate an answer based on retrieved context)

📊 How It Works
Pipeline:

chunk_text() → splits input text

create_chroma_collection() → embeds and stores chunks

retrieve_relevant_chunks() → retrieves top-k chunks for a query

generate_answer_gemini() → feeds context and query to Gemini for a final answer

🚀 Future Enhancements
📌 Add support for file uploads (PDF/TXT).

📌 Build a web interface (React/Flask) instead of CLI.

📌 Implement caching for faster repeated queries.

🤝 Contributing
Feel free to fork this repository and submit PRs for improvements.

import google.generativeai as genai
from sentence_transformers import SentenceTransformer
from chromadb import PersistentClient

# ✅ Step 1: Configure Gemini API key
genai.configure(api_key="AIzaSyBsgCEYb-9J1gbvumPKhd2Az0UVkDWe4Bw")  # ⬅️ Replace with your Gemini API key

# ✅ Step 2: Input your custom text manually
input_text = """
Businesses, professions, and organizations
Paramount Global, traded as PARA on the Nasdaq stock exchange
Para Group, the former name of CT Corp
Para Rubber, now Skellerup, a New Zealand manufacturer
Para USA, formerly Para-Ordnance, a firearms manufacturer
Pan American Rugby Association
Philippine Amateur Radio Association
Paraprofessional
Paralegal
Paramilitary, organisations not part of the armed forces but operate as such
Paramedic
Parapsychology, the study of alleged psychic phenomena
"""

# ✅ Step 3: Split text into chunks
def chunk_text(text, chunk_size=500):
    words = text.split()
    return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

# ✅ Step 4: Create Chroma collection
def create_chroma_collection(chunks):
    client = PersistentClient(path=".chromadb")

    try:
        client.delete_collection("text_chunks")
    except:
        pass

    collection = client.create_collection("text_chunks")

    embed_model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = embed_model.encode(chunks).tolist()

    for i, (chunk, emb) in enumerate(zip(chunks, embeddings)):
        collection.add(
            documents=[chunk],
            embeddings=[emb],
            ids=[f"id_{i}"]
        )

    return collection

# ✅ Step 5: Retrieve relevant chunks
def retrieve_relevant_chunks(collection, query, k=2):
    embed_model = SentenceTransformer("all-MiniLM-L6-v2")
    query_embedding = embed_model.encode([query]).tolist()[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )
    return results["documents"][0]

# ✅ Step 6: Generate response from Gemini
def generate_answer_gemini(query, retrieved_chunks):
    model = genai.GenerativeModel("models/gemini-2.0-flash")  # ✅ Correct model name

    context = "\n".join(retrieved_chunks)
    prompt = f"Context: {context}\n\nQuestion: {query}\nAnswer:"

    response = model.generate_content(prompt)
    return response.text.strip()


# ✅ Main program
if __name__ == "__main__":
    chunks = chunk_text(input_text)
    print(f"✅ Loaded {len(chunks)} chunks from input text\n")

    collection = create_chroma_collection(chunks)

    while True:
        question = input("Ask a question (or type 'exit'): ")
        if question.lower() == "exit":
            break

        relevant_chunks = retrieve_relevant_chunks(collection, question)
        answer = generate_answer_gemini(question, relevant_chunks)
        print("\n📌 Answer:\n", answer)


import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")  # Add to .env

def run_llm_reasoning(query, top_chunks):
    context = "\n\n".join([f"Clause:\n{chunk}" for chunk in top_chunks])
    prompt = f"Given the following policy clauses:\n\n{context}\n\nAnswer the query: {query}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response["choices"][0]["message"]["content"]

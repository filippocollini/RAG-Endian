import openai
import os
from rag_engine.retriever import retrieve_relevant_chunks

def generate_answer(query):
    chunks = retrieve_relevant_chunks(query)
    context = "\n---\n".join(chunks)

    system_prompt = open("app/prompts/system_prompt.txt").read()

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}
        ]
    )
    return response.choices[0].message.content

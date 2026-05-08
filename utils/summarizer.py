import requests

def call_llm(prompt):
    url = ENDPOINT
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "messages": [
            {"role": "system", "content": "You are a helpful summarization assistant."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 500,
        "temperature": 0.3
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def summarize_document(text):
    chunks = chunk_text(text)
    
    summaries = []
    
    for chunk in chunks:
        prompt = f"Summarize the following:\n\n{chunk}"
        result = call_llm(prompt)
        summaries.append(result["choices"][0]["message"]["content"])
    
    combined = "\n".join(summaries)

    final_prompt = f"Provide a concise summary of the following:\n{combined}"
    final_summary = call_llm(final_prompt)

    return final_summary["choices"][0]["message"]["content"]
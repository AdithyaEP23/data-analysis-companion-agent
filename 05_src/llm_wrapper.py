import os

def call_llm(prompt: str, temperature: float = 0.2, max_tokens: int = 600):
    api_key = os.getenv("LLM_API_KEY")
    if not api_key:
        return "[LLM_PLACEHOLDER]\n" + prompt[:800].replace("\n"," ")
    return "[LLM_PLACEHOLDER]\n" + prompt[:800].replace("\n"," ")

import os, json

MEM_PATH = "data/memory.json"

def load_memory():
    if os.path.exists(MEM_PATH):
        return json.load(open(MEM_PATH))
    mem = {
        "preferred_tone": "business",
        "summary_length": 800,
        "last_dataset": None
    }
    save_memory(mem)
    return mem

def save_memory(m):
    os.makedirs(os.path.dirname(MEM_PATH), exist_ok=True)
    with open(MEM_PATH,'w') as f:
        json.dump(m,f,indent=2)

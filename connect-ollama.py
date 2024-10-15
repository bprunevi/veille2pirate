import os
import json
from ollama import Client

OLLAMA_HOST_FILE = "secret/server_info.json"

def create_ollama():

    OLLAMA_IP = os.environ.get("OLLAMA_IP")
    OLLAMA_PORT = os.environ.get("OLLAMA_PORT")

    # Check if credentials file exists
    if os.path.exists(OLLAMA_HOST_FILE):
        with open(OLLAMA_HOST_FILE, 'r') as file:
            creds = json.load(file)
            return Client(host=f"{creds['ip']}:{creds['port']}")

    if OLLAMA_IP is None or OLLAMA_PORT is None:
        print(f"Could not find ollama server details in {OLLAMA_HOST_FILE} nor OLLAMA_IP and OLLAMA_PORT env variable.")

    return EOFError



client = create_ollama()

response = client.chat(model='llama3.2', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky red?',
  },
])

print(response['message']['content'])
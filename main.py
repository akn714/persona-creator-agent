import os
import json

from utils.llm import llm
from utils.prompts import SYSTEM_PROMPT, USER_PROMPT
from utils.sample_user_persona import sample_user_persona
from utils.reddit import reddit
from utils.chunks import split_into_token_chunks

def generate_persona(conversations):
    """
    Generate a persona based on the user's conversations
    """
    # print("[+] Generating persona...")
    messages = [
        {
            'role': 'system',
            'content': SYSTEM_PROMPT
        },
        {
            'role': 'user',
            'content': USER_PROMPT.format(sample_user_persona=sample_user_persona, conversations=conversations)
        }
    ]
    response = llm.get_llm_response(messages)
    response = response.strip().strip('```json').strip()
    return json.loads(response)

def merge_personas(personas):
    """
    Merge all the personas into one
    """
    print('[+] Merging all personas...')
    messages = [
        {
            'role': 'system',
            'content': """
            You are a persona creator agent.
            You will be given a list of personas in the form of a JSON array. You have to merge all the personas into one persona.
            Your response should only contains a JSON containing only one merged persona.
            """
        },
        {
            'role': 'user',
            'content': "personas: {personas}".format(personas=personas)
        }
    ]
    response = llm.get_llm_response(messages)
    response = response.strip().strip('```json').strip()
    return json.loads(response)

def save_persona(username, persona):
    """
    Save the persona to a file
    """
    os.makedirs("personas", exist_ok=True)

    # Save to file inside 'personas' folder
    file_path = os.path.join("personas", f"{username}_persona.json")
    with open(file_path, "w") as f:
        json.dump(persona, f, indent=2)

    print(f"\nPersona saved to: {file_path}")

def main():
    """
    Main function to generate a persona based on the user's conversations
    """
    user = input("[+] Enter your username: ")
    comments = reddit.get_user_comments(user)
    # persona = generate_persona(conversations)
    persona = {}
    personas = []
    chunks = split_into_token_chunks(comments, 10000)
    if len(chunks)>1:
        for i in range(len(chunks)):
            persona = generate_persona(comments[i*len(chunks):(i+1)*len(chunks)])
            personas.append(persona)
            persona = merge_personas(personas)
            print(f"[+] generating persona {i}")
    else:
        persona = generate_persona(comments)
    # print(json.dumps(persona, indent=2))
    
    save_persona(user, persona)

main()
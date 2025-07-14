import json
from utils.llm import llm
from utils.prompts import SYSTEM_PROMPT, USER_PROMPT
from utils.sample_user_persona import sample_user_persona
from utils.reddit import reddit

def generate_persona(conversations):
    """
    Generate a persona based on the user's conversations
    """
    print("[+] Generating persona...")
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
    print(response)
    return json.loads(response)

def main():
    """
    Main function to generate a persona based on the user's conversations
    """
    user = input("[+] Enter your username: ")
    conversations = reddit.get_user_comments(user)
    persona = generate_persona(conversations)
    print(persona)

main()
import requests
import json
import os

def get_response_message(message_history, message, system_prompt, user_name, url, headers):

    payload = {
        "bot_setting": [
            {
                "bot_name": "Jessie",
                "content": system_prompt,
                }
        ],
        "messages": [{"sender_type": "USER", "sender_name": user_name, "text": message}],
        "reply_constraints": {"sender_type": "BOT", "sender_name": "Jessie"},
        "model": "abab5.5-chat",
        "tokens_to_generate": 1034,
        "temperature": 0.01,
        "top_p": 0.95,
        # "stream": True,
    }

    response = requests.request("POST", url, headers=headers, json=payload)
    response_message = json.loads(response.text)['choices'][0]['messages']
    reply = json.loads(response.text)['reply']

    return response_message, reply

def get_conversation_from_message_histroy(history):
    conversation = []
    for h in history:
        if isinstance(h, list):
            h = h[0]
        conversation.append((h['sender_name'] + ": "+h['text']))
    return conversation


class MiniAgent:

    def __init__(self, group_id, api_key, user_name, system_prompt):
        self.group_id = group_id
        self.api_key = api_key
        self.user_name = user_name
        self.message_history = []
        self.system_prompt = system_prompt
        self.url = "https://api.minimax.chat/v1/text/chatcompletion_pro?GroupId=" + group_id
        self.headers = {"Content-Type": "application/json", "Authorization": "Bearer " + api_key}
    
    def chat(self, message):
        
        response_message, reply = get_response_message(self.message_history, message, self.system_prompt, self.user_name, self.url, self.headers)
        self.message_history.append({"sender_type": "USER", "sender_name": self.user_name, "text": message})
        self.message_history.append(response_message)
        return reply

    def get_conversation(self):
        return get_conversation_from_message_histroy(self.message_history)
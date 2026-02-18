# import anthropic
import json
from groq import Groq
from config import API_KEY, MODEL, MAX_STEPS
from tools.registry import TOOL_SCHEMAS, TOOL_MAP

# client = anthropic.Anthropic(api_key=API_KEY)
client = Groq(api_key=API_KEY)

def load_system_prompt():
    with open('prompts/system.txt') as f:
        return f.read()
    
def run_agent(conversation_history: list) -> str:
    system = load_system_prompt()

    for step in range(MAX_STEPS):
        response = client.chat.completions.create(
            model=MODEL,
            max_tokens=1024,
            messages=[{'role': 'system', 'content': system}] + conversation_history,
            tools=TOOL_SCHEMAS,
            tool_choice='auto'
        )

        message = response.choices[0].message
        finish_reason = response.choices[0].finish_reason
        
        # If Agent is done: return its final message
        if finish_reason == 'stop':
            return message.content
        
        # If Agent wants to use a tool
        if finish_reason == 'tool_calls':
            conversation_history.append({
                'role': 'assistant',
                'content': message.content,
                'tool_calls': [
                    {
                        'id': tc.id,
                        'type': 'function',
                        'function': {
                            'name': tc.function.name,
                            'arguments': tc.function.arguments
                        }
                    }
                    for tc in message.tool_calls
                ]
            })

            for tc in message.tool_calls:
                tool_name = tc.function.name
                tool_args = json.loads(tc.function.arguments)
                print(f"  [tool call] {tool_name}({tool_args})")

                tool_fn = TOOL_MAP.get(tool_name)
                if tool_fn:
                    result = tool_fn(**tool_args)
                else:
                    result = f"Error: tool '{tool_name}' not found."

                conversation_history.append({
                    'role': 'tool',
                    'tool_call_id': tc.id,
                    'content': result
                })
    return 'I lost track of things, could you say that again?'
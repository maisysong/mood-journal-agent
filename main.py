from agent import run_agent

def main():
    print("Mood Journal -- type 'quit' to exit.\n")

    conversation_history = []

    while True:
        user_input = input('You: ').strip()
        if user_input.lower() == 'quit':
            print("Take care of yourself. See you next time.")
            break

        if not user_input: continue

        conversation_history.append({
            'role': 'user',
            'content': user_input
        })

        response = run_agent(conversation_history)

        conversation_history.append({
            'role': 'assistant',
            'content': response
        })

        print(f'\nAgent: {response}\n')
    
if __name__ == "__main__":
    main()
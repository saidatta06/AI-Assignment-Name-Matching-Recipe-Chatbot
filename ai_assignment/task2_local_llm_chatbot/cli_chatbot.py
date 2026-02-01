import requests

API_URL = "http://127.0.0.1:8000/chat"

def run_chatbot():
    print(" Recipe Chatbot (CLI)")
    print("Type ingredients separated by commas.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Bot: Goodbye! ")
            break

        ingredients = [i.strip() for i in user_input.split(",")]

        try:
            response = requests.post(
                API_URL,
                json={"ingredients": ingredients}
            )

            if response.status_code == 200:
                data = response.json()
                print(f"Bot: Suggested Recipe → {data['suggested_recipe']}\n")
            else:
                print("Bot: Error contacting server.\n")

        except Exception as e:
            print("Bot: Server is not running.\n")

if __name__ == "__main__":
    run_chatbot()

import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

def main():
    try:
        # Initialize the Client
        client = AzureOpenAI(
            azure_endpoint=os.getenv("PROJECT_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_KEY"),
            api_version="2024-08-01-preview"
        )

        deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

        print(f"--- Chatting with {deployment_name} ---")

        while True:
            user_input = input("\nYou: ")
            if user_input.lower() in ['exit', 'quit']:
                break

            # This call uses your Deployment Name
            response = client.chat.completions.create(
                model=deployment_name,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ]
            )

            print(f"AI: {response.choices[0].message.content}")

    except Exception as ex:
        print(f"\nERROR: {ex}")

if __name__ == "__main__":
    main()
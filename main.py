from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai.chat_models import GoogleRateLimitError
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv(override=True)


@tool
def calculator(a: float, b: float) -> str:
    """Add two numbers and return the result as a string."""
    return str(a + b)
@tool
def say_hello(name: str) -> str:
    """GREETING THE USER"""
    return(f'hello: {name}, what i can help you for today? ')


def main():
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0)
   

    tools = [calculator]
    agent_executor = create_agent(model, tools)

    print('Hello im Your AI assistant. Type (quit) to exit: ') 
    print('You can ask me to preform calculations and chat with me: ')   

    while True:
        user = input('\nYou: ').strip()

        if user == 'quit':
            break
        print('\nAssistant: ', end='', flush=True)
        try:
            response = agent_executor.invoke(
                {'messages': [HumanMessage(content=user)]}
            )
        except GoogleRateLimitError:
            print(
                'Gemini API quota or rate limit reached. Check your Google AI '
                'Studio usage and billing, or try again after the quota resets.'
            )
            continue
        print(response['messages'][-1].text)

        

if __name__ == '__main__':
    main()

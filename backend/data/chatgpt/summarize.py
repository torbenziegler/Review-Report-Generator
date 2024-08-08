import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

IS_DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY)

SAMPLE_TEXT = """
- Users generally express high satisfaction with the app, often giving it a 5-star rating.
- Comments indicate that users find the app excellent for navigation and trip planning.
- Many users appreciate features like offline maps and the ability to plan trips on a laptop.
- Users describe the app as "the best," "fantastic," and "awesome."
- There are expressions of gratitude towards the app for its usefulness in finding locations and navigating.
- Some users mention it as a go-to tool for discovering new places.
- A few reviews highlight concerns about the future of the app, particularly regarding changes to Google Maps for browsers.
- Overall, the app is perceived positively with users enjoying its functionality and ease of use.
"""

def gpt_decorator(func):
    def wrapper(*args, **kwargs):
        if IS_DEBUG is None:
            print("Missing DEBUG environment variable. Please set the DEBUG environment variable.")
            return SAMPLE_TEXT
        if IS_DEBUG:
            print("Debug mode enabled. Retrieve sample text")
            return SAMPLE_TEXT
        if API_KEY is None:
            print("OpenAI API Key not found. Please set the OPENAI_API_KEY environment variable.")
            return SAMPLE_TEXT
        
        result = func(*args, **kwargs)
        summary = summarize(result)
        print("Summary:", summary)
        return summary
    return wrapper

def summarize(text, model="gpt-4o-mini"):
    print(f"Running {model} to summarize text...")
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"The following are reviews of an app. Create a bullet point list on user perception on the app. Return straight the answer without any additional sentences: \n\n{text}"}
        ],
        max_tokens=150,  # Adjust the token count as needed
        n=1,
        stop=None,
        temperature=0.5,
    )
    summary = completion.choices[0].message.content
    return summary

@gpt_decorator
def summarize_text(text):
    return text

def get_sample_text():
    return SAMPLE_TEXT
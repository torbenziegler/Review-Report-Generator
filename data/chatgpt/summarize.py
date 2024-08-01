import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

IS_DEBUG = bool(os.getenv("DEBUG"))
API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY)

SAMPLE_TEXT = """
Artificial intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think like humans and mimic their actions. The term may also be applied to any machine that exhibits traits associated with a human mind such as learning and problem-solving. The ideal characteristic of artificial intelligence is its ability to rationalize and take actions that have the best chance of achieving a specific goal. A subset of artificial intelligence is machine learning, which refers to the concept that computer programs can automatically learn from and adapt to new data without being assisted by humans. Deep learning techniques enable this automatic learning through the absorption of huge amounts of unstructured data such as text, images, or video.
"""

def summarize_text(text, model="gpt-3.5-turbo"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Summarize the following text:\n\n{text}"}
        ],
        max_tokens=150,  # Adjust the token count as needed
        n=1,
        stop=None,
        temperature=0.5,
    )
    summary = response.choices[0].message['content'].strip()
    return summary

def get_sample_text():
    return SAMPLE_TEXT

def gpt_wrapper(text):
    print("Running GPT-3.5 model to summarize text...")
    print("Input text:", text)
    if IS_DEBUG is None:
        print("DEBUG environment variable not found. Please set the DEBUG environment variable.")
        return SAMPLE_TEXT
    elif IS_DEBUG:
        print("Debug mode enabled. Retrieve sample text")
        print("OpenAI API Key:", API_KEY)
        return SAMPLE_TEXT
    elif API_KEY is None:
        print("OpenAI API Key not found. Please set the OPENAI_API_KEY environment variable.")
        return SAMPLE_TEXT
    else:
        summary = summarize_text(text)
        print("Summary:", summary)
        return summary

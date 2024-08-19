import os
os.environ["OPENAI_API_KEY"]
from openai import OpenAI

def output(thread_id):
    client = OpenAI()

    messages = client.beta.threads.messages.list(
        thread_id=thread_id
    )

    print(messages.data[0].content[0].text.annotations)
    print(messages.data[0].content[0].text.value)


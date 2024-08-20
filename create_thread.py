import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"]

from openai import OpenAI
import csv
CSV_FILENAME = "thread_info.csv"

def create_thread(input_message: str, file_id: str) -> str:
    client = OpenAI()
    
    # Create a thread and attach the file to the message
    thread = client.beta.threads.create(
    messages=[
        {
        "role": "user",
        "content": input_message,
        # Attach the new file to the message.
        "attachments": [
            { "file_id": file_id, "tools": [{"type": "file_search"}, {"type": "code_interpreter"}] }
        ],
        }
    ]
    )
    
    # The thread now has a vector store with that file in its tool resources.
    print("thread.tool_resources.file_search", thread.tool_resources.file_search)

    # Write file_id and assistant_id to a CSV file
    with open(CSV_FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([thread.id])
    
    return thread.id


if __name__ == "__main__":
    input_message = "What is microcluster?"
    file_id = "file-KVTYcwlNECnPGJ5Q6EuiDsgx"
    create_thread(input_message, file_id)
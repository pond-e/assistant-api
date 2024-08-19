import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"]

from openai import OpenAI
client = OpenAI()

file_id = "file-KVTYcwlNECnPGJ5Q6EuiDsgx"
 
# Create a thread and attach the file to the message
thread = client.beta.threads.create(
  messages=[
    {
      "role": "user",
      "content": "What is microcluster?",
      # Attach the new file to the message.
      "attachments": [
        { "file_id": file_id, "tools": [{"type": "file_search"}, {"type": "code_interpreter"}] }
      ],
    }
  ]
)
 
# The thread now has a vector store with that file in its tool resources.
print(thread.tool_resources.file_search)

# Write file_id and assistant_id to a CSV file
import csv

csv_filename = "thread_info.csv"

with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([thread.id])
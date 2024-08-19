import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"]

from openai import OpenAI
client = OpenAI()

name = "Financial Analyst Assistant"
# Assistantの作成
assistant = client.beta.assistants.create(
  name=name,
  instructions="You are an expert financial analyst. Use you knowledge base to answer questions about audited financial statements.",
  model="gpt-4o",
  tools=[{"type": "file_search"}],
)
assistant_id = assistant.id
print("assistant_id:", assistant_id)

# Write file_id and assistant_id to a CSV file
import csv

csv_filename = "assistant_info.csv"

with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([name, assistant_id])



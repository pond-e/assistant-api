import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"]

from openai import OpenAI
client = OpenAI()

pdf_file = "clustream.pdf"

# Fileのアップロード
uploaded_file = client.files.create(
    file=open(pdf_file, "rb"),
    purpose="assistants",
)
file_id = uploaded_file.id
print("file_id:", file_id)

# Write file_id and assistant_id to a CSV file
import csv

csv_filename = "file_info.csv"

with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([pdf_file, file_id])
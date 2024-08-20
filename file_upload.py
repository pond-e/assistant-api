import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"]

from openai import OpenAI
import csv
CSV_FILENAME = "file_info.csv"

def file_upload(pdf_file: str) -> str:
    client = OpenAI()
    # Fileのアップロード
    uploaded_file = client.files.create(
        file=open(pdf_file, "rb"),
        purpose="assistants",
    )
    file_id = uploaded_file.id

    # output csv
    with open(CSV_FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([pdf_file, file_id])

    return file_id

if __name__ == "__main__":
    file_upload("attention_is_all_you_need.pdf")
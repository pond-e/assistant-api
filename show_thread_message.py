import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"]

from openai import OpenAI
OUTPUT_FILENAME = "output.md"

def show_thread_message(thread_id: str, assistant_id: str) -> str:
    client = OpenAI()

    # Use the create and poll SDK helper to create a run and poll the status of
    # the run until it's in a terminal state.

    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread_id, assistant_id=assistant_id
    )

    messages = list(client.beta.threads.messages.list(thread_id=thread_id, run_id=run.id))

    message_content = messages[0].content[0].text
    annotations = message_content.annotations
    citations = []
    for index, annotation in enumerate(annotations):
        message_content.value = message_content.value.replace(annotation.text, f"[{index}]")
        if file_citation := getattr(annotation, "file_citation", None):
            cited_file = client.files.retrieve(file_citation.file_id)
            citations.append(f"[{index}] {cited_file.filename}")

    # Write message_content.value to output.md
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as file:
        file.write(message_content.value)
        file.write("\n".join(citations))

    return message_content.value


if __name__ == "__main__":
    thread_id = "thread_a4jVO5Tc5npSWlE3151IIN5I"
    assistant_id = "asst_QIukNizMCuawDmX3RQAugIfs"
    show_thread_message(thread_id, assistant_id)
import os
os.environ["OPENAI_API_KEY"]
from openai import OpenAI

def check_status(thread_id, run_id) -> bool:
    client = OpenAI()

    # Runのステータスの確認
    run_retrieve = client.beta.threads.runs.retrieve(
        thread_id=thread_id,
        run_id=run_id,
    )
    print(run_retrieve.status)
    return run_retrieve.status == "completed"
    
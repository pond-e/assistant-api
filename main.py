import os
os.environ["OPENAI_API_KEY"]

import time

from openai import OpenAI
from check_status import check_status
from output import output
client = OpenAI()
assistant_id = 'asst_x3hmqarlq8hYxcZwD97NWIQs'

# Threadの作成
empty_thread = client.beta.threads.create()
thread_id = empty_thread.id
print(thread_id)

# Messageの作成
client.beta.threads.messages.create(
    thread_id=thread_id,
    role="user",
    content="日本としてどうすべきか。基本的には３つの戦略について教えて",
)

# Assistantの実行
run = client.beta.threads.runs.create(
    thread_id=thread_id,
    assistant_id=assistant_id,
)
run_id = run.id
print(run_id)

while check_status(thread_id, run_id) == False:
    time.sleep(3)

output(thread_id)
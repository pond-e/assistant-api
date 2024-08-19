import os
os.environ["OPENAI_API_KEY"]

from openai import OpenAI
client = OpenAI()


# Fileのアップロード
uploaded_file = client.files.create(
    file=open("20230217_AIの進化と日本の戦略_松尾研.pdf", "rb"),
    purpose="assistants",
)
file_id = uploaded_file.id
print("file_id:", file_id)

# Assistantの作成
my_assistant = client.beta.assistants.create(
    name="Prompt Engineer Bot",
    description="日本の今後のAI戦略について回答してくれるアシスタント",
    model="gpt-4-1106-preview",
    instructions="あなたは、現在のAIについて詳しいアシスタントです。AIの進化と日本の戦略を参考にして、回答してください。",
    tools=[{"type": "retrieval"}, {"type": "code_interpreter"}],
    file_ids=[file_id],
)
assistant_id = my_assistant.id
print("assistant_id:", assistant_id)

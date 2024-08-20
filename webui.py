import gradio as gr
from create_thread import create_thread
from show_thread_message import show_thread_message

from typing import List, Tuple

def handle_submit(
    user_message: str, file_id: str, assistant_id: str, chat_history: List[Tuple[str, str]]
) -> Tuple[str, List[Tuple[str, str]]]:
    """
    gradioのchatbot機能を使うために必要な関数
    質問文とそれに対する回答のリストを返す
    """
    created_thread_id = create_thread(user_message, file_id)
    bot_message = show_thread_message(created_thread_id, assistant_id)
    chat_history.append((user_message, bot_message))
    return "", chat_history, user_message # return "" で入力がクリアされる


with gr.Blocks() as demo:
    last_user_message = gr.State("") # "session" stateで管理することで他のユーザーと共有しないようにする。

    chatbot = gr.Chatbot()
    chatbot.show_copy_button = True

    regenerate_button = gr.Button("再生成")
    file_id = gr.Textbox(label="attach flie id")
    thread_id = gr.Textbox(label="thread id")
    assistant_id = gr.Textbox(label="assistant id")
    msg = gr.Textbox(label="質問欄")
    with gr.Row():
        submit_button = gr.Button("送信")
        clear = gr.ClearButton([msg, chatbot])
        submit_button.click(handle_submit, inputs=[msg, file_id, assistant_id, chatbot], outputs=[msg, chatbot, last_user_message])
    
    regenerate_button.click(handle_submit, inputs=[last_user_message, file_id, assistant_id, chatbot], outputs=[msg, chatbot])


if __name__ == "__main__":
    demo.launch()
import os
import gradio as gr

def chat_function(message, history):
    response = f"?????{message}"
    history.append((message, response))
    return history, history

chatbot = gr.ChatInterface(
    fn=chat_function,
    title="??????Agent",
    examples=["??", "???", "????????"],
)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    chatbot.launch(
        server_name="0.0.0.0",
        server_port=port,
        share=False,
    )
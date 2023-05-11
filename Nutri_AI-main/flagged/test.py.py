import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a personal Nutritional assistant for everyday diet planning with BMI"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Nutri_AI")

demo.launch(share=True)
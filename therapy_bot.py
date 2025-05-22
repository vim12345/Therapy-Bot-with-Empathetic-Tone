import openai
import os
import gradio as gr
 
# Set your OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")  # Or insert your key directly
 
def therapy_response(user_input):
    messages = [
        {"role": "system", "content": 
         "You are a compassionate and empathetic virtual therapist. "
         "You listen carefully, validate the user's emotions, and offer gentle, supportive guidance. "
         "Do not diagnose or give medical advice. Use a calm, warm tone."},
        {"role": "user", "content": user_input}
    ]
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"
 
iface = gr.Interface(
    fn=therapy_response,
    inputs="text",
    outputs="text",
    title="🧠 EmpathyBot – Virtual Therapy Chat",
    description="Talk about how you're feeling. This bot responds with warmth and kindness. (Not a substitute for real therapy.)"
)
 
iface.launch()
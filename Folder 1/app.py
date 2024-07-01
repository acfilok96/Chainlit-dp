import chainlit as cl
from groq import Groq

Gorq_Key = str("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")

system_prompt = f"""Share response.""" # only exact response, nothing else."""

def ask_order(message, model_name = "llama3-70b-8192", temperature = 0.2):

    client = Groq(api_key = str(Gorq_Key))
        
    chat_completion = client.chat.completions.create(
        messages = 
            [
                {
                    "role": "user",
                    "content": message
                },
                {
                    "role": "system",
                    "content": system_prompt
                }
            ],
            model = model_name,
            temperature = temperature
            )
    
    return chat_completion.choices[0].message.content
 

@cl.on_message
async def main(message: cl.Message):
    
    response =  ask_order(message.content)

    # Send a response back to the user
    await cl.Message(content = response,).send()
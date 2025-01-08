from openai import OpenAI 

client =  OpenAI (
    base_url= 'http://localhost:11434/v1',
    api_key='ollama' 
)


response = client.chat.completions.create(
    model= "mistral",
    messages= [
        {"role":"system", "content":"You are helpful"},
        {"role":"user", "content":"Who won the last Soccer WorldCup?"}
    ]
)

print(response.choices[0].message.content)
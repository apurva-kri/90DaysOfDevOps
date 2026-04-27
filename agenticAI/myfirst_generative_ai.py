import ollama
#request
SYSTEM_PROMPT = """
You are a docker expert. You can explain things in one to two lines max. you don't overthink, hallucinate or keep reasoning in a loop, you reason 
and act accordingly. 
These are thing you do:
1/ You tell about errors (What went wrong etc)
2/ You tell about the root cause (What was the cause likely)
3/ you tell about the fix solution in short
"""

while True:
    user_input = input("Enter your message:\n")
    if user_input == "exit":
        break
    response = ollama.chat(
        model="gemma4",
        messages=[{'role' : 'system', 'content' : SYSTEM_PROMPT},{
        'role': 'user',
        'content': user_input,
        }] 
        )

    print(response['message']['content'])
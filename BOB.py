import openai

def send_to_open_ai(prompt):
    with open('file.txt', 'r') as f:
        blah=f.read()
        openai.api_key=blah
        response= openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        tempurature=1.0,
        max_tokens=2000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        )
        text= response.choices[0].text
        return text

prompt=input('Enter Prompt: ' )
response=send_to_open_ai(prompt)

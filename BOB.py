import requests
import json
import pyperclip


import warnings


warnings.filterwarnings("ignore")

with open('file.txt', 'r') as f:
    blah=f.read()

while True:
    clear_clipboard=pyperclip.copy('')
    prompt=input('\nEnter Prompt And/OR copy content: ')
    paste_clipboard = pyperclip.paste()
    prompt=prompt + ('\n'+paste_clipboard)
    url = 'https://api.openai.com/v1/completions'
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer '+blah}
    data = {
      "model": "text-davinci-003",
      "prompt": prompt,
      "temperature": 0.3,
      "max_tokens": 521,
      "top_p": 1,
      "frequency_penalty": 0,
      "presence_penalty": 0
    }

    response = requests.post(url, headers=headers, json=data,verify=False)
    

    data = json.loads(response.text)
    
    try:
        print((data)['choices'][0]['text'])
        
    except Exception as e:
        print(response.text)

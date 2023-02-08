from flask import Flask, request, render_template
import requests
import json
import warnings


warnings.filterwarnings("ignore")
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        name =  request.form['name']
        
        with open('chat.txt', 'a') as ifile:
            ifile.write("Question: \n"+name+"\n")
        
        url = 'https://api.openai.com/v1/completions'
        headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer APIKEY'}
        data = {
            "model": "text-davinci-003",
            "prompt": name,
            "temperature": 0.3,
            "max_tokens": 521,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0
        }
        response = requests.post(url, headers=headers, json=data,verify=False)
        data = json.loads(response.text)
        databob=(data)['choices'][0]['text']
        with open('chat.txt', 'a') as ifile:
            ifile.write("Answer: \n"+databob+"\n")
        return '<body> <br></br><h4>' + databob + '</h4><br></br></body>' + '''<form method="POST">
                  Ask me anything: <input style="height:50px;width:75%;font-size:14pt;" type="text" name="name">
                  <br></br>
                  <input type="submit" value="Submit">
              </form>'''
        
    return '''<form method="POST">
                  <br></br>
                  Ask me anything: <input style="height:50px;width:75%;font-size:14pt;" type="text" name="name">
                  <br></br>
                  <input type="submit" value="Submit">
              </form>'''

if __name__ == "__main__":
    app.run(host= '0.0.0.0',port=50050)

from flask import Flask, render_template, request,redirect
import flask
import sys
import json
import datetime

app = flask.Flask(__name__)
app.config["DEBUG"] = True
@app.route('/', methods=['GET', 'POST'])
def home():
        if request.form.get('submit') == 'submit':
                name = request.form.get('string')
                if 'Electrical' in str(name):
                        #return f'<center><h1 color = "red" >Welcome</h1><br><b> Enter String : <form method="post"> <input type = "text" name = "string"><br><input type = "submit" name = "submit" value = "submit"><input type = "submit" value = "Retrive" name = "Retrive"></form><br><h1>OOPS! String contains Electrical</h1></center>'
                        return '<script>function Redirect() {window.location = "https://picsum.photos/200/300";}</script><center><h1>OOPS! String contains Electrical</h1><br><input type = "button" name = "ok" value = "ok" onclick = "Redirect()"> </center>'
                        #return redirect('https://picsum.photos/200/300')
                data = {f'{name}':f'{datetime.datetime.now()}'}
                with open('data.json', 'w') as outfile:
                        json.dump(data, outfile)
                return f'<center><h1 color = "red" >Welcome</h1><br><b> Enter String : <form method="post"> <input type = "text" name = "string"><br><input type = "submit" name = "submit" value = "submit"><input type = "submit" value = "Retrive" name = "Retrive"></form><br><h1>String recorded successfully</h1></center>'
        if request.form.get('Retrive') == 'Retrive':
                print('entered')
                with open('data.json', 'r') as outfile1:
                        data1 = json.load(outfile1)
                print(data1)
                for key, value in data1.items():
                        Key = key
                        Value = value
                return f'<center><h1 color = "red">Welcome</h1><br><b> Enter String : <form method="post"> <input type = "text" name = "string"><br><input type = "submit" name = "submit" value = "submit"><input type = "submit" value = "Retrive" name = "Retrive"></form><br><h1> {Key} :- {Value}</h1></center>'
        return '<center><h1 color = "red">Welcome</h1><br><b> Enter String : <form method="post"> <input type = "text" name = "string"><br><input type = "submit" name = "submit" value = "submit"><input type = "submit" value = "Retrive" name = "Retrive"></form></center>'
 
app.run()

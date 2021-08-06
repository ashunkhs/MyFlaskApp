from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('layout.html')


@app.route('/', methods=['POST'])
def my_form_post():
    uid = request.form['uid']
    pwd = request.form['pwd']
    
    if uid == "a@gmail.com" :
        if pwd == "123" :
            return render_template('Base.html')
        else:
            processed_text = "Incorret password . Please try again"
    else:
            processed_text = "Incorret username . Please try again"

    return processed_text
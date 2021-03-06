from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)

app.config['DEBUG'] = True  

form = """
<!doctype html>

<html>
    <head>
        <style>
            form {{
                background-color: red;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>


        <form method ="post">
            <div>
                <label for="rot">Rotate by:</label>
                <input name="rot" value="0" type="text">
                <p class="error"></p>
            </div>
            <textarea type="text" name="text">{0}</textarea>
            <br>
            <input type="submit">
        </form>        
    </body>
</html>
"""
@app.route("/")
def index():
    return form.format('')


@app.route("/", methods=['POST'])
def encrypt():
    text = request.form['text']
    rot = request.form['rot']
    rot = int(rot)
    encrypted = ""
    for char in text:
        message = rotate_string(char, rot)
        encrypted = encrypted + message
    return form.format(encrypted) 



app.run()
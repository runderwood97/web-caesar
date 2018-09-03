from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form method = "POST">
            <p>Rotate By: <input type = "text" name = "rot" value = "0"/></p>
            <p><textarea name = "text" ></textarea></p>
            <p><input type = "submit" name = "Submit" value = "Submit Query" /></p>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

app.run()
from flask import request, redirect, render_template, session, flash, Flask
import cgi

app = Flask(__name__)

def getBinMsg(msg):
    lst = []
    for char in msg:
        lst.append(ord(char))

    msg = ""
    for each in lst:
        msg += "{0:b}".format(each)

    return msg 

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def indexkPost():
    plaintext = request.form['plaintext']
    bintext = getBinMsg(plaintext)

    return render_template("index.html", bintext=bintext)

if __name__ == "__main__":
    app.run()
from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2
from validation import *

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/", methods=['POST'])
def indexPost():
    uname = cgi.escape(request.form['uname'])
    pwd = cgi.escape(request.form['pwd'])
    vpwd = cgi.escape(request.form['vpwd'])
    email = cgi.escape(request.form['email'])

    uname_error = ""
    pwd_error = ""
    vpwd_error = ""
    email_error = ""

    if not valid_uname(uname):
        uname_error = "Invalid username"
        uname = ""
    if not valid_pwd(pwd):
        pwd_error = "Invalid password"
    if pwd != vpwd:
        vpwd_error = "Passwords do not match"
    if not valid_email(email) and not is_empty(email):
        email_error = "Invalid email"
        email = ""
    
    if uname_error != "" or pwd_error != "" or vpwd_error != "" or email_error != "":
        return render_template('form.html', uname=uname, email=email, uname_error = uname_error, pwd_error = pwd_error, vpwd_error = vpwd_error, email_error = email_error)
    else:
        return render_template('welcome.html', uname=uname)


if __name__ == "__main__":
    app.run()
        

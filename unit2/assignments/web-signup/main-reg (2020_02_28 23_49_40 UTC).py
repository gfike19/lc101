from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2
import re

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

uname_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_uname(uname):
    return uname_re.match(uname)

pwd_re = re.compile(r"^.{3,20}$")
def valid_pwd(pwd):
    return pwd_re.match(pwd)

email_re = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
    return email_re.match(email)

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

    if valid_uname(uname) == False:
        uname_error = "Invalid username"
    if valid_pwd(pwd) == False:
        pwd_error = "Invalid password"
    if pwd != vpwd:
        vpwd = "Passwords do not match"
    if email != "" and valid_email(email) == False:
        email_error = "Invalid email address"

    if uname_error != "" or pwd_error != "" or vpwd_error != "" or email_error != "":
        return render_template('form.html', uname=uname, email=email, uname_error = uname_error, pwd_error = pwd_error, vpwd_error = vpwd_error, email_error = email_error)
    else:
        return render_template('welcome.html', uname=uname)

if __name__ == "__main__":
    app.run()

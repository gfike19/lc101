from flask import request, redirect, render_template, session, flash, Flask
import cgi
from validation import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True      
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://blogz:blogz@localhost:3306/blogz'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = 'some secret key'

db = SQLAlchemy(app)

class Blog(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(200))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, title, body):
        self.title = title
        self.body = body
        self.owner = owner

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    pwd = db.Column(db.String(20))
    blogs = db.relationship('Blog', backref='user')

    def __init__(self, username, password):
        self.username = username
        self.paswword = password


@app.before_request
def require_login():
    allowed_routes = ['index', 'blog', 'login', 'register', 'user']
    if request.endpoint not in allowed_routes and 'user' not in session:
        return redirect('/login')

@app.route("/", methods=['GET'])
def index():
    
    if request.method == "GET":
        users = User.query.all()
        return render_template("index.html", users=users)

@app.route("/login", methods=['GET', 'POST'])
def login():
    
    if request.method == "POST":
        error = ""

        uname = request.form['uname']
        pwd = request.form['pwd']

        old_user = User.query.filter_by(name=uname).first()

        if not old_user:
            error += "Username not found<br>"
            return render_template("login.html", error=error)
        else:
            vpwd = old_user.password

            if vpwd != pwd:
                error += "Incorrect password<br>"
                return render_template("login.html", error=error)
            else:
                session['user'] = uname
                return redirect("/newpost")
    return render_template("login.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        error = ""

        uname = request.form['uname']
        pwd = request.form['pwd']
        vpwd = request.form['vpwd']

        old_user = User.query.filter_by(username=uname).first()

        if old_user:
            error += "Username already in use <br>"
        elif not valid_uname(uname):
            error += "Invalid username<br>"
        elif not valid_pwd(pwd):
            error += "Invalid password<br>"
        elif vpwd != pwd:
            error += "Passwords do not match"
        
        else:
            user = User(uname, pwd)
            db.session.add(user)
            db.session.commit()
            session['user'] = uname
            return redirect("/newpost")

@app.route("/newpost", methods=['GET','POST'])
def newpost():
    if request.method == 'GET':
        return render_template('newpost.html')
    if request.method == "POST":
        error = ""

        title = request.form['title']
        body = request.form['body']

        if title == "" or body == "":
            error = "One or more fields are empty<br>"
            return render_template("newpost.html", error=error)
        
        uname = session['user']
        user = User.query.filter_by(username=uname).first()
        blog = Blog(title, body, user)
        db.session.add(blog)
        db.session.commit()

        new_blog = Blog.query.filter_by(title=title).first()
        blog_id = new_blog.id
        url = "/blog?blog_id=" + str(blog_id)

        return redirect(url)

@app.route("/blog", methods=['GET'])
def blog():
    if request.method =="GET":
        blog_id = request.args.get('blog_id')
        if blog_id:
            blog = Blog.query.filter_by(id=blog_id).first()
            return render_template("blog.html", blog=blog)

if __name__ == "__main__":
    app.run()
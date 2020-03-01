from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://thebestiary@localhost:8889/thebestiary'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Monster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    descr = db.Column(db.String(500))

    def __init__(self, name, descr):
        self.name = name
        self.descr = descr

@app.route("/")
def index():
    if request.method == "GET":
        all_mons = Monster.query.all()
        return render_template("index.html", all_mons = all_mons)
    return "error.html"


@app.route("/add", methods=['GET', 'POST'])
def add():
    
    if request.method == "GET":
        return render_template("add.html")

    if request.method == "POST":
        error = ""

        name = request.form['name']
        descr = request.form['descr']

        if name == "" or len(name) > 120:
            error += "Invalid name <br>"
        
        if descr == "":
            descr += "Too terrifying for words."
        
        if len(descr) > 500:
            error += "Descriptions need to be succint <br>"
        
        if not error:
            mons = Monster(name, descr)
            db.session.add(mons)
            db.session.commit()
            return render_template("index.html")
        else:
            return render_template("add.html", error=error)


app.run()
from flask import request, redirect, render_template, session, flash, Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True      
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:password@localhost:3306/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Blog(db.Model):
        
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(200))

    def __init__(self, title, body):
        self.title = title
        self.body = body


@app.route("/", methods=['GET'])
def index():
    blogs = Blog.query.all()
    return render_template("index.html", blogs=blogs)

@app.route("/newBlog", methods=['GET','POST'])
def newBlog():

    if request.method == 'GET':
        return render_template("form.html")
    
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        blog = Blog(title, body)
        db.session.add(blog)
        db.session.commit()
        query_param_url = "/blog?id=" + str(blog.id)

        return redirect(query_param_url)

@app.route("/blog", methods=['GET'])
def viewBlog():

    if request.args:
        blogId = request.args.get("id")
        blog = Blog.query.get(blogId)

        return render_template("singleBlog.html", blog=blog)


if __name__ == "__main__":
    app.run()
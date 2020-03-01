from flask import Flask, request
app = Flask(__name__)
app.config['DEBUG'] = True

some_html = """ 
<!DOCTYPE html>
<html>
<body>
Last text inputted was: {0}
<form method="post">
<input type="text" name="val"/>
<button type="submit">submit</submit>
</form>
</body>
</html>
"""

@app.route("/")
def index():
    return some_html.format("")

@app.route("/", methods=['POST'])
def take2():
    val = request.form["val"]
    
    return some_html.format(val)

app.run()
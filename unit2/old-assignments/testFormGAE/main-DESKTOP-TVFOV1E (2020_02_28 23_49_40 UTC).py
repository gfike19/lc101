form = """<!DOCTYPE html>
<html>
<head>
    <title>Test</title>
</head>
<body>
    <form action = "/input" method = "post">
    <label> This is a test:
    <input type = "text" name = "box" />
    words
    </label>
    <input type = "submit"/>
    </form>
</body>
</html>
"""
import webapp2

class Index(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)

    def post(self):
        self.response.write(string.replace(form,"words","blah blah blah"))

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)

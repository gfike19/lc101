form = """
<!DOCTYPE html>
<html>
<head>
    <title>Test</title>
</head>
<body>
<form action = "display">
    <label>%(words)s</label>
</form>
</body>
</html>
"""
import webapp2

class Index(webapp2.RequestHandler):
    def write_page(self, words = ""):
        self.response.write(form % {"words":words})

    def get(self):
        self.write_page()

class display(webapp2.RequestHandler):
    def write_page(self, words = ""):
        self.response.write(form % {"words":words})

    def post(self):
        self.write_page(words = "blah blah blah")


app = webapp2.WSGIApplication([
    ('/', Index),
    ('/display', display)
], debug=True)

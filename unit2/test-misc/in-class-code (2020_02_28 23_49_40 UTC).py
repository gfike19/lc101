import cgi
import webapp2



# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>FlickList</title>
</head>
<body>
    <h1>FlickList</h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

def getCurrentWatchList(self):
    #return current watch list
    watch-lst = ["Maltilda","Independence Day","Saw 5"]

    return watch-lst

def getUnwanted():
    bad-movies = ['Saw 6', 'Dirty Dancing']
    return bad-movies

class Index(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
        e.g. www.flicklist.com/
    """

    def get(self):
        eorr = self.request.get['error']
        edit_header = "<h3>Edit My Watchlist</h3>"

        # a form for adding new movies
        add_form = """
        <form action="/add" method="post">
            <label>
                I want to add
                <input type="text" name="new-movie"/>
                to my watchlist.
            </label>
            <input type="submit" value="Add It"/>
        </form>
        """

        #make a string containing options for the remove form

        options = ""

        for movie in getCurrentWatchList():
            options += '<option value = "{0}">{0}</option>'.format(cgi.escape(movie, quote = "True"))

            #0 are for referring to parameters

        movie_list.append(self.request.get("new-movie"))

        # TODO 1
        # Include another form so the user can "cross off" a movie from their list.

            # a form for adding new movies
            remove_form = """
            <form action="/remove" method="post">
                <label>
                    I want to remove
                    <input type="text" name="old-movie"/>
                    from my watchlist.
                </label>
                <input type="submit" value="Remove It"/>
            </form>
            """.format(options)
            movie_list.remove(self.request.get("old-movie"))


        # TODO 4 (Extra Credit)
        # modify your form to use a dropdown (<select>) instead a
        # text box (<input type="text"/>)


        response = page_header + edit_header + add_form + remove_form + page_footer
        self.response.write(response)


class AddMovie(webapp2.RequestHandler):
    """ Handles requests coming in to '/add'
        e.g. www.flicklist.com/add
    """

    def post(self):
        # look inside the request to figure out what the user typed
        new_movie = self.request.get("new-movie")

        if new_movie in getUnwanted():
            error = "{} is not the movie you are looking for".format(movie)#don't need to escape since you are doing it on the next line
            self.redirect('/?error={}'.format(cgi.escape(error, quote = "True"))) #root directory so user knows what's going on, error so we can handle error
            # self.repsonse.write("<br>Bad movies, pick another") not this


        # build response content
        new_movie_element = "<strong>" + new_movie + "</strong>"
        sentence = new_movie_element + " has been added to your Watchlist!"

        response = page_header + "<p>" + sentence + "</p>" + page_footer
        self.response.write(response)


# TODO 2
# Create a new RequestHandler class called CrossOffMovie, to receive and
# handle the request from your 'cross-off' form. The user should see a message like:
# "Star Wars has been crossed off your watchlist".

class RemoveMovie(webapp2.RequestHandler):

    def post(self):
        # look inside the request to figure out what the user typed
        old_movie = self.request.get("old-movie")

        # build response content
        old_movie_element = "<strike>" + old_movie + "</strike>"
        sentence = old_movie_element + " has been removed from your Watchlist!"

        response = page_header + "<p>" + sentence + "</p>" + page_footer
        self.response.write(response)



# TODO 3
# Include a route for your cross-off handler, by adding another tuple to the list below.
app = webapp2.WSGIApplication([
    ('/', Index),
    ('/add', AddMovie),
    ('/remove', RemoveMovie)
], debug=True)

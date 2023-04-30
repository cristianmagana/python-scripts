import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create SQL lol
books = [
    {'id': 0,
     'title': 'book1',
     'author': 'author',
     'first_sentence': 'Tis was data',
     'year_published': '1990'},
    {'id': 1,
     'title': 'book2',
     'author': 'some dude',
     'first_sentence': 'Tis was another first sentence',
     'published': '1983'},
    {'id': 2,
     'title': 'book3',
     'author': 'authorette',
     'first_sentence': 'something about something',
     'published': '1989'}
]

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Cozy Coffee Book Club</h1>
<p>An Api for the hipsters.</p>'''


# A route to return books
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api.v/1/users/<user_id>', methods = ['GET', 'POST', 'DELETE'])
def user(user_id):
    if request.method == 'GET':
        """return the information for <user_id>"""
        .
        .
        .
    if request.method == 'POST':
        """modify/update the information for <user_id>"""
        # you can use <user_id>, which is a str but could
        # changed to be int or whatever you want, along
        # with your lxml knowledge to make the required
        # changes
        print(request.body)
        .
        .
        .
    if request.method == 'DELETE':
        """delete user with ID <user_id>"""
        .
        .
        .
    else:
        # POST Error 405 Method Not Allowed
        .
        .
        .  

app.run()
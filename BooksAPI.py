import flask
import psycopg2
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True



conn = psycopg2.connect("dbname=postgres user=postgres password=pass host=localhost")

cur = conn.cursor()


@app.route('/', methods=['GET'])
def home():
    return '''<h1>OPENMESSAGE</h1>
<p>API assignment</p>'''


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():

    return jsonify(listReset())

@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.


    listReset()

    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in listReset():
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)


def listReset():
    list = []

    cur.execute("SELECT id, title, author, sentence, year_made from books")

    rows = cur.fetchall()

    for user in rows:
        mydict={}

        mydict['id'] = user[0]
        mydict['title'] = user[1]
        mydict['author'] = user[2]
        mydict['first_sentence'] = user[3]
        mydict['year_published'] = user[4]
        list.append(mydict)

    return list

app.run()

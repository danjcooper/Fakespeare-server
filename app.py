from flask import Flask
import json
from flask.json import jsonify
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
from sqlalchemy import create_engine
import os
import random

load_dotenv()

app = Flask(__name__)
CORS(app)

# DB init
db_string = os.getenv("DB_URL")
db = create_engine(db_string)
test = db.execute("SELECT * FROM book_input_book")  
results = [dict(row) for row in test]


@app.route('/')
@cross_origin()
def index():
    return jsonify(results)

# Send back a random book.
# Get an array from the client of which index's have already been used.
@app.route('/random')
@cross_origin()
def random_book():
    book_length = len(results)
    random_index = random.randint(0, book_length -1)
    return jsonify(results[random_index])

@app.route('/shuffle')
@cross_origin()
def shuffled_books():
    random.shuffle(results)
    return jsonify(results)

@app.route('/play/<int:number_of_books>')
@cross_origin()
def get_game_books(number_of_books):
    if number_of_books > len(results):
        return

    random.shuffle(results)

    output = []
    for book in range(number_of_books):
        output.append(results[book])
    return jsonify(output)

if __name__ == "main":
    app.run(debug=False)
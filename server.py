from flask import Flask
from flask.json import jsonify
from flask_cors import CORS

import random


server = Flask(__name__)
CORS(server)

book_data = [
  {
    "book_id": 1,
    "title": "Frankenstein",
    "author": "Mary Shelly",
    "blurb": "Victor Frankenstein is a scientist obsessed with generating life from lifeless matter. He subsequently manages to create a horrifying, sentient creature assembled from pieces of stolen body parts. Shunned by society and faced with eternal isolation, the creature becomes murderous with revenge against the one who brought him into existence, Frankenstein.",
    "first_line": "You will rejoice to hear that no disaster has accompanied the commencement of an enterprise which you have regarded with such evil forebodings.",
    "last_line": "He was soon borne away by the waves, and lost in darkness and distance."
  },
  {
    "book_id": 2,
    "title": "Pride and Prejudice",
    "author": "Jane Austin",
    "blurb": "The only thing in the world that matters to Mrs Bennett, is marrying all five of her daughters to rich, landed gentlemen. So when two wealthy young gentlemen move to town, she vows that at least one of her daughters will marry into their fortunes. Jane and Elizabeth, her eldest daughters, soon discover that love is rarely straightforward and is often surprising. Because, surely that sullen, quiet, mysterious Mr Darcy can't be more than he seems . . . can he?",
    "first_line": "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.",
    "last_line": "and they were both ever sensible of the warmest gratitude towards the persons who, by bringing her into Derbyshire, had been the means of uniting them."
  },
  {
    "book_id": 3,
    "title": "1984",
    "author": "George Orwell",
    "blurb": "Winston Smith works for the Ministry of Truth in London, chief city of Airstrip One. Big Brother stares out from every poster, the Thought Police uncover every act of betrayal. When Winston finds love with Julia, he discovers that life does not have to be dull and deadening, and awakens to new possibilities. Despite the police helicopters that hover and circle overhead, Winston and Julia begin to question the Party; they are drawn towards conspiracy. Yet Big Brother will not tolerate dissent - even in the mind. For those with original thoughts they invented Room 101. . ",
    "first_line": "It was a bright cold day in April, and the clocks were striking thirteen.",
    "last_line": "He loved Big Brother."
  }
  

]


@server.route('/')
def index():
    return jsonify(book_data)

# Send back a random book.
# Get an array from the client of which index's have already been used.
@server.route('/random')
def random_book():
    book_length = len(book_data)
    random_index = random.randint(0, book_length -1)
    return jsonify(book_data[random_index])

@server.route('/shuffle')
def shuffled_books():
    random.shuffle(book_data)
    print(book_data)
    return jsonify(book_data)

server.run(debug=True)
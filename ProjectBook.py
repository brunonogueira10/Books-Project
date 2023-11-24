from flask import Flask,jsonify, request

app = Flask(__name__)

books = [
    {
        'id': 1,
        'tittle': 'Ruined King',
        'autor': 'J.K. lion',
    },
    {
        'id': 2,
        'tittle': 'Stop and Drive',
        'autor': 'Bryan Gospel',
    },
    {
        'id': 3,
        'tittle': 'Baby queen',
        'autor': 'Clarisse Liss',
    },
    {
        'id': 4,
        'tittle': 'View FrontEnd',
        'autor': 'Lara Louis',
    },
]

#Consult(all)

@app.route('/books',methods=['GET'])
def obter_books():
    return jsonify(books)

#Consult(ID)

@app.route('/books/<int:id>',methods=['GET'])
def obter_book_for_id(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)

#Edit

@app.route('/books/<int:id>',methods=['PUT'])
def edit_book_for_id(id):
    book_change = request.get_json()
    for indice,book in enumerate(books):
        if book.get('id') == id:
            books[indice].update(book_change)
            return jsonify(books[indice])

#Create

@app.route('/books',methods=['POST'])
def include_new_book():
    new_book = request.get_json()
    books.append(new_book)

#Delete

@app.route('/books/<int:id>',methods=['DELETE'])
def delete_book(id):
    for indice, book in enumerate(books):
        if book.get('id') == id:
            del books[indice]

    return jsonify(books)




app.run(port=5000,host="localhost",debug=True)

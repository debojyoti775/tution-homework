from flask import Flask
app = Flask(__name__)

@app.route('/book')
def home():
    books = ["sherlock Holmes", "Feluda", "crime and punishment", "Macbeth", "ANSI C"]
    return books

if __name__ == '__main__':
    app.run(debug=True)
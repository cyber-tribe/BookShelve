from flask import *
import db

app = Flask(__name__)

@app.route("/")
def index():
    books = db.get_book()
    return render_template("index.html",books=books)


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, url_for, request
app = Flask(__name__)


from zasady import *


from db import *


@app.route('/migrate', methods=['GET'])
def migrate():
    init_db()
    return "migracja"


@app.route('/', methods=['POST', 'GET'])
def index():
    slowko = ""
    query = query_db("SELECT * FROM slowko");
    print(query)

    cursor = get_db()
    if request.method == "POST":
        slowko = request.form['slowko']
        tlumaczenie = request.form['tlumaczenie']
        if not litery(slowko):
            return render_template('error.html')

        slowko = transkrypca_fonetyczna(slowko)


    return render_template('index.html', slowko=slowko)


@app.route('/opis')
def opis():
    return render_template('opis.html')


@app.route('/dodaj')
def dodaj():
    return render_template('dodaj.html')


"""if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5019, debug=True)

if __name__ == '__main__':
    app.run()"""

if __name__ == '__main__':
    app.run()


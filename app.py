from flask import (
    render_template, request
)
from zasady import *
from db import *


@app.route('/migrate', methods=['GET'])
def migrate():
    init_db()
    return "migracja"


@app.route('/', methods=['POST', 'GET'])
def index():
    slowo = ""

    tlumaczenie = ""
    query = query_db("SELECT * FROM slowko")
    print(query)

    if request.method == "POST":
        slowo = request.form['slowo']
        if not litery(slowo):
            return render_template('error.html')

        tlumaczenie = transkrypca_fonetyczna(slowo)

    return render_template('index.html', tlumaczenie=tlumaczenie, slowo=slowo)

@app.route('/opis')
def opis():
    return render_template('opis.html')


@app.route('/dodaj', methods=['GET', 'POST'])
def dodaj():

    if request.method == "POST":
        slowko = request.form['slowo']

        if not litery(slowko):
            return render_template('error.html')

        id = len(query_db("SELECT * FROM slowko")) + 1

        query_db("INSERT INTO slowko values ({0}, '{1}')".format(id, slowko))

        return render_template('dodaj.html', status=True, slowko=slowko)

    return render_template('dodaj.html', status=False)


"""if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5019, debug=True)
"""

if __name__ == '__main__':
    app.run()
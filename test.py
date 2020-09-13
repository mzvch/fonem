from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


    def index():
        if request.method == "POST":
            slowko = request.form['slowko']
            tlumaczenie = request.form['tlumaczenie']
            if not litery(slowko):
                return render_template('error.html')

            slowko = transkrypca_fonetyczna(slowko)


        return render_template('index.html', slowko=slowko)



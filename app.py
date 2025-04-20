from flask import Flask, render_template, request, url_for
from bereshit import bereshit_cont

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/bereshit')
def bereshit():
    spanish_verses = bereshit_cont['cap_1']['spanish']
    hebrew_verses = bereshit_cont['cap_1']['hebrew']
    phonetics_verses = bereshit_cont['cap_1']['phonetics']

    return render_template('bereshit.html', español=spanish_verses, hebreo=hebrew_verses, fonetica=phonetics_verses)



if __name__=='__main__':
    app.run(debug=True)
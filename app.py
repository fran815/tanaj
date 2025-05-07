from flask import Flask, render_template, request, url_for
from bereshit import bereshit_cont

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/bereshit')
def bereshit():
    spanish_verses = bereshit_cont
    hebrew_verses = bereshit_cont
    phonetics_verses = bereshit_cont

    return render_template('bereshit.html', español=spanish_verses, hebreo=hebrew_verses, fonetica=phonetics_verses)


@app.route('/tefilot')
def tefilot():
    return render_template('tefilot.html')


@app.route('/alef-bet')
def alphabet():
    return render_template('alphabet.html')


if __name__=='__main__':
    app.run(debug=True)
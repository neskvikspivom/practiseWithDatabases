from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users')
def users():  # put application's code here
    conect = sqlite3.connect('identifier.sqlite')
    cursor = conect.cursor()
    data = cursor.execute('SELECT * FROM users').fetchall()
    return render_template('userslist.html', seq=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
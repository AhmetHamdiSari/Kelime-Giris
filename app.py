import os
import json
from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

DEFAULT_USERNAME = 'ahs'
DEFAULT_PASSWORD = 'ahs'


WORDS_DATA_FILE = 'data/words.json'


def load_words():
    if not os.path.exists(WORDS_DATA_FILE):
        return []
    with open(WORDS_DATA_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_words(words):
    with open(WORDS_DATA_FILE, 'w') as f:
        json.dump(words, f)

@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    words = load_words()
    return render_template('index.html', words=words)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if os.path.exists('data/users.json'):
            with open('data/users.json', 'r') as f:
                users = json.load(f)
        else:
            users = []
        
        
        for user in users:
            if user['username'] == username and user['password'] == password:
                session['username'] = username
                return redirect(url_for('index'))
        
        flash('Invalid username or password', 'danger')
    
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/add_word', methods=['GET', 'POST'])
def add_word():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        word = request.form['word']
        definition = request.form['definition']
        words = load_words()
        words.append({'word': word, 'definition': definition})
        save_words(words)
        flash('Word added successfully', 'success')
        return redirect(url_for('index'))
    return render_template('add_word.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        

        user_data = {'username': username, 'password': password}
        

        if os.path.exists('data/users.json'):
            with open('data/users.json', 'r') as f:
                users = json.load(f)
        else:
            users = []
        

        users.append(user_data)
        

        with open('data/users.json', 'w') as f:
            json.dump(users, f)
        
        flash('Registration successful', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    return render_template('forgot_password.html')



if __name__ == '__main__':
    if not os.path.exists('data'):
        os.makedirs('data')
    if not os.path.exists(WORDS_DATA_FILE):
        with open(WORDS_DATA_FILE, 'w') as f:
            json.dump([], f)
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, session
from flask_bootstrap import Bootstrap
import sqlite3

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Change this to a secure random key
bootstrap = Bootstrap(app)

# Connect to the SQLite database
conn = sqlite3.connect('citizendevs.db', check_same_thread=False)
c = conn.cursor()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        c.execute("SELECT * FROM user WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        if user:
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error=True)
    return render_template('login.html', error=False)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        task1 = 'To Do'
        task2 = 'To Do'
        try:
            c.execute("INSERT INTO user (username, password, task1,  task2) VALUES (?, ?, ?, ?)", (username, password, task1, task2))
            conn.commit()
            session['username'] = username
            return redirect(url_for('dashboard'))
        except sqlite3.IntegrityError:
            # If the username already exists, show an error message
            return render_template('signup.html', error=True)
    return render_template('signup.html', error=False)

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']
        c.execute("SELECT * FROM user")
        users = c.fetchall()
        return render_template('dashboard.html', username=username, users=users)
    return redirect(url_for('login'))

@app.route('/update/<username>', methods=['GET', 'POST'])
def update(username):
    if request.method == 'POST':
        status1 = request.form['status1']
        status2 = request.form['status2']
        c.execute("UPDATE user SET task1=?, task2=? WHERE username=?", (status1, status2, username))
        conn.commit()
        return redirect(url_for('dashboard'))
    else:
        c.execute("SELECT * FROM user WHERE username=?", (username,))
        user = c.fetchone()
        return render_template('update.html', username=username, user=user)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

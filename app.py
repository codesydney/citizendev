from flask import Flask, render_template, request, redirect, url_for, session
from flask_bootstrap import Bootstrap
import sqlite3

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Change this to a secure random key
bootstrap = Bootstrap(app)

# Connect to the SQLite database
conn = sqlite3.connect('./citizendevs.db', check_same_thread=False)
c = conn.cursor()

@app.route('/app', methods=['GET', 'POST'])
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

@app.route('/app/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        PY4E1 = 'To Do'
        PY4E2 = 'To Do'
        PY4E3 = 'To Do'
        PY4E4 = 'To Do'     
        PY4E5 = 'To Do'
        PY4E6 = 'To Do'
        PY4E7 = 'To Do'
        PY4E8 = 'To Do'
        PY4E9 = 'To Do'
        PY4E10 = 'To Do'
        PY4E11 = 'To Do'
        PY4E12 = 'To Do'     
        PY4E13 = 'To Do'
        PY4E14 = 'To Do'
        PY4E15 = 'To Do'
        PY4E16 = 'To Do'                    
        try:
            c.execute("INSERT INTO user (username, password, PY4E1, PY4E2, PY4E3, PY4E4, PY4E5, PY4E6, PY4E7, PY4E8, PY4E9, PY4E10, PY4E11, PY4E12, PY4E13, PY4E14, PY4E15, PY4E16 ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (username, password, PY4E1, PY4E2, PY4E3, PY4E4, PY4E5, PY4E6, PY4E7, PY4E8, PY4E9, PY4E10, PY4E11, PY4E12, PY4E13, PY4E14, PY4E15, PY4E16))
            conn.commit()
            session['username'] = username
            return redirect(url_for('dashboard'))
        except sqlite3.IntegrityError:
            # If the username already exists, show an error message
            return render_template('signup.html', error=True)
    return render_template('signup.html', error=False)

@app.route('/app/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']
        c.execute("SELECT * FROM user")
        users = c.fetchall()
        return render_template('dashboard.html', username=username, users=users)
    return redirect(url_for('login'))

@app.route('/app/update/<username>', methods=['GET', 'POST'])
def update(username):
    if request.method == 'POST':
        status1 = request.form['status1']
        status2 = request.form['status2']
        status3 = request.form['status3']
        status4 = request.form['status4']
        status5 = request.form['status5']
        status6 = request.form['status6']
        status7 = request.form['status7']
        status8 = request.form['status8']
        status9 = request.form['status9']
        status10 = request.form['status10']
        status11 = request.form['status11']
        status12 = request.form['status12']
        status13 = request.form['status13']
        status14 = request.form['status14']
        status15 = request.form['status15']
        status16 = request.form['status16']
        c.execute("UPDATE user SET PY4E1=?, PY4E2=?, PY4E3=?, PY4E4=?, PY4E5=?, PY4E6=?, PY4E7=?, PY4E8=?, PY4E9=?, PY4E10=?, PY4E11=?, PY4E12=?, PY4E13=?, PY4E14=?, PY4E15=?, PY4E16=? WHERE username=?", (status1, status2, status3, status4, status5, status6, status7, status8, status9, status10, status11, status12, status13, status14, status15, status16, username))
        conn.commit()
        return redirect(url_for('dashboard'))
    else:
        c.execute("SELECT * FROM user WHERE username=?", (username,))
        user = c.fetchone()
        return render_template('update.html', username=username, user=user)

@app.route('/app/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
else:
    application = app

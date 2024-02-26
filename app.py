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
        PY4E1 = PY4E2 = PY4E3 = PY4E4 = PY4E5 = PY4E6 = PY4E7 = PY4E8 = PY4E9 = PY4E10 = PY4E11 = PY4E12 = PY4E13 = PY4E14 = PY4E15 = PY4E16 = PY4E17 = 'To Do'                    
        DJ4E1 = DJ4E2 = DJ4E3 = DJ4E4 = DJ4E5 = DJ4E6 = DJ4E7 = DJ4E8 = DJ4E9 = DJ4E10 = DJ4E11 = DJ4E12 = DJ4E13 = DJ4E14 = DJ4E15 = DJ4E16 = DJ4E17 = DJ4E18 = DJ4E19 = DJ4E20 = DJ4E21 = DJ4E22 = DJ4E23 = DJ4E24 = DJ4E25 = DJ4E26 = DJ4E27 = DJ4E28  = DJ4E29 = DJ4E30 = DJ4E31 = DJ4E32 = DJ4E33 = DJ4E34 = DJ4E35 = DJ4E36 = DJ4E37 = DJ4E38 = DJ4E39 = DJ4E40 = 'To Do'

        try:
            c.execute("INSERT INTO user (username, password, PY4E1, PY4E2, PY4E3, PY4E4, PY4E5, PY4E6, PY4E7, PY4E8, PY4E9, PY4E10, PY4E11, PY4E12, PY4E13, PY4E14, PY4E15, PY4E16, PY4E17, DJ4E1, DJ4E2, DJ4E3, DJ4E4, DJ4E5, DJ4E6, DJ4E7, DJ4E8, DJ4E9, DJ4E10, DJ4E11, DJ4E12, DJ4E13, DJ4E14, DJ4E15, DJ4E16, DJ4E17, DJ4E18, DJ4E19, DJ4E20, DJ4E21, DJ4E22, DJ4E23, DJ4E24, DJ4E25, DJ4E26, DJ4E27, DJ4E28 , DJ4E29, DJ4E30, DJ4E31, DJ4E32, DJ4E33, DJ4E34, DJ4E35, DJ4E36, DJ4E37, DJ4E38, DJ4E39, DJ4E40) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (username, password, PY4E1, PY4E2, PY4E3, PY4E4, PY4E5, PY4E6, PY4E7, PY4E8, PY4E9, PY4E10, PY4E11, PY4E12, PY4E13, PY4E14, PY4E15, PY4E16, PY4E17, DJ4E1, DJ4E2, DJ4E3, DJ4E4, DJ4E5, DJ4E6, DJ4E7, DJ4E8, DJ4E9, DJ4E10, DJ4E11, DJ4E12, DJ4E13, DJ4E14, DJ4E15, DJ4E16, DJ4E17, DJ4E18, DJ4E19, DJ4E20, DJ4E21, DJ4E22, DJ4E23, DJ4E24, DJ4E25, DJ4E26, DJ4E27, DJ4E28 , DJ4E29, DJ4E30, DJ4E31, DJ4E32, DJ4E33, DJ4E34, DJ4E35, DJ4E36, DJ4E37, DJ4E38, DJ4E39, DJ4E40))
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
        #PY4E
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
        status17 = request.form['status17']
        #DJ4E
        status18 = request.form['status18']
        status19 = request.form['status19']
        status20 = request.form['status20']
        status21 = request.form['status21']        
        status22 = request.form['status22']        
        status23 = request.form['status23']        
        status24 = request.form['status24']        
        status25 = request.form['status25']        
        status26 = request.form['status26']        
        status27 = request.form['status27']        
        status28 = request.form['status28']        
        status29 = request.form['status29']        
        status30 = request.form['status30']        
        status31 = request.form['status31']        
        status32 = request.form['status32']      
        status33 = request.form['status33']      
        status34 = request.form['status34']      
        status35 = request.form['status35']      
        status36 = request.form['status36']      
        status37 = request.form['status37']      
        status38 = request.form['status38']                                                      
        status39 = request.form['status39']      
        status40 = request.form['status40']   
        status41 = request.form['status41']   
        status42 = request.form['status42']   
        status43 = request.form['status43']   
        status44 = request.form['status44']   
        status45 = request.form['status45']   
        status46 = request.form['status46']   
        status47 = request.form['status47']                                                      
        status48 = request.form['status48']   
        status49 = request.form['status49']   
        status50 = request.form['status50']   
        status51 = request.form['status51']   
        status52 = request.form['status52']   
        status53 = request.form['status53']   
        status54 = request.form['status54']   
        status55 = request.form['status55']   
        status56 = request.form['status56']   
        status57 = request.form['status57']   
        c.execute("UPDATE user SET PY4E1=?, PY4E2=?, PY4E3=?, PY4E4=?, PY4E5=?, PY4E6=?, PY4E7=?, PY4E8=?, PY4E9=?, PY4E10=?, PY4E11=?, PY4E12=?, PY4E13=?, PY4E14=?, PY4E15=?, PY4E16=?, PY4E17=?, DJ4E18=?, DJ4E2=?, DJ4E3=?, DJ4E4=?, DJ4E5=?, DJ4E6=?, DJ4E7=?, DJ4E8=?, DJ4E9=?, DJ4E10=?, DJ4E11=?, DJ4E12=?, DJ4E13=?, DJ4E14=?, DJ4E15=?, DJ4E16=?, DJ4E17=?, DJ4E18=?, DJ4E19=?, DJ4E20=?, DJ4E21=?, DJ4E22=?, DJ4E23=?, DJ4E24=?, DJ4E25=?, DJ4E26=?, DJ4E27=?, DJ4E28 =?, DJ4E29=?, DJ4E30=?, DJ4E31=?, DJ4E32=?, DJ4E33=?, DJ4E34=?, DJ4E35=?, DJ4E36=?, DJ4E37=?, DJ4E38=?, DJ4E39=?, DJ4E40=? WHERE username=?", (status1, status2, status3, status4, status5, status6, status7, status8, status9, status10, status11, status12, status13, status14, status15, status16, status17, status18, status19, status20, status21, status22, status23, status24, status25, status26, status27, status28, status29, status30, status31, status32, status33, status34, status35, status36, status37, status38, status39, status40, status41, status42, status43, status44, status45, status46, status47, status48, status49, status50, status51, status52, status53, status54, status55, status56, status57, username))
 
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

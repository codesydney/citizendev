import sqlite3
from datetime import datetime

from flask import Flask, redirect, render_template, request, session, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder="./templates/py4e")
app.secret_key = "your_secret_key"  # Change this to a secure random key
bootstrap = Bootstrap(app)

# Connect to the SQLite database
# conn = sqlite3.connect("./citizendevs.db", check_same_thread=False)
conn = sqlite3.connect("./citizendevs.db", check_same_thread=False)
c = conn.cursor()


@app.route("/py4e", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        c.execute(
            "SELECT * FROM user WHERE username=? AND password=? ORDER BY last_update DESC",
            (username, password),
        )
        user = c.fetchone()
        if user:
            session["username"] = username
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error=True)
    return render_template("login.html", error=False)


@app.route("/py4e/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        initial_values = ["To Do" for _ in range(17)]

        query = "INSERT INTO user (username, password, last_update"
        for i in range(1, 18):
            query += f", PY4E{i}"
        query += ") VALUES (?, ?, ?"
        for _ in range(17):
            query += ", ?"
        query += ")"

        try:
            current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            c.execute(query, (username, password, current_timestamp, *initial_values))
            conn.commit()
            session["username"] = username
            return redirect(url_for("dashboard"))
        except sqlite3.IntegrityError:
            # If the username already exists, show an error message
            return render_template("signup.html", error=True)
    return render_template("signup.html", error=False)


@app.route("/py4e/dashboard")
def dashboard():
    if "username" in session:
        username = session["username"]
        c.execute("SELECT * FROM user ORDER BY last_update DESC")
        users = c.fetchall()
        return render_template("dashboard.html", username=username, users=users)
    return redirect(url_for("login"))


@app.route("/py4e/update/<username>", methods=["GET", "POST"])
def update(username):
    if request.method == "POST":
        status_values = [
            request.form[f"status{i}"] for i in range(1, 18)
        ]  # Status values for PY4E1 to PY4E17

        query = "UPDATE user SET "
        query += ", ".join([f"PY4E{i} = ?" for i in range(1, 18)])
        query += ", last_update = ?"  # Add last_update column
        query += " WHERE username = ?"

        # Append current timestamp and username to status_values
        status_values.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        status_values.append(username)

        c.execute(query, status_values)
        conn.commit()

        return redirect(url_for("dashboard"))
    else:
        fn = "./lessons.txt"
        fh = open(fn)
        lessons = [line.rstrip() for line in fh.readlines()]

        c.execute("SELECT * FROM user WHERE username=?", (username,))
        user = c.fetchone()
        return render_template(
            "update.html", username=username, user=user, lessons=lessons
        )


@app.route("/py4e/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
else:
    application = app

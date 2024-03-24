import sqlite3
from datetime import datetime

from flask import Flask, redirect, render_template, request, session, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder="./templates/py4e")
app.secret_key = "your_secret_key"  # Change this to a secure random key
bootstrap = Bootstrap(app)

# Connect to the SQLite database
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
        PY4E1 = PY4E2 = PY4E3 = PY4E4 = PY4E5 = PY4E6 = PY4E7 = PY4E8 = PY4E9 = (
            PY4E10
        ) = PY4E11 = PY4E12 = PY4E13 = PY4E14 = PY4E15 = PY4E16 = PY4E17 = "To Do"
        DJ4E1 = DJ4E2 = DJ4E3 = DJ4E4 = DJ4E5 = DJ4E6 = DJ4E7 = DJ4E8 = DJ4E9 = (
            DJ4E10
        ) = DJ4E11 = DJ4E12 = DJ4E13 = DJ4E14 = DJ4E15 = DJ4E16 = DJ4E17 = DJ4E18 = (
            DJ4E19
        ) = DJ4E20 = DJ4E21 = DJ4E22 = DJ4E23 = DJ4E24 = DJ4E25 = DJ4E26 = DJ4E27 = (
            DJ4E28
        ) = DJ4E29 = DJ4E30 = DJ4E31 = DJ4E32 = DJ4E33 = DJ4E34 = DJ4E35 = DJ4E36 = (
            DJ4E37
        ) = DJ4E38 = DJ4E39 = DJ4E40 = "To Do"

        try:
            current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            c.execute(
                """
                INSERT INTO user (username, password, PY4E1, PY4E2, PY4E3, PY4E4, PY4E5, PY4E6, PY4E7, PY4E8,
                                PY4E9, PY4E10, PY4E11, PY4E12, PY4E13, PY4E14, PY4E15, PY4E16, PY4E17,
                                DJ4E1, DJ4E2, DJ4E3, DJ4E4, DJ4E5, DJ4E6, DJ4E7, DJ4E8, DJ4E9, DJ4E10,
                                DJ4E11, DJ4E12, DJ4E13, DJ4E14, DJ4E15, DJ4E16, DJ4E17, DJ4E18, DJ4E19,
                                DJ4E20, DJ4E21, DJ4E22, DJ4E23, DJ4E24, DJ4E25, DJ4E26, DJ4E27, DJ4E28,
                                DJ4E29, DJ4E30, DJ4E31, DJ4E32, DJ4E33, DJ4E34, DJ4E35, DJ4E36, DJ4E37,
                                DJ4E38, DJ4E39, DJ4E40, last_update)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    username,
                    password,
                    PY4E1,
                    PY4E2,
                    PY4E3,
                    PY4E4,
                    PY4E5,
                    PY4E6,
                    PY4E7,
                    PY4E8,
                    PY4E9,
                    PY4E10,
                    PY4E11,
                    PY4E12,
                    PY4E13,
                    PY4E14,
                    PY4E15,
                    PY4E16,
                    PY4E17,
                    DJ4E1,
                    DJ4E2,
                    DJ4E3,
                    DJ4E4,
                    DJ4E5,
                    DJ4E6,
                    DJ4E7,
                    DJ4E8,
                    DJ4E9,
                    DJ4E10,
                    DJ4E11,
                    DJ4E12,
                    DJ4E13,
                    DJ4E14,
                    DJ4E15,
                    DJ4E16,
                    DJ4E17,
                    DJ4E18,
                    DJ4E19,
                    DJ4E20,
                    DJ4E21,
                    DJ4E22,
                    DJ4E23,
                    DJ4E24,
                    DJ4E25,
                    DJ4E26,
                    DJ4E27,
                    DJ4E28,
                    DJ4E29,
                    DJ4E30,
                    DJ4E31,
                    DJ4E32,
                    DJ4E33,
                    DJ4E34,
                    DJ4E35,
                    DJ4E36,
                    DJ4E37,
                    DJ4E38,
                    DJ4E39,
                    DJ4E40,
                    current_timestamp,
                ),
            )

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
        status_values += [
            request.form[f"status{i}"] for i in range(18, 58)
        ]  # Status values for DJ4E1 to DJ4E40

        query = "UPDATE user SET "
        query += ", ".join([f"PY4E{i} = ?" for i in range(1, 18)])
        query += ", "  # Add comma separator
        query += ", ".join(
            [f"DJ4E{i - 17} = ?" for i in range(18, 58)]
        )  # DJ4E1 to DJ4E40
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

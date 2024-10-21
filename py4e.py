import sqlite3
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for, g
from flask_bootstrap import Bootstrap
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import os  # For saving the image in the static folder

app = Flask(__name__, template_folder="./templates/py4e")
app.secret_key = "your_secret_key"  # Change this to a secure random key
bootstrap = Bootstrap(app)

# Database configuration
DATABASE = './citizendevs.db'

def get_db():
    """Open a new database connection if there is none yet for the current application context."""
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE, check_same_thread=False)
        g.db.row_factory = sqlite3.Row  # Allows access by column name
    return g.db

@app.teardown_appcontext
def close_connection(exception):
    """Close the database connection at the end of the request."""
    db = g.pop('db', None)
    if db is not None:
        db.close()

@app.route("/py4e", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        cur = db.cursor()
        cur.execute(
            "SELECT * FROM user WHERE username=? AND password=? ORDER BY last_update DESC",
            (username, password),
        )
        user = cur.fetchone()
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
            db = get_db()
            cur = db.cursor()
            current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cur.execute(query, (username, password, current_timestamp, *initial_values))
            db.commit()
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
        db = get_db()
        cur = db.cursor()
        
        # Query to get all user data
        cur.execute("SELECT * FROM user ORDER BY last_update DESC")
        users = cur.fetchall()

        # Initialize counts
        py4e_columns = [f'PY4E{i}' for i in range(1, 18)]
        py4e_done_counts = {}
        py4e_nickname_counts = {}

        total_done_count = 0  # Total number of 'Done' values
        google_form_count = 0  # Variable for Google Form count

        # Query counts
        for column in py4e_columns:
            cur.execute(f'SELECT COUNT(*) FROM user WHERE {column} = "Done"')
            done_count = cur.fetchone()[0]
            py4e_done_counts[column] = done_count
            total_done_count += done_count  # Total 'Done' count

            cur.execute(f'''
                SELECT COUNT(*) FROM user
                WHERE {column} = "Done" AND Nickname IS NOT NULL
            ''')
            nickname_count = cur.fetchone()[0]
            py4e_nickname_counts[column] = nickname_count

        # Count for Google Form registrations
        cur.execute('SELECT COUNT(*) FROM user WHERE Nickname IS NOT NULL')
        google_form_count = cur.fetchone()[0]

        # Query to get the status of the logged-in user
        cur.execute("SELECT PY4E1, PY4E2, PY4E3, PY4E4, PY4E5, PY4E6, PY4E7, PY4E8, PY4E9, PY4E10, PY4E11, PY4E12, PY4E13, PY4E14, PY4E15, PY4E16, PY4E17 FROM user WHERE username=?", (username,))
        user_status = cur.fetchone()  # Fetch the status row for the logged-in user

        # Close the database connection
        cur.close()

        # Commenting out matplotlib plotting
        '''
        # Plot the graph
        fig, ax = plt.subplots(figsize=(12, 6))
        bars = ax.bar(py4e_done_counts.keys(), py4e_done_counts.values(), color='#B6D0E2')

        # Title and labels
        total_records = len(users)  # Total number of records
        fig.suptitle(f'Total enrollees: {total_records}', fontsize=16, color='#143b6e')

        # Adjusted Y positions for better spacing between the two lines
        ax.text(0.5, 1.05, f'Number of chapter completions: {total_done_count}', 
                ha='center', va='bottom', fontsize=14, color='#2c63ab', transform=ax.transAxes)

        # Increased space by lowering the y value of the second text line
        ax.text(0.5, 1.00, f'Total enrollees who also registered in Google form (G): {google_form_count}', 
                ha='center', va='bottom', fontsize=14, color='purple', transform=ax.transAxes)

        # Additional formatting for the bar chart
        ax.set_xlabel('PY4E Lessons', fontsize=12)
        ax.set_ylabel('Number of Completions', fontsize=12)
        ax.tick_params(axis='x', rotation=45)

        # Set x-axis labels directly to the lesson identifiers
        lesson_labels = [f'PY4E{i}' for i in range(1, 18)]
        ax.set_xticks(range(len(lesson_labels)))  # Set the x-ticks to the range of labels
        ax.set_xticklabels(lesson_labels, fontsize=10)  # Set explicit labels without counts

        # Debugging prints to check x-tick labels
        print("X-axis labels:", lesson_labels)

        # Add labels on top of the bars without changing x-axis labels
        for i, bar in enumerate(bars):
            height = bar.get_height()
            x_position = bar.get_x() + bar.get_width() / 2

            # Add the "Done" count label in blue directly above each bar
            if height > 0:
                ax.text(x_position, height * 1.02, str(height), ha='center', va='bottom', fontsize=10, color='#2c63ab')

                # Add the nickname count indicator in purple just below the bar label
                nickname_count = py4e_nickname_counts.get(py4e_columns[i], 0)  # Use .get to avoid KeyErrors
                ax.text(x_position, height * 0.95, f'G: {nickname_count}', ha='center', va='top', fontsize=9, color='purple')
        
        # Set y-axis limits to ensure labels are visible
        ax.set_ylim(0, max(py4e_done_counts.values()) * 1.2)

        # Adjust layout to make space for the headers and avoid truncation
        plt.subplots_adjust(left=0.1, right=0.95, top=0.85, bottom=0.25)

        # Save the plot as an image
        img_path = os.path.join('static', 'plot.png')
        plt.savefig(img_path)
        plt.close()
        '''

        # Render the dashboard without the plot
        return render_template("dashboard.html", username=username, users=users, user_status=user_status)

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

        db = get_db()
        cur = db.cursor()
        cur.execute(query, status_values)
        db.commit()

        return redirect(url_for("dashboard"))
    else:
        fn = "./lessons.txt"
        with open(fn) as fh:
            lessons = [line.rstrip() for line in fh.readlines()]

        db = get_db()
        cur = db.cursor()
        cur.execute("SELECT * FROM user WHERE username=?", (username,))
        user = cur.fetchone()
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

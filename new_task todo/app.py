from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
app.secret_key = "your_secret_key"

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root' 
app.config['MYSQL_PASSWORD'] = '1423' 
app.config['MYSQL_DB'] = 'taskflow'

mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/guest-login')
def guest_login():
    session['username'] = 'Guest'  # Store session as 'Guest'
    return redirect(url_for('todo'))  # Redirect to To-Do page

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        account = cursor.fetchone()

        if account:
            return "Username already exists! <a href='/signup'>Try again</a>"

        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        mysql.connection.commit()
        cursor.close()
        
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        account = cursor.fetchone()

        if account:
            session['username'] = username
            return redirect(url_for('todo'))
        else:
            return "Invalid username or password! <a href='/login'>Try again</a>"

    return render_template('login.html')

@app.route("/todo")
def todo():
    if 'username' in session:
        username = session['username']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        
        if username == "Guest":
            cursor.execute("SELECT * FROM tasks WHERE username IS NULL")  # Guest tasks
        else:
            cursor.execute("SELECT * FROM tasks WHERE username = %s", (username,))
        
        tasks = cursor.fetchall()
        cursor.close()
        return render_template("todo.html", username=username, tasks=tasks)

    return redirect(url_for('login'))

@app.route('/add', methods=['POST'])
def add_task():
    if 'username' in session:
        username = session['username']
        subject = request.form['subject'].strip()
        description = request.form['description'].strip()

        cursor = mysql.connection.cursor()
        if username == "Guest":
            cursor.execute("SELECT * FROM tasks WHERE subject = %s AND username IS NULL", (subject,))
        else:
            cursor.execute("SELECT * FROM tasks WHERE subject = %s AND username = %s", (subject, username))
        
        task_exists = cursor.fetchone()

        if task_exists:
            return "Error: Task title must be unique!", 400

        if username == "Guest":
            cursor.execute("INSERT INTO tasks (subject, description) VALUES (%s, %s)", (subject, description))
        else:
            cursor.execute("INSERT INTO tasks (username, subject, description) VALUES (%s, %s, %s)", (username, subject, description))
        
        mysql.connection.commit()
        cursor.close()

        return redirect(url_for('todo'))

    return redirect(url_for('login'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if 'username' in session:
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        mysql.connection.commit()
        cursor.close()

        return redirect(url_for('todo'))

    return redirect(url_for('login'))

@app.route('/edit/<int:task_id>', methods=['POST'])
def edit_task(task_id):
    if 'username' in session:
        new_subject = request.form['subject'].strip()
        new_description = request.form['description'].strip()

        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE tasks SET subject = %s, description = %s WHERE id = %s", (new_subject, new_description, task_id))
        mysql.connection.commit()
        cursor.close()

        return redirect(url_for('todo'))

    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)

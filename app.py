from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/students")
def students():
    return render_template("students.html")

@app.route("/subjects")
def subjects():
    return render_template("subjects.html")

@app.route("/teachers")
def teachers():
    return render_template("teachers.html")

@app.route("/timetable")
def timetable():
    return render_template("timetable.html")

@app.route("/marks")
def marks():
    return render_template("marks.html")

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email_add = request.form["email"]
        date = request.form["date"]
        occupation = request.form["occupation"]

app.run(debug=True, port=5001)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        return redirect(url_for("user", name=request.form["name"]))
    return render_template("index.html")

@app.route("/contact")
def contract():
    return render_template("contact.html")

@app.route("/<name>")
def user(name):
    return f"<h1>I see you've come to torcher me {name}... Prepare for some chaos comming for you.</h1>"


if __name__ == "__main__":
    app.run(debug=True)
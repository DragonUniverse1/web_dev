from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        return redirect(url_for("user", name=request.form["name"]))
    return render_template("index.html")

@app.route("/contact")
def contract():
    return "<p>Dont't contact me. I don't want to talk to you. I'm tired.</p>"

@app.route("/<name>")
def user(name):
    return f"<h1>I said don't contact to me {name}!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
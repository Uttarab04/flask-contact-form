from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not message:
            return render_template("contact.html", error="Both name and message are required.", submitted=False)

        # Store message in a file
        with open("messages.txt", "a") as file:
            file.write(f"{datetime.now()} - {name}: {message}\n")

        return render_template("contact.html", name=name, message=message, submitted=True)

    return render_template("contact.html", submitted=False)

if __name__ == "__main__":
    app.run(debug=True)

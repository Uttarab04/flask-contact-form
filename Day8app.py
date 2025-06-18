from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template("home.html")

# About Page
@app.route('/about')
def about():
    return render_template("about.html")

# Contact Page with Form Handling
@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        message = request.form.get("message", "").strip()

        # Validate form inputs
        if not name or not message:
            error = "Both name and message are required."
            return render_template("contact.html", error=error, submitted=False)

        # Save message to file with timestamp
        with open("messages.txt", "a", encoding="utf-8") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp} - {name}: {message}\n")

        return render_template("contact.html", name=name, message=message, submitted=True)

    return render_template("contact.html", submitted=False)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

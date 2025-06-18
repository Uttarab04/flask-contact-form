from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to My Flask App</h1><p>This is the Home Page.</p>"

@app.route('/about')
def about():
    return "<h1>About</h1><p>This is a basic Flask app created during my internship.</p>"

if __name__ == "__main__":
    app.run(debug=True)


# After running python Day7app.py
# Visit:
# http://127.0.0.1:5000/ → Home page
# http://127.0.0.1:5000/about → About page
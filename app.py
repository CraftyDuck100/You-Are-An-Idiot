from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        name = request.form.get('like', '').strip()
        if not name.lower() == "yes":
            return render_template("index2.html", hi="good")
        else:
            return render_template("index2.html", hi="idiot")
    return render_template("index.html")
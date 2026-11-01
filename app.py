from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route("/memories")
def memories():
    return render_template("memories.html")
@app.route("/letter")
def letter():
    return render_template("letter.html")
@app.route("/final")
def final():
    return render_template("final.html")
@app.route("/love")
def love():
    return render_template("love.html")
if __name__ == '__main__':
    app.run(debug=True)
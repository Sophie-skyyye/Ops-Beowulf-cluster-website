from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# to add more pages you will add this 
# def about():
#    return render_templates("about.html")

if __name__ == "__main__":
    app.run(debug=True)
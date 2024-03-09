from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def predict():
    return render_template('base.html')

if __name__ == "__main__":
    print("Starting the python flask server for home prediction model...")
    app.run(debug=True)

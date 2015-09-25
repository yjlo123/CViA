from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return render_template('base.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)

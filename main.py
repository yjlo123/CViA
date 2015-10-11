import os
from flask import Flask, render_template, url_for, redirect, request
from werkzeug import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'cv/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'doc', 'docx'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    print request.method
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print "Uploaded file", filename
            print os.path.abspath(__file__)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('cv.html', filename=filename)
        return render_template('cv.html', filename=None)
    return render_template('upload.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)

import os
from flask import Flask, render_template, url_for, redirect, request
from werkzeug import secure_filename
from doc_converter import DocConverter

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
    # POST
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print "Uploaded file", filename

            full_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(full_path)
            print "Stored file", filename

            text = DocConverter().documentToText(full_path)
            return render_template('cv.html', filename=filename, text=text)

        return render_template('cv.html', filename=None)

    # GET
    return render_template('upload.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)

import os

from flask import Flask, render_template, request, send_from_directory
from werkzeug import secure_filename

from doc_converter import DocConverter
from cvParser.Parser import Parser
import Service
from Service import input_requirement, evaluate_cvs, input_weight, input_job_function

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'cv/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'doc', 'docx'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def get_cvs():
    files = os.listdir(os.path.join(app.config['UPLOAD_FOLDER']))
    allowed_files = []
    for filename in files:
        if allowed_file(filename):
            allowed_files.append(app.config['UPLOAD_FOLDER'] + filename)
    return allowed_files

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
            print full_path
            file.save(full_path)
            print "Stored file", filename

            return render_template(
                'cv.html',
                filename=filename
            )

        return render_template('cv.html', filename=None)

    # GET
    return render_template('upload.html')

@app.route('/upload/<filename>', methods=['GET'])
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/upload/all', methods=['GET'])
def all_cvs():
    cvs = get_cvs()
    return render_template('cvs.html', cvs=[cv.split('/')[-1] for cv in cvs])

@app.route('/process', methods=['POST'])
def process():
    # POST
    if request.method == 'POST':
        def parse(text):
            keywords = []
            for keyword in text.split(','):
                if keyword.strip():
                    keywords.append(str(keyword.strip()))
            return keywords

        def parse_number(text):
            try:
                number = int(text)
                return number if number >= 1 else 1
            except e:
                return 1

        req = {
            'education': request.form['education'],
            'skill': {
                'must': parse(request.form['skill_must']),
                'good': parse(request.form['skill_good'])
            },
            'language': {
                'must': parse(request.form['language_must']),
                'good': parse(request.form['language_good'])
            },
            'experience': {
                'must': parse(request.form['experience_must']),
                'good': parse(request.form['experience_good'])
            },
            'other': parse(request.form['other'])
        }

        weights = {
            'education': parse_number(request.form['education_weight']),
            'skill': parse_number(request.form['skill_weight']),
            'language': parse_number(request.form['language_weight']),
            'experience': parse_number(request.form['experience_weight']),
            'other': parse_number(request.form['other_weight'])
        }

        cvs = get_cvs()

        input_requirement(req)
        input_weight(weights)
        input_job_function(request.form['job'])
        results = evaluate_cvs(cvs)
        for cv in results:
            detailed_scores = ""
            for category in cv['score']:
                detailed_scores += category + ": " + str(cv['score'][category]) + "\n"
            cv['detailed_scores'] = detailed_scores
            cv['filename'] = cv['cv'].split('/')[-1]
            cv['total'] = round(cv['total'], 1)

        results.sort(key=lambda x: -x['total'])

        return render_template('result.html', cvs=results)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)

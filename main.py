import os

from flask import Flask, render_template, request
from werkzeug import secure_filename

from doc_converter import DocConverter
from cvParser.Parser import Parser
import Service
from Service import init, input_requirement, evaluate_cvs

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
            print full_path
            file.save(full_path)
            print "Stored file", filename

            cv_text = DocConverter().documentToText(full_path)
            cv_dict = Parser().convertToObj(cv_text)
            return render_template(
                'cv.html',
                filename=filename,
                cv_text=cv_text,
                cv_dict=cv_dict
            )

        return render_template('cv.html', filename=None)

    # GET
    return render_template('upload.html')

@app.route('/process', methods=['POST'])
def process():
    # POST
    if request.method == 'POST':
        def parse(text):
            keywords = []
            for keyword in text.split(','):
                if keyword.strip():
                    keywords.append(keyword.strip())
            return keywords

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

        cvs = [
            "cv/LinkedIn/YaminiBhaskar.pdf",
            "cv/LinkedIn/DonnabelleEmbodo.pdf",
            "cv/LinkedIn/PraveenDeorani.pdf",
            "cv/LinkedIn/RussellOng.pdf",
            "cv/LinkedIn/YaminiBhaskar.pdf"
        ]

        init()
        input_requirement(req)
        results = evaluate_cvs(cvs)
        for cv in results:
            detailed_scores = ""
            print cv['score']
            for category in cv['score']:
                detailed_scores += category + ": " + str(cv['score'][category]) + "\n"
            cv['detailed_scores'] = detailed_scores
        return render_template('result.html', cvs=results)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)

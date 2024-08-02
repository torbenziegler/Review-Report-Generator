import os
from flask import Flask, make_response, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

PDF_DIR = os.path.join(os.getcwd())
# PDF_DIR = os.path.join(os.getcwd(), "backend", "output")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/pdf/<string:filename>", methods=['GET', 'OPTIONS'])
def return_pdf(filename):
    try:
        file_path = os.path.join(PDF_DIR, filename)
        # print current dir
        print(f"Current dir: {os.getcwd()}")
        print(f"File path: {file_path}")
        if os.path.isfile(file_path):
            response = make_response(send_file(file_path))
            response.headers['Content-Type'] = 'application/pdf'
            response.headers['Content-Disposition'] = \
            'inline; filename=%s.pdf' % 'yourfilename'
            return response
        else:
            return make_response(f"File '{filename}' not found.", 404)
    except Exception as e:
        return make_response(f"Error: {str(e)}", 500)
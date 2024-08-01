import os
from flask import Flask, make_response, send_file

app = Flask(__name__)

PDF_DIR = "../"

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/pdf/<string:filename>", methods=['GET'])
def return_pdf(filename):
    try:
        file_path = os.path.join(PDF_DIR, filename)
        print(f"File path: {file_path}")
        if os.path.isfile(file_path):
            return send_file(file_path, as_attachment=True)
        else:
            return make_response(f"File '{filename}' not found.", 404)
    except Exception as e:
        return make_response(f"Error: {str(e)}", 500)
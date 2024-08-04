import os
from flask import Flask, make_response, send_file
from flask_cors import CORS
from main import generate_report
import asyncio

app = Flask(__name__)
CORS(app)

PDF_DIR = os.path.join(os.getcwd())
# PDF_DIR = os.path.join(os.getcwd(), "backend", "output")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/pdf/<string:package_name>", methods=['GET', 'OPTIONS'])
def return_pdf(package_name):
    try:
        generate_report(package_name)

        file_name = "Review_Report.pdf"
        file_path = os.path.join(PDF_DIR, file_name)
        if os.path.isfile(file_path):
            response = make_response(send_file(file_path))
            response.headers['Content-Type'] = 'application/pdf'
            response.headers['Content-Disposition'] = \
            'inline; filename=%s.pdf' % file_name
            return response
        else:
            return make_response(f"File '{file_name}' not found.", 404)
    except Exception as e:
        print(f"Error: {str(e)}")
        return make_response(f"Error: {str(e)}", 500)
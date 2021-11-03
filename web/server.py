# TODO: Error Handling

from flask import Flask, render_template, request, redirect, abort
from werkzeug import secure_filename

from functools import cache
from pathlib import Path
import logging
import sys


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '../../code'
app.config['MAX_CONTENT_PATH'] = 5000     # is this enough? do we need this at all?

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_code():
    f = request.files['file']
    f.save(secure_filename(f.filename))
    return 'file uploaded successfully'


def main(debug=False):
    if debug:
        app.logger.setLevel(logging.DEBUG)
    app.run(debug=debug)


if __name__ == '__main__':
    main(debug=True)

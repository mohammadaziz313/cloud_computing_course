from flask import Flask, render_template, flash, request, jsonify
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import requests
import json
import logging
import requests_toolbelt.adapters.appengine

requests_toolbelt.adapters.appengine.monkeypatch()

try:
    # For Python 3.0 and later
    from urllib.error import HTTPError
    from urllib.parse import quote
    from urllib.parse import urlencode
except ImportError:
    # Fall back to Python 2's urllib2 and urllib
    from urllib2 import HTTPError
    from urllib import quote
    from urllib import urlencode

# App config.
DEBUG = True
app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def index():
    if request.method == "POST":
        return render_template('cat.html')
    return render_template('index.html')

@app.route("/map", methods=['GET','POST'])
def map():
    return render_template('map.html')

@app.route('/query-example')
def query_example():
    language = request.args.get('language')
    framework = request.args.get('framework')
    return '<h1>The Language is: {} and Framework:{}</h1>'.format(language,framework)

@app.route('/form-example',methods=['GET','POST'])
def form_example():
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form.get('framework')
        return '<h1>Language:{} and Framework:{}</h1>'.format(language,framework)

    return '''<form method="POST">
                     Language: <input type="text" name="language"><br><br>
                     Framework: <input type="text" name="framework"><br><br>
                     <input type="submit" value="Submit"><br>
              </form>''';

@app.route('/json-example',methods=['POST'])
def json_example():
    req_data = request.get_json()
    language = None
    if 'language' in req_data:
        language = req_data['language']
    
    framework = req_data['framework']
    python_version = req_data['version_info']['python']
    example = req_data['examples'][2]
    boolean_test = req_data['boolean_test']

    return '''<p>
                Language:{}<br>
                Framework:{}<br>
                Python:{}<br>
                Example:{}<br>
                boolean_test:{}<br>
             </p>'''.format(language,framework,python_version,example,boolean_test);


if __name__ == '__main__':
    app.run()


from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

# @app.route('/omg', strict_slashes=False)
# def omg():
#     return 'OMG'

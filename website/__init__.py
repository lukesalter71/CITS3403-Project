from flask import Flask
from flask import render_template
import os
from flask import send_from_directory

def create_app():
    app = Flask(__name__)
    app.static_folder = 'static'

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'),
                              'favicon.ico',mimetype='image/vnd.microsoft.icon')

    @app.route("/")
    def home():
        return render_template('homepage.html', title='Home')

    return app
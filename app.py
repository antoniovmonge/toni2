from flask import Flask, render_template, request
from flask_cors import CORS
from models import create_post, get_posts

# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# db = SQLAlchemy(app)

CORS(app)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        name = request.form.get('name')
        post = request.form.get('post')
        create_post(name, post)

    posts = get_posts()

    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
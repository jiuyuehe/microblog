from app import app
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    user = {'nickname': 'manbuzhiwu'}
    return render_template('index.html',user = user)

@app.route('/index1')
def index1():
    user = {'nickname':'manbu'}
    post = [
        {
            'author':{'nickname':'Johnson'},
            'body':'The Avengers movie was so cool!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The bar  was so white!'
        }
    ]
    return render_template('index1.html',
                           title ='Home',
                           user = user,
                           posts = post)

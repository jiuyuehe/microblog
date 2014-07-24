from app import app
from flask import render_template, flash, redirect
from forms import LoginForm


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


@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print 'openid :'+form.openid.data
        flash('Login requested for OpenId= "' + form.openid.data +'",remember me='+str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',title='Sign In',form = form,providers = app.config['OPENID_PROVIDERS'])

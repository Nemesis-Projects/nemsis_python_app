#View file
from flask import render_template, flash, redirect, url_for, request, g
from app import app, mongo, login_manager
from .forms import LoginForm 
from flask.ext.login import login_user, logout_user, current_user, login_required
from .models import User

@app.route('/authorize/<provider>')
def oauth_authorize(provider):
	#Flask-Login function
	if not current_user.is_anonymous():
		return redirect(url_for('index'))
	oauth = OAuthSignIn.get_provider(provider)
	return oauth.authorize()

@app.route('/callback/provider')
def oauth_callback(provider):
	if not current_user.is_anonymous():
		return redirect(url_for('index'))
	oauth = OAuthSignIn.get_provider(provider)
	username, email = oauth.callback()
	if email is None:
		# Valid email address for user identification
		flash('Authentication failed !!')
		return redirect(url_for('index'))
	if email != 'mail2shivendra@gmail.com' or email !=  'neelgagan.adepu@gmail.com' :
		flash('You are not authorized to login to the application !!')
		return redirect(url_for('index'))
	login_user(user, remember=True)
	return redirect(url_for('index'))

@app.route('/')
@app.route('/index')
def index():
	user = {'name' : 'Shivendra Srivastava'}
	title = 'Home'
	cursor = mongo.coupon.find()
	for doc in cursor:
		print inside 
		print "Record is ", doc
	return render_template('index.html', 
    	title=title, 
    	user=user) 

def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login request for Open ID= "%s", remember_me=%s' %
			(form.openid.data, str(form.remember_me.data)))
		return redirect('/index')
	return render_template('login.html', 
		title="Sign In", 
		form=form,
		providers=app.config['OPENID_PROVIDERS'])

@app.route('/login', methods=['GET', 'POST'])
def oauth_login():
	print "In the OAuth function"
	g.user = current_user
	if g.user is None: #and g.user.is_authenticated():
		print "the user is :- ", g.user
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign In')

@login_manager.user_loader
def load_user(id):
	if id is None:
		redirect(url_for('login'))
	user = User()
	user.get

from flask import Flask, url_for, request, render_template, session, escape
app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return "You are signed in as %s." % escape(session['username'])
    return "You are not signed in!"

@app.route('/hello')
def hello_world():
    return render_template('hello.html')

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % (username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'This is the POST method.'
    else:
        session['username'] = 'Davin'
        return 'This is NOT the POST method.'

with app.test_request_context():
    print url_for('index')
    print url_for('hello_world', next='main')
    print url_for('show_user_profile', username='davin')
    print url_for('show_post', post_id=2)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

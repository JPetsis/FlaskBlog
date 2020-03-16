from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
  user = {'username': 'John'}
  posts = [
    {
      'author': {'username': 'Adam'},
      'body': 'Beautiful day in Berlin!'
    },
    {
      'author': {'username': 'Susan'},
      'body': 'The Avengers movie was so cool!'
    }
  ]
  return render_template('index.html', title='home', user=user, posts=posts)

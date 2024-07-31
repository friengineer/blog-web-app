import os

# code below configures SQLite so the database can be used and queried
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

# code below prevents cross-site request forgery from happening when submitting data in the forms
WTF_CSRF_ENABLED = True
SECRET_KEY = 'simply-raveena'

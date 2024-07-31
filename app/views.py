from flask import render_template, session, redirect, url_for, flash
from app import app, db, models
from .forms import RegisterForm, LoginForm, ChangeForm

# displays the login page
@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()

    if 'user' in session:
        return redirect(url_for('home'))

    if form.validate_on_submit():
        try:
            data = login(form.username.data, form.password.data)

            if data[0] == 0:
                return redirect(url_for('home'))
            else:
                flash('Incorrect username or password.')

        except:
            flash('An error occurred and you were not logged in. Please check your login details. Password: ' + form.password.data)

    return render_template('login.html',
                           hide='hidden',
                           hide2='',
                           active1='',
                           active2='',
                           active3='',
                           active4='',
                           active5='',
                           active6='',
                           timeline='col-sm-2 invisible',
                           title='',
                           title1='',
                           title2='',
                           title3='',
                           title4='',
                           title5='',
                           form=form,
                           socials='col-sm-2 socialContainer invisible')

# displays the register page
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if 'user' in session:
        return redirect(url_for('home'))

    if form.validate_on_submit():
        try:
            register(form.name.data, form.username.data, form.password.data)
            flash('Your account has been created.')
        except:
            flash('An error occurred and your account was not created or the username you entered already exists.')

    return render_template('register.html',
                           hide='hidden',
                           hide2='',
                           active1='',
                           active2='',
                           active3='',
                           active4='',
                           active5='',
                           active6='',
                           timeline='col-sm-2 invisible',
                           title='',
                           title1='',
                           title2='',
                           title3='',
                           title4='',
                           title5='',
                           form=form,
                           socials='col-sm-2 socialContainer invisible')

# displays the home page
@app.route('/home')
def home():
    if 'user' not in session:
        return redirect(url_for('index'))

    name = models.Account.query.get(session['user']).name
    return render_template('home.html',
                           name=name,
                           hide='',
                           hide2='hidden',
                           active1='active',
                           active2='',
                           active3='',
                           active4='',
                           active5='',
                           active6='',
                           timeline='col-sm-2 invisible',
                           title='',
                           title1='',
                           title2='',
                           title3='',
                           title4='',
                           title5='',
                           socials='col-sm-2 socialContainer')

# displays the blog page
@app.route('/blog')
def blog():
    if 'user' not in session:
        return redirect(url_for('index'))

    name = models.Account.query.get(session['user']).name
    post1 = models.Post.query.get(1)
    post2 = models.Post.query.get(2)
    post3 = models.Post.query.get(3)
    post4 = models.Post.query.get(4)
    post5 = models.Post.query.get(5)

    return render_template('blog.html',
                           name=name,
                           hide='',
                           hide2='hidden',
                           active1='',
                           active2='active',
                           active3='',
                           active4='',
                           active5='',
                           active6='',
                           timeline='col-sm-2 show',
                           title='Blog Posts',
                           title1='Awkward Introductions and Random Ramblings',
                           title2='Sports Matches and Leeds Varsity',
                           title3='Serious Adulting...',
                           title4='Warmer and Magical Times',
                           title5='Fun, Friends and Food',
                           post1=post1,
                           post2=post2,
                           post3=post3,
                           post4=post4,
                           post5=post5,
                           socials='col-sm-2 socialContainer')

# displays the daily favourites page
@app.route('/favourites')
def favourites():
    if 'user' not in session:
        return redirect(url_for('index'))

    name = models.Account.query.get(session['user']).name
    return render_template('daily_favourites.html',
                           name=name,
                           hide='',
                           hide2='hidden',
                           active1='',
                           active2='',
                           active3='active',
                           active4='',
                           active5='',
                           active6='',
                           timeline='col-sm-2 show',
                           title='Favourites Timeline',
                           title1='02/02/2018',
                           title2='09/02/2018',
                           title3='16/02/2018',
                           title4='23/02/2018',
                           title5='02/03/2018',
                           socials='col-sm-2 socialContainer')

# displays the about page
@app.route('/about')
def about():
    if 'user' not in session:
        return redirect(url_for('index'))

    name = models.Account.query.get(session['user']).name
    return render_template('about_me.html',
                           name=name,
                           hide='',
                           hide2='hidden',
                           active1='',
                           active2='',
                           active3='',
                           active4='active',
                           active5='',
                           active6='',
                           timeline='col-sm-2 invisible',
                           title='',
                           title1='',
                           title2='',
                           title3='',
                           title4='',
                           title5='',
                           socials='col-sm-2 socialContainer')

# displays the contact page
@app.route('/contact')
def contact():
    if 'user' not in session:
        return redirect(url_for('index'))

    name = models.Account.query.get(session['user']).name
    return render_template('contact.html',
                           name=name,
                           hide='',
                           hide2='hidden',
                           active1='',
                           active2='',
                           active3='',
                           active4='',
                           active5='active',
                           active6='',
                           timeline='col-sm-2 invisible',
                           title='',
                           title1='',
                           title2='',
                           title3='',
                           title4='',
                           title5='',
                           socials='col-sm-2 socialContainer')

# displays the posts that the user has favourited
@app.route('/user')
def user():
    if 'user' not in session:
        return redirect(url_for('index'))

    name = models.Account.query.get(session['user']).name
    posts = models.Post.query.all()


    return render_template('user.html',
                           name=name,
                           hide='',
                           hide2='hidden',
                           active1='',
                           active2='',
                           active3='',
                           active4='',
                           active5='',
                           active6='active',
                           timeline='col-sm-2 invisible',
                           title='',
                           title1='',
                           title2='',
                           title3='',
                           title4='',
                           title5='',
                           posts=posts,
                           socials='col-sm-2 socialContainer')

# dispalys the page for a user to change their password
@app.route('/change', methods=['GET', 'POST'])
def change():
    if 'user' not in session:
        return redirect(url_for('index'))

    name = models.Account.query.get(session['user']).name
    form = ChangeForm()

    if form.validate_on_submit():
        try:
            if change(form.old.data, form.new.data) == 0:
                flash('Your password has been changed.')
            else:
                flash('Your password has not been changed. Make sure you have entered your old password correctly.')

        except:
            flash('An error occurred and your password has not been changed. Make sure you have entered your old password correctly.')

    return render_template('change.html',
                           name=name,
                           hide='',
                           hide2='hidden',
                           active1='',
                           active2='',
                           active3='',
                           active4='',
                           active5='',
                           timeline='col-sm-2 invisible',
                           title='',
                           title1='',
                           title2='',
                           title3='',
                           title4='',
                           title5='',
                           form=form,
                           socials='col-sm-2 socialContainer')

# logs the user out
@app.route('/logout')
def logout():
    if 'user' not in session:
        return redirect(url_for('index'))

    session.pop('user', None)
    return redirect(url_for('index'))

# favourites the first blog post
@app.route('/post1')
def post1():
    if 'user' not in session:
        return redirect(url_for('index'))

    from app import db, models

    post = models.Post.query.get(1)
    account = models.Account.query.get(session['user'])
    post.comments.append(account)
    db.session.commit()

    return redirect(url_for('user'))

# favourites the second blog post
@app.route('/post2')
def post2():
    if 'user' not in session:
        return redirect(url_for('index'))

    from app import db, models

    post = models.Post.query.get(2)
    account = models.Account.query.get(session['user'])
    post.comments.append(account)
    db.session.commit()

    return redirect(url_for('user'))

# favourites the third blog post
@app.route('/post3')
def post3():
    if 'user' not in session:
        return redirect(url_for('index'))

    from app import db, models

    post = models.Post.query.get(3)
    account = models.Account.query.get(session['user'])
    post.comments.append(account)
    db.session.commit()

    return redirect(url_for('user'))

# favourites the fourth blog post
@app.route('/post4')
def post4():
    if 'user' not in session:
        return redirect(url_for('index'))

    from app import db, models

    post = models.Post.query.get(4)
    account = models.Account.query.get(session['user'])
    post.comments.append(account)
    db.session.commit()

    return redirect(url_for('user'))

# favourites the fifth blog post
@app.route('/post5')
def post5():
    if 'user' not in session:
        return redirect(url_for('index'))

    from app import db, models

    post = models.Post.query.get(5)
    account = models.Account.query.get(session['user'])
    post.comments.append(account)
    db.session.commit()

    return redirect(url_for('user'))

# logs an account in
def login(username, password):
    from app import db, models

    accounts = models.Account.query.all()

    for i in accounts:
        if i.username == username:
            if i.password == password:
                session['user'] = i.id
                return 0, i.name
            else:
                return 1, None

    return 1, None

# creates a new account
def register(name, username, password):
    from app import db, models

    accounts = models.Account.query.all()

    newAccount = models.Account(name=name, username=username, password=password)
    db.session.add(newAccount)
    db.session.commit()

# changes the password of the currently logged in account
def change(old, new):
    from app import db, models

    account = models.Account.query.get(session['user'])

    if account.password == old:
        account.password = new
        db.session.commit()

        return 0

    return 1

from flask import (
    Blueprint, 
    render_template, 
    url_for, 
    redirect, 
    request, 
    session, 
    flash
    )
from app.forms import UserCreationForm, UserLoginForm,ProfileUpdate
from app.models import User, db, Blog
from app.forms import NewBlogForm, UpdateBlogForm
from app.helpers import get_match, get_all_current
from flask_login import (
    current_user, 
    login_fresh, 
    login_required, 
    login_user,
    logout_user
    )


home = Blueprint(
    'home',
    __name__,
    static_folder='static',
    template_folder='templates',
    # url_prefix='/'
)

@home.route('/')
def homepage():
    blogs = Blog.query.all()
    return render_template('index.html', blogs=blogs)

@home.route('/blogs/myposts')
@login_required
def my_blogs():
    blogs = current_user.blogs
    return render_template('blogs.html', blogs=blogs)

@home.route('/login', methods=['GET','POST'])
def sign_in():
    form = UserLoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('home.homepage'))

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.confirm_password(form.password.data):
            flash("Check your email or password", 'danger')
            return redirect(url_for('home.sign_in'))

        login_user(user)
        session.permanent = True
        flash(f'Welcome back {user.username}', 'success')
        return redirect(url_for('home.homepage'))

    return render_template('login.html', form=form)


@home.route('/register', methods=['GET','POST'])
def sign_up():
    form = UserCreationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.encrypt_password(form.password.data)
        try:
            db.session.add(user)
            db.session.commit()
            flash('Account created successfully', 'success')
            return redirect(url_for('home.sign_in'))
        except Exception as e:
            print(e)
            flash('Account creation failed please try again')
            return redirect(url_for('home.sign_up'))
    return render_template('register.html', form=form)


@home.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@home.route('/profile/edit', methods=['GET', 'POST'])
def update_profile():
    title = 'Update profile'
    form = ProfileUpdate()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Changes saved successfully",category='success')
        return redirect(url_for('home.homepage'))
    if request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        # form.done.data = todo.done
    return render_template('update_profile.html', form=form, title=title)


@home.route('/logout')
def sign_out():
    logout_user()
    flash('You are currently logged out', 'info')
    return redirect(url_for('home.sign_in'))


# Blog posts

@home.route('/new_blog', methods=['GET','POST'])
@login_required
def new_post():
    form = NewBlogForm()
    if form.validate_on_submit():
        blog = Blog(title=form.title.data, subtitle=form.subtitle.data,body=form.body.data)
        blog.author_id = current_user.id
        # blog=Blog()
        # blog.title = form.title.data
        # blog.subtitle = form.subtitle.data
        # blog.body = form.body.data
        # blog.author_id = current_user.id
        try:
            print(blog)
            db.session.add(blog)
            db.session.commit()
            flash('Blog created successfully', 'success')
            return redirect(url_for('home.homepage'))
        except Exception as e:
            print(e)
            flash('Failed to add blog try again')
            return redirect(url_for('home.homepage'))
    return render_template('new.html', form=form)


@home.route('/update/<int:id>', methods=['GET', 'POST'])
def update_blog(id):
    title = 'updtate'
    form = UpdateBlogForm()
    blog = Blog.query.filter_by(id=id).first()
    if form.validate_on_submit():
        blog.title = form.title.data
        blog.subtitle = form.subtitle.data
        blog.body = form.body.data
        try:
            db.session.commit()
            flash("Blog updated successfully",category='successs')
            return redirect(url_for('home.homepage'))
        except Exception as e:
            flash("Could not update the blog",category='danger')
            return redirect(url_for('home.my_blogs'))
    if request.method == 'GET':
        form.title.data = blog.title
        form.subtitle.data = blog.subtitle
        form.body.data = blog.body
        # form.done.data = todo.done
    return render_template('update.html', form=form, title=title)




@home.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    blog = Blog.query.get(id)
    print(blog.id)
    db.session.delete(blog)
    db.session.commit()
    flash(f"Deleted the todo: {blog.body}", 'warning')
    return redirect(url_for('home.homepage'))
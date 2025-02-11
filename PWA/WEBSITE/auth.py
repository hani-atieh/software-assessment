from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, render_template, request, flash, redirect, url_for, request
from .models import User, Review
from . import db
from .models import Games
from flask_login import login_user, login_required, logout_user, current_user
import datetime
from .forms import GameSelectForm

auth = Blueprint('auth', __name__)
logged_in : bool = False
gameimage = ""

@auth.route('/logout')
def logout():
    flash('You have been logged out successfully', category='success')
    logout_user()
    logged_in = False
    return redirect(url_for('auth.login'))


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('You have logged in successfully', category='success')
                login_user(user, remember=True)
                logged_in = True
                return redirect(url_for('views.home'))
            else:
                flash('The password you have written is incorrect, try again', category='error')
        else:
            flash('There is no account created with that email address..', category='error')

    return render_template("login.html", user=current_user)



@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        username = request.form.get('username')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('There is already an account created with that email', category='error')
        elif len(email) < 4:
            flash('Your email must have more than 3 characters in it..', category='error')
        elif len(username) < 2:
            flash('The username you create must be atleast 2 characters long', category='error')
        elif len(password) < 7:
            flash('Your password must be atleast 7 characters long', category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            logged_in = True
            flash('Your account has been successfully created!', category='success')
            return redirect(url_for('auth.login'))
            

    return render_template("signup.html", user=current_user)
    


@auth.route('/posting', methods=['GET', 'POST'])
@login_required
def post_reviews():

    form = GameSelectForm()

    if request.method == 'POST':
        review = request.form.get('review')
        score = request.form.get('score')
        title = request.form.get('title')
        username = current_user.username
        userid = current_user.id
        time = datetime.datetime.now()
        day = time.strftime("%d ")
        month = time.strftime("%b ")
        year = time.strftime("%Y")
        date = day + month + year
        print(date)

        acceptable_score = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

        if len(title) < 1:
            flash("The name of your chosen game cannot be left blank", category='error')
        elif len(review) < 1:
            flash("Don't forget to write your review!", category='error')
        elif len(score) < 1:
            flash("Give this game a rating before proceeding.", category='error')
        elif score not in acceptable_score:
            flash("The rating you have given is invalid. Please enter a number between 0 and 10.", category='error')
        else:
            new_review = Review(text=review, user_name=username, user_id=userid, score=int(score), title=title, date=date)
            db.session.add(new_review)
            db.session.commit()
            flash('Your review has been posted', category='success')
            return redirect(url_for('views.home'))

    return render_template("submitreview.html", user=current_user, form=form)
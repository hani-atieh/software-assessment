from flask import Blueprint, render_template, request
from .auth import auth
from .auth import logged_in
from flask_login import login_required, current_user
from .models import *
from sqlalchemy import *
from flask_sqlalchemy import *
from sqlalchemy.sql import *
from WEBSITE import db




views = Blueprint('views', __name__)
image = str
page_title = str


@views.route('/')
def home():
    return render_template("home.html", page_title = "Home", user=current_user)



@views.route('/games to review')
def gamelist():
    return render_template("gamestoreview.html", page_title = "Games To Review", user=current_user)



@views.route('/reviews', methods=['GET', 'POST'])
def view_reviews():
    row = 0
    reviews = db.session.query(Review).all()
    review_count = len(reviews)
    print(review_count)
    

    
    return render_template("reviews.html", page_title = "View All Reviews", user=current_user, 
                           reviews=reviews, row=row, review_count=review_count
                           )


@views.route('/about')
def about():
    
    return render_template("aboutweb.html", page_title = "About This Website", user=current_user)
from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import db, Review
from app.forms import ReviewForm

review_routes = Blueprint('reviews', __name__)

#get all reviews
@review_routes.route('')
def getAllReviews():
  reviews = Review.query.all()

  return {'reviews': [review.to_dict() for review in reviews]}


#get one review
@review_routes.route('/<int:id>')
def getOneReview(id):
  review = Review.query.get(id)

  return review.to_dict()


#create a new review
@review_routes.route('/<int:id>', methods=['POST'])
def createReview(id):
  form = ReviewForm()

  new_review = Review(
    userId = form.data['userId'],
    bookingId = form.data['bookingId'],
    numberOfStars = form.data['numberOfStars'],
    content = form.data['content']
  )

  db.session.add(new_review)
  db.session.commit()

  return new_review.to_dict()



@review_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def deleteReview(id):
  review = Review.query.get(id)
  db.session.delete(review)
  db.session.commit()

  return review.to_dict()
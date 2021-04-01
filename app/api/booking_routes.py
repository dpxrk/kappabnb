from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import db, Booking, Picture, Review, State, Comment, Reservation, User

booking_routes = Blueprint("bookings", __name__)


#get all booking_routes
@booking_routes.route('/')
def allBookings():
  bookings = Booking.query.all()
  return {"bookings" : [booking.to_dict() for booking in bookings]}


#get one booking
@booking_routes.route('/<int:id>')
def getOneBooking(id):
  booking = Booking.query.get(id)
  pictures = Picture.query.filter_by(bookingId=id).all()
  reviews = Review.query.filter_by(bookingId=id).all()
  # host = User.query.get(Booking.userId)
  state = Booking.query.filter_by(Booking.stateId==id).first()

  bookingData = {**booking.to_dict()}
  bookingData['booking'] = booking
  bookingData['pictures'] = [picture.to_dict() for picture in pictures]
  bookingData['reviews'] = [review.to_dict() for review in reviews]
  # bookingData['host'] = host
  bookingData['State'] = state

  return bookingData
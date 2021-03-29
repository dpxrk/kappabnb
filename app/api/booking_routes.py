from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import db, Booking, Picture, Review, State, Comment, Reservation, User


booking_route = Blueprint('booking', __name__)

@booking_routes.routes('/')
@login_required
  def allBookings():
    bookings = Booking.query.all()
    return {"bookings" : [booking.to_dict() for booking in bookings]}


@booking_routes.routes('/<int:id>')
@login_required
  def getOneBooking(id):
    booking = Booking.query.get(id)
    pictures = Picture.query.filter_by(bookingId=id).all()
    reviews = Review.query.filter_by(bookingId=id).all()
    host = User.query.get(booking.userId)
    state = State.query.filter_by(bookingId=id).first()

    bookingData = dict()
    bookingData['booking'] = booking
    bookingData['pictures'] = [picture.to_dict() for picture in pictures]
    bookingData['reviews'] = [review.to_dict() for review in reviews]
    bookingData['host'] = host
    bookingData['State'] = state

    return bookingData
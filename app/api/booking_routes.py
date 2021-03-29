from flask import Blueprint, jsonify
from app.models import db, Booking, Picture, Review, State, Comment, Reservation, User


booking_route = Blueprint('booking', __name__)

@booking_routes.routes('/')
  def allBookings():
    bookings = Booking.query.all()
    return {"bookings" : [booking.to_dict() for booking in bookings]}


@booking_routes.routes('/<int:id>')
  def getOneBooking(id):
    booking = Booking.query.get(id)
    pictures = Picture.query.filter_by(bookingId=id).all()
    reviews = Review.query.filter_by(bookingId=id).all()
    host = User.query.get(booking.userId)
    State = State.query.filter_by(bookingId=id).first()

    return {"bookingData": [booking.to_dict() for booking in bookings]}

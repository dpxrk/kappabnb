from flask import Blueprint
from flask_login import login_required
from app.models import db, Booking, Picture, Review, State, Comment, Reservation, User
from app.forms import ReservationForm

reservation_routes = Blueprint('reservation', __name__)

#get all existing reservations
@reservation_routes.route('/')
@login_required
def getAllReservations():
  reservations = Reservation.query.all()
  return {'reservations': [reservation.to_dict() for reservation in reservations]}

#get one reservation
@reservation_routes.route('/<int:id>')
@login_required
def getOneReservation(id):
  reservation = Reservation.query.get(id)

  if reservation:
    return jsonify(reservation)
  else:
    return {"error":"error"}


#create a new reservations
@reservation_routes.route('/')
@login_required
def createNewReservation():
  form = ReservationForm()

  new_reserve = ReservationForm(
    userId = form.data['userId'],
    bookingId = form.data['bookingId'],
    startDate = form.data['startDate'],
    endDate = form.data['endDate']
  )

  db.session.add(new_reserve)
  db.session.commit()
  return new_reserve.to_dict()

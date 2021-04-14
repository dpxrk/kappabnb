from .db import db
import datetime



class Reservation(db.Model):
  __tablename__="reservations"

  id = db.Column(db.Integer, primary_key=True, nullable=False)
  userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  bookingId = db.Column(db.Integer, db.ForeignKey('bookings.id'), nullable=False)
  startDate = db.Column(db.DateTime, nullable=False)
  endDate = db.Column(db.DateTime, nullable=False)
  createdAt = db.Column(db.DateTime("%Y-%m-%d"),  default=db.func.current_timestamp())
  updatedAt = db.Column(db.DateTime("%Y-%m-%d"),  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

  user = db.relationship('User', backref='reservations')
  booking = db.relationship('Booking', backref='reservations')


  def to_dict(self):
    return {
      'id': self.id,
      'userId': self.userId,
      'bookingId': self.bookingId,
      'startDate' : self.startDate,
      'endDate' :self.endDate
    }


  def to_dict_with_booking_information(self):
    title = self.booking.title
    state = self.booking.state.stateName
    picture = self.booking.pictures[0].photoURL

    return {
      'id': self.id,
      'startDate' : self.startDate,
      'endDate': self.endDate,
      'title': title,
      'state': state,
      'picture' : picture,
      'bookingId': self.bookingId,
      'userId': self.userId
    }

from .db import db


class State(db.Model):
  __tablename__='states'


  id = db.Column(db.Integer, primary_key=True,nullable=False)
  stateName = db.Column(db.String(50), nullable=False)
  capital = db.Column(db.String(50), nullable=False)
  bookingId = db.Column(db.Text, db.ForeignKey('bookings.id'), nullable=False)
  createdAt = db.Column(db.DateTime,  default=db.func.current_timestamp())
  updatedAt = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

  booking = db.relationship('Booking', backref='states')

  def to_dict(self):
    return {
      'id': self.id,
      'stateName':self.stateName,
      'capital': self.captial,
      'bookingId':self.bookingId,
    }

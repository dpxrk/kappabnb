from .db import db
from sqlalchemy.orm import relationship

class Picture(db.Model):
  __tablename__ ='pictures'


  id = db.Column(db.Integer, primary_key=True)
  bookingId = db.Column(db.Integer, db.ForeignKey('bookings.id'), nullable=False)
  photoURL = db.Column(db.Text, nullable = False)
  createdAt = db.Column(db.DateTime,  default=db.func.current_timestamp())
  updatedAt = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
  booking = relationship('Booking', back_populates='pictures')

  def to_dict(self):
    return {
      "id": self.id,
      "bookingId": self.bookingId,
      "photoURL": self.photoURL
    }
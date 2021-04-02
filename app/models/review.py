from .db import db


class Review(db.Model):
  __tablename__ = 'reviews'

  id = db.Column(db.Integer, primary_key=True)
  userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  bookingId = db.Column(db.Integer, db.ForeignKey('bookings.id'), nullable=False)
  numberOfStars = db.Column(db.Integer)
  content = db.Column(db.Text, nullable=False)
  booking = db.relationship('Booking')
  user = db.relationship('User', backref='reviews')

  def to_dict(self):
    return {
      "id": self.id,
      "userId": self.userId,
      'bookingId': self.bookingId,
      'numberOfStars': self.numberOfStars,
      'content': self.content,
    }
from .db import db
from .bookingsAmenitiesJoinTable import bookingsAmenitiesJoinTable


class Amenity(db.Model):
  __tablename__= 'amenities'


  id = db.Column(db.Integer, primary_key=True)
  amenity = db.Column(db.String, nullable=False, unique=True)

  bookings = db.relationship('Booking', secondary=bookingsAmenitiesJoinTable, back_populates='amenities')
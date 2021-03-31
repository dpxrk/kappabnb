from .db import db

bookingsAmenitiesJoinTable = db.Table('bookingsAmenitiesJoinTable',
                                      db.Column('bookingId', db.Integer, db.ForeignKey('bookings.id')),
                                      db.Column('amenityId', db.Integer, db.ForeignKey('amenities.id')),
                                      )
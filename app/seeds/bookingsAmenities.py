from app.models import db, bookingsAmenitiesJoinTable
from app.seeds import booking # 50 bookings for now
from app.seeds import amenity #17 amenities
import random

def seed_bookingsAmenities():


  count = 1
  while count < 500:
    newBookingAmenitiesJoin = bookingsAmenitiesJoinTable(
      bookingId = (random.randrange(1,50))
      amenityId = (random.range(1,17))
    )
    count += 1
    db.session.add(newBookingAmenitiesJoin)


  db.session.commit()

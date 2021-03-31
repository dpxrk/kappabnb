from app.models import db, bookingsAmenitiesJoinTable
from app.seeds import bookings
from app.seeds import amenities
import random


# 50 bookings for now
 #17 amenities
def seed_bookingsAmenities():


  count = 1
  while count < 500:
    newBookingAmenitiesJoin = bookingsAmenitiesJoinTable(
      bookingId = (random.randrange(1,50)),
      amenityId = (random.range(1,17))
    )
    count += 1
    db.session.add(newBookingAmenitiesJoin)


  db.session.commit()



def undo_bookingsAmenities():
  db.session.excecute("TRUNCATE bookingsAmenities;")
  db.session.commit()
from app.models import db, bookingsAmenitiesJoinTable
from app.seeds import bookings
from app.seeds import amenities
import random


# 50 bookings for now
 #17 amenities
def seed_bookingsAmenities():


  count = 1
  while count < 50:
    for num in range (1, 17):
      new_join = bookingsAmenitiesJoinTable.insert().values(bookingId=(count), amenityId=num)
      db.session.execute(new_join)
    count += 1

  db.session.commit()




def undo_bookingsAmenities():
  db.session.excecute("TRUNCATE bookingsAmenities;")
  db.session.commit()
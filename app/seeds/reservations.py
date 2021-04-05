from app.models import db, Reservation
import random

def seed_reservations():
  reservation1 = Reservation(
    userId=10,
    bookingId=(random.randrange(0,50)),
    startDate=("2/1/21"),
    endDate=("2/7/21")
  )
  reservation2 = Reservation(
    userId=10,
    bookingId=(random.randrange(0,50)),
    startDate=("1/5/21"),
    endDate=("1/12/21")
  )
  reservation3 = Reservation(
    userId=10,
    bookingId=(random.randrange(0,50)),
    startDate=("1/15/21"),
    endDate=("1/19/21")
  )

  db.session.add(reservation1)
  db.session.add(reservation2)
  db.session.add(reservation3)

  db.session.commit()





def undo_reservations():
  db.session.execute("TRUNCATE reservation;")
  db.session.commit()

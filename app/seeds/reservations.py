from app.models import db, Reservation
import random

def seed_reservations():
  reservation1 = Reservation(
    userId=10,
    bookingId=(random.randrange(0,50)),
    startDate=("2021-02-01"),
    endDate=("2021-02-07")
  )
  reservation2 = Reservation(
    userId=10,
    bookingId=(random.randrange(0,50)),
    startDate=("2021-01-05"),
    endDate=("2021-01-12")
  )
  reservation3 = Reservation(
    userId=10,
    bookingId=(random.randrange(0,50)),
    startDate=("2021-01-15"),
    endDate=("2021-01-19")
  )

  db.session.add(reservation1)
  db.session.add(reservation2)
  db.session.add(reservation3)

  db.session.commit()





def undo_reservations():
  db.session.execute("TRUNCATE reservation;")
  db.session.commit()

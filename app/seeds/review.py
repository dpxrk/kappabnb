from app.models import Review
import random

def seed_reviews():
  reviewComments=[
    "Not able to tell you how happy I am with place",
    "Place is awesome! We're loving it.",
    "Place is both attractive and highly adaptable. I could probably go into sales for you. We were treated like royalty.",
    "I highly recommend this location",
    "Incredible Host",
    "Very neat and clean"
  ]

  count = 0
  while count < 50:
    new_review = Review(
      userId=(random.randrange(1,12))
      bookingId=(random.randrange(0,50))
      numberOfStars=(random.randrange(1, 6))
      content=reviewComments[random.randrange(0,5)]
    )
    count += 1
    db.session.add(new_review)

  db.session.commit()



def undo_reviews():
  db.session.execute('TRUNCATE reviews;')
  db.session.commit()
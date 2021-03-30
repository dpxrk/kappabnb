from app.models import db, Booking
import random


def seed_bookings():
  alabamaBooking = Booking(
    title='Modern House w/ Wi-Fi + Netflix',
    userId=(random.randrange(1,10)),
    price=(random.randrange(50,200))
    description='My modern 3-bedroom house has everything you need for your Montgomery trip. The unit comes with Wi-Fi, Netflix, and a TV. An ideal base to explore Montgomery.'
    address='103 N Perry St',
    stateId=1
  )

  alaskaBooking = Booking(
    title= 'Green House w/ Free Coffee and Tea + Breakfast'
    userId=(random.randrange(1,10)),
    price=(random.randrange(50,200)),
    description="Stay in this green house and live like a true local in Juneau. Our rental comes with 1 bedroom -- free coffee and tea, breakfast, a TV -- we've got everything you need.",
    address='155 S Seward St',
    stateId=2
  )

  arizonaBooking = Booking(
    title= 'Charming Bungalow w/ Free Coffee and Tea + Breakfast',
    userId=(random.randrange(1,10)),
    price=(random.randrange(50,200)),
    description="Want to visit Sacramento without breaking the bank? We have exactly what you're looking for. Our charming bungalow comes with 4 bedrooms, hot tub, indoor fireplace, free coffee and tea, breakfast, and a TV.",
    address='1700 W Washington St'
    stateId=3
  )

  arkansasBooking = Booking(
    title= "Charming Cabin w/ a Dryer + a Coffee Maker",
    userId=(random.randrange(1,10)),
    price=(random.randrange(50,200)),
    description="Thinking about visiting Little Rock? I have a 3-bedroom cabin that will be perfect for your stay. This charming rental comes with amenities such as a dryer, a coffee maker, and a TV. Our private bathroom and living room are yours to enjoy, as well.",
    address="500 Woodlane St",
    stateId=4
  )

  californiaBooking = Booking(
    title="Rare Villa w/ a Dryer + Free Parking"
    userId=(random.randrange(1,10)),
    price=(random.randrange(50,200)),
    description="My rare 5-bedroom villa in Sacramento comes complete with hot tub, indoor fireplace, and living room. The a dryer, free parking, and a coffee maker will make you wish you could stay even longer. If you rent my Airbnb, I know you'll have a great stay in Sacramento."
    stateId=5
  )

  coloradoBooking = Booking(
    
  )

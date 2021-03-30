from app.models import db, Amenity


def seed_amenities(): #17 Amenities
  heating = Amenity(amenity='Heating')
  AC = Amentiy(amenity='Air-conditioning')
  washer = Amenity(amenity='Washer')
  dryer = Amenity(amenity='Dryer')
  wifi = Amenity(amenity='Washer')
  netflix = Amenity(amenity='Netflix')
  roku = Amenity(amenity='Roku TV')
  selfCheckIn = Amenity(amenity='Self Check In')
  freeParking = Amenity(amenity='Free Parking')
  laptopFriendly = Amenity(amenity='Laptop-friendly Workspace')
  freeCoffeeAndTea = Amenity(amenity='Free Coffee and Tea')
  bike = Amenity(amenity='bike')
  coffeeMaker = Amenity(amenity='Coffee Maker')
  shampoo = Amenity(amenity="Shampoo")
  conditioner = Amenity(amenity='Conditioner')
  hairDryer = Amenity(amenity="Hair dryer")
  iron = Amenity(amenity='iron')



  db.session.add(heating)
  db.session.add(AC)
  db.session.add(washer)
  db.session.add(dryer)
  db.session.add(wifi)
  db.session.add(netflix)
  db.session.add(roku)
  db.session.add(selfCheckIn)
  db.session.add(freeParking)
  db.session.add(laptopFriendly)
  db.session.add(freeCoffeeandTea)
  db.session.add(bike)
  db.session.add(coffeeMaker)
  db.session.add(shampoo)
  db.session.add(conditioner)
  db.session.add(hairDryer)
  db.session.add(iron)


  db.session.commit()


def undo_amenities():
  db.session.execute('TRUNCATE amenities;')
  db.session.commit()
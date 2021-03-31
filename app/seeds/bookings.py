from app.models import db, Booking
import random


def seed_bookings():
  alabamaBooking = Booking(
    title='Modern House',
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description='My modern 3-bedroom house has everything you need for your Montgomery trip. The unit comes with Wi-Fi, Netflix, and a TV. An ideal base to explore Montgomery.',
    address='103 N Perry St',
    stateId=1
  )

  alaskaBooking = Booking(
    title= 'Green House',
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Stay in this green house and live like a true local in Juneau. Our rental comes with 1 bedroom -- free coffee and tea, breakfast, a TV -- we've got everything you need.",
    address='155 S Seward St',
    stateId=2
  )

  arizonaBooking = Booking(
    title= 'Charming Bungalow',
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Want to visit Sacramento without breaking the bank? We have exactly what you're looking for. Our charming bungalow comes with 4 bedrooms, hot tub, indoor fireplace, free coffee and tea, breakfast, and a TV.",
    address='1700 W Washington St',
    stateId=3
  )

  arkansasBooking = Booking(
    title= "Charming Cabin",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Thinking about visiting Little Rock? I have a 3-bedroom cabin that will be perfect for your stay. This charming rental comes with amenities such as a dryer, a coffee maker, and a TV. Our private bathroom and living room are yours to enjoy, as well.",
    address="500 Woodlane St",
    stateId=4
  )

  californiaBooking = Booking(
    title="Rare Villa ",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="My rare 5-bedroom villa in Sacramento comes complete with hot tub, indoor fireplace, and living room. The a dryer, free parking, and a coffee maker will make you wish you could stay even longer. If you rent my Airbnb, I know you'll have a great stay in Sacramento.",
    address="1215 10th St",
    stateId=5
  )

  coloradoBooking = Booking(
    title="Glamorous Villa",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="My glamorous 8-bedroom villa has everything you need for your Denver trip. The unit comes with a washer, a coffee maker, and a high chair. During your stay, you can also enjoy using a convenient gym, indoor fireplace, and living room. Our Airbnb is within driving distance to several popular bars, hikes, and national parks. An ideal base to explore Denver.",
    address="1437 Bannock St",
    stateId=6
  )

  connecticutBooking = Booking(
    title="Welcoming Cottage w/ AC + Gym",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Bars, hikes, and national parks in Hartford will make this a vacation to remember, and my welcoming 4-bedroom cottage comes complete with gym, indoor fireplace, and living room. The AC, laptop-friendly workspace, and a high chair will make you wish you could stay even longer. If you rent my Airbnb, I know you'll have a great stay in Hartford.",
    address="550 Main St",
    stateId=7
  )

  delawareBooking = Booking(
    title='Historic Resort w/ Netflix + Gym',
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="My historic 2-bedroom resort has everything you need for your Dover trip. The unit comes with Netflix, free coffee and tea, and breakfast. During your stay, you can also enjoy using a convenient gym, indoor fireplace, and living room. Our Airbnb is within driving distance to several popular bars, hikes, and national parks. An ideal base to explore Dover.",
    address="15 Loockerman Plaza",
    stateId=8
  )

  floridaBooking = Booking(
    title="Historic Chalet w/ a Washer + Gym",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Stay in this historic chalet and live like a true local in Tallahassee. We're within driving distance to bus routes, national parks, and night clubs. Our rental comes with 7 bedrooms, and a gym, private bathroom, and indoor fireplace that you're free to use any time. A washer, free coffee and tea, an iron -- we've got everything you need.",
    address="300 S Adams St",
    stateId=9
  )

  georgiaBooking = Booking(
    title="Historic Loft w/ Roku TV + Private Bathroom",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Want to visit Atlanta without breaking the bank? We have exactly what you're looking for. Our historic loft comes with 3 bedrooms, private bathroom, kitchen, living room, Roku TV, free coffee and tea, and a hair dryer, and we're within driving distance to bus routes, national parks, and night clubs.",
    address="55 Trinity Ave SW",
    stateId=10,
  )

  hawaiiBooking = Booking(
    title="Secluded Boutique hotel w/ a Dryer + Hot Tub",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Thinking about visiting Honolulu? I have a 6-bedroom boutique hotel that will be perfect for your stay. This secluded rental comes with amenities such as a dryer, Wi-Fi, and a bike. Our hot tub, private bathroom, and kitchen are yours to enjoy, as well. If you want to go to bus routes, national parks, and night clubs, we're within walking distance.",
    address="530 S King St",
    stateId=11,
  )

  idahoBooking = Booking(
    title='Glamorous Cottage w/ a Dryer + Hot Tub',
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Shops, national parks, and night clubs in Boise will make this a vacation to remember, and my glamorous 6-bedroom cottage comes complete with hot tub, private bathroom, and kitchen. The a dryer, Wi-Fi, and a bike will make you wish you could stay even longer. If you rent my Airbnb, I know you'll have a great stay in Boise.",
    address="150 N Capitol Blvd",
    stateId=12,
  )

  illinoisBooking = Booking(
    title='Rustic House w/ AC + Hot Tub',
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="My rustic 3-bedroom house has everything you need for your Springfield trip. The unit comes with AC, Wi-Fi, and a bike. During your stay, you can also enjoy using a convenient hot tub, kitchen, and living room. Our Airbnb is within walking distance to several popular hikes, national parks, and beaches. An ideal base to explore Springfield.",
    address="800 E Monroe St",
    stateId=12,
  )

  indianaBooking = Booking(
    title='Spacious Apartment w/ a Dryer + Living Room',
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Hikes, national parks, and beaches in Indianapolis will make this a vacation to remember, and my spacious 4-bedroom apartment comes complete with living room. The a dryer, Netflix, and free coffee and tea will make you wish you could stay even longer. If you rent my Airbnb, I know you'll have a great stay in Indianapolis.",
    address="200 E Washington St",
    stateId=14,
  )

  iowaBooking = Booking(
    title='Modern Bungalow w/ a Washer + Living Room',
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="My modern 5-bedroom bungalow has everything you need for your Des Moines trip. The unit comes with a washer, Wi-Fi, and breakfast. During your stay, you can also enjoy using a convenient living room. Our Airbnb is within walking distance to several popular hikes, national parks, and beaches. An ideal base to explore Des Moines",
    address="400 Robert D. Ray Dr",
    stateId=15,
  )

  kansasBooking = Booking(
    title='Glamorous RV w/ Netflix + Living Room',
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Stay in this glamorous RV and live like a true local in Topeka. We're within walking distance to hikes, national parks, and beaches. Our rental comes with 6 bedrooms, and a living room that you're free to use any time. Netflix, free parking, an iron -- we've got everything you need.",
    address="215 SE 7th S",
    stateId=16,
  )

  kentuckyBooking = Booking(
    title="Green Cabin w/ Hangers + Indoor Fireplace",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Want to visit Frankfort without breaking the bank? We have exactly what you're looking for. Our green cabin comes with 7 bedrooms, indoor fireplace, kitchen, living room, hangers, and a hair dryer, and we're within walking distance to hikes, national parks, and beaches.",
    address="315 W 2nd St",
    stateId=17,
  )

  louisianaBooking = Booking(
    title="Luxurious Chalet w/ AC + Indoor Fireplace",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Thinking about visiting Baton Rouge? I have a 8-bedroom chalet that will be perfect for your stay. This luxurious rental comes with amenities such as AC, laptop-friendly workspace, and a hair dryer. Our indoor fireplace, kitchen, and living room are yours to enjoy, as well. If you want to go to hikes, national parks, and beaches, we're within walking distance.",
    address="222 St Louis St",
    stateId=18,
  )

  maineBooking = Booking(
    title= "Peaceful Cottage w/ a Bike + Gym",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="My peaceful 9-bedroom cottage has everything you need for your Augusta trip. The unit comes with a bike, a high chair, and a hair dryer. During your stay, you can also enjoy using a convenient gym, private bathroom, and living room. Our Airbnb is within walking distance to several popular hikes, national parks, and beaches. An ideal base to explore Augusta.",
    address="16 Cony St",
    stateId=19,
  )

  marylandBooking = Booking(
    title="Secluded Cottage w/ a Bike + Gym",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Stay in this secluded cottage and live like a true local in Annapolis. We're within walking distance to hikes, national parks, and beaches. Our rental comes with 1 bedroom, and a gym, private bathroom, and living room that you're free to use any time. A bike, a high chair, a hair dryer -- we've got everything you need.",
    address='160 Duke of Gloucester St',
    stateId=20
  )

  massachusettsBooking = Booking(
    title="Charming Guest suite w/ Wi-Fi + Gym",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Want to visit Boston without breaking the bank? We have exactly what you're looking for. Our charming guest suite comes with 2 bedrooms, gym, private bathroom, living room, Wi-Fi, Netflix, and a hair dryer, and we're within walking distance to hikes, national parks, and beaches.",
    address="1 City Hall Square",
    stateId=21
  )

  michiganBooking = Booking(
    title="Comfortable Guesthouse w/ Wi-Fi + Gym",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Thinking about visiting Lansing? I have a 3-bedroom guesthouse that will be perfect for your stay. This comfortable rental comes with amenities such as Wi-Fi, Netflix, and a hair dryer. Our gym, private bathroom, and living room are yours to enjoy, as well. If you want to go to hikes, national parks, and beaches, we're within walking distance.",
    address='124 W Michigan Ave',
    stateId=22,
  )

  minnesotaBooking = Booking(
    title='Welcoming Hostel w/ Free Parking + Kitchen',
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Hikes, national parks, and beaches in St. Paul will make this a vacation to remember, and my welcoming 4-bedroom hostel comes complete with kitchen and kitchenette. The free parking and a high chair will make you wish you could stay even longer. If you rent my Airbnb, I know you'll have a great stay in St. Paul.",
    address="15 W Kellogg Blvd",
    stateId=23,

  )

  mississippiBooking = Booking(
    title='Upscale Hotel w/ Heating + Kitchen',
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="My upscale 5-bedroom hotel has everything you need for your Jackson trip. The unit comes with heating and a TV. During your stay, you can also enjoy using a convenient kitchen and kitchenette. Our Airbnb is within walking distance to several popular hikes, national parks, and beaches. An ideal base to explore Jackson.",
    address="219 S President St",
    stateId=24,
  )

  missouriBooking = Booking(
    title="Upscale Loft w/ Heating + Private Bathroom",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Stay in this upscale loft and live like a true local in Jefferson City. We're within walking distance to hikes, national parks, and beaches. Our rental comes with studio, and a private bathroom, kitchen, and kitchenette that you're free to use any time. Heating, a TV -- we've got everything you need.",
    address="320 E McCarty St",
    stateId=25
  )

  montanaBooking = Booking(
    title="Rare Townhouse w/ Heating + Private Bathroom",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Want to visit Helena without breaking the bank? We have exactly what you're looking for. Our rare townhouse comes with 1 bedroom, private bathroom, kitchen, kitchenette, heating, and a TV, and we're within walking distance to hikes, national parks, and beaches.",
    address="316 N Park Ave",
    stateId=26,
  )

  nebraksaBooking = Booking(
    title="Rustic Villa w/ a Coffee Maker + Private Bathroom",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Thinking about visiting Lincoln? I have a 2-bedroom villa that will be perfect for your stay. This rustic rental comes with amenities such as a coffee maker and a TV. Our private bathroom, kitchen, and kitchenette are yours to enjoy, as well. If you want to go to hikes, national parks, and beaches, we're within walking distance.",
    address="920 O St",
    stateId=27,
  )

  nevadaBooking = Booking(
    title="Spacious House w/ Wi-Fi + Living Room",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Hikes, national parks, and beaches in Carson City will make this a vacation to remember, and my spacious 3-bedroom house comes complete with living room and kitchenette. The Wi-Fi and a coffee maker will make you wish you could stay even longer. If you rent my Airbnb, I know you'll have a great stay in Carson City.",
    address="201 N Carson St",
    stateId=28
  )

  newHampshireBooking = Booking(
    title="Modern House w/ Wi-Fi + Living Room",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="My modern 4-bedroom house has everything you need for your Concord trip. The unit comes with Wi-Fi. During your stay, you can also enjoy using a convenient living room and kitchenette. Our Airbnb is within walking distance to several popular hikes, national parks, and beaches. An ideal base to explore Concord.",
    address='41 Green St',
    stateId=29
  )

  newJerseyBooking = Booking(
    title="Modern Bed and breakfast w/ Laptop-friendly Workspace + Indoor Fireplace",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Stay in this modern bed and breakfast and live like a true local in Trenton. We're within walking distance to hikes, national parks, and beaches. Our rental comes with 5 bedrooms, and a indoor fireplace, living room, and kitchenette that you're free to use any time. Laptop-friendly workspace, free coffee and tea -- we've got everything you need.",
    address='319 E State St',
    stateId=30,

  )

  newMexicoBooking = Booking(
    title="Glamorous House w/ AC + Indoor Fireplace",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Want to visit Sante Fe without breaking the bank? We have exactly what you're looking for. Our glamorous house comes with 6 bedrooms, indoor fireplace, kitchen, kitchenette, AC, and a TV, and we're within walking distance to hikes, national parks, and beaches.",
    address="200 Lincoln Ave",
    stateId=31,
  )

  newYorkBooking = Booking(
    title="Glamorous House w/ AC + Private Bathroom",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Thinking about visiting City Hall Park? I have a 7-bedroom house that will be perfect for your stay. This glamorous rental comes with amenities such as AC, self check-in, and a TV. Our private bathroom, kitchen, and kitchenette are yours to enjoy, as well. If you want to go to hikes, national parks, and beaches, we're within walking distance.",
    address="City Hall Park",
    stateId=32,
  )

  northCarolinaBooking = Booking(
    title="Peaceful House w/ AC + Private Bathroom",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Hikes, national parks, and beaches in Raleigh will make this a vacation to remember, and my peaceful 1-bedroom house comes complete with private bathroom, kitchen, and kitchenette. The AC, self check-in, and a TV will make you wish you could stay even longer. If you rent my Airbnb, I know you'll have a great stay in Raleigh.",
    address="222 W Hargett St",
    stateId=33,
  )

  northDakotaBooking = Booking(
    title='Secluded House w/ Roku TV + Indoor Fireplace',
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="My secluded 2-bedroom house has everything you need for your Bismarck trip. The unit comes with Roku TV, a TV, and a high chair. During your stay, you can also enjoy using a convenient indoor fireplace and kitchenette. Our Airbnb is within walking distance to several popular hikes, national parks, and beaches. An ideal base to explore Bismarck.",
    address="221 N 5th St",
    stateId=34,
  )

  ohioBooking = Booking(
    title="Charming House w/ Netflix + Hot Tub",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Stay in this charming house and live like a true local in Columbus. We're within walking distance to hikes, national parks, and beaches. Our rental comes with 3 bedrooms, and a hot tub, indoor fireplace, and kitchenette that you're free to use any time. Netflix, a TV, a high chair -- we've got everything you need.",
    address="90 W Broad St",
    stateId=35
  )

  oklahomaBooking = Booking(
    title="Comfortable House w/ a TV + Gym",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Want to visit Oklahoma City without breaking the bank? We have exactly what you're looking for. Our comfortable house comes with 4 bedrooms, gym, indoor fireplace, kitchenette, a TV, and a high chair, and we're within walking distance to hikes, national parks, and beaches.",
    address="200 N Walker Ave",
    stateId=36,
  )

  oregonBooking = Booking(
    title="Welcoming Apartment w/ Wi-Fi + Gym",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Thinking about visiting Salem? I have a 5-bedroom apartment that will be perfect for your stay. This welcoming rental comes with amenities such as Wi-Fi and a TV. Our gym, indoor fireplace, and kitchenette are yours to enjoy, as well. If you want to go to hikes, national parks, and beaches, we're within walking distance.",
    address="555 Liberty St SE",
    stateId=37,

  )

  pennsylvaniaBooking = Booking(
    title="Upscale House w/ Wi-Fi + Gym",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Shops, museums, and hikes in Harrisburg will make this a vacation to remember, and my upscale 5-bedroom house comes complete with gym, indoor fireplace, and kitchenette. The Wi-Fi and a TV will make you wish you could stay even longer. If you rent my Airbnb, I know you'll have a great stay in Philadelphia.",
    address="501 N 3rd St",
    stateId=38,

  )

  rhodeIslandBooking = Booking(
    title="Rare Villa w/ Wi-Fi + Private Bathroom",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Stay in this rare villa and live like a true local in Providence. We're within walking distance to shops, museums, and hikes. Our rental comes with 6 bedrooms, and a private bathroom, kitchen, and kitchenette that you're free to use any time. Wi-Fi, a TV, a hair dryer -- we've got everything you need.",
    address="25 Dorrance St",
    stateId=39
  )

  southCarolinaBooking = Booking(
    title="Glamorous Villa w/ Wi-Fi + Private Bathroom",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Thinking about visiting Columbia? I have a 7-bedroom villa that will be perfect for your stay. This glamorous rental comes with amenities such as Wi-Fi, a TV, and a hair dryer. Our private bathroom, kitchen, and kitchenette are yours to enjoy, as well. If you want to go to shops, museums, and hikes, we're within walking distance.",
    address="1737 Main St",
    stateId=40
  )

  southDakotaBooking = Booking(
    title="Historic Villa w/ a High Chair + Gym",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Shops, museums, and hikes in Pierre will make this a vacation to remember, and my historic 8-bedroom villa comes complete with gym and kitchenette. The a high chair, an iron, and a hair dryer will make you wish you could stay even longer. If you rent my Airbnb, I know you'll have a great stay in Pierre.",
    address="222 E Dakota Ave",
    stateId=41,
  )

  tennesseeBooking = Booking(
    title="Green Villa w/ Netflix + Hot Tub",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="My green 3-bedroom villa has everything you need for your Nashville trip. The unit comes with Netflix, Roku TV, and a hair dryer. During your stay, you can also enjoy using a convenient hot tub and kitchenette. Our Airbnb is within walking distance to several popular shops, museums, and hikes. An ideal base to explore Nashville.",
    address="1 Public Square",
    stateId=42,

  )

  texasBooking = Booking(
    title="Luxurious Villa w/ Wi-Fi + Hot Tub",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Want to visit Austin without breaking the bank? We have exactly what you're looking for. Our luxurious villa comes with 5 bedrooms, hot tub, kitchen, kitchenette, Wi-Fi, and a hair dryer, and we're within walking distance to shops, museums, and hikes.",
    address="301 W 2nd St",
    stateId=43,
  )

  utahBooking = Booking(
    title="Luxurious Villa w/ Wi-Fi + Hot Tub",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Thinking about visiting Salt Lake City? I have a 6-bedroom villa that will be perfect for your stay. This luxurious rental comes with amenities such as Wi-Fi and a hair dryer. Our hot tub, kitchen, and kitchenette are yours to enjoy, as well. If you want to go to shops, museums, and hikes, we're within walking distance.",
    address="451 S State St",
    stateId=44,
  )

  vermontBooking = Booking(
    title="Luxurious Villa w/ Breakfast + Kitchenette",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Shops, museums, and hikes in Montpelier will make this a vacation to remember, and my luxurious 7-bedroom villa comes complete with kitchenette. The breakfast and a hair dryer will make you wish you could stay even longer. If you rent my Airbnb, I know you'll have a great stay in Montpelier.",
    address="39 Main St",
    stateId=45,

  )

  virginiaBooking = Booking(
    title='Upscale Townhouse w/ AC + Private Bathroom',
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="My upscale 7-bedroom townhouse has everything you need for your Richmond trip. The unit comes with AC and a hair dryer. During your stay, you can also enjoy using a convenient private bathroom, indoor fireplace, and kitchenette. Our Airbnb is within walking distance to several popular shops, museums, and hikes. An ideal base to explore Richmond.",
    address="900 E Broad St",
    stateId=46,
  )

  washingtonBooking = Booking(
    title="Upscale Chalet w/ AC + Indoor Fireplace",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Stay in this upscale chalet and live like a true local in Olympia. We're within walking distance to shops, museums, and hikes. Our rental comes with 4 bedrooms, and a indoor fireplace, kitchen, and kitchenette that you're free to use any time. AC, a TV, a hair dryer -- we've got everything you need.",
    address="601 4th Ave E",
    stateId=47,
  )

  westVirginiaBooking = Booking(
    title="Rare Chalet w/ AC + Indoor Fireplace",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="My rare 5-bedroom chalet has everything you need for your Charleston trip. The unit comes with AC, a TV, and a hair dryer. During your stay, you can also enjoy using a convenient indoor fireplace, kitchen, and kitchenette. Our Airbnb is within walking distance to several popular shops, museums, and hikes. An ideal base to explore Charleston.",
    address="501 Virginia St. E",
    stateId=48
  )

  wisconsinBooking = Booking(
    title="Glamorous Chalet w/ AC + Indoor Fireplace",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Stay in this glamorous chalet and live like a true local in Madison. We're within walking distance to shops, museums, and hikes. Our rental comes with 7 bedrooms, and a indoor fireplace, kitchen, and kitchenette that you're free to use any time. AC, a TV, a hair dryer -- we've got everything you need.",
    address="2120 Fish Hatchery Road",
    stateId=49,

  )

  wyomingBooking = Booking(
    title="Glamorous Chalet w/ Self Check-in + Indoor Fireplace",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Want to visit Cheyenne without breaking the bank? We have exactly what you're looking for. Our glamorous chalet comes with 4 bedrooms, indoor fireplace, kitchen, kitchenette, self check-in, a TV, and a hair dryer, and we're within walking distance to shops, museums, and hikes.",
    address="2101 O Neil Ave",
    stateId=50
  )

  db.session.add(alabamaBooking)
  db.session.add(alaskaBooking)
  db.session.add(arizonaBooking)
  db.session.add(arkansasBooking)
  db.session.add(californiaBooking)
  db.session.add(coloradoBooking)
  db.session.add(connecticutBooking)
  db.session.add(delawareBooking)
  db.session.add(floridaBooking)
  db.session.add(georgiaBooking)
  db.session.add(hawaiiBooking)
  db.session.add(idahoBooking)
  db.session.add(illinoisBooking)
  db.session.add(indianaBooking)
  db.session.add(iowaBooking)
  db.session.add(kansasBooking)
  db.session.add(kentuckyBooking)
  db.session.add(louisianaBooking)
  db.session.add(maineBooking)
  db.session.add(marylandBooking)
  db.session.add(massachusettsBooking)
  db.session.add(michiganBooking)
  db.session.add(minnesotaBooking)
  db.session.add(mississippiBooking)
  db.session.add(missouriBooking)
  db.session.add(montanaBooking)
  db.session.add(nebraksaBooking)
  db.session.add(nevadaBooking)
  db.session.add(newHampshireBooking)
  db.session.add(newJerseyBooking)
  db.session.add(newMexicoBooking)
  db.session.add(newYorkBooking)
  db.session.add(northCarolinaBooking)
  db.session.add(northDakotaBooking)
  db.session.add(ohioBooking)
  db.session.add(oklahomaBooking)
  db.session.add(oregonBooking)
  db.session.add(pennsylvaniaBooking)
  db.session.add(rhodeIslandBooking)
  db.session.add(southCarolinaBooking)
  db.session.add(southDakotaBooking)
  db.session.add(tennesseeBooking)
  db.session.add(texasBooking)
  db.session.add(utahBooking)
  db.session.add(vermontBooking)
  db.session.add(virginiaBooking)
  db.session.add(washingtonBooking)
  db.session.add(westVirginiaBooking)
  db.session.add(wisconsinBooking)
  db.session.add(wyomingBooking)

  db.session.commit()


def undo_bookings():
  db.session.execute('TRUNCATE bookings;')
  db.session.commit()

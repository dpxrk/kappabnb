from app.models import db, Booking
import random


def seed_bookings():
  alabamaBooking = Booking(
    title='Modern House',
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description='My modern 3-bedroom house has everything you need for your Montgomery trip. The unit comes with Wi-Fi, Netflix, and a TV. An ideal base to explore Montgomery.',
    address='600 Dexter Ave',
    stateId=1,
    lat=32.37759554303203,
    lng=-86.29983130085529
  )

  alaskaBooking = Booking(
    title= 'Green House',
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Stay in this green house and live like a true local in Juneau. Our rental comes with 1 bedroom -- free coffee and tea, breakfast, a TV -- we've got everything you need.",
    address='120 4th St',
    stateId=2,
    lat=58.302170692253064,
    lng= -134.40959456769474
  )

  arizonaBooking = Booking(
    title= 'Charming Bungalow',
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Want to visit Sacramento without breaking the bank? We have exactly what you're looking for. Our charming bungalow comes with 4 bedrooms, hot tub, indoor fireplace, free coffee and tea, breakfast, and a TV.",
    address='1700 W Washington St',
    stateId=3,
    lat=33.448552956045965,
    lng=-112.09734044685861
  )

  arkansasBooking = Booking(
    title= "Charming Cabin",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Thinking about visiting Little Rock? I have a 3-bedroom cabin that will be perfect for your stay. This charming rental comes with amenities such as a dryer, a coffee maker, and a TV. Our private bathroom and living room are yours to enjoy, as well.",
    address="500 Woodlane St",
    stateId=4,
    lat=34.7471184617871,
    lng=-92.28853501799948
  )

  californiaBooking = Booking(
    title="Rare Villa ",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="My rare 5-bedroom villa in Sacramento comes complete with hot tub, indoor fireplace, and living room. The a dryer, free parking, and a coffee maker will make you wish you could stay even longer. If you rent my Airbnb, I know you'll have a great stay in Sacramento.",
    address="1315 10th St",
    stateId=5,
    lat=38.576705605078004,
    lng=-121.49255015656027
  )

  coloradoBooking = Booking(
    title="Glamorous Villa",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="My glamorous 8-bedroom villa has everything you need for your Denver trip. The unit comes with a washer, a coffee maker, and a high chair. During your stay, you can also enjoy using a convenient gym, indoor fireplace, and living room. Our Airbnb is within driving distance to several popular bars, hikes, and national parks. An ideal base to explore Denver.",
    address="200 E Colfax Ave",
    stateId=6,
    lat=39.739407579962204,
    lng=-104.98422754488732
  )

  connecticutBooking = Booking(
    title="Welcoming Cottage w/ AC + Gym",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Bars, hikes, and national parks in Hartford will make this a vacation to remember, and my welcoming 4-bedroom cottage comes complete with gym, indoor fireplace, and living room. The AC, laptop-friendly workspace, and a high chair will make you wish you could stay even longer. If you rent my Airbnb, I know you'll have a great stay in Hartford.",
    address="210 Capitol Ave",
    stateId=7,
    lat=41.76433392255175,
    lng=-72.68189837367765
  )

  delawareBooking = Booking(
    title='Historic Resort w/ Netflix + Gym',
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="My historic 2-bedroom resort has everything you need for your Dover trip. The unit comes with Netflix, free coffee and tea, and breakfast. During your stay, you can also enjoy using a convenient gym, indoor fireplace, and living room. Our Airbnb is within driving distance to several popular bars, hikes, and national parks. An ideal base to explore Dover.",
    address="411 Legislative Ave",
    stateId=8,
    lat=39.15741620760195,
    lng=-75.51891502771275
  )

  floridaBooking = Booking(
    title="Historic Chalet w/ a Washer + Gym",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Stay in this historic chalet and live like a true local in Tallahassee. We're within driving distance to bus routes, national parks, and night clubs. Our rental comes with 7 bedrooms, and a gym, private bathroom, and indoor fireplace that you're free to use any time. A washer, free coffee and tea, an iron -- we've got everything you need.",
    address="400 S Monroe St.",
    stateId=9,
    lat=30.43881248346581,
    lng=-84.28155934137122
  )

  georgiaBooking = Booking(
    title="Historic Loft w/ Roku TV + Private Bathroom",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Want to visit Atlanta without breaking the bank? We have exactly what you're looking for. Our historic loft comes with 3 bedrooms, private bathroom, kitchen, living room, Roku TV, free coffee and tea, and a hair dryer, and we're within driving distance to bus routes, national parks, and night clubs.",
    address="206 Washington St. SW",
    stateId=10,
    lat=33.74923911728103,
    lng=-84.387761973842
  )

  hawaiiBooking = Booking(
    title="Secluded Boutique hotel w/ a Dryer + Hot Tub",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Thinking about visiting Honolulu? I have a 6-bedroom boutique hotel that will be perfect for your stay. This secluded rental comes with amenities such as a dryer, Wi-Fi, and a bike. Our hot tub, private bathroom, and kitchen are yours to enjoy, as well. If you want to go to bus routes, national parks, and night clubs, we're within walking distance.",
    address="415 S Beretania St",
    stateId=11,
    lat=21.307722940255292,
    lng=-157.85641720101037
  )

  idahoBooking = Booking(
    title='Glamorous Cottage w/ a Dryer + Hot Tub',
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Shops, national parks, and night clubs in Boise will make this a vacation to remember, and my glamorous 6-bedroom cottage comes complete with hot tub, private bathroom, and kitchen. The a dryer, Wi-Fi, and a bike will make you wish you could stay even longer. If you rent my Airbnb, I know you'll have a great stay in Boise.",
    address="700 W Jefferson St.",
    stateId=12,
    lat=43.6179303200972,
    lng=-116.19917517917337
  )

  illinoisBooking = Booking(
    title='Rustic House w/ AC + Hot Tub',
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="My rustic 3-bedroom house has everything you need for your Springfield trip. The unit comes with AC, Wi-Fi, and a bike. During your stay, you can also enjoy using a convenient hot tub, kitchen, and living room. Our Airbnb is within walking distance to several popular hikes, national parks, and beaches. An ideal base to explore Springfield.",
    address="S Spring Street",
    stateId=12,
    lat=39.79862713869016,
    lng=-89.65476532954527
  )

  indianaBooking = Booking(
    title='Spacious Apartment w/ a Dryer + Living Room',
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Hikes, national parks, and beaches in Indianapolis will make this a vacation to remember, and my spacious 4-bedroom apartment comes complete with living room. The a dryer, Netflix, and free coffee and tea will make you wish you could stay even longer. If you rent my Airbnb, I know you'll have a great stay in Indianapolis.",
    address="200 W Washington St",
    stateId=14,
    lat=39.768916742565814,
    lng=-86.16235194673301
  )

  iowaBooking = Booking(
    title='Modern Bungalow w/ a Washer + Living Room',
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="My modern 5-bedroom bungalow has everything you need for your Des Moines trip. The unit comes with a washer, Wi-Fi, and breakfast. During your stay, you can also enjoy using a convenient living room. Our Airbnb is within walking distance to several popular hikes, national parks, and beaches. An ideal base to explore Des Moines",
    address="1007 E Grand Ave",
    stateId=15,
    lat=41.59127439607835,
    lng=-93.60322047737414
  )

  kansasBooking = Booking(
    title='Glamorous RV w/ Netflix + Living Room',
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Stay in this glamorous RV and live like a true local in Topeka. We're within walking distance to hikes, national parks, and beaches. Our rental comes with 6 bedrooms, and a living room that you're free to use any time. Netflix, free parking, an iron -- we've got everything you need.",
    address="SW 8th & SW Van Buren",
    stateId=16,
    lat=39.04827826235054,
    lng= -95.67717963751684
  )

  kentuckyBooking = Booking(
    title="Green Cabin w/ Hangers + Indoor Fireplace",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Want to visit Frankfort without breaking the bank? We have exactly what you're looking for. Our green cabin comes with 7 bedrooms, indoor fireplace, kitchen, living room, hangers, and a hair dryer, and we're within walking distance to hikes, national parks, and beaches.",
    address="700 Capital Ave",
    stateId=17,
    lat=38.18690457107311,
    lng=-84.87470711608503
  )

  louisianaBooking = Booking(
    title="Luxurious Chalet w/ AC + Indoor Fireplace",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Thinking about visiting Baton Rouge? I have a 8-bedroom chalet that will be perfect for your stay. This luxurious rental comes with amenities such as AC, laptop-friendly workspace, and a hair dryer. Our indoor fireplace, kitchen, and living room are yours to enjoy, as well. If you want to go to hikes, national parks, and beaches, we're within walking distance.",
    address="640 Capitol Access Road,
    stateId=18,
    lat=30.457340841899573,
    lng= -91.18648796466717
  )

  maineBooking = Booking(
    title= "Peaceful Cottage w/ a Bike + Gym",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="My peaceful 9-bedroom cottage has everything you need for your Augusta trip. The unit comes with a bike, a high chair, and a hair dryer. During your stay, you can also enjoy using a convenient gym, private bathroom, and living room. Our Airbnb is within walking distance to several popular hikes, national parks, and beaches. An ideal base to explore Augusta.",
    address="Maine State House",
    stateId=19,
    lat=44.307265910374355,
    lng= -69.78084014904574
  )

  marylandBooking = Booking(
    title="Secluded Cottage w/ a Bike + Gym",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Stay in this secluded cottage and live like a true local in Annapolis. We're within walking distance to hikes, national parks, and beaches. Our rental comes with 1 bedroom, and a gym, private bathroom, and living room that you're free to use any time. A bike, a high chair, a hair dryer -- we've got everything you need.",
    address='100 State Circle',
    stateId=20,
    lat=38.97903428479546,
    lng=-76.49036319888131
  )

  massachusettsBooking = Booking(
    title="Charming Guest suite w/ Wi-Fi + Gym",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Want to visit Boston without breaking the bank? We have exactly what you're looking for. Our charming guest suite comes with 2 bedrooms, gym, private bathroom, living room, Wi-Fi, Netflix, and a hair dryer, and we're within walking distance to hikes, national parks, and beaches.",
    address="24 Beacon St",
    stateId=21,
    lat=42.35894366632064,
    lng=-71.06313418531208
  )

  michiganBooking = Booking(
    title="Comfortable Guesthouse w/ Wi-Fi + Gym",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Thinking about visiting Lansing? I have a 3-bedroom guesthouse that will be perfect for your stay. This comfortable rental comes with amenities such as Wi-Fi, Netflix, and a hair dryer. Our gym, private bathroom, and living room are yours to enjoy, as well. If you want to go to hikes, national parks, and beaches, we're within walking distance.",
    address='100 N Capitol Ave',
    stateId=22,
    lat=42.73367466218707,
    lng=-84.55479358714975
  )

  minnesotaBooking = Booking(
    title='Welcoming Hostel w/ Free Parking + Kitchen',
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Hikes, national parks, and beaches in St. Paul will make this a vacation to remember, and my welcoming 4-bedroom hostel comes complete with kitchen and kitchenette. The free parking and a high chair will make you wish you could stay even longer. If you rent my Airbnb, I know you'll have a great stay in St. Paul.",
    address="75 Rev Dr. Martin Luther King Jr. Boulevard",
    stateId=23,
    lat=44.955317010971015,
    lng=-93.10137469505223

  )

  mississippiBooking = Booking(
    title='Upscale Hotel w/ Heating + Kitchen',
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="My upscale 5-bedroom hotel has everything you need for your Jackson trip. The unit comes with heating and a TV. During your stay, you can also enjoy using a convenient kitchen and kitchenette. Our Airbnb is within walking distance to several popular hikes, national parks, and beaches. An ideal base to explore Jackson.",
    address="400 High St",
    stateId=24,
    lat=32.303953373715466,
    lng= -90.18102750511939
  )

  missouriBooking = Booking(
    title="Upscale Loft w/ Heating + Private Bathroom",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Stay in this upscale loft and live like a true local in Jefferson City. We're within walking distance to hikes, national parks, and beaches. Our rental comes with studio, and a private bathroom, kitchen, and kitchenette that you're free to use any time. Heating, a TV -- we've got everything you need.",
    address="201 W Capitol Ave",
    stateId=25,
    lat= 38.57933681354461,
    lng=-92.17235735840643
  )

  montanaBooking = Booking(
    title="Rare Townhouse w/ Heating + Private Bathroom",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Want to visit Helena without breaking the bank? We have exactly what you're looking for. Our rare townhouse comes with 1 bedroom, private bathroom, kitchen, kitchenette, heating, and a TV, and we're within walking distance to hikes, national parks, and beaches.",
    address="1301 E 6th Ave",
    stateId=26,
    lat=46.58570723036694,
    lng=-112.01678344898947
  )

  nebraksaBooking = Booking(
    title="Rustic Villa w/ a Coffee Maker + Private Bathroom",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Thinking about visiting Lincoln? I have a 2-bedroom villa that will be perfect for your stay. This rustic rental comes with amenities such as a coffee maker and a TV. Our private bathroom, kitchen, and kitchenette are yours to enjoy, as well. If you want to go to hikes, national parks, and beaches, we're within walking distance.",
    address="1445 K St",
    stateId=27,
    lat=40.80818366886233,
    lng=-96.69899751233606
  )

  nevadaBooking = Booking(
    title="Spacious House w/ Wi-Fi + Living Room",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Hikes, national parks, and beaches in Carson City will make this a vacation to remember, and my spacious 3-bedroom house comes complete with living room and kitchenette. The Wi-Fi and a coffee maker will make you wish you could stay even longer. If you rent my Airbnb, I know you'll have a great stay in Carson City.",
    address="101 N Carson St",
    stateId=28,
    lat=39.16396010179522,
    lng=-119.76536459887747
  )

  newHampshireBooking = Booking(
    title="Modern House w/ Wi-Fi + Living Room",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="My modern 4-bedroom house has everything you need for your Concord trip. The unit comes with Wi-Fi. During your stay, you can also enjoy using a convenient living room and kitchenette. Our Airbnb is within walking distance to several popular hikes, national parks, and beaches. An ideal base to explore Concord.",
    address='107 N Main St.',
    stateId=29,
    lat=43.20703866039465,
    lng=-71.53749425830343
  )

  newJerseyBooking = Booking(
    title="Modern Bed and breakfast w/ Laptop-friendly Workspace + Indoor Fireplace",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Stay in this modern bed and breakfast and live like a true local in Trenton. We're within walking distance to hikes, national parks, and beaches. Our rental comes with 5 bedrooms, and a indoor fireplace, living room, and kitchenette that you're free to use any time. Laptop-friendly workspace, free coffee and tea -- we've got everything you need.",
    address='125 W State St',
    stateId=30,
    lat=40.220754808630375,
    lng=-74.76950134856943

  )

  newMexicoBooking = Booking(
    title="Glamorous House w/ AC + Indoor Fireplace",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Want to visit Sante Fe without breaking the bank? We have exactly what you're looking for. Our glamorous house comes with 6 bedrooms, indoor fireplace, kitchen, kitchenette, AC, and a TV, and we're within walking distance to hikes, national parks, and beaches.",
    address="490 Old Sante Fe Trail",
    stateId=31,
    lat=35.68232286126534,
    lng=-105.93936420751096
  )

  newYorkBooking = Booking(
    title="Glamorous House w/ AC + Private Bathroom",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Thinking about visiting City Hall Park? I have a 7-bedroom house that will be perfect for your stay. This glamorous rental comes with amenities such as AC, self check-in, and a TV. Our private bathroom, kitchen, and kitchenette are yours to enjoy, as well. If you want to go to hikes, national parks, and beaches, we're within walking distance.",
    address="State St. an, Washington Ave",
    stateId=32,
    lat=42.65287455913259,
    lng=-73.75631612209592
  )

  northCarolinaBooking = Booking(
    title="Peaceful House w/ AC + Private Bathroom",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Hikes, national parks, and beaches in Raleigh will make this a vacation to remember, and my peaceful 1-bedroom house comes complete with private bathroom, kitchen, and kitchenette. The AC, self check-in, and a TV will make you wish you could stay even longer. If you rent my Airbnb, I know you'll have a great stay in Raleigh.",
    address="1 E Edeonton St",
    stateId=33,
    lat=35.78037578801615,
    lng=-78.6387321351668
  )

  northDakotaBooking = Booking(
    title='Secluded House w/ Roku TV + Indoor Fireplace',
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="My secluded 2-bedroom house has everything you need for your Bismarck trip. The unit comes with Roku TV, a TV, and a high chair. During your stay, you can also enjoy using a convenient indoor fireplace and kitchenette. Our Airbnb is within walking distance to several popular hikes, national parks, and beaches. An ideal base to explore Bismarck.",
    address="600 E Boulevard Ave",
    stateId=34,
    lat=46.82102069442997,
    lng=-100.78127482327072
  )

  ohioBooking = Booking(
    title="Charming House w/ Netflix + Hot Tub",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Stay in this charming house and live like a true local in Columbus. We're within walking distance to hikes, national parks, and beaches. Our rental comes with 3 bedrooms, and a hot tub, indoor fireplace, and kitchenette that you're free to use any time. Netflix, a TV, a high chair -- we've got everything you need.",
    address="1 Capitol Square",
    stateId=35,
    lat=39.96158404100039,
    lng=-82.99823186633239
  )

  oklahomaBooking = Booking(
    title="Comfortable House w/ a TV + Gym",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Want to visit Oklahoma City without breaking the bank? We have exactly what you're looking for. Our comfortable house comes with 4 bedrooms, gym, indoor fireplace, kitchenette, a TV, and a high chair, and we're within walking distance to hikes, national parks, and beaches.",
    address="2300 N Lincoln Blvd",
    stateId=36,
    lat=35.49243062855047,
    lng=-97.5022484204018
  )

  oregonBooking = Booking(
    title="Welcoming Apartment w/ Wi-Fi + Gym",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Thinking about visiting Salem? I have a 5-bedroom apartment that will be perfect for your stay. This welcoming rental comes with amenities such as Wi-Fi and a TV. Our gym, indoor fireplace, and kitchenette are yours to enjoy, as well. If you want to go to hikes, national parks, and beaches, we're within walking distance.",
    address="900 Court St NE",
    stateId=37,
    lat=44.93860207045837,
    lng=-123.0302163870971

  )

  pennsylvaniaBooking = Booking(
    title="Upscale House w/ Wi-Fi + Gym",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Shops, museums, and hikes in Harrisburg will make this a vacation to remember, and my upscale 5-bedroom house comes complete with gym, indoor fireplace, and kitchenette. The Wi-Fi and a TV will make you wish you could stay even longer. If you rent my Airbnb, I know you'll have a great stay in Philadelphia.",
    address="501 N 3rd St",
    stateId=38,
    lat=40.264328213709184,
    lng=-76.8834222602166
  )

  rhodeIslandBooking = Booking(
    title="Rare Villa w/ Wi-Fi + Private Bathroom",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Stay in this rare villa and live like a true local in Providence. We're within walking distance to shops, museums, and hikes. Our rental comes with 6 bedrooms, and a private bathroom, kitchen, and kitchenette that you're free to use any time. Wi-Fi, a TV, a hair dryer -- we've got everything you need.",
    address="82 Smith St.",
    stateId=39,
    lat=41.83090378499833,
    lng=-71.41544078816148
  )

  southCarolinaBooking = Booking(
    title="Glamorous Villa w/ Wi-Fi + Private Bathroom",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Thinking about visiting Columbia? I have a 7-bedroom villa that will be perfect for your stay. This glamorous rental comes with amenities such as Wi-Fi, a TV, and a hair dryer. Our private bathroom, kitchen, and kitchenette are yours to enjoy, as well. If you want to go to shops, museums, and hikes, we're within walking distance.",
    address="1737 Main St",
    stateId=40,
    lat=34.000521161025425,
    lng=-81.03249352966147
  )

  southDakotaBooking = Booking(
    title="Historic Villa w/ a High Chair + Gym",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Shops, museums, and hikes in Pierre will make this a vacation to remember, and my historic 8-bedroom villa comes complete with gym and kitchenette. The a high chair, an iron, and a hair dryer will make you wish you could stay even longer. If you rent my Airbnb, I know you'll have a great stay in Pierre.",
    address="500 E Capitol Ave",
    stateId=41,
    lat=44.367270964947444,
    lng=-100.34586434662774

  )

  tennesseeBooking = Booking(
    title="Green Villa w/ Netflix + Hot Tub",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="My green 3-bedroom villa has everything you need for your Nashville trip. The unit comes with Netflix, Roku TV, and a hair dryer. During your stay, you can also enjoy using a convenient hot tub and kitchenette. Our Airbnb is within walking distance to several popular shops, museums, and hikes. An ideal base to explore Nashville.",
    address="600 Dr. M.L.K Jr. Blvd",
    stateId=42,
    lat=36.166023679430815,
    lng=-86.78345502592771

  )

  texasBooking = Booking(
    title="Luxurious Villa w/ Wi-Fi + Hot Tub",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Want to visit Austin without breaking the bank? We have exactly what you're looking for. Our luxurious villa comes with 5 bedrooms, hot tub, kitchen, kitchenette, Wi-Fi, and a hair dryer, and we're within walking distance to shops, museums, and hikes.",
    address="1100 Congress Ave",
    stateId=43,
    lat=30.27468371304496,
    lng=-97.73997499293507
  )

  utahBooking = Booking(
    title="Luxurious Villa w/ Wi-Fi + Hot Tub",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Thinking about visiting Salt Lake City? I have a 6-bedroom villa that will be perfect for your stay. This luxurious rental comes with amenities such as Wi-Fi and a hair dryer. Our hot tub, kitchen, and kitchenette are yours to enjoy, as well. If you want to go to shops, museums, and hikes, we're within walking distance.",
    address="350 State St",
    stateId=44,
    lat=40.77749694810096,
    lng=-111.88743701233685
  )

  vermontBooking = Booking(
    title="Luxurious Villa w/ Breakfast + Kitchenette",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Shops, museums, and hikes in Montpelier will make this a vacation to remember, and my luxurious 7-bedroom villa comes complete with kitchenette. The breakfast and a hair dryer will make you wish you could stay even longer. If you rent my Airbnb, I know you'll have a great stay in Montpelier.",
    address="115 State St",
    stateId=45,
    lat=44.26274829803464,
    lng=-72.57976575458572

  )

  virginiaBooking = Booking(
    title='Upscale Townhouse w/ AC + Private Bathroom',
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="My upscale 7-bedroom townhouse has everything you need for your Richmond trip. The unit comes with AC and a hair dryer. During your stay, you can also enjoy using a convenient private bathroom, indoor fireplace, and kitchenette. Our Airbnb is within walking distance to several popular shops, museums, and hikes. An ideal base to explore Richmond.",
    address="100 Bank St",
    stateId=46,
    lat=37.53899894086567,
    lng=-77.4326936798779
  )

  washingtonBooking = Booking(
    title="Upscale Chalet w/ AC + Indoor Fireplace",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Stay in this upscale chalet and live like a true local in Olympia. We're within walking distance to shops, museums, and hikes. Our rental comes with 4 bedrooms, and a indoor fireplace, kitchen, and kitchenette that you're free to use any time. AC, a TV, a hair dryer -- we've got everything you need.",
    address="First St SE",
    stateId=47,
    lat=38.89021069888154,
    lng=-77.00945255287183
  )

  westVirginiaBooking = Booking(
    title="Rare Chalet w/ AC + Indoor Fireplace",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="My rare 5-bedroom chalet has everything you need for your Charleston trip. The unit comes with AC, a TV, and a hair dryer. During your stay, you can also enjoy using a convenient indoor fireplace, kitchen, and kitchenette. Our Airbnb is within walking distance to several popular shops, museums, and hikes. An ideal base to explore Charleston.",
    address="1900 Kanawha Blvd E",
    stateId=48,
    lat=38.336584998230556,
    lng=-81.61165164676336
  )

  wisconsinBooking = Booking(
    title="Glamorous Chalet w/ AC + Indoor Fireplace",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Stay in this glamorous chalet and live like a true local in Madison. We're within walking distance to shops, museums, and hikes. Our rental comes with 7 bedrooms, and a indoor fireplace, kitchen, and kitchenette that you're free to use any time. AC, a TV, a hair dryer -- we've got everything you need.",
    address="2 E Main St",
    stateId=49,
    lat=43.07492690442282,
    lng=-89.38335465646024

  )

  wyomingBooking = Booking(
    title="Glamorous Chalet w/ Self Check-in + Indoor Fireplace",
    userId=(random.randrange(1,12)),
    price=(random.randrange(50,200)),
    description="Want to visit Cheyenne without breaking the bank? We have exactly what you're looking for. Our glamorous chalet comes with 4 bedrooms, indoor fireplace, kitchen, kitchenette, self check-in, a TV, and a hair dryer, and we're within walking distance to shops, museums, and hikes.",
    address="200 W 24th St",
    stateId=50,
    lat=41.140480556323666,
    lng=-104.81954591048232
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

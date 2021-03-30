from app.models import db, Picture


def seed_pictures():
  alabamaPhotoList=['https://upload.wikimedia.org/wikipedia/commons/1/1b/Montgomery_City_Hall_Feb_2012_02.jpg',
                    'https://exploringmontgomery.com/wp-content/uploads/sites/11/2015/10/mont-city-auditorium-inside.jpg',
                    'https://www.wsfa.com/resizer/Xy2PER0c6QXehiDE6CieKqbwp6U=/1400x0/arc-anglerfish-arc2-prod-raycom.s3.amazonaws.com/public/ACWHPGV4XBDPPCPQZENQCM5OOA.jpg',
                    'https://livingnewdeal.org/wp-content/uploads/2011/12/IMG_0820.jpg]

  alaksaPhotoList=[]

  count = 0
  while count < 4
  alabamaPictures = Picture(
    bookingId=1,
    photoUrl=alabamaPhotoList[count]
  )

  alaskaPictures = Picture(
    bookingId=2,
    photoURL=
  )

  count +=1
  db.session.add(alabamaPictures)
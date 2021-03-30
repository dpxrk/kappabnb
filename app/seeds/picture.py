from app.models import db, Picture


def seed_pictures():

  alabamaPhotoList=['https://upload.wikimedia.org/wikipedia/commons/1/1b/Montgomery_City_Hall_Feb_2012_02.jpg',
                    'https://exploringmontgomery.com/wp-content/uploads/sites/11/2015/10/mont-city-auditorium-inside.jpg',
                    'https://www.wsfa.com/resizer/Xy2PER0c6QXehiDE6CieKqbwp6U=/1400x0/arc-anglerfish-arc2-prod-raycom.s3.amazonaws.com/public/ACWHPGV4XBDPPCPQZENQCM5OOA.jpg',
                    'https://livingnewdeal.org/wp-content/uploads/2011/12/IMG_0820.jpg
                    ]

  alaksaPhotoList=['https://media.ktoo.org/2019/05/DowtownParkingGarage-830x552.jpg',
  'https://chstm2y9cx63tv84u2p8shc3-wpengine.netdna-ssl.com/wp-content/uploads/2019/06/City-Hall.jpg',
  'https://assets.simpleviewinc.com/simpleview/image/upload/c_fill,h_600,q_75,w_1200/v1/clients/juneau/TJJO_Downtown_Juneau_4_2015_868ae45f-1b73-4c52-9c4f-dbea12170952.jpg',
  'https://mm.aiircdn.com/258/5cff08bd4c1cd.jpg']

  arizonaPhotoList=['https://assets.simpleviewinc.com/simpleview/image/upload/crm/phoenix/828_9453_cityhall2_b9e0c6d3-5056-b3a8-493bce49239ab605.jpg',
  'https://arizonadailyindependent.com/wp-content/uploads/2019/04/phoenix-678x381.jpg',
  'https://i.pinimg.com/originals/c8/a6/bc/c8a6bcc9fe92783ebe817df814357659.jpg',
  'https://previews.123rf.com/images/melastmohican/melastmohican1702/melastmohican170200329/72822704-phoenix-city-hall-is-the-city-hall-for-the-city-of-phoenix-arizona-united-states-.jpg']

  arkansasPhotoList=['https://i.pinimg.com/originals/c5/d7/a2/c5d7a2346b36d367c977dc99e30c019c.jpg',
  'https://mediad.publicbroadcasting.net/p/kuar/files/styles/x_large/public/201611/2016-11-09-Robinson01-8920.jpg',
  'https://pbs.twimg.com/media/D43Q3_SX4AAqERu.jpg',
  'https://www.gpsmycity.com/img/gd_attr/45898.jpg']

  californiaPhotoList=['https://thumbs.dreamstime.com/b/sacramento-feb-interior-view-beautiful-city-hall-california-112164298.jpg','https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/South_and_east_elevations%2C_photographed_from_slightly_more_western_position_-_Sacramento_City_Hall%2C_915_I_Street%2C_Sacramento%2C_Sacramento_County%2C_CA_HABS_CAL%2C34-SAC%2C48-2.tif/lossy-page1-1200px-thumbnail.tif.jpg',
  'https://previews.123rf.com/images/kitleong/kitleong1803/kitleong180300311/97537067-exterior-view-of-the-sacramento-city-hall-at-sacramento-california.jpg', 'https://www.nationsonline.org/gallery/USA/Sacramento-Skyline.jpg']

  coloradoPhotolist=['https://media-cdn.tripadvisor.com/media/photo-s/01/3c/7f/f9/denver-city-hall.jpg','https://www.goodfreephotos.com/albums/united-states/colorado/denver/city-hall-of-denver-colorado-and-garden.jpg', 'https://photos.smugmug.com/Colorado/Denver/i-gxz2sqQ/0/c802cc10/L/Colorado-City-Hall-Christmas-6585-L.jpg',
  'http://www.historic-structures.com/co/denver/images/021155pv.jpg']

  connecticutPhotoList=['https://i.pinimg.com/originals/86/50/70/865070ee9c39ba407f226977d72505dd.jpg','https://images2.minutemediacdn.com/image/upload/c_fill,g_auto,h_1248,w_2220/v1555351386/shape/mentalfloss/istock_000058757164_small.jpg', 'https://s3-media3.fl.yelpcdn.com/bphoto/Fk6hxM84W4dQB6XnPJcxhA/348s.jpg','https://www.wnpr.org/sites/wnpr/files/201309/cityhall.JPG']

  delawarePhotoList=['https://3iqhm91wtiv21y4zza4dqwj2-wpengine.netdna-ssl.com/wp-content/uploads/Delaware-Dover-Delaware-State-Capitol-Legislative-Hall-1440x943.jpg','https://wpcdn.us-east-1.vip.tn-cloud.net/www.wmdt.com/content/uploads/2020/05/Delaware-Legislative-Hall-Dover.png','https://www.nationsonline.org/gallery/USA/Delaware-Legislative-Hall-in-Dover.jpg','https://previews.123rf.com/images/pabrady63/pabrady631804/pabrady63180400058/100430117-delaware-state-capitol-building-in-dover-delaware.jpg']

  floridaPhotoList=['https://www.floridamemory.com/fpc/commerce/K024496.jpg', 'https://i.pinimg.com/originals/04/1c/39/041c390afb96f7f498ee8feac894e382.jpg', 'https://c8.alamy.com/comp/R5FFCK/usa-florida-tallahassee-historic-1902-state-capitol-state-house-of-representatives-chamber-R5FFCK.jpg','https://www.floridamemory.com/fpc/political/pt05036.jpg']

  georgiaPhotoList=['https://www.nps.gov/nr/travel/atlanta/buildings/cit1.jpg', 'https://thumbs.dreamstime.com/z/architectural-details-city-hall-atlanta-georgia-147089328.jpg','https://cdn2.atlantamagazine.com/wp-content/uploads/sites/4/2015/10/1015_hallpower07_afremiotti_oneuseonly.jpg','https://cdn.vox-cdn.com/thumbor/tT56FtUCV_nx9igzBFfL3eCOdno=/0x0:3600x2405/1400x1400/filters:focal(1445x546:2021x1122):format(jpeg)/cdn.vox-cdn.com/uploads/chorus_image/image/54559735/006Milton.0.jpg']

  hawaiiPhotoList=[]
  idahoPhotoList=[]
  illinoisPhotoList=[]
  indianaPhotoList=[]
  iowaPhotoList=[]
  kansasPhotoList=[]
  kentuckyPhotoList=[]
  louisianaPhotoList=[]
  mainePhotoList=[]
  marylandPhotoList=[]
  massachusettsPhotoList=[]
  michiganPhotoList=[]
  minnesotaPhotoList=[]
  mississippiPhotoList=[]
  missouriPhotoList=[]
  montanaPhotoList=[]
  nebraskaPhotoList=[]
  nevadaPhotoList=[]
  newhampshirePhotoList=[]
  newjerseyPhotoList=[]
  newmexicoPhotoList=[]
  newyorkPhotoList=[]
  northcarolinaPhotoList=[]
  northdakotaPhotoList=[]
  ohioPhotoList=[]
  oklahomaPhotoList=[]
  oregonPhotoList=[]
  pennsylvaniaPhotoList=[]
  rhodeislandPhotoList=[]
  southcarolinaPhotoList=[]
  southdakotaPhotoList=[]
  tennesseePhotoList=[]
  texasPhotoList=[]
  utahPhotoList=[]
  vermontPhotoList=[]
  virginiaPhotoList=[]
  washingtonPhotoList=[]
  westvirginiaPhotoList=[]
  wisconsinPhotoList=[]
  wyomingPhotoList=[]

  count = 0
  while count < 4
    alabama = Picture(
      bookingId=1,
      photoURL=alabamaPhotoList[count]
    )

    alaska = Picture(
      bookingId=2,
      photoURL=alaskaPhotoList[count]
    )

    arizona = Picture(
      bookingId=3,
      photoURL=arizonaPhotoList[count]
    )

    arkansas = Picture(
      bookingId=4,
      photoURL=arkansasPhotoList[count]
    )

    california= Picture(
      bookingId=5,
      photoURL=californiaPhotoList[count]
    )

    colorado = Picture(
      bookingId=6,
      photoURL=coloradoPhotolist[count]
    )

    connecticut = Picture(
      bookingId=7,
      photoURL=connecticutPhotoList[count]
    )

    delaware = Picture(
      bookingId=8,
      photoURL=delawarePhotoList[count]
    )

    florida = Picture( bookingId=9, photoURL=floridaPhotoList[count])
    georgia = Picture( bookingId=10, photoURL=georgiaPhotoList[count])
    hawaii = Picture( bookingId=11, photoURL=hawaiiPhotoList[count])
    idaho = Picture( bookingId=12, photoURL=idahoPhotoList[count])
    illinois = Picture( bookingId=13, photoURL=illinoisPhotoList[count])
    indiana = Picture( bookingId=14, photoURL=indianaPhotoList[count])
    iowa = Picture( bookingId=15, photoURL=iowaPhotoList[count])
    kansas = Picture( bookingId=16, photoURL=kansasPhotoList[count])
    kentucky = Picture( bookingId=17, photoURL=kentuckyPhotoList[count])
    louisiana = Picture( bookingId=18, photoURL=louisianaPhotoList[count])
    maine = Picture( bookingId=19, photoURL=mainePhotoList[count])
    maryland = Picture( bookingId=20, photoURL=marylandPhotoList[count])
    massachusetts = Picture( bookingId=21, photoURL=massachusettsPhotoList[count])
    michigan = Picture( bookingId=22, photoURL=michiganPhotoList[count])
    minnesota = Picture( bookingId=23, photoURL=minnesotaPhotoList[count])
    mississippi = Picture( bookingId=24, photoURL=mississippiPhotoList[count])
    missouri = Picture( bookingId=25, photoURL=missouriPhotoList[count])
    montana = Picture( bookingId=26, photoURL=montanaPhotoList[count])
    nebraska = Picture( bookingId=27, photoURL=nebraskaPhotoList[count])
    nevada = Picture( bookingId=28, photoURL=nevadaPhotoList[count])
    newhampshire = Picture( bookingId=29, photoURL=new hampshirePhotoList[count])
    newjersey = Picture( bookingId=30, photoURL=new jerseyPhotoList[count])
    newmexico = Picture( bookingId=31, photoURL=new mexicoPhotoList[count])
    newyork = Picture( bookingId=32, photoURL=new yorkPhotoList[count])
    northcarolina = Picture( bookingId=33, photoURL=north carolinaPhotoList[count])
    northdakota = Picture( bookingId=34, photoURL=north dakotaPhotoList[count])
    ohio = Picture( bookingId=35, photoURL=ohioPhotoList[count])
    oklahoma = Picture( bookingId=36, photoURL=oklahomaPhotoList[count])
    oregon = Picture( bookingId=37, photoURL=oregonPhotoList[count])
    pennsylvania = Picture( bookingId=38, photoURL=pennsylvaniaPhotoList[count])
    rhodeisland = Picture( bookingId=39, photoURL=rhode islandPhotoList[count])
    southcarolina = Picture( bookingId=40, photoURL=south carolinaPhotoList[count])
    southdakota = Picture( bookingId=41, photoURL=south dakotaPhotoList[count])
    tennessee = Picture( bookingId=42, photoURL=tennesseePhotoList[count])
    texas = Picture( bookingId=43, photoURL=texasPhotoList[count])
    utah = Picture( bookingId=44, photoURL=utahPhotoList[count])
    vermont = Picture( bookingId=45, photoURL=vermontPhotoList[count])
    virginia = Picture( bookingId=46, photoURL=virginiaPhotoList[count])
    washington = Picture( bookingId=47, photoURL=washingtonPhotoList[count])
    westvirginia = Picture( bookingId=48, photoURL=west virginiaPhotoList[count])
    wisconsin = Picture( bookingId=49, photoURL=wisconsinPhotoList[count])
    wyoming = Picture( bookingId=50, photoURL=wyomingPhotoList[count])

    count +=1
    db.session.add(alabama)
    db.session.add(alaska)
    db.session.add(arizona)
    db.session.add(arkansas)
    db.session.add(california)
    db.session.add(colorado)
    db.session.add(connecticut)
    db.session.add(delaware)
    db.session.add(florida)
    db.session.add(georgia)
    db.session.add(hawaii)
    db.session.add(idaho)
    db.session.add(illinois)
    db.session.add(indiana)
    db.session.add(iowa)
    db.session.add(kansas)
    db.session.add(kentucky)
    db.session.add(louisiana)
    db.session.add(maine)
    db.session.add(maryland)
    db.session.add(massachusetts)
    db.session.add(michigan)
    db.session.add(minnesota)
    db.session.add(mississippi)
    db.session.add(missouri)
    db.session.add(montana)
    db.session.add(nebraska)
    db.session.add(nevada)
    db.session.add(newhampshire)
    db.session.add(newjersey)
    db.session.add(newmexico)
    db.session.add(newyork)
    db.session.add(northcarolina)
    db.session.add(northdakota)
    db.session.add(ohio)
    db.session.add(oklahoma)
    db.session.add(oregon)
    db.session.add(pennsylvania)
    db.session.add(rhodeisland)
    db.session.add(southcarolina)
    db.session.add(southdakota)
    db.session.add(tennessee)
    db.session.add(texas)
    db.session.add(utah)
    db.session.add(vermont)
    db.session.add(virginia)
    db.session.add(washington)
    db.session.add(westvirginia)
    db.session.add(wisconsin)
    db.session.add(wyoming)




  db.session.commit()
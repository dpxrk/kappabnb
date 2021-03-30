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

  hawaiiPhotoList=['https://img2.10bestmedia.com/Images/Photos/332953/p-5932957300-dba9bb7f35-o_54_990x660.jpg', 'https://i.pinimg.com/originals/c2/7c/35/c27c3518bbb8319eb0e11109bd77b8f8.jpg','http://www.honolulu.gov/rep/site/ccl/ccl_imgs/honolulu-hale.jpg', 'https://upload.wikimedia.org/wikipedia/commons/7/7e/Honolulu-Hale-widefront.JPG']

  idahoPhotoList=['https://pbs.twimg.com/media/DeSu8V_V4AA2KFB.jpg', 'https://media.ktvb.com/assets/KTVB/images/7eb74054-976c-48c1-9604-1fb97aafe8cf/7eb74054-976c-48c1-9604-1fb97aafe8cf_750x422.jpg', 'https://i.pinimg.com/736x/12/b5/b9/12b5b9cc99c4fb2b65b2c8b860ea30b9--idaho-usa-boise-idaho.jpg', 'https://www.troutarchitects.com/app/uploads/2015/09/CityHall-3.jpg']
  illinoisPhotoList=['https://www.evanlloydarchitects.com/images/projects/IL-state-capitol-government-historic-architecture-1-house.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Springfield_Municipal_Group_2012_12_24.JPG/1200px-Springfield_Municipal_Group_2012_12_24.JPG', 'https://www.uis.edu/studentunion/wp-content/uploads/sites/103/2019/10/Union_Lounge_500x348.jpg', 'https://rdgusa.com/img/gallery/2014_05_22_091402_23327700/original.jpg' ]
  indianaPhotoList=['https://upload.wikimedia.org/wikipedia/commons/4/49/Old_Indianapolis_City_Hall_in_color.jpg','https://cdn.britannica.com/78/76678-050-B44743D1/Downtown-Indianapolis-Indiana.jpg', 'https://historicindianapolis.com/wp-content/uploads/2012/08/oldcityhall-033-610x816.jpg', 'https://upload.wikimedia.org/wikipedia/commons/f/fe/StateCapitolIndiana.jpg' ]
  iowaPhotoList=['https://upload.wikimedia.org/wikipedia/commons/e/e0/Des_Moines_City_Hall.jpg', 'https://holaamericanews.com/wp-content/uploads/2020/09/DSM-City-Hall.jpg', 'https://rdgusa.com/img/gallery/2014_09_03_071304_75570600/original.jpg', 'https://rdgusa.com/img/gallery/2014_08_29_103738_10532000/original.jpg' ]
  kansasPhotoList=["https://media.cntraveler.com/photos/53e2d8a3c2d3f39d36104ee0/master/w_1600%2Cc_limit/kansas-state-capitol-building.jpg", "https://c8.alamy.com/comp/F4KNT4/inside-the-kansas-state-capitol-topeka-kansas-usa-F4KNT4.jpg", "https://c8.alamy.com/comp/DTX2JP/usa-kansas-topeka-kansas-state-capital-interior-DTX2JP.jpg", "https://www.kansas.com/news/politics-government/bu3rwc/picture226242510/alternates/FREE_768/topeka%20capitol%20interior%20web.jpg" ]
  kentuckyPhotoList=["https://media.cntraveler.com/photos/53e2d8a6c2d3f39d36104ef2/master/w_1600%2Cc_limit/kentucky-state-capitol-building.jpg", 'https://i.pinimg.com/originals/b6/54/01/b654015fcc0267a88484061fc07e61c8.jpg', "https://capitol.ky.gov/Capitol%20Photos/capitol_tulips.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/U.S._Route_60_Frankfort%2C_KY_%2823892062134%29.jpg/1200px-U.S._Route_60_Frankfort%2C_KY_%2823892062134%29.jpg" ]
  louisianaPhotoList=["https://media.cntraveler.com/photos/53e2d8a9c2d3f39d36104f04/master/w_1600%2Cc_limit/louisianna-state-capitol-building.jpg", "https://thumbs.dreamstime.com/z/entrance-hall-louisiana-state-baton-rouge-usa-july-capitol-july-baton-rouge-usa-new-capitol-was-build-32848739.jpg","https://www.findingtheuniverse.com/wp-content/uploads/2016/05/State252520Capitol252520Building252520Baton252520Rouge252520Louisiana_by_Laurence252520Norah-725255B325255D.jpg", "https://www.thechurchnews.com/wp-content/uploads/2019/10/144270139f065af25bf7ac34426d63ee1aa9a6a9.jpg" ]
  mainePhotoList=["https://media.cntraveler.com/photos/53e2d8acc2d3f39d36104f16/master/w_1600%2Cc_limit/maine-state-capitol-building.jpg","http://www.etravelmaine.com/wp-content/uploads/2011/12/augusta-capital1.jpg", "https://c8.alamy.com/comp/HWAKY7/united-states-maine-augusta-maine-state-house-interior-with-bust-of-HWAKY7.jpg", "https://c8.alamy.com/comp/W2CG5D/usa-maine-augusta-maine-state-house-chamber-of-the-state-house-of-representatives-W2CG5D.jpg"   ]
  marylandPhotoList=["https://media.cntraveler.com/photos/53e2d8aec2d3f39d36104f28/master/w_1600%2Cc_limit/maryland-state-capitol-building.jpg", "https://fscomps.fotosearch.com/compc/UNS/UNS083/annapolis-state-house-state-capitol-picture__u12343584.jpg","https://149434078.v2.pressablecdn.com/wp-content/uploads/2020/12/Maryland-Annapolis-MD-Holiday-Annapolis-Events-Magical-for-Over-300-Years-credit-Visit-Annapolis.jpg", "https://www.traditionalbuilding.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTQ0NDE5NzQzNDA2Njk2MzQ3/projecta.jpg"  ]
  massachusettsPhotoList=["https://media.cntraveler.com/photos/53e2d8b1c2d3f39d36104f3a/master/w_1600%2Cc_limit/massachusetts-state-capitol-building.jpg", "https://static.dezeen.com/uploads/2019/10/boston-city-hall-renovation-brutalism-architecture-interiors-usa_dezeen_2364_col_6-852x569.jpg", "https://www.utiledesign.com/wp-content/uploads/2017/04/City-Hall-Lobby-410_low.jpg", "https://i.pinimg.com/originals/2f/da/ec/2fdaec1f968e14ffc9a778efbc2964a8.jpg"]
  michiganPhotoList=["https://media.cntraveler.com/photos/53e2d8b3c2d3f39d36104f4c/master/w_1600%2Cc_limit/michigan-state-capitol-building.jpg","http://s3.amazonaws.com/michiganmodern-prod/photos/966/building_homepage/mm_black_lansingcityhall_20160129.jpg?1454349474","https://assets.simpleviewinc.com/simpleview/image/upload/c_fill,h_600,q_80,w_1920/v1/clients/lansing/Downtown_Lansing_Capitol_ced58252-206a-4dfa-adb2-e168e6c9cb65.jpg","https://pbs.twimg.com/media/Evuj_emXIAIbfbw.jpg:large"  ]
  minnesotaPhotoList=["https://media.cntraveler.com/photos/53e2d8b6dddaa35c30f5fce7/master/w_1600%2Cc_limit/minnesota-state-capitol-building.jpg","https://www.stpaul.gov/sites/default/files/styles/large/public/2021-01/Saint_Paul_City_Hall_and_Ramsey_County_Courthouse_16.jpg?itok=1PeJlxxR", "https://www.tripsavvy.com/thmb/7qWbyBHPHDd3M75uleXI8wu2ZEg=/1500x844/smart/filters:no_upscale()/GettyImages-611475729-5b93df2146e0fb00507db045.jpg", "https://www.lakesnwoods.com/images/StPaul172.jpg" ]
  mississippiPhotoList=["https://media.cntraveler.com/photos/53e2d8b9dddaa35c30f5fcf9/master/w_1600%2Cc_limit/mississippi-state-capitol-building.jpg", "https://media-cdn.tripadvisor.com/media/photo-s/09/20/fa/68/city-hall.jpg", "https://media-cdn.tripadvisor.com/media/photo-s/09/20/fa/6b/city-hall.jpg", "https://images2.minutemediacdn.com/image/upload/c_fill,g_auto,h_740,w_1100/v1555003086/shape/mentalfloss/503186-istock-577642470.jpg?itok=k7JYNlU1"]
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
    newhampshire = Picture( bookingId=29, photoURL=newhampshirePhotoList[count])
    newjersey = Picture( bookingId=30, photoURL=newjerseyPhotoList[count])
    newmexico = Picture( bookingId=31, photoURL=newmexicoPhotoList[count])
    newyork = Picture( bookingId=32, photoURL=newyorkPhotoList[count])
    northcarolina = Picture( bookingId=33, photoURL=northcarolinaPhotoList[count])
    northdakota = Picture( bookingId=34, photoURL=northdakotaPhotoList[count])
    ohio = Picture( bookingId=35, photoURL=ohioPhotoList[count])
    oklahoma = Picture( bookingId=36, photoURL=oklahomaPhotoList[count])
    oregon = Picture( bookingId=37, photoURL=oregonPhotoList[count])
    pennsylvania = Picture( bookingId=38, photoURL=pennsylvaniaPhotoList[count])
    rhodeisland = Picture( bookingId=39, photoURL=rhodeislandPhotoList[count])
    southcarolina = Picture( bookingId=40, photoURL=southcarolinaPhotoList[count])
    southdakota = Picture( bookingId=41, photoURL=southdakotaPhotoList[count])
    tennessee = Picture( bookingId=42, photoURL=tennesseePhotoList[count])
    texas = Picture( bookingId=43, photoURL=texasPhotoList[count])
    utah = Picture( bookingId=44, photoURL=utahPhotoList[count])
    vermont = Picture( bookingId=45, photoURL=vermontPhotoList[count])
    virginia = Picture( bookingId=46, photoURL=virginiaPhotoList[count])
    washington = Picture( bookingId=47, photoURL=washingtonPhotoList[count])
    westvirginia = Picture( bookingId=48, photoURL=westvirginiaPhotoList[count])
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
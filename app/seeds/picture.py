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
  missouriPhotoList=["https://media.cntraveler.com/photos/53e2d8bcdddaa35c30f5fd0b/master/w_1600%2Cc_limit/missouri-state-capitol-building.jpg", "https://upload.wikimedia.org/wikipedia/commons/8/8f/AP_of_Missouri_State_Capitol_Building.jpg", "https://mediad.publicbroadcasting.net/p/ksmumain/files/styles/x_large/public/201810/mo_state_capitol_house_chambers--clio.com_.jpg", "https://bloximages.newyork1.vip.townnews.com/stltoday.com/content/tncms/assets/v3/editorial/a/c7/ac722974-9d89-583f-b94d-b8dab00fc049/5bc8a8fd18890.image.jpg?resize=1200%2C810" ]
  montanaPhotoList=["https://media.cntraveler.com/photos/53e2d8bfc2d3f39d36104f5e/master/w_1600%2Cc_limit/montana-state-capitol-building.jpg", "https://thumbs.dreamstime.com/z/city-hall-helena-montana-23832852.jpg", "https://thumbs.dreamstime.com/z/city-hall-helena-montana-25022123.jpg", "https://hitraveltales.com/wp-content/uploads/helena-at-night-from-mount-helena-48-hours-in-helena.jpg" ]
  nebraskaPhotoList=["https://media.cntraveler.com/photos/53e2d8c2c2d3f39d36104f70/master/w_1600%2Cc_limit/nebraska-state-capitol-building.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Nebraska_State_Capitol_aerial.jpg/1200px-Nebraska_State_Capitol_aerial.jpg", "https://www.planetware.com/photos-large/USNE/nebraska-lincoln-capitol-building.jpg", "https://bloximages.chicago2.vip.townnews.com/journalstar.com/content/tncms/assets/v3/editorial/a/55/a55cbef8-e528-5063-99c8-cfb1d1c7c416/5dfedd227b1ba.image.jpg" ]
  nevadaPhotoList=['https://media.cntraveler.com/photos/53e2d8c4c2d3f39d36104f82/master/w_1600%2Cc_limit/nevada-state-capitol-building.jpg', "https://wnhpc.com/wnhpccom0239-m.jpg", "https://s3-media2.fl.yelpcdn.com/bphoto/taoU_b-trWgzzuQcf2PJmQ/o.jpg", "https://live.staticflickr.com/7279/7768113924_c4ce73fc49_b.jpg"]
  newhampshirePhotoList=["https://media.cntraveler.com/photos/53e2d8c7dddaa35c30f5fd1e/master/w_1600%2Cc_limit/new-hampshire-state-capitol-building.jpg", "https://i.pinimg.com/originals/8f/5d/f5/8f5df5639e27e3ec72b46a0591bc1a8b.jpg", "https://www.concordnhchamber.com/UploadedFiles/Images/NHStateHouseSenateChamber.jpg", "https://www.getawaymavens.com/wp-content/uploads/2014/08/Tour-Guide-NH-State-House-in-Senate-Room.jpg"]
  newjerseyPhotoList=["https://media.cntraveler.com/photos/53e2d8cac2d3f39d36104f94/master/w_1600%2Cc_limit/new-jersey-state-capitol-building.jpg", "https://upload.wikimedia.org/wikipedia/commons/b/b1/2014-08-30_10_51_43_View_of_Trenton_City_Hall_in_Trenton%2C_New_Jersey_from_the_northeast.JPG", "https://www.nj.com/resizer/D1RaGbEM9zcgpDBH57YbRasXB-k=/450x0/smart/cloudfront-us-east-1.images.arcpublishing.com/advancelocal/QU7QXT6W45DITDZLBMILIMVCQA.JPG", "https://www.nj.com/resizer/U4OszzDeMLzLiRn0_qvEwlroeuQ=/1280x0/smart/advancelocal-adapter-image-uploads.s3.amazonaws.com/image.nj.com/home/njo-media/width2048/img/the-times/photo/2017/10/19/-107978e700be085f.jpg"]
  newmexicoPhotoList=["https://media.cntraveler.com/photos/53e2d8ccdddaa35c30f5fd30/master/w_1600%2Cc_limit/new-mexico-state-capitol-building.jpg", "https://www.studioswarch.com/wp-content/uploads/2017/09/lcch-9.jpg", "https://c8.alamy.com/comp/P43KKT/dome-on-city-hall-roswell-new-mexico-usa-P43KKT.jpg", "https://c8.alamy.com/comp/P43KBC/city-hall-roswell-new-mexico-usa-P43KBC.jpg"]
  newyorkPhotoList=["https://media.cntraveler.com/photos/53e2d8cec2d3f39d36104fa6/master/w_1600%2Cc_limit/new-york-state-capitol-building.jpg", "https://contractdesign.com/wp-content/uploads/hirstoricgallery4.jpg", "http://www.andrewcusack.com/nycityhall5.jpg", "https://storage.googleapis.com/clio-images/19646.39799.jpg" ]
  northcarolinaPhotoList=["https://media.cntraveler.com/photos/53e2d8d2dddaa35c30f5fd43/master/w_1600%2Cc_limit/north-carolina-state-capitol-building.jpg", "https://assets.simpleviewinc.com/simpleview/image/upload/c_fill,h_571,q_80,w_1603/v1/clients/raleigh/EX_skyline_GarrettPoulos_08_10_19_21_d426ec8d-46d3-4e1a-a43a-7b5a46f69b5b.jpg",  "https://upload.wikimedia.org/wikipedia/commons/d/d4/North_Carolina_State_Capitol%2C_Raleigh.jpg", "http://res.cloudinary.com/simpleview/image/upload/v1502138390/clients/raleigh/165_3_0042_jpeg_a32ab91e-8245-42f1-baa2-36a6f2a54dbb.jpg"]
  northdakotaPhotoList=["https://media.cntraveler.com/photos/53e2d8d4c2d3f39d36104fb8/master/w_1600%2Cc_limit/north-dakota-state-capitol-building.jpg", "https://www.nd.gov/omb/sites/omb/files/documents/public/state-capitol-info/capitolgroundsnew.jpg", "https://www.nationsonline.org/gallery/USA/North-Dakota-Heritage-center.jpg", "https://thumbs.dreamstime.com/z/interior-house-representatives-chamber-north-dakota-state-capitol-bismarck-north-dakota-north-dakota-house-101339599.jpg" ]
  ohioPhotoList=["https://media.cntraveler.com/photos/53e2d8d7dddaa35c30f5fd55/master/w_1600%2Cc_limit/ohio-state-capitol-building.jpg", "https://upload.wikimedia.org/wikipedia/commons/c/c1/Columbus%2C_Ohio_JJ_52-crop.jpg", "https://media.bizj.us/view/img/10118404/columbus-city-hall-city-council*1024xx5577-3147-0-626.jpg", "https://cdn.britannica.com/07/84507-050-35C6F597/Columbus-Ohio.jpg"]
  oklahomaPhotoList=["https://media.cntraveler.com/photos/53e2d8d9dddaa35c30f5fd67/master/w_1600%2Cc_limit/oklahoma-state-capitol-building.jpg", "https://livingnewdeal.org/wp-content/uploads/2012/01/7db47abc-ac48-40db-8a8a-f13fa5980e5f.jpg", "https://livingnewdeal.org/wp-content/uploads/2012/01/IMG_1725.jpg", "https://c8.alamy.com/comp/KPHT3D/usa-oklahoma-oklahoma-city-oklahoma-state-capitol-building-interior-KPHT3D.jpg"]
  oregonPhotoList=["https://media.cntraveler.com/photos/53e2d8dbc2d3f39d36104fca/master/w_1600%2Cc_limit/oregon-state-capitol-building.jpg", "https://i.redd.it/svjlu7qbco841.jpg", "https://upload.wikimedia.org/wikipedia/commons/c/ce/Oregon_State_Capitol_1.jpg", "https://www.nationsonline.org/gallery/USA/Oregon-State-Capitol2.jpg"]
  pennsylvaniaPhotoList=["https://media.cntraveler.com/photos/53e2d8dddddaa35c30f5fd79/master/w_1600%2Cc_limit/pennsylvania-state-capitol-building.jpg", "https://cimg1.ibsrv.net/ibimg/www.apartmentratings.com/650x433_85-1/8/7/9/879810827189821766684.jpg","https://upload.wikimedia.org/wikipedia/commons/f/ff/Market_Square_in_Harrisburg.jpg", "https://i.ytimg.com/vi/NEw9pbiAtb8/maxresdefault.jpg" ]
  rhodeislandPhotoList=["https://media.cntraveler.com/photos/53e2d8dfc2d3f39d36104fdc/master/w_1600%2Cc_limit/rhode-island-state-capitol-building.jpg", "https://assets.simpleviewinc.com/simpleview/image/fetch/c_limit,q_80,w_1200/https://assets.simpleviewinc.com/simpleview/image/upload/crm/rhodeisland/City-Hall-Providence-b4ac85615056a36_b4ac861f-5056-a36a-09e13b956395c3ec.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Providence_City_Council_Chambers.jpg/220px-Providence_City_Council_Chambers.jpg", "https://www.providenceri.gov/wp-content/uploads/2019/06/City-Hall-Atrium-View-600x300.jpg" ]
  southcarolinaPhotoList=["https://media.cntraveler.com/photos/53e2d8e2dddaa35c30f5fd8b/master/w_1600%2Cc_limit/south-carolina-state-capitol-building.jpg", "https://scpictureproject.org/wp-content/uploads/sc-state-house-interior.jpg","http://pics4.city-data.com/cpicv/vfiles23481.jpg", "https://www.scpictureproject.org/wp-content/uploads/south-carolina-statehouse-front-aerial.jpg" ]
  southdakotaPhotoList=["https://media.cntraveler.com/photos/53e2d8e4c2d3f39d36104fee/master/w_1600%2Cc_limit/south-dakota-state-capitol-building.jpg", "https://media-cdn.tripadvisor.com/media/photo-s/08/41/15/a6/state-capitol.jpg", "https://images.c-span.org/Files/451/20171007083247003_hd.jpg", "https://c8.alamy.com/comp/CR6P7F/pierre-south-dakota-state-capitol-building-inside-CR6P7F.jpg"  ]
  tennesseePhotoList=["https://media.cntraveler.com/photos/53e2d8e7c2d3f39d36105000/master/w_1600%2Cc_limit/tennessee-state-capitol-building.jpg", "https://i.pinimg.com/originals/98/3d/d1/983dd1650b5d9d8b43ffffd16026dcc3.jpg", "https://i.pinimg.com/originals/e0/03/df/e003df9914bb9eb00e55fae9fba5c27e.jpg", "https://www.nashvillemusiccitycenter.com/sites/default/files/media/Holiday/cvb_interior-1.jpg"]
  texasPhotoList=["https://media.cntraveler.com/photos/53e2d8eadddaa35c30f5fd9d/master/w_1600%2Cc_limit/texas-state-capitol-building.jpg", "http://www.austintexas.gov/sites/default/files/files/Communications/atxgov_cityhall_portal.jpg", "https://c8.alamy.com/comp/A0JRWE/texas-austin-city-hall-building-modern-architecture-plaza-landscaping-A0JRWE.jpg", "https://communityimpact.com/wp-content/uploads/2019/01/1.7-Austin-City-Hall.jpg"]
  utahPhotoList=["https://media.cntraveler.com/photos/53e2d8ecdddaa35c30f5fdaf/master/w_1600%2Cc_limit/utah-state-capitol-building.jpg", "https://c8.alamy.com/comp/CPYTBX/united-states-utah-salt-lake-city-town-hall-CPYTBX.jpg", "https://c8.alamy.com/comp/BDYJEY/interior-of-the-utah-state-capital-building-in-salt-lake-city-utah-BDYJEY.jpg", "https://thumbs.dreamstime.com/z/interior-utah-state-capitol-salt-lake-city-main-hall-downtown-82115769.jpg" ]

  vermontPhotoList=["https://media.cntraveler.com/photos/53e2d8eec2d3f39d36105013/master/w_1600%2Cc_limit/vermont-state-capitol-building.jpg", "https://cdn.wedding-spot.com/__sized__/images/venues/12290/Vermont-College-Of-Fine-Arts-Montpelier-VT-b7ca9799-0768-45f8-a924-75207fcecbbf-97450e389c42885476f1fbe9bc5bca5a.JPG", "https://www.vermont.gov/themes/custom/vt2018/images/menu-features/statehouse_inside.jpg", "https://b386363e680359b5cc19-97ec1140354919029c7985d2568f0e82.ssl.cf1.rackcdn.com/assets/uploads/area_profile/banner_image/28833/optimized_cdde5f14758dcfd3f8bacb8807366862.jpg" ]

  virginiaPhotoList=["https://media.cntraveler.com/photos/53e2d8f1c2d3f39d36105025/master/w_1600%2Cc_limit/virginia-state-capitol-building.jpg", "https://bloximages.newyork1.vip.townnews.com/richmond.com/content/tncms/assets/v3/editorial/8/6f/86f98810-5c1a-11e2-8a81-001a4bcf6878/50f05629c4a06.image.jpg", "https://upload.wikimedia.org/wikipedia/commons/c/c9/Atrium_Old_City_Hall_Richmond%2C_VA_%288748859851%29.jpg", "https://upload.wikimedia.org/wikipedia/commons/6/66/Stairs_Old_City_Hall_Richmond%2C_VA_%288749986776%29.jpg" ]

  washingtonPhotoList=["https://media.cntraveler.com/photos/53e2d8f4c2d3f39d36105037/master/w_1600%2Cc_limit/washington-state-capitol-building.jpg", "https://c8.alamy.com/comp/B1T8XC/interior-of-rotunda-of-washington-state-legislative-building-in-the-B1T8XC.jpg", "https://i.pinimg.com/originals/7d/23/2f/7d232f573c2c944171086ed8992c0956.jpg", "https://bloximages.newyork1.vip.townnews.com/ifiberone.com/content/tncms/assets/v3/editorial/b/15/b15c6d18-8ca2-11eb-8740-73e99648ad6b/605b3b05bbd5f.image.jpg" ]
  westvirginiaPhotoList=["https://media.cntraveler.com/photos/53e2d8f7c2d3f39d36105049/master/w_1600%2Cc_limit/west-virginia-state-capitol-building.jpg", "https://www.charlestonwv.gov/sites/default/files/footer-images/cityhall.jpg", "https://media-cdn.tripadvisor.com/media/photo-s/0a/2f/a9/f6/city-hall-charleston.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/The_West_Virginia_Capitol_in_Charleston_LCCN2015631770.tif/lossy-page1-1200px-The_West_Virginia_Capitol_in_Charleston_LCCN2015631770.tif.jpg"]
  wisconsinPhotoList=["https://media.cntraveler.com/photos/53e2d8fcc2d3f39d3610505b/master/w_1600%2Cc_limit/wisconsin-state-capitol-building.jpg", "https://www.cityofmadison.com/sites/default/files/category/images/imageSkyline.jpg", "https://previews.123rf.com/images/benkrut/benkrut1109/benkrut110900042/10484363-interior-of-state-capitol-building-in-madison-wisconsin-usa.jpg"]
  wyomingPhotoList=["https://media.cntraveler.com/photos/53e2d8ffc2d3f39d3610506d/master/w_1600%2Cc_limit/wyoming-state-capitol-building.jpg", "https://m.psecn.photoshelter.com/img-get2/I0000cwFXR_B4Hh4/fit=1000x750/Wyoming-Cheyenne-Wyoming-State-Capitol-Interior-Staircase.jpg", "https://www.cheyennecity.org/files/oc-templates/00000000-0000-0000-0000-000000000000/b32c9b6c-7400-488a-8246-4bc7b2004122/Municipal_Building_drone1.jpg", "https://image1.masterfile.com/getImage/NzAwLTAwMDg4NTAxZW4uMDAwMDAwMDA=AMa-4h/700-00088501en_Masterfile.jpg"]

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
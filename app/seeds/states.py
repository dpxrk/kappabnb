from app.models import db, State


def seed_states():
  stateNames = [
   "Alabama",
   'Alaska',
   'Arizona',
   'Arkansas',
   'California',
   'Colorado',
   'Connecticut',
   'Delaware',
   'Florida',
   'Georgia',
   'Hawaii',
   'Idaho',
   'Illinois',
   'Indiana',
   'Iowa',
   'Kansas',
   'Kentucky',
   'Louisiana',
   'Maine',
   'Maryland',
   'Massachusetts',
   'Michigan',
   'Minnesota',
   'Mississippi',
   'Missouri',
   'Montana',
   'Nebraska',
   'Nevada',
   'New Hampshire',
   'New Jersey',
   'New Mexico',
   'New York',
   'North Dakota',
   'North Carolina',
   'Ohio',
   'Oklahoma',
   'Oregon',
   'Pennsylvania',
   'Rhode Island',
   'South Carolina',
   'South Dakota',
   'Tennessee',
   'Texas',
   'Utah',
   'Vermont',
   'Virginia',
   'Washington',
   'West Virginia',
   'Wisconsin',
   'Wyoming'
  ]

  capitals = [
    'Montgomery',
    'Juneau',
    'Phoenix',
    'Little Rock',
    'Sacramento',
    'Denver',
    'Hartford',
    'Dover',
    'Tallahassee',
    'Atlanta',
    'Honolulu',
    'Boise',
    'Springfield',
    'Indianapolis',
    'Des Moines',
    'Topeka',
    'Frankfort',
    'Baton Rouge',
    'Augusta',
    'Annapolis',
    'Boston',
    'Lansing',
    'St. Paul',
    'Jackson',
    'Jefferson City',
    'Helena',
    'Lincoln',
    'Carson City',
    'Concord',
    'Trenton',
    'Santa Fe',
    'Albany',
    'Raleigh',
    'Bismarck',
    'Columbus',
    'Oklahoma City',
    'Salem',
    'Harrisburg',
    'Providence',
    'Columbia',
    'Pierre',
    'Nashville',
    'Austin',
    'Salt Lake City',
    'Montpelier',
    'Richmond',
    'Olympia',
    'Charleston',
    'Madison',
    'Cheyenne'
  ]


  count = 0
  while count < 50:
    new_state = State(
      stateName= stateNames[count],
      capital= capitals[count]
    )
    count += 1
    db.session.add(new_state)


  db.session.commit()



def undo_states():
  db.session.execute('TRUNCATE states;')
  db.session.commit()
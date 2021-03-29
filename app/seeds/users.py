from werkzeug.security import generate_password_hash
from app.models import db, User

# Adds a demo user, you can add other users here if you want
def seed_users():

    demo = User(fullName='Demolicious', email='demo@aa.io',
                password='password', profileImage='https://image.shutterstock.com/image-photo/tall-backpacker-poles-hand-sunny-260nw-348249572.jpg')

    host = User(fullName='Host-age', email='host@aa.io', password='password', profileImage='https://previews.123rf.com/images/hermandesign2015/hermandesign20151709/hermandesign2015170900212/86257516-cartoon-host-holding-a-microphone.jpg')

    db.session.add(demo)
    db.session.add(host)

    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_users():
    db.session.execute('TRUNCATE users;')
    db.session.commit()

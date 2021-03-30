from .db import db
from sqlalchemy.orm import relationship


class Booking(db.Model):
  __tablename__ ='bookings'


  id = db.Column(db.Integer, primary_key=True, nullable=False)
  title = db.Column(db.String(250), nullable=False)
  userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  price = db.Column(db.Numeric, nullable=False)
  description = db.Column(db.Text, nullable=False)
  address = db.Column(db.Text, nullable=False)
  stateId = db.Column(db.Integer, db.ForeignKey('states.id'), nullable=False,)
  createdAt = db.Column(db.DateTime,  default=db.func.current_timestamp())
  updatedAt = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


  pictures = relationship('Picture', back_populates='bookings')
  state = db.relationship('State', backref='states')
  user = db.relationship('User', backref='bookings')



  def to_dict(self):
    state = self.state.stateName
    userFullName = self.user.fullName

    return {
      'id': self.id,
      'title': self.title,
      'userId': userFullName,
      'price': float(self.price),
      'description': self.description,
      'address' : self.address,
      'pictures': [picture.photoURL for picture in self.pictures],
      'state' : state
    }

from .db import db


class Comment(db.Model):
  __tablename__ = 'comments'

  id = db.Column(db.Integer, primary_key=True, nullable=False)
  userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  reviewId = db.Column(db.Integer, db.ForeignKey('reviews.id'), nullable=False)
  content = db.Column(db.Text, nullable=False)
  createdAt = db.Column(db.DateTime,  default=db.func.current_timestamp())
  updatedAt = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

  user = db.relationship('User', backref='comments')
  review = db.relationship('Review', backref='comments')


  def to_dict(self):
    return {
      'id':self.id,
      'userId':self.userId,
      'reviewId':self.reviewId,
      'content':self.content
    }
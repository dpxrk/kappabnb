from flask_wtf import FlaskForm
from wtforms import TextAreaField, HiddenField, IntegerField
from wtforms_validators import DataRequired



class ReviewForm(FlaskForm):
  userId = HiddenField('userId')
  bookingId = HiddenField('bookingId')
  numberOfStars = IntegerField('numberOfFields', [DataRequired()])
  content = TextAreaField('content', [DataRequired()])

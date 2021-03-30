from flask_wtf import FlaskForm
from wtforms import TextAreaField, HiddenField, IntegerField
from wtforms.validators import DataRequired


class ReviewForm(FlaskForm):
  userId = HiddenField('userId')
  bookingId = HiddenField('bookingId')
  numberOfStars = IntegerField('numberOfFields', validators=[DataRequired()])
  content = TextAreaField('content', validators=[DataRequired()])

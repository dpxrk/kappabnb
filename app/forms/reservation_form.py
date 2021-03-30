from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired



class ReservationForm(FlaskForm):
  userId = HiddenField('userId')
  bookingId = HiddenField('bookingId')
  startDate = StringField('startDate',validators=[DataRequired()])
  endDate = StringField('endDate', validators=[DataRequired()])

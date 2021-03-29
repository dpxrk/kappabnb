from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms_validators import DataRequired
from app.models import Reservation


class ReservationForm(FlaskForm):
  userId = HiddenField('userId')
  bookingId = HiddenField('bookingId')
  startDate = StringField('startDate',[DataRequired()])
  endDate = strringField('endDate', [DataRequired()])

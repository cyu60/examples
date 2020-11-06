from flask_wtf import FlaskForm
from wtforms import IntegerField, TimeField, SubmitField
from wtforms.validators import DataRequired, NumberRange

# time, threshold value
class UserInputForm(FlaskForm):
    threshold_value = IntegerField('Threshold Value', 
        validators=[DataRequired(), NumberRange(min=0, max=None, message="Numeric Input Required")])
    time_ago = IntegerField('Number of hours ago', validators=[ DataRequired(), 
        NumberRange(min=0, max=72, message="Numeric Input Required, max 72 hrs")])
        # Change to Time slider in the future?
    submit = SubmitField('Get Transactions')


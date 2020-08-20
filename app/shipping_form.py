from flask_wtf import FlaskForm
from wtforms.fields import (
    BooleanField, SelectField, StringField, SubmitField,
)
from wtforms.validators import DataRequired
from map.map import map


choices = [(city, city) for city in map.keys()]


class ShippingForm(FlaskForm):
    sender = StringField('sender', [DataRequired()])
    recipient = StringField('recipient', [DataRequired()])
    origin = SelectField('origin', [DataRequired()], choices=choices)
    destination = SelectField('destination', [DataRequired()], choices=choices)
    express = BooleanField('express')
    submit = SubmitField('submit')
    cancel = SubmitField('cancel')

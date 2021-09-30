from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
class inputform(FlaskForm):
        Input_circuit= StringField('Circuit String', validators=[DataRequired(), Length(min=3, max=50)])
        submit = SubmitField('Find the answer here')
        Answer= StringField('Final Answer is')

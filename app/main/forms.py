from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required


class CommentsForm(FlaskForm):

    title = StringField('Comments title', validators=[Required()])
    comments = TextAreaField('News comments', validators=[Required()])
    submit = SubmitField('Submit')

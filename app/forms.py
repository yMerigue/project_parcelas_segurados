from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.fields import DateField
from wtforms.validators import DataRequired

class ClientForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    seguradora = StringField('Seguradora', validators=[DataRequired()])
    tipo_seguro = StringField('Tipo de Seguro', validators=[DataRequired()])
    qtde_parcelas = IntegerField('Quantidade de Parcelas', validators=[DataRequired()])
    forma_pagamento = StringField('Forma de Pagamento', validators=[DataRequired()])
    submit = SubmitField('Registrar')

class DueDateForm(FlaskForm):
    date = DateField('Due Date', format='%Y-%m-%d', validators=[DataRequired()])

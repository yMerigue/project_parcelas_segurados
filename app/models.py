from . import db

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    seguradora = db.Column(db.String(100), nullable=False)
    tipo_seguro = db.Column(db.String(100), nullable=False)
    qtde_parcelas = db.Column(db.Integer, nullable=False)
    forma_pagamento = db.Column(db.String(100), nullable=False)
    due_dates = db.relationship('DueDate', backref='client', lazy=True)

class DueDate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    pago = db.Column(db.Boolean, default=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)

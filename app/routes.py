from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import Client, DueDate
from .forms import ClientForm
from datetime import datetime

main_bp = Blueprint('main', __name__)

def format_date(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.strftime('%d/%m/%Y')

@main_bp.context_processor
def utility_processor():
    return dict(enumerate=enumerate, format_date=format_date)

@main_bp.route('/')
def home():
    clients = Client.query.all()
    return render_template('home.html', clients=clients)

@main_bp.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = ClientForm()
    if form.validate_on_submit():
        nome = form.nome.data
        seguradora = form.seguradora.data
        tipo_seguro = form.tipo_seguro.data
        qtde_parcelas = form.qtde_parcelas.data
        forma_pagamento = form.forma_pagamento.data

        client = Client(nome=nome, seguradora=seguradora, tipo_seguro=tipo_seguro, qtde_parcelas=qtde_parcelas, forma_pagamento=forma_pagamento)
        db.session.add(client)
        db.session.commit()

        for i in range(1, qtde_parcelas + 1):
            due_date = request.form[f'due_date_{i}']
            due_date_record = DueDate(date=due_date, client_id=client.id)
            db.session.add(due_date_record)

        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('registrar.html', form=form)


@main_bp.route('/toggle_payment/<int:due_date_id>', methods=['POST'])
def toggle_payment(due_date_id):
    due_date = DueDate.query.get(due_date_id)
    due_date.pago = not due_date.pago
    db.session.commit()
    return redirect(url_for('main.parcelas_de_hoje'))


@main_bp.route('/parcelas_de_hoje')
def parcelas_de_hoje():
    today = datetime.today().strftime('%Y-%m-%d')
    due_dates = DueDate.query.filter_by(date=today).all()
    form = ClientForm()  # Ou o formulário correto que você deseja usar
    return render_template('parcelas_de_hoje.html', due_dates=due_dates, form=form)

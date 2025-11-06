import os
from flask import Flask, render_template, send_from_directory, flash, request, \
                        redirect, url_for, render_template

from model import *
from werkzeug.utils import secure_filename
from app import app, db
from util import *
from model import SMS, SMSTemplate, DeliveryOrder

sms_template = None

with app.app_context():
    try:
        sms_template = db.session.query(SMSTemplate).order_by(SMSTemplate.id.desc()).first().text
    except:
        sms_template = ''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/settings')
def settings():
    global sms_template

    try:
        sms_template = db.session.query(SMSTemplate).order_by(SMSTemplate.id.desc()).first().text
    except Exception as e:
        print('An error occurred while retrieving template ' + repr(e))
        sms_template = ''

    return render_template('settings.html', sms_template=sms_template)

@app.route('/sms')
def list_sms():
    index = request.args.get('page', 1, type=int)
    page = db.paginate(db.select(SMS).order_by(SMS.insert_date), per_page=5, page=index)
    return render_template('list_sms.html', items=page, title='Ordini')


@app.route('/order/update', methods=['POST'])
def update_order():
    data = request.json
    order = db.session.query(DeliveryOrder).get(data['id'])
    order.phonenumber = data['phonenumber']
    print(data['phonenumber'])
    order.delivery_date = data['delivery_date']
    order.address = data['address']
    order.city = data['city']
    db.session.commit()
    return { 'status' : 'ok'}

@app.route('/sms-template', methods=['POST'])
def update_sms_template():
    data = request.json
    template = SMSTemplate(text = data['text'])
    
    db.session.add(
        template
    )
    db.session.commit()

    global sms_template
    sms_template = template.text
    

    return { 'status' : 'ok'}

@app.route('/orders')
def list_orders():
    index = request.args.get('page', 1, type=int)
    page = db.paginate(db.select(DeliveryOrder).order_by(DeliveryOrder.insert_date), per_page=5, page=index)
    return render_template('list_orders.html', items=page, title='Ordini')

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

@app.route('/success', methods = ['POST', 'GET'])   
def success():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_location = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_location)
            delivery_orders = extract_delivery_orders(file_location)
            db.session.add_all(delivery_orders)
            db.session.commit()
            send_sms(delivery_orders=delivery_orders, sms_template=sms_template)
            return { 'status': 'ok'}
#            return redirect(url_for('download_file', name=filename))

        else:
            flash('File not supported')
        
    return render_template('success.html')


from app import db
from datetime import datetime
import requests



class DeliveryOrder(db.Model):
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), unique=False)
    phonenumber = db.Column(db.String(100), unique=False)
    address = db.Column(db.String(100), unique=False)
    delivery_date = db.Column(db.String(100), unique=False)
    city = db.Column(db.String(100), unique=False)
    insert_date = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, delivery_date, customer_name, phonenumber, address, city):
        self.delivery_date = delivery_date
        self.customer_name = customer_name
        self.phonenumber = phonenumber
        self.address = address
        self.city = city


class SMSTemplate(db.Model):
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(144), unique=False)
    insert_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, text):
        self.text = text
    


class SMS(db.Model):
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    phonenumber = db.Column(db.String(100), unique=False)
    content = db.Column(db.String(144), unique=False)
    error = db.Column(db.String(400), unique=False)
    order_number = db.Column(db.Integer, primary_key=False)
    sent = db.Column(db.Boolean, unique=False)
    insert_date = db.Column(db.DateTime, default=datetime.utcnow)

    url = 'https://smsgateway24.com/getdata/addsms'
    token = 'token'
    device_id = 'device_id'

    headers = {
        'apikey' : 'api_key',
        'Content-Type' : 'application/x-www-form-urlencoded',
        'Cache-Control' : 'no-cache'
    }

    def __init__(self, dst_number, msg):
        self.phonenumber = dst_number
        self.content = msg
    
    def serialize(sms):
        return {
            'id': sms.id,
            'content': sms.content,
            'phonenumber': sms.phonenumber
        }
    def send_sms(self):
        if True:
            import random
            self.sent = bool(random.getrandbits(1))
            return
        payload = 'token=' + self.token + \
                    '&sendto=' + self.dst_number + \
                    '&body=' + self.msg + \
                    '&device_id=' + self.device_id
        try:
            requests.request('POST', self.url, data = payload, headers = self.headers)
            self.sent = True
        except Exception as e:
            self.sent = False
            self.error = repr(e)
            print('Error while sending message ' + repr(e))

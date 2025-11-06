from xlrd import open_workbook
from model import *
from app import app


COLUMN = {
    'FOR_DATE' : 0,
    'FOR_CUSTOMER_NAME' : 3,
    'FOR_phonenumber' : 4,
    'FOR_ADDRESS': 5,
    'FOR_CITY': 6
}

UPLOAD_FOLDER = './data'
ALLOWED_EXTENSIONS = {'xls', 'xlsx', 'csv', 'icns'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def send_sms(delivery_orders, sms_template):
    processed_sms = []
    for order in delivery_orders:
        print(sms_template)
        print(order.customer_name,'-----~', order.delivery_date)
        sms = SMS(
            dst_number = order.phonenumber,
            msg = sms_template % (order.customer_name, order.delivery_date)
        )
        sms.send_sms()
        processed_sms.append(sms)

    db.session.add_all(processed_sms)
    db.session.commit()

    


def extract_delivery_orders(file_location):
    wb = open_workbook(file_location, 'r')
    wb_sheet = wb.sheet_by_index(0)
    values = []

    for row_idx in range(1, wb_sheet.nrows):
#        attrib = str(wb_sheet.cell(row_idx, 0).value)
        print(wb_sheet.cell(row_idx, COLUMN['FOR_DATE']).value)
        delivery_order = DeliveryOrder(
            str(wb_sheet.cell(row_idx, COLUMN['FOR_DATE']).value),
            str(wb_sheet.cell(row_idx, COLUMN['FOR_CUSTOMER_NAME']).value),
            str(wb_sheet.cell(row_idx, COLUMN['FOR_phonenumber']).value),
            str(wb_sheet.cell(row_idx, COLUMN['FOR_ADDRESS']).value),
            str(wb_sheet.cell(row_idx, COLUMN['FOR_CITY']).value),
        )
        values.append(delivery_order)
    return values


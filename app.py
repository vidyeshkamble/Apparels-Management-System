import os
import random
import secrets
import mysql
import numpy as np
import qrcode
import requests
import ast
from flask import Flask, redirect, render_template, Response, request, jsonify, json , session, url_for
import bcrypt
import cv2
from pyzbar.pyzbar import decode
import time
import winsound
from flask_mail import Mail, Message
from email.mime.base import MIMEBase
import pdfkit
import jinja2
import datetime
from openai import Client, OpenAI
from flask import Flask, render_template, Response, jsonify, request
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import mysql.connector


import tkinter as tk
from tkinter import simpledialog, messagebox


import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from ConnectionDatabase import FetchDataFromDatabase


app = Flask(__name__)
app.secret_key = 'apparelsystem'
Purchase_Bag = []
qty = ""

# Main Route
@app.route('/')
def index():
    return render_template('login.html')

# login detals to page
@app.route('/logintodatabase')
def logintodatabase():
    mydb = FetchDataFromDatabase(int(session.get('user_id', 0))).Connection()
    mycursor = mydb.cursor()

    class Login:
        def __init__(self, id, name, mono, email, address, password):
            self.user_id = id
            self.user_name = name
            self.user_mobl = mono
            self.user_email = email
            self.user_address = address
            self.password = password
        
        def StoreinDatabase(self):
            sql = "SELECT user_id FROM customer WHERE user_id = %s"
            mycursor.execute(sql, (self.user_id,))
            myresult = mycursor.fetchall()
            if myresult:
                return render_template('login.html', error="User already exists! Try Again")
            else:
                password_hash = hash_password(self.password)
                insert = "INSERT INTO apparels.customer(user_id, user_name, user_mobl, user_email, user_address, user_password) VALUES (%s, %s, %s, %s, %s, %s);"
                val = (self.user_id, self.user_name, self.user_mobl, self.user_email, self.user_address, password_hash)
                mycursor.execute(insert, val)
                mydb.commit()
                return render_template('login.html', success="Login Successfully")

    def hash_password(password):
        # Generate a salt and hash the password
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    user_id = request.args.get("user_id")
    user_name = request.args.get("user_name")
    user_mobl = request.args.get("user_mobl")
    user_email = request.args.get("user_email")
    user_address = request.args.get("user_address")
    user_password_temp = request.args.get("user_password_temp")
    user_password = request.args.get("user_password")

    if user_password_temp == user_password:
        obj = Login(user_id, user_name, user_mobl, user_email, user_address, user_password)
        return obj.StoreinDatabase()  # Ensure the return value is passed back
    else:
        return render_template('login.html', error="Password does not match!")



@app.route('/signintodatabase',methods = ['POST'])
def signintodatabase():
    mydb = FetchDataFromDatabase(int(session.get('user_id', 0))).Connection()
    mycursor = mydb.cursor()
    class SignUp:
        def __init__(self,us,passw):
            self.user_id = us
            self.user_password = passw
        
        def CheckUser(self):
            check = "SELECT user_password FROM customer WHERE user_id = %s;"
            mycursor.execute(check,[self.user_id])
            myresult = mycursor.fetchone()
            if myresult:
                incript_Code = check_password(myresult[0],str(self.user_password))
                if incript_Code:
                    session['user_id']=self.user_id
                    
                    optionlist = "select type from apparels.inventory where type not in ('men','women')"
                    mycursor.execute(optionlist)
                    optionListArray = mycursor.fetchall()
                    unicOption = list(dict.fromkeys(item[0] for item in optionListArray))
                    
                    return render_template('index.html', user_id=self.user_id,optionList = unicOption)
                else:
                    return render_template('login.html', error="Password incorect !")
            else:
                return render_template('login.html', error="User not found. Please try again.")
            
    def check_password(stored_password_hash, entered_password):
        # Convert string back to bytes for verification
        return bcrypt.checkpw(entered_password.encode('utf-8'), stored_password_hash.encode('utf-8'))

    user_id = request.form.get("user_id")
    user_password = request.form.get("user_password")
    
    obj = SignUp(user_id,user_password)
    return obj.CheckUser()

@app.route('/logout')
def logout():
    session.pop('user_id',None)
    return render_template('login.html')


@app.route('/selectedOption', methods=['GET'])
def selectedOption():
    try:
        mydb = FetchDataFromDatabase(int(session.get('user_id', 0))).Connection()
        mycursor = mydb.cursor()

        selected_value = request.args.get('selected')
        print(selected_value)

        mycursor.execute("SELECT id, name, image, price FROM apparels.inventory WHERE type=%s", (selected_value,))
        data = mycursor.fetchall()

        mycursor.close()
        mydb.close()

        return jsonify({"data": data})  # Ensure key is 'data' to match JavaScript

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)})

    
    
# Ajax to Add the Items to Purchase card
@app.route('/Addto', methods=['POST'])
def Addto():
    item_id = request.json['code']
    title = request.json['title']
    image = request.json['image']
    qty = int(request.json['qty'])
    pricem = int(request.json['price'])
    
    print(item_id,title,image,qty,pricem)
    
    price = pricem * qty
    
    if any(item['code'] == item_id for item in Purchase_Bag):
        return jsonify({"error": "Item already in bag"}), 400
    item = {
        "code": item_id,
        "title": title,
        "image": image,
        "qty":qty,
        "price": price
    }
    Purchase_Bag.append(item)
    return jsonify(Purchase_Bag)


# Ajax to remove the Items to Purchase card
@app.route('/Removeitem', methods = ['POST'])
def Removeitem():
    indexValue = request.json['data']
    Purchase_Bag.pop(indexValue)
    return jsonify(Purchase_Bag)


#Goto BUY Page
@app.route('/BuyPage')
def BuyPage():
    return render_template('Buy.html',bag=Purchase_Bag)

@app.route('/removeds')
def removeds():
    index = request.args.get('index_value')
    for item in Purchase_Bag:
        if item['code'] == index:
            Purchase_Bag.remove(item)
    return render_template('Buy.html',bag=Purchase_Bag)

@app.route('/paymentpage')
def paymentpage():
    qty = request.args.get('qty')
    totle_price = request.args.get('totle_price')
    return render_template('payment.html',Amount = totle_price,qty = qty)
import traceback  # For better error debugging

@app.route('/sendOtp')
def sendOtp():
    try:
        totle_price = request.args.get('totle_price')
        payment_mode = request.args.get('payment_mode')

        obj = FetchDataFromDatabase(int(session.get('user_id', 0)))
        customer_data = obj.Customer()
        
        # otp = send_otp_email(customer_data[3])
        otp = "".join([str(random.randint(0, 9)) for _ in range(6)])
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("vidyeshmy@gmail.com","sqzp gcof aida usit")
        massage = f"""
        Hi there,

        Apparel Shop sent you an OTP [One Time Password].

        Your OTP is: **{otp}**

        Please **DO NOT** share or forward this email.

        Regards,  
        Apparel Shop Team
        """
        s.sendmail("vidyeshmy@gamil.com",customer_data[3],massage)
        s.quit()
        
        print("Return OTP IS : ", otp)

        return render_template('otp.html', Amount=totle_price, payment_mode=payment_mode,otp=otp)
    
    except Exception as e:
        print("Error in sendOtp:", str(e))
        print(traceback.format_exc())  # Logs full error traceback
        return jsonify({"error": "Something went wrong"}), 500  # Return a proper JSON error response

    
        
@app.route('/verifyOtp', methods=['POST'])
def verifyOtp():
    try:
        user_otp = request.form.get('user_otp')
        totle_price = request.form.get('Amount')
        payment_mode = request.form.get('payment_mode')
        otp = request.form.get('otp')

        obj = FetchDataFromDatabase(int(session.get('user_id', 0)))
        # customer_data = obj.Customer()
        correct_otp =  otp # This should ideally be stored in session
        print(correct_otp)
        print(user_otp)
         
        if user_otp == correct_otp:
            return addtodatabase(totle_price, payment_mode) # Exit Form OTP page
        else:
            return render_template('otp.html', error="Invalid OTP. Try again.", Amount=totle_price, payment_mode=payment_mode)
    except Exception as e:
        print("Error in verifyOtp:", str(e))
        return render_template(
            "otp.html",
            error="An error occurred. Please try again.",
            Amount=request.form.get("Amount"),
            payment_mode=request.form.get("payment_mode")
        ), 500

@app.route('/addtodatabase')
def addtodatabase(tot, paymode):    
    try: 
        obj = FetchDataFromDatabase(int(session['user_id']))
        customer_data = obj.Customer()
        
        # Ensure Purchase_Bag is not empty
        if not Purchase_Bag:
            raise Exception("Purchase Bag is empty.")
        
        # Connect to the database
        mydb = FetchDataFromDatabase(int(session.get('user_id', 0))).Connection()
        mycursor = mydb.cursor()

        # Extract purchase codes and quantities
        String_code = [item['code'] for item in Purchase_Bag]
        qtys = [item['qty'] for item in Purchase_Bag]  
        j = len(Purchase_Bag)  
        
        totle_price = tot
        payment_mode = paymode
        
        # Insert into bill table
        x = datetime.datetime.now()
        inserttobill = """
        INSERT INTO apparels.bill(date, time, inv_ids, sales_qty, sales_price, payment_mode) 
        VALUES(%s, %s, %s, %s, %s, %s)
        """
        bill_values = (
            x.strftime("%Y-%m-%d"), x.strftime("%X"), 
            session['user_id'], j, totle_price, payment_mode
        )
        mycursor.execute(inserttobill, bill_values)
        
        # Fetch inserted bill number
        query = """
        SELECT bill_no 
        FROM apparels.bill 
        WHERE time=%s AND date=%s AND inv_ids=%s
        """
        query_values = (x.strftime("%X"), x.strftime("%Y-%m-%d"), int(session['user_id']))
        mycursor.execute(query, query_values)
        result = mycursor.fetchone()
        
        if not result:
            raise Exception("Failed to retrieve bill number.")
        
        bill_no = result[0]  # Ensure bill_no is always defined

        # Checking items in inventory and updating stock
        for idx, item in enumerate(Purchase_Bag):
            mycursor.execute("SELECT qty FROM apparels.inventory WHERE id=%s", (item['code'],))
            check_stock = mycursor.fetchone()
            
            if check_stock:
                current_stock = check_stock[0]
                
                if current_stock >= item['qty']:
                    # Reduce stock directly
                    mycursor.execute(
                        "UPDATE apparels.inventory SET qty = qty - %s WHERE id = %s", (qtys[idx], item['code'])
                    )
                else:
                    # Request additional stock
                    required_stock = item['qty'] - current_stock
                    mycursor.execute(
                        "UPDATE apparels.inventory SET qty = 0 WHERE id = %s", (item['code'],)
                    )
                    query_insert = """
                    INSERT INTO apparels.requeststock (code, name, bill_no, price, qty) 
                    VALUES (%s, %s, %s, %s, %s)
                    """
                    insert_set = (item['code'], item['title'], bill_no, item['price'], required_stock)
                    mycursor.execute(query_insert, insert_set)
        
        # Insert into items table
        item_values = [
            (bill_no, String_code[i], qtys[i], totle_price) for i in range(j)
        ]
        mycursor.executemany(
            "INSERT INTO apparels.items (item_table_id, item_code, qty, total_price) VALUES (%s, %s, %s, %s)", 
            item_values
        )

        mydb.commit()  # Commit changes

        return bill_Generate(customer_data, bill_no)
    
    except Exception as e:
        print(f"Error: {e}")
        return render_template('index.html', Error=str(e))



# Generate Bill

def bill_Generate(data,result):
    try:
        for item in Purchase_Bag:
            item['price'] = int(item['price']) 

        total_sum = sum(item['price'] for item in Purchase_Bag)  
        x = datetime.datetime.now()
        context ={'inv_no':result,'ph':data[2],'name':data[1],'email':data[3],'bag':Purchase_Bag,'totle':total_sum ,'date':x.strftime("%Y-%m-%d"),'time':x.strftime("%X")} 
        
        template_loader = jinja2.FileSystemLoader('./')
        template_env = jinja2.Environment(loader=template_loader)
        
        template = template_env.get_template('bill.html')
        output_text = template.render(context)
        
        
        path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

        
    
        options = {
            'page-width': '80mm',
            'page-height': '150mm',  
            'margin-top': '5mm',
            'margin-right': '5mm',
            'margin-bottom': '5mm',
            'margin-left': '5mm',
            'encoding': 'UTF-8',  
        }

        # Configure pdfkit
        config = pdfkit.configuration(wkhtmltopdf=path)

        # Generate PDF
        pdfkit.from_string(output_text,'bill.pdf', configuration=config ,options=options)
        Purchase_Bag.clear()
        return send_Mail(data[3])
        
    except Exception as e:
        print(f"Error:{e} In This")
        return render_template('index.html', Error=str(e))
    



# Send Email

def send_Mail(email):
    try:
        app.config['MAIL_SERVER'] = 'smtp.gmail.com'
        app.config['MAIL_PORT'] = 587
        app.config['MAIL_USE_TLS'] = True
        app.config['MAIL_USE_SSL'] = False
        app.config['MAIL_USERNAME'] = 'vidyeshmy@gmail.com'
        app.config['MAIL_PASSWORD'] = 'sqzp gcof aida usit' 
        app.config['MAIL_DEFAULT_SENDER'] = 'vidyeshmy@gmail.com'

        mail = Mail(app)
        msg = Message(
            'Shopping Bill...', 
            recipients=[email], 
            body='Hi there, Apparel Shop Send you a Shopping bill in PDF Formate.... This is System Generate bill, Dont forword this mail...!'  
        )

    
        pdf_path = 'bill.pdf'

        with app.open_resource(pdf_path) as pdf:
            msg.attach(
                "bill.pdf",  
                "application/pdf",  
                pdf.read()  
            )

        try:
            mydp = FetchDataFromDatabase(int(session.get('user_id', 0))).Connection()
            mycursor = mydp.cursor()
            mail.send(msg)
            optionlist = "select type from apparels.inventory where type not in ('men','women')"
            mycursor.execute(optionlist)
            optionListArray = mycursor.fetchall()
            unicOption = list(dict.fromkeys(item[0] for item in optionListArray))
            return render_template('index.html',Message = "Bill Send to your Email ID...!",optionList = unicOption)
        except Exception as e:
            return f"Failed to send email: {e}"
    except Exception as e:
        print(f"Error:{e}")
        return render_template('index.html', Error=str(e))


    
#     # Scanning

scanning = False 

def get_product(barcode):
    """Fetch product details from MySQL database."""
    conn = FetchDataFromDatabase(int(session.get('user_id', 0))).Connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM apparels.inventory WHERE id = %s", (barcode,))
    product = cursor.fetchone()
    conn.close()
    return product

def scan_barcodes():
    global scanning
    cap = cv2.VideoCapture(0)
    while True:
        if not scanning:
            cap.release()
            break

        success, frame = cap.read()
        if not success:
            break

        for barcode in decode(frame):
            barcode_data = barcode.data.decode('utf-8')
            product = get_product(barcode_data)
            if product and product not in Purchase_Bag: 
                Purchase_Bag.append(product)
                try:
                    winsound.Beep(1000,200)
                except Exception as e:
                    print("Error Playing Sound",e)
                    
            pts = np.array([barcode.polygon], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(frame, [pts], True, (0, 255, 0), 3)

        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(scan_barcodes(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/cart')
def get_cart():
    return jsonify(Purchase_Bag)

@app.route('/start_scan', methods=['POST'])
def start_scan():
    global scanning
    scanning = True
    return jsonify({"status": "started"})

@app.route('/stop_scan', methods=['POST'])
def stop_scan():
    global scanning
    scanning = False
    return jsonify({"status": "stopped"})

@app.route('/clear_cart', methods=['POST'])
def clear_cart():
    Purchase_Bag.clear()
    return jsonify({"status": "cart cleared"})

# Generate QR For Payment

def generate_unique_otp(length=6):
    """Generates a unique OTP of given length using digits only."""
    return ''.join(str(secrets.randbelow(10)) for _ in range(length))


@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    """Generate a UPI QR Code and return the image URL."""
    upi_id = "vidyeshym@ybl"
    data = request.json
    amount = data.get('amount')
    transaction_id = str(int(time.time()))

    db = FetchDataFromDatabase(int(session.get('user_id', 0))).Connection()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO payments (transaction_id, upi_id, amount, status) VALUES (%s, %s, %s, %s)",
        (transaction_id, upi_id, amount, "pending")
    )
    db.commit()
    cursor.close()
    db.close()

    qr_path = generate_upi_qr(upi_id, amount, transaction_id)

    return jsonify({
        "qr_path": url_for('static', filename=f"{transaction_id}.png", _external=True),  # Full URL
        "transaction_id": transaction_id
    })

def generate_upi_qr(upi_id, amount, transaction_id):
    """Generate a QR Code for UPI payment."""
    upi_link = f"upi://pay?pa={upi_id}&pn=Merchant&tid={transaction_id}&tr={transaction_id}&tn=Payment&am={amount}&cu=INR"
    qr = qrcode.make(upi_link)

    qr_dir = os.path.join(os.getcwd(), "static")
    os.makedirs(qr_dir, exist_ok=True)  # Ensure directory exists   

    qr_path = os.path.join(qr_dir, f"{transaction_id}.png")
    qr.save(qr_path)

    return qr_path

@app.route('/GetDonepayment')
def GetDonepayment():
    db = FetchDataFromDatabase(int(session.get('user_id', 0))).Connection()
    mycursor = db.cursor()
    transaction_id = request.args.get('transactionId')
    totle_price = request.args.get('totle_price')
    payment_mode = request.args.get('payment_mode')
    

    
    if totle_price is None or payment_mode is None:
        raise Exception("Purchase Bag is empty.")

    mycursor.execute("UPDATE payments SET status = 'success' WHERE transaction_id = %s", (transaction_id,))
    db.commit()
    
    return addtodatabase(totle_price, payment_mode)
    
    

    
    
if __name__ == '__main__':
    app.run(debug=True)
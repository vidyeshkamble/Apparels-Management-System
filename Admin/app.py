import datetime
import json
import os
import time
from flask import Flask, flash, redirect, render_template, jsonify, request, send_file, url_for
import mysql.connector
import openpyxl
import pandas as pd
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'apparelsystem'

@app.route('/')
def index():
    return render_template('index.html')

#data base
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="system",
        database="apparels"
    )

mycursor = mydb.cursor()




@app.route('/CustomerDataFetch', methods = ['GET'])
def CustomerDataFetch():
    mycursor.execute("SELECT * FROM customer")
    customers = mycursor.fetchall()
    return jsonify(customers)
    
@app.route('/SalesDataFetch', methods=['GET'])
def SalesDataFetch():
    try:
        mycursor.execute("SELECT bill_no,inv_ids,sales_qty,sales_price,payment_mode FROM apparels.bill")
        sales = mycursor.fetchall()
        # Ensure proper JSON format
        return jsonify(sales)
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500
    
    
@app.route('/itemorderDataFetch', methods = ['GET'])
def itemorderDataFetch():
    mycursor.execute("SELECT * FROM itemorder")
    items = mycursor.fetchall()
    return jsonify(items)

@app.route('/DeletSales', methods = ['GET'])
def DeletSales():
    sales_id = request.args.getlist('SalesID')
    deletequery = "DELETE FROM sales WHERE sal_no = %s"
    mycursor.execute(deletequery,sales_id)
    mydb.commit()

    return SalesDataFetch()

@app.route('/ApproveRequest',methods = ['GET'])
def ApproveRequest():
    ItemNO = request.args.getlist('ItemId')
    # redues this from New Stock Request        
    remove = "DELETE FROM apparels.requeststock WHERE code = %s"
    mycursor.execute(remove,ItemNO)
    mydb.commit()
    return ApproveFetch()

@app.route('/InventoryFetch', methods=['GET'])
def InventoryFetch():
    try:
        mycursor.execute("SELECT * FROM apparels.inventory")
        inventory = mycursor.fetchall()

        mycursor.execute("SELECT COUNT(*) FROM apparels.inventory;")
        count = mycursor.fetchone()[0]  # Extract count value from tuple

        return jsonify({"inventory": inventory, "count": count})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


    
@app.route('/ItemsFetch', methods=['GET'])
def ItemsFetch():
    try:
        mycursor.execute("SELECT * FROM apparels.items")
        items = mycursor.fetchall()
        return jsonify(items)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/RequestFetch', methods = ['GET'])
def RequestFetch():
    try:
        mycursor.execute("SELECT * FROM apparels.requeststock")
        request = mycursor.fetchall()
        return jsonify(request)
    except Exception as e:
        return jsonify({"error": str(e)}),500  
    
@app.route('/ApproveFetch', methods = ['GET'])
def ApproveFetch():
    try:
        mycursor.execute("SELECT * FROM apparels.inventory WHERE qty < 5")
        more = mycursor.fetchall()
        return jsonify(more)
    except Exception as e:
        return jsonify({"error": str(e)}),500   
    
    
@app.route('/FileGet', methods=['GET'])
def FileGet():
    return jsonify()

# Upload File

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/process', methods=['POST'])
def process_file():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    type = request.form['type']
    qty = request.form['qty']
    
    if file.filename == '':
        return "No selected file"
    
    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        # Extract product data correctly
        result = data.get("plpList", {}).get("productList", [])
        type_list,qty_list,id_list, image_list, name_list, price_list =[],[], [], [], [], []

        for item in result:
            type_list.append(type)
            qty_list.append(qty)
            id_list.append(item.get('id', ''))
            image_list.append(item.get('productImage', ''))    
            name_list.append(item.get('productName', ''))
            price_list.append(item.get('prices', [{}])[0].get('formattedPrice', ''))

        # Debugging print
        print("Extracted Products:")
        print(id_list, name_list, image_list, price_list)

        # Define custom output directory
        output_directory = "C:\\Users\\vidye\\OneDrive\\Desktop\\Admin\\Admin\\Excel"  # Change this to your target location
        os.makedirs(output_directory, exist_ok=True)  # Ensure the directory exists

        # Set custom filename dynamically with type
        output_file = os.path.join(output_directory, f"Products_{ type }.xlsx")
        df = pd.DataFrame({'type':type_list,'qty':qty_list,'id': id_list, 'name': name_list, 'image': image_list, 'price': price_list})
        df.to_excel(output_file, index=False)

        send_file(output_file, as_attachment=True)
        return file_to_database()


DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "system",
    "database": "apparels"
}
@app.route('/fileToDatabase', methods=['POST'])
def file_to_database():

    if 'file' not in request.files:
        print("No file part in request", flush=True)
        flash("No file part")
        return redirect(url_for("index"))

    file = request.files['file']
    
    if file.filename == '':
        print("No file selected", flush=True)
        flash("No selected file")
        return redirect(url_for("index"))

    try:
        workbook = openpyxl.load_workbook(file.stream)
        sheet = workbook.active

        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

        insert_query = """
            INSERT INTO inventory (type, qty, id, name, image, price) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        data_to_insert = []
        for row in sheet.iter_rows(min_row=2, values_only=True):
            if None in row:  # Skip empty rows
                continue

            type_ = str(row[0]).strip()
            qty = int(row[1])  # Convert quantity to integer
            id_ = str(row[2]).strip()  # Ensure ID is treated as text
            name = str(row[3]).strip()
            image = str(row[4]).strip()
            price = float(str(row[5]).replace("Rs.", "").replace(",", "").strip())  # Convert price to float

            data_to_insert.append((type_, qty, id_, name, image, price))


        if data_to_insert:
            cursor.executemany(insert_query, data_to_insert)
            connection.commit()

        cursor.close()
        connection.close()

        return render_template('index.html', message="Records inserted successfully!")

    except Exception as e:
        print(f"Error: {str(e)}", flush=True)
        flash(f"Error: {str(e)}")
        return render_template('index.html', error=f"Error: {str(e)}")
    
     
if __name__ == '__main__':
    app.run(debug=True)
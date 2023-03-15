import pymysql
from app import app
from db import mysql
from flask import jsonify
import cv2
from pyzbar import pyzbar
import numpy as np
from flask import request

@app.route('/')
def users():
    conn = mysql.connect()
    
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM student")
    
    rows = cursor.fetchall()
    
    resp = jsonify({
        "status": "SUCCESS",
        "data": rows
    })
    resp.status_code = 200
    conn.close()
    return resp
@app.route('/read_barcode', methods=['POST'])
def read_barcode():
    if 'image' not in request.files:
        return 'No image uploaded', 400
    

    file = request.files['image']
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    barcodes = pyzbar.decode(img)
    if len(barcodes) > 0:
        try:
            barcode_data = barcodes[0].data.decode('utf-8')
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            query = "SELECT * FROM student WHERE student_id="+barcode_data
            cursor.execute(query)
            rows = cursor.fetchall()
            resp = jsonify({
                "status": "SUCCESS",
                "data": rows
            })
            resp.status_code = 200
            conn.close()

            return resp
        except:
            return jsonify({
                "status": "FAILED",
                "data": {
                    "student_id": "undefined",
                    "faculty": "undefined",
                    "class": "undefined",
                    "full_name": "undefined"
                }

            }),404
    else:
        return jsonify({
                "status": "FAILED",
                "data": {
                    "student_id": "undefined",
                    "faculty": "undefined",
                    "class": "undefined",
                    "full_name": "undefined"
                }

            }),404

if __name__ == "__main__":
    app.run(host='0.0.0.0')